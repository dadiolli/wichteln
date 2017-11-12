# -*- coding: utf-8 -*-
#from https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
key = 'FYLÄ,Xäcu2bÄLU!GECö3Qowo-lAfU7Pö'
import base64
def encode(clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))

def decode(enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)