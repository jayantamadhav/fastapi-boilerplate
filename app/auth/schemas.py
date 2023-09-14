from typing import Optional
from pydantic import BaseModel, Field


class SocialLoginSchema(BaseModel):
    token: str = Field(...)

    class Config:
        orm_mode = True


class LoginSchema(BaseModel):
    phone: str = Field(...)
    otp: str = Field(None)

    class Config:
        orm_mode = True


class UpdateDeviceToken(BaseModel):
    user_id: int = Field(...)
    token: str = Field(...)
    identifier: str = Field(None)

    class Config:
        orm_mode = True


class ResendOtpSchema(BaseModel):
    phone: str = Field(...)

    class Config:
        orm_mode = True
