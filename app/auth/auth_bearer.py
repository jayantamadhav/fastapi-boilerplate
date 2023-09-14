from fastapi import Request, HTTPException, FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.exceptions import HTTPException as StarletteHTTPException

from .auth_handler import decodeJWT

from . import utils

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=200, detail=utils.Response({}, 403, False, "Invalid authentication scheme."))
            if not (await self.verify_jwt(credentials.credentials)):
                raise HTTPException(status_code=200, detail=utils.Response({}, 403, False, "Invalid token or expired token."))
            return credentials.credentials
        else:
            raise HTTPException(status_code=200, detail=utils.Response({}, 403, False, "Invalid authorization code."))

    async def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload =await decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
