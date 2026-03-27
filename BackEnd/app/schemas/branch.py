from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BranchBase(BaseModel):
    name: str
    code: str
    country: str | None = None
    city: str | None = None
    address: str | None = None
    phone: str | None = None
    is_main: bool = False


class BranchCreate(BranchBase):
    company_id: int


class BranchResponse(BranchBase):
    id: int
    company_id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
