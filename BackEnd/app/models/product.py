from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    sku: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    sale_price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    stock: Mapped[int] = mapped_column(nullable=False, default=0)
