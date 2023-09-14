from app.kyc.models import Aadhaar
from app.users.models import User
from app.users.schemas import UpdateUserSchema


async def update_user_kyc_verification_status(user, status):
    user.is_kyc_verified = True if status == "accepted" else False
    user.kyc_verification_status = status
    await user.save()
    return user


async def get_user(id: int = None, phone: int = None, email: str = None):
    if id:
        user = await User.get_or_none(id=id)
    elif phone:
        user = await User.get_or_none(phone=phone)
    else:
        user = await User.get_or_none(email=email)
    return user


async def update_user(data: UpdateUserSchema):
    user = await User.get_or_none(id=data.id)
    if data.first_name:
        user.first_name = data.first_name
    if data.last_name:
        user.last_name = data.last_name
    if data.email:
        user.email = data.email
    if data.latitude:
        user.latitude = data.latitude
    if data.longitude:
        user.longitude = data.longitude
    if data.is_kyc_verified:
        user.is_kyc_verified = data.is_kyc_verified
    if data.is_aadhaar_verified:
        user.is_aadhaar_verified = data.is_aadhaar_verified
    await user.save()
    return user


async def list_users(limit: int, offset: int):
    return await User.all().limit(limit).offset(offset).order_by("-id")