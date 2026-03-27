from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class CompanyResponse(BaseModel):
    id: int
    name: str
    code: str
    business_type: str | None = None
    country: str | None = None
    city: str | None = None
    address: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
