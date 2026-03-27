from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

# Contexto para hashear contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si la contraseña en texto plano coincide con el hash guardado.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Convierte una contraseña normal en hash seguro.
    """
    return pwd_context.hash(password)


def create_access_token(subject: str,
                        expires_delta: timedelta | None = None) -> str:
    """
    Crea el JWT de acceso.
    subject normalmente será el user.id.
    """
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
    )

    to_encode = {
        "sub": subject,
        "exp": expire,
    }

    return jwt.encode(to_encode, settings.SECRET_KEY,
                      algorithm=settings.ALGORITHM)


def decode_token(token: str):
    """
    Decodifica el JWT.
    Si falla, devuelve None.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None
