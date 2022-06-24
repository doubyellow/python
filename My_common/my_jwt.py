import hmac
import json
import base64
import time
import copy


class Jwt:

    @staticmethod
    def encode(payload_dict: dict, key: str, expiration_time=300) -> bytes:
        # init header.txt.txt
        header = {"alg": "HS256", "type": "JWT"}
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        header_base64 = Jwt.base64_encode(header_json.encode())

        # init(初始化) payload.txt
        payload_copy = copy.deepcopy(payload_dict)
        payload_copy["exp"] = expiration_time + time.time()
        payload_json = json.dumps(payload_copy)
        payload_base64 = Jwt.base64_encode(payload_json.encode())

        # init(初始化) sign
        sign_base64 = Jwt._sign_base64(key, header_base64, payload_base64)

        return header_base64 + b"." + payload_base64 + b"." + sign_base64

    @staticmethod
    def decode(tokens: bytes, key: str) -> bytes:
        header_base64, payload_base64, sign_base64 = tokens.split(b".")
        # check sign
        sign_base64_self = Jwt._sign_base64(key, header_base64, payload_base64)
        if sign_base64_self != sign_base64:
            raise Exception("token or key error")
        payload_json = Jwt.base64_decode(payload_base64)
        payload_dict = json.loads(payload_json)
        expiration_time = payload_dict["exp"]
        if time.time() > expiration_time:
            raise Exception("timeout")
        del payload_dict["exp"]
        return payload_dict

    @staticmethod
    def base64_encode(byte_str: bytes) -> bytes:
        return base64.urlsafe_b64encode(byte_str).replace(b"=", b"")

    @staticmethod
    def base64_decode(byte_str: bytes) -> bytes:
        if len(byte_str) % 4:
            eq_numbers = 4 - len(byte_str) % 4
            byte_str = byte_str + b"=" * eq_numbers
        return base64.urlsafe_b64decode(byte_str)

    @staticmethod
    def _sign_base64(key: str, header_base64: bytes, payload_base64: bytes) -> bytes:
        sign = hmac.new(key.encode(), header_base64 + b"." + payload_base64, digestmod="SHA256")
        sign_bytes = sign.digest()
        return Jwt.base64_encode(sign_bytes)


if __name__ == '__main__':
    payload = {"name": "Huang"}
    kay = "2021/5/12"
    token = Jwt.encode(payload, kay)
    print(token)
    payload = Jwt.decode(token, kay)
    print(payload)
