from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Empresa a la que pertenece el usuario.
    # Super admin podría no tener company_id.
    company_id: Mapped[int | None] = mapped_column(
        ForeignKey("companies.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    # Rol del usuario: super_admin, admin, seller
    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False,
                                          unique=True, index=True)
    email: Mapped[str] = mapped_column(String(120), nullable=False,
                                       unique=True, index=True)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)

    # Contraseña hasheada, nunca guardes texto plano.
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    # Si está activo puede iniciar sesión.
    # Para empleados nuevos lo dejaremos en False hasta aprobación.
    is_active: Mapped[bool] = mapped_column(Boolean, default=True,
                                            nullable=False)

    # Solo para control global si quieres distinguir super admin.
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False,
                                               nullable=False)

    # Quién aprobó a este usuario.
    approved_by: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    approved_at: Mapped[datetime | None] = mapped_column(DateTime,
                                                         nullable=True)

    # Cuándo fue desactivado.
    deactivated_at: Mapped[datetime | None] = mapped_column(DateTime,
                                                            nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 default=datetime.utcnow,
                                                 nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    company = relationship("Company", back_populates="users")
    role = relationship("Role", back_populates="users")

    # Relación autorreferenciada: quién aprobó a quién
    approver = relationship("User", remote_side=[id],
                            foreign_keys=[approved_by])

    user_branches = relationship("UserBranch", back_populates="user",
                                 cascade="all, delete-orphan")
    branches = relationship("Branch", secondary="user_branches",
                            back_populates="users", viewonly=True)

    created_products = relationship("Product",
                                    back_populates="created_by_user")
    sales = relationship("Sale", back_populates="user")
    inventory_movements = relationship("InventoryMovement",
                                       back_populates="user")
