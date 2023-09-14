from pydantic import BaseModel, Field
from typing import Optional


class UpdateUserSchema(BaseModel):
    id: int = Field(...)
    first_name: str = Field(None)
    last_name: str = Field(None)
    email: str = Field(None)
    latitude: int = Field(None)
    longitude: int = Field(None)
    is_kyc_verified: bool = Field(None)
    is_aadhaar_verified: bool = Field(None)

    class Config:
        orm_mode = True
