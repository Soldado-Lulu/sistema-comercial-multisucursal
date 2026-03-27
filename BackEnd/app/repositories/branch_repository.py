from sqlalchemy.orm import Session

from app.models.branch import Branch


class BranchRepository:
    def create(self, db: Session, data: dict) -> Branch:
        """
        Crea una sucursal.
        """
        branch = Branch(**data)
        db.add(branch)
        db.flush()
        return branch
