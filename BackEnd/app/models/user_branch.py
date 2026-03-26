from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class UserBranch(Base):
    __tablename__ = "user_branches"
    __table_args__ = (
        UniqueConstraint("user_id", "branch_id", name="uq_user_branch"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    branch_id: Mapped[int] = mapped_column(
        ForeignKey("branches.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    assigned_at: Mapped[datetime] = mapped_column(DateTime,
                                                  default=datetime.utcnow,
                                                  nullable=False)

    user = relationship("User", back_populates="user_branches")
    branch = relationship("Branch", back_populates="user_branches")
