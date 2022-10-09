from jwt import encode, decode, exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify

def expire_date(days: int):
    now = datetime.now()
    newDate = now + timedelta(days)
    return newDate

def writeToken(data):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': data
        }
        return encode(
            payload,
            getenv("SECRET_KEY"),
            algorithm='HS256'
        )
    except Exception as e:
        return e

    

def validateToken(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        response = jsonify({"message":"Token inválido"})
        response.status = 401
        return response

    except exceptions.ExpiredSignatureError:
        response = jsonify({"message":"Token ha expirado"})
        response.status = 401
        return response