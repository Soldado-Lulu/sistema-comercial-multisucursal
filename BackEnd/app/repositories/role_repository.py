from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.role import Role


class RoleRepository:
    def get_by_name(self, db: Session, name: str) -> Role | None:
        """
        Busca un rol por nombre.
        """
        stmt = select(Role).where(Role.name == name)
        return db.scalar(stmt)

    def create(self, db: Session, name: str,
               description: str | None = None) -> Role:
        """
        Crea un rol nuevo.
        """
        role = Role(name=name, description=description, is_active=True)
        db.add(role)
        db.commit()
        db.refresh(role)
        return role
