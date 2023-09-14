from app.auth.schemas import UpdateDeviceToken
from app.users.models import User
from app.auth.models import OTP, DeviceToken
from app.kyc.models import KYC


async def save_otp(data):
    otp = await OTP.create(phone=data["phone"], otp=data["otp"])
    return otp


async def delete_otp(otp_obj):
    return await OTP.get(id=otp_obj.id).delete()


async def get_saved_otp(phone: str, otp: str):
    _saved_otp = await OTP.get_or_none(phone=phone, otp=otp)
    return _saved_otp


async def get_user_by_phone(data):
    return await User.get_or_none(phone=data.phone)


async def create_user(data):
    user = await User.create(phone=data.phone)
    return user


async def update_or_create_device_token(user, payload: UpdateDeviceToken):
    device_token = await DeviceToken.filter(user=user).first()
    if not device_token:
        device_token = await DeviceToken.create(
            token=payload.token,
            user=user,
        )
    else:
        device_token.token = payload.token

    if payload.identifier:
        device_token.identifier = payload.identifier
    await device_token.save()
    return device_token
