# this file is responsible for signing, encoding, decoding and returning JWTs


import time
import jwt
from decouple import config
from typing import Dict


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {
        "access_token": token
    }

# function used for signing the JWT string
def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithm=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}