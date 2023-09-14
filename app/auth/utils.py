import random, requests, os
import urllib.request
import urllib.parse
import requests

from twilio.rest import Client
from decouple import config
from jwt.api_jwt import decode
from app.auth import controller, auth_handler, models
from fastapi import HTTPException

def fast2sms_send_otp(otp, phone):
    payload = urllib.parse.urlencode({
        'authorization': config('FAST2SMS_API_KEY'), 
        'route': 'dlt',
        'sender_id': config('FAST2SMS_SENDER_ID'),
        'message': config('FAST2SMS_MESSAGE_ID'),
        'variables_values' : otp,
        'numbers': phone,
        'flash': "0" 
        
    })
    req = requests.get('https://www.fast2sms.com/dev/bulkV2', params=payload)
    return req
    
async def sendOTP(phone):
    otp = str(random.random()).split(".")[1][:6]
    data = {
        "phone" : phone,
        "otp" : otp
    }
    fast2sms_send_otp(otp, phone)
    save_otp = await controller.save_otp(data)
    return otp

async def verifyOTP(phone, otp):
    saved_otp = await controller.get_saved_otp(phone, otp)
    if saved_otp:
        delete_otp = await controller.delete_otp(saved_otp)
        return True
    else:
        return False
