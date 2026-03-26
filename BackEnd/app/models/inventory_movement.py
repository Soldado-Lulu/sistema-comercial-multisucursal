from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class InventoryMovement(Base):
    __tablename__ = "inventory_movements"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    branch_id: Mapped[int] = mapped_column(
        ForeignKey("branches.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    movement_type: Mapped[str] = mapped_column(String(30), nullable=False,
                                               index=True)
    quantity: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    previous_stock: Mapped[Decimal] = mapped_column(Numeric(10, 2),
                                                    nullable=False, default=0)
    new_stock: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False,
                                               default=0)

    reason: Mapped[str | None] = mapped_column(String(255), nullable=True)
    reference_type: Mapped[str | None] = mapped_column(String(50),
                                                       nullable=True)
    reference_id: Mapped[int | None] = mapped_column(nullable=True)

    notes: Mapped[str | None] = mapped_column(String(500), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 default=datetime.utcnow,
                                                 nullable=False)

    company = relationship("Company", back_populates="inventory_movements")
    branch = relationship("Branch", back_populates="inventory_movements")
    product = relationship("Product", back_populates="inventory_movements")
    user = relationship("User", back_populates="inventory_movements")
