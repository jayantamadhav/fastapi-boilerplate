from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=200, null=True)
    last_name = fields.CharField(max_length=200, null=True)
    phone = fields.BigIntField()
    email = fields.CharField(max_length=200, null=True)
    latitude = fields.BigIntField(null=True)
    longitude = fields.BigIntField(null=True)
    kyc_verification_status = fields.CharField(max_length=50, default="pending")
    is_kyc_verified = fields.BooleanField(default=False)
    is_aadhaar_verified = fields.BooleanField(default=False)
    current_address = fields.TextField(null=True, blank=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"

    def __str__(self):
        return "User " + str(self.id)


class UsedCoupon(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", on_delete=fields.CASCADE)
    coupon = fields.ForeignKeyField("models.CouponCode", null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_used_coupons"
