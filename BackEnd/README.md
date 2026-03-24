# BackEnd

API del sistema comercial multisucursal para la gestión de inventario, ventas, usuarios y sucursales.

## Tecnologías previstas
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT para autenticación

## Objetivo
Construir una API segura, escalable y mantenible para soportar las operaciones del sistema comercial.

## Responsabilidades del backend
- Autenticación y autorización
- Gestión de usuarios y roles
- Gestión de sucursales
- Gestión de productos
- Control de inventario por sucursal
- Registro de ventas
- Reportes

## Buenas prácticas a seguir
- Arquitectura modular por dominios
- Separación entre rutas, servicios, esquemas y modelos
- Validación de datos con Pydantic
- Variables sensibles en `.env`
- Migraciones con Alembic
- Manejo centralizado de errores
- Documentación automática con Swagger

## Estructura prevista
```text
BackEnd/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── tests/
├── requirements.txt
└── README.md