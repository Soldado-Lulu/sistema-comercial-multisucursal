from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.company import Company


class CompanyRepository:
    def get_by_code(self, db: Session, code: str) -> Company | None:
        """
        Busca una empresa por su código.
        """
        stmt = select(Company).where(Company.code == code)
        return db.scalar(stmt)

    def create(self, db: Session, data: dict) -> Company:
        """
        Crea una empresa.
        """
        company = Company(**data)
        db.add(company)
        db.flush()  # importante para obtener company.id sin hacer commit aún
        return company
