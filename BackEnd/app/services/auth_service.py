from datetime import datetime

from sqlalchemy.orm import Session

from app.core.secutiry import create_access_token, get_password_hash
from app.core.secutiry import verify_password
from app.repositories.branch_repository import BranchRepository
from app.repositories.company_repository import CompanyRepository
from app.repositories.role_repository import RoleRepository
from app.repositories.user_repository import UserRepository
from app.utils.helpers import generate_company_code


class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.role_repository = RoleRepository()
        self.company_repository = CompanyRepository()
        self.branch_repository = BranchRepository()

    def ensure_base_roles(self, db: Session):
        """
        Crea roles base si no existen.
        Esto evita depender de seed manual al inicio.
        """
        base_roles = [
            ("super_admin", "Administrador global del sistema"),
            ("admin", "Dueño o administrador del negocio"),
            ("seller", "Empleado o vendedor"),
        ]

        for name, description in base_roles:
            role = self.role_repository.get_by_name(db, name)
            if not role:
                self.role_repository.create(db, name=name,
                                            description=description)

    def login(self, db: Session, email: str, password: str):
        """
        Login normal con email y password.
        Solo permite acceso si el usuario está activo.
        """
        user = self.user_repository.get_by_email(db, email)

        if not user:
            return None

        if not user.is_active:
            return None

        if not verify_password(password, user.password_hash):
            return None

        token = create_access_token(subject=str(user.id))

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": user,
        }

    def register_company(self, db: Session, data):
        """
        Registra empresa + admin + sucursal principal.
        Todo se hace en una sola transacción.
        """
        self.ensure_base_roles(db)

        if self.user_repository.username_exists(db, data.username):
            raise ValueError("El username ya está en uso.")

        if self.user_repository.email_exists(db, data.email):
            raise ValueError("El email ya está en uso.")

        admin_role = self.role_repository.get_by_name(db, "admin")
        if not admin_role:
            raise ValueError("No se encontró el rol admin.")

        # Generar código único de empresa
        company_code = None
        while True:
            candidate = generate_company_code()
            existing = self.company_repository.get_by_code(db, candidate)
            if not existing:
                company_code = candidate
                break

        try:
            # 1. Crear empresa
            company = self.company_repository.create(
                db,
                {
                    "name": data.company_name,
                    "code": company_code,
                    "business_type": data.business_type,
                    "country": data.country,
                    "city": data.city,
                    "address": data.address,
                    "phone": data.phone,
                    "email": data.company_email,
                    "is_active": True,
                },
            )

            # 2. Crear admin dueño
            user = self.user_repository.create(
                db,
                {
                    "company_id": company.id,
                    "role_id": admin_role.id,
                    "first_name": data.first_name,
                    "last_name": data.last_name,
                    "username": data.username,
                    "email": data.email,
                    "phone": data.user_phone,
                    "password_hash": get_password_hash(data.password),
                    "is_active": True,
                    "is_superuser": False,
                    "approved_by": None,
                    "approved_at": datetime.utcnow(),
                },
            )

            # 3. Crear sucursal principal
            self.branch_repository.create(
                db,
                {
                    "company_id": company.id,
                    "name": data.main_branch_name,
                    "code": "MAIN",
                    "country": data.country,
                    "city": data.city,
                    "address": data.address,
                    "phone": data.phone,
                    "is_main": True,
                    "is_active": True,
                },
            )

            db.commit()
            db.refresh(company)
            db.refresh(user)

            return {
                "message": "Negocio registrado correctamente.",
                "company_code": company.code,
                "company": company,
                "user": user,
            }

        except Exception:
            db.rollback()
            raise

    def register_employee(self, db: Session, data):
        """
        Registra un empleado usando company_code.
        Queda inactivo hasta aprobación del admin.
        """
        self.ensure_base_roles(db)

        if self.user_repository.username_exists(db, data.username):
            raise ValueError("El username ya está en uso.")

        if self.user_repository.email_exists(db, data.email):
            raise ValueError("El email ya está en uso.")

        company = self.company_repository.get_by_code(db, data.company_code)
        if not company:
            raise ValueError("El código de empresa no existe.")

        seller_role = self.role_repository.get_by_name(db, "seller")
        if not seller_role:
            raise ValueError("No se encontró el rol seller.")

        try:
            user = self.user_repository.create(
                db,
                {
                    "company_id": company.id,
                    "role_id": seller_role.id,
                    "first_name": data.first_name,
                    "last_name": data.last_name,
                    "username": data.username,
                    "email": data.email,
                    "phone": data.phone,
                    "password_hash": get_password_hash(data.password),
                    "is_active": False,  # queda pendiente
                    "is_superuser": False,
                    "approved_by": None,
                    "approved_at": None,
                },
            )

            db.commit()
            db.refresh(user)

            return {
                "message": "Tu cuenta tiene que ser aprobada.",
                "user": user,
            }

        except Exception:
            db.rollback()
            raise
