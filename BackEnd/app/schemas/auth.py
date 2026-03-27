from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    # Login con email y password
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)


class Token(BaseModel):
    # Respuesta de login
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    # Datos mínimos del token
    sub: str | None = None


class RegisterCompanyRequest(BaseModel):
    # Datos de la empresa
    company_name: str
    business_type: str | None = None
    country: str | None = None
    city: str | None = None
    address: str | None = None
    phone: str | None = None
    company_email: EmailStr | None = None

    # Datos del dueño/admin
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    user_phone: str | None = None
    password: str = Field(..., min_length=6, max_length=72)

    # Sucursal principal
    main_branch_name: str


class RegisterEmployeeRequest(BaseModel):
    # Código de empresa que le pasa el admin
    company_code: str

    # Datos del empleado
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    phone: str | None = None
    password: str = Field(..., min_length=6, max_length=72)


class RegisterResponse(BaseModel):
    message: str
