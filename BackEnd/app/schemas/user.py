from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserResponse(BaseModel):
    id: int
    company_id: int | None
    role_id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    phone: str | None
    is_active: bool
    is_superuser: bool
    approved_by: int | None = None
    approved_at: datetime | None = None
    deactivated_at: datetime | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserStatusResponse(BaseModel):
    message: str
    user: UserResponse
