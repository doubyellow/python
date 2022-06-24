from typing import List


class SM4:
    def __init__(self):
        self.SM4_ENCRYPT = 1
        self.SM4_DECRYPT = 0
        self.SBoxTable = [-42, -112, -23, -2, -52, -31, 61, -73, 22, -74, 20, -62, 40, -5, 44, 5, 43, 103, -102, 118,
                          42, -66, 4, -61, -86, 68, 19, 38, 73, -122, 6, -103, -100, 66, 80, -12, -111, -17, -104, 122,
                          51, 84, 11, 67, -19, -49, -84, 98, -28, -77, 28, -87, -55, 8, -24, -107, -128, -33, -108, -6,
                          117, -113, 63, -90, 71, 7, -89, -4, -13, 115, 23, -70, -125, 89, 60, 25, -26, -123, 79, -88,
                          104, 107, -127, -78, 113, 100, -38, -117, -8, -21, 15, 75, 112, 86, -99, 53, 30, 36, 14, 94,
                          99, 88, -47, -94, 37, 34, 124, 59, 1, 33, 120, -121, -44, 0, 70, 87, -97, -45, 39, 82, 76, 54,
                          2, -25, -96, -60, -56, -98, -22, -65, -118, -46, 64, -57, 56, -75, -93, -9, -14, -50, -7, 97,
                          21, -95, -32, -82, 93, -92, -101, 52, 26, 85, -83, -109, 50, 48, -11, -116, -79, -29, 29, -10,
                          -30, 46, -126, 102, -54, 96, -64, 41, 35, -85, 13, 83, 78, 111, -43, -37, 55, 69, -34, -3,
                          -114, 47, 3, -1, 106, 114, 109, 108, 91, 81, -115, 27, -81, -110, -69, -35, -68, 127, 17, -39,
                          92, 65, 31, 16, 90, -40, 10, -63, 49, -120, -91, -51, 123, -67, 45, 116, -48, 18, -72, -27,
                          -76, -80, -119, 105, -105, 74, 12, -106, 119, 126, 101, -71, -15, 9, -59, 110, -58, -124, 24,
                          -16, 125, -20, 58, -36, 77, 32, 121, -18, 95, 62, -41, -53, 57, 72]
        self.FK = [-1548633402, 1453994832, 1736282519, -1301273892]
        self.CK = [462357, 472066609, 943670861, 1415275113, 1886879365, -1936483679, -1464879427, -993275175,
                   -521670923, -66909679, 404694573, 876298825, 1347903077, 1819507329, -2003855715, -1532251463,
                   -1060647211, -589042959, -117504499, 337322537, 808926789, 1280531041, 1752135293, -2071227751,
                   -1599623499, -1128019247, -656414995, -184876535, 269950501, 741554753, 1213159005, 1684763257]

        def GET_ULONG_BE(b: List[bytes], i: int):
            n = (b[i] & 0xFF) << 24 | (b[(i + 1)] & 0xFF) << 16 | (b[(i + 2)] & 0xFF) << 8 | b[
                (i + 3)] & 0xFF & 0xFFFFFFFF

            return n

        def PUT_ULONG_BE(n, b: List[bytes], i: int):
            b[i] = bytes(int(0xFF & n >> 24))
            b[(i + 1)] = bytes(int(0xFF & n >> 16))
            b[(i + 2)] = bytes(int(0xFF & n >> 8))
            b[(i + 3)] = bytes(int(0xFF & n))

        def SHL(x, n: int):
            return (x & 0xFFFFFFFF) << n

        def ROTL(x, n: int):
            return SHL(x, n) | x >> 32 - n

        def SWAP(sk, i):
            t = sk[i]
            sk[i] = sk[(31 - i)]
            sk[(31 - i)] = t

        def sm4Sbox(inch: bytes):
            i = inch & 0xFF
            retVal = self.SBoxTable[i]
            return retVal


def accountPayableClean(request):
    headerJsonObj = {"txCode": request["TxCode"],
                     "PtCode": request["PtCode"],
                     "TraceNo": request["TraceNo"],
                     "EncryptKey": "",
                     "SignData": ""
                     }
    contentJsonObj = request
    req_json = {"Head": headerJsonObj, "Req": contentJsonObj}


def EncryptUtil(req_json, publicKey):
    head = req_json["Head"]
    reqData = req_json["Req"]
    import hashlib
    import time
    str = "C1010444009784" + time.strftime("%Y%m%d%H%M%S", time.localtime())
    md5 = hashlib.md5()
    md5.update(str.encode(encoding="utf-8"))
    secretKey = md5.hexdigest()
    keyBytes = bytes.fromhex(secretKey)
    SM4_content = {"mode": 1, "isPadding": True, "sk": int()}


# def hexStringTobytes(str):
#     # str = str.replace(" ", "")
#     return bytes.fromhex(str)
#     # return a2b_hex(str)


import hashlib
import time
# from Cryptodome.Cipher import AES
pubKey = "04F6E0C3345AE42B51E06BF50B98834988D54EBC7460FE135A48171BC0629EAE205EEDE253A530608178A98F1E19BB737302813BA39ED3FA3C51639D7A20C7391A"


str = "C1010444009784" + time.strftime("%Y%m%d%H%M%S", time.localtime())
md5 = hashlib.md5()
md5.update(str.encode(encoding="utf-8"))
secretKey = md5.hexdigest()

SM4_content = {"mode": 1, "isPadding": True, "sk": int()}
print(SM4_content)
# print(secretKey)
