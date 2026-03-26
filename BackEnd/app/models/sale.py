from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class Sale(Base):
    __tablename__ = "sales"
    __table_args__ = (
        UniqueConstraint("company_id", "sale_number",
                         name="uq_sale_company_sale_number"),
    )

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
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    sale_number: Mapped[str] = mapped_column(String(50), nullable=False,
                                             index=True)

    customer_name: Mapped[str | None] = mapped_column(String(150),
                                                      nullable=True)
    customer_document: Mapped[str | None] = mapped_column(String(50),
                                                          nullable=True)

    subtotal: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False,
                                              default=0)
    discount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False,
                                              default=0)
    total: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False,
                                           default=0)

    payment_method: Mapped[str | None] = mapped_column(String(30),
                                                       nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False,
                                        default="completed", index=True)
    notes: Mapped[str | None] = mapped_column(String(500), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 default=datetime.utcnow,
                                                 nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    company = relationship("Company", back_populates="sales")
    branch = relationship("Branch", back_populates="sales")
    user = relationship("User", back_populates="sales")

    sale_details = relationship("SaleDetail", back_populates="sale",
                                cascade="all, delete-orphan")
