from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class Branch(Base):
    __tablename__ = "branches"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(120), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    country: Mapped[str | None] = mapped_column(String(100), nullable=True)
    city: Mapped[str | None] = mapped_column(String(100), nullable=True)
    address: Mapped[str | None] = mapped_column(String(255), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)

    is_main: Mapped[bool] = mapped_column(Boolean,
                                          default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True,
                                            nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 default=datetime.utcnow,
                                                 nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    company = relationship("Company", back_populates="branches")

    user_branches = relationship("UserBranch", back_populates="branch",
                                 cascade="all, delete-orphan")
    users = relationship("User", secondary="user_branches",
                         back_populates="branches", viewonly=True)

    inventories = relationship("Inventory", back_populates="branch")
    inventory_movements = relationship("InventoryMovement",
                                       back_populates="branch")
    sales = relationship("Sale", back_populates="branch")
