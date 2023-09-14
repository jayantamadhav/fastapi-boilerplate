from fastapi import APIRouter, Depends
from app.users.controller import get_user
from services.utils import ErrorResponse, Response
from app.auth import schemas, utils, controller, auth_handler
from app.auth.auth_bearer import JWTBearer

from app.auth.auth_handler import signJWT

auth_routes = APIRouter()


@auth_routes.post("/login")
async def login(data: schemas.LoginSchema):
    if data.phone and not data.otp:
        otp = await utils.sendOTP(data.phone)
        return Response({"otp": otp}, 200, True, "Otp has been sent")
    else:
        verify_otp = await utils.verifyOTP(data.phone, data.otp)
        if not verify_otp:
            return Response({}, 400, False, "OTP did not match")
        user = await controller.get_user_by_phone(data)
        if not user:
            db_user = await controller.create_user(data)
            token = await auth_handler.signJWT(db_user)
            db_user = db_user.__dict__
            db_user["access_token"] = token
            return Response(db_user, 200)
        else:
            token = await auth_handler.signJWT(user)
            user = user.__dict__
            user["access_token"] = token
            return Response(user, 200)


@auth_routes.post("/resend-otp")
async def resend_otp(data: schemas.ResendOtpSchema):
    otp = await utils.sendOTP(data.phone)
    return Response({"otp": otp}, 200, True, "Otp has been sent")


@auth_routes.post("/device-token", dependencies=[Depends(JWTBearer())])
async def update_device_token(payload: schemas.UpdateDeviceToken):
    a = JWTBearer()
    print(a.__dict__)
    user = await get_user(id=payload.user_id)
    if not user:
        return ErrorResponse.bad_request()
    device_token = await controller.update_or_create_device_token(user, payload)
    return Response(device_token, 200, True)
