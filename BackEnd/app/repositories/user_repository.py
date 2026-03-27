from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.user import User


class UserRepository:
    def get_by_email(self, db: Session, email: str) -> User | None:
        stmt = (
            select(User)
            .options(joinedload(User.role))
            .where(User.email == email)
        )
        return db.scalar(stmt)

    def get_by_username(self, db: Session, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        return db.scalar(stmt)

    def get_by_id(self, db: Session, user_id: int) -> User | None:
        stmt = (
            select(User)
            .options(joinedload(User.role))
            .where(User.id == user_id)
        )
        return db.scalar(stmt)

    def get_pending_by_company(self, db: Session,
                               company_id: int) -> list[User]:
        """
        Lista empleados inactivos/pending de una empresa.
        """
        stmt = (
            select(User)
            .options(joinedload(User.role))
            .where(
                User.company_id == company_id,
                User.is_active == False,  # noqa: E712
                User.is_superuser == False,  # noqa: E712
            )
            .order_by(User.created_at.desc())
        )
        return list(db.scalars(stmt).all())

    def email_exists(self, db: Session, email: str) -> bool:
        return self.get_by_email(db, email) is not None

    def username_exists(self, db: Session, username: str) -> bool:
        return self.get_by_username(db, username) is not None

    def create(self, db: Session, data: dict) -> User:
        """
        Crea un usuario.
        """
        user = User(**data)
        db.add(user)
        db.flush()
        return user

    def save(self, db: Session, user: User) -> User:
        """
        Guarda cambios de un usuario ya existente.
        """
        db.add(user)
        db.flush()
        return user
