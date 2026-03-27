from datetime import datetime

from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def list_pending_users(self, db: Session, admin_user):
        """
        Lista usuarios pendientes de la empresa del admin.
        """
        return self.user_repository.get_pending_by_company(
            db, admin_user.company_id)

    def approve_user(self, db: Session, user_id: int, admin_user):
        """
        Aprueba un empleado pendiente.
        """
        user = self.user_repository.get_by_id(db, user_id)

        if not user:
            raise ValueError("Usuario no encontrado.")

        if user.company_id != admin_user.company_id:
            raise ValueError("No puedes aprobar usuarios de otra empresa.")

        if user.is_superuser:
            raise ValueError("No puedes aprobar este tipo de usuario.")

        user.is_active = True
        user.approved_by = admin_user.id
        user.approved_at = datetime.utcnow()
        user.deactivated_at = None

        try:
            self.user_repository.save(db, user)
            db.commit()
            db.refresh(user)
            return user
        except Exception:
            db.rollback()
            raise

    def deactivate_user(self, db: Session, user_id: int, admin_user):
        """
        Desactiva un empleado.
        """
        user = self.user_repository.get_by_id(db, user_id)

        if not user:
            raise ValueError("Usuario no encontrado.")

        if user.company_id != admin_user.company_id:
            raise ValueError("No puedes desactivar usuarios de otra empresa.")

        if user.id == admin_user.id:
            raise ValueError("No puedes desactivarte a ti mismo.")

        if user.is_superuser:
            raise ValueError("No puedes desactivar este tipo de usuario.")

        user.is_active = False
        user.deactivated_at = datetime.utcnow()

        try:
            self.user_repository.save(db, user)
            db.commit()
            db.refresh(user)
            return user
        except Exception:
            db.rollback()
            raise

    def reactivate_user(self, db: Session, user_id: int, admin_user):
        """
        Reactiva un usuario inactivo.
        """
        user = self.user_repository.get_by_id(db, user_id)

        if not user:
            raise ValueError("Usuario no encontrado.")

        if user.company_id != admin_user.company_id:
            raise ValueError("No puedes reactivar usuarios de otra empresa.")

        if user.is_superuser:
            raise ValueError("No puedes reactivar este tipo de usuario.")

        user.is_active = True
        user.deactivated_at = None

        if user.approved_at is None:
            user.approved_at = datetime.utcnow()
            user.approved_by = admin_user.id

        try:
            self.user_repository.save(db, user)
            db.commit()
            db.refresh(user)
            return user
        except Exception:
            db.rollback()
            raise
