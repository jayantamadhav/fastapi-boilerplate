from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields


class OTP(Model):
    id = fields.IntField(pk=True)
    phone = fields.CharField(max_length=20)
    otp = fields.CharField(max_length=10)

    def __str__(self):
        return str(self.id)


class DeviceToken(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="user_device_tokens")
    token = fields.CharField(max_length=500)
    identifier = fields.CharField(max_length=256, null=True, blank=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "device_token"

    def __str__(self):
        return str(self.id)
