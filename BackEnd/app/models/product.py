from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Numeric, String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class Product(Base):
    __tablename__ = "products"
    __table_args__ = (
        UniqueConstraint("company_id", "code", name="uq_product_company_code"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    subcategory_id: Mapped[int | None] = mapped_column(
        ForeignKey("subcategories.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    created_by: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    code: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    barcode: Mapped[str | None] = mapped_column(String(100), nullable=True,
                                                index=True)

    purchase_price: Mapped[float] = mapped_column(Numeric(10, 2), default=0,
                                                  nullable=False)
    sale_price: Mapped[float] = mapped_column(Numeric(10, 2), default=0,
                                              nullable=False)

    stock_min: Mapped[float] = mapped_column(Numeric(10, 2), default=0,
                                             nullable=False)
    stock_max: Mapped[float | None] = mapped_column(Numeric(10, 2),
                                                    nullable=True)

    has_expiration: Mapped[bool] = mapped_column(Boolean, default=False,
                                                 nullable=False)
    has_batch: Mapped[bool] = mapped_column(Boolean, default=False,
                                            nullable=False)

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

    company = relationship("Company", back_populates="products")
    category = relationship("Category", back_populates="products")
    subcategory = relationship("Subcategory", back_populates="products")
    created_by_user = relationship("User", back_populates="created_products")

    product_tags = relationship("ProductTag", back_populates="product",
                                cascade="all, delete-orphan")
    tags = relationship("Tag", secondary="product_tags",
                        back_populates="products", viewonly=True)

    inventories = relationship("Inventory", back_populates="product")
    inventory_movements = relationship("InventoryMovement",
                                       back_populates="product")
    sale_details = relationship("SaleDetail", back_populates="product")
