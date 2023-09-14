from decouple import config
from fastapi import FastAPI
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig


def Response(data, status_code: int = 200, success: bool = True, message: str = "OK"):
    if success:
        error = False
    else:
        error = True
    return {
        "status_code": status_code,
        "error": error,
        "success": success,
        "message": message,
        "data": data,
    }


class ErrorResponse:
    def not_found(message: str = "Not Found"):
        return Response(None, 404, False, message)

    def bad_request():
        return Response(None, 400, False, "Bad request")


class EmailMessage:
    def __init__(self):
        self.config = ConnectionConfig(
            MAIL_FROM="no-reply@banjararide.com",
            MAIL_USERNAME=config("EMAIL_USERNAME"),
            MAIL_PASSWORD=config("EMAIL_PASSWORD"),
            MAIL_PORT= 587, #int(config("EMAIL_PORT")),
            MAIL_SERVER=config("EMAIL_HOST"),
            MAIL_STARTTLS = True,
            MAIL_SSL_TLS = False,
            USE_CREDENTIALS = True,
            VALIDATE_CERTS = False
            # MAIL_TLS=True if config("EMAIL_USE_TLS") == "True" else False,
            # MAIL_SSL=True if config("EMAIL_USE_SSL") == "True" else False,
        )

    async def send_message(
        self, subject: str, recipients: list, body: str, subtype: str = "html"
    ):
        message = MessageSchema(
            subject=subject, recipients=recipients, body=body, subtype=subtype
        )
        fm = FastMail(self.config)
        res = await fm.send_message(message)
        return res
