import time
import jwt
import json
import random
from typing import Dict
from decouple import config
from passlib.hash import pbkdf2_sha256


SECRET_KEY = config('SECRET_KEY')


async def signJWT(user):
    payload = {
        "id": user.id,
        "phone" : user.phone,
        "expires": int(time.time() + int(config("JWT_EXPIRY_IN_SECONDS")))
    }
    token = jwt.encode(payload, key = SECRET_KEY)
    return token

async def signJWTadmin(admin):
    payload = {
        "id": admin.id,
        "username" : admin.username,
        "expires": int(time.time() + int(config("JWT_EXPIRY_IN_SECONDS")))
    }
    token = jwt.encode(payload, key = SECRET_KEY)

    return token

async def decodeJWT(token: str) -> dict:
    try:
        # key = jwt.get_unverified_header(token)['kid']
        decoded_token =jwt.decode(token, key=SECRET_KEY)
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

async def refreshJWT(user):
    payload = {
        "id": user['id'],
        "fullname" : user['fullname'],
        "email" : user['email'],
        "is_superuser" : user['is_superuser'],
        "is_active" : user['is_active'],
        "expires": int(time.time() + int(config("JWT_EXPIRY_IN_SECONDS")))
    }
    token = jwt.encode(payload, key = SECRET_KEY)
    return token

def makepassword(password: str):
    return pbkdf2_sha256.hash(password)

def checkpassword(password: str, hash: str):
    return pbkdf2_sha256.verify(password, hash)
