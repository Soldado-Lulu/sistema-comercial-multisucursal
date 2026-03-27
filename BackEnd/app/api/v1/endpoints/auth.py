from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user
from app.db.session import get_db
from app.schemas.auth import (
    LoginRequest,
    RegisterCompanyRequest,
    RegisterEmployeeRequest,
    RegisterResponse,
    Token,
)
from app.schemas.user import UserResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register-company")
def register_company(data: RegisterCompanyRequest,
                     db: Session = Depends(get_db)):
    """
    Registro público del dueño del negocio.
    Crea empresa + admin + sucursal principal.
    """
    service = AuthService()
    try:
        result = service.register_company(db, data)
        return {
            "message": result["message"],
            "company_code": result["company_code"],
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/register-employee", response_model=RegisterResponse)
def register_employee(data: RegisterEmployeeRequest,
                      db: Session = Depends(get_db)):
    """
    Registro público de empleado usando el código de empresa.
    Queda pendiente hasta aprobación.
    """
    service = AuthService()
    try:
        result = service.register_employee(db, data)
        return {"message": result["message"]}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    """
    Login con JWT.
    Solo permite acceso si el usuario está activo.
    """
    service = AuthService()
    result = service.login(db, data.email, data.password)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas o cuenta pendiente/inactiva.",
        )

    return {
        "access_token": result["access_token"],
        "token_type": result["token_type"],
    }


@router.get("/me", response_model=UserResponse)
def me(current_user=Depends(get_current_active_user)):
    """
    Devuelve el usuario autenticado.
    Sirve para probar que el token funciona.
    """
    return current_user
