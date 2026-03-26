from datetime import datetime

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    code: Mapped[str] = mapped_column(String(50), nullable=False,
                                      unique=True, index=True)

    business_type: Mapped[str | None] = mapped_column(String(100),
                                                      nullable=True)
    country: Mapped[str | None] = mapped_column(String(100), nullable=True)
    city: Mapped[str | None] = mapped_column(String(100), nullable=True)
    address: Mapped[str | None] = mapped_column(String(255), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    email: Mapped[str | None] = mapped_column(String(120), nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean,
                                            default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 default=datetime.utcnow,
                                                 nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    branches = relationship("Branch", back_populates="company",
                            cascade="all, delete-orphan")
    users = relationship("User", back_populates="company")
    categories = relationship("Category", back_populates="company")
    subcategories = relationship("Subcategory", back_populates="company")
    tags = relationship("Tag", back_populates="company")
    products = relationship("Product", back_populates="company")
    inventories = relationship("Inventory", back_populates="company")
    inventory_movements = relationship("InventoryMovement",
                                       back_populates="company")
    sales = relationship("Sale", back_populates="company")
