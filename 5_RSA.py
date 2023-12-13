# pip install pycryptodome
import binascii

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")

pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

privKey = keyPair
print(f"Public key: (n={hex(privKey.n)}, d={hex(privKey.d)})")

privKeyPEM = privKey.exportKey()
print(privKeyPEM.decode('ascii'))


msg = input("Enter a message: ")

encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg.encode('utf-8'))
print("Encrypted: ", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(privKey)
decrypted = decryptor.decrypt(encrypted)
print("Decrypted: ",decrypted.decode('utf-8'))



"""
OUTPUT:-
Public key: (n=0xf42253e59b6d5b3a4e06297df103e520c24dc24a64470be6cb582fec770ee8f5c8e22f2806613dccbf744791bf4740ca4c9a01b56fc2f3519169f6d06162ea70abf32b7769d487db86f365084f1af5c7483789f3c1804d8af8bd7c7f8c9d0f06d828be20da775ab03c3ef5519d0b91b433b3d1fe67c8cee5489837a9160c7255, e=0x10001)
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQD0IlPlm21bOk4GKX3xA+Ugwk3C
SmRHC+bLWC/sdw7o9cjiLygGYT3Mv3RHkb9HQMpMmgG1b8LzUZFp9tBhYupwq/Mr
d2nUh9uG82UITxr1x0g3ifPBgE2K+L18f4ydDwbYKL4g2ndasDw+9VGdC5G0M7PR
/mfIzuVImDepFgxyVQIDAQAB
-----END PUBLIC KEY-----
Public key: (n=0xf42253e59b6d5b3a4e06297df103e520c24dc24a64470be6cb582fec770ee8f5c8e22f2806613dccbf744791bf4740ca4c9a01b56fc2f3519169f6d06162ea70abf32b7769d487db86f365084f1af5c7483789f3c1804d8af8bd7c7f8c9d0f06d828be20da775ab03c3ef5519d0b91b433b3d1fe67c8cee5489837a9160c7255, d=0x2d608962396c2f7366e293a9150de448c7d4d6dd7cf0b7b0439b8b4cd329b24dfcf362fb22df1add890dd3ea588dfb3cf42aabfbf80a045a8f976288d8e67481f52b9255e7e61c67ff0d97ef109596200b1938c6adc00742cf4ca30aff85442b1fee869bfa2bdbad815e7cdb11afd29b182e8dc47b205c42dd5f11a3c0acb9)
-----BEGIN RSA PRIVATE KEY-----
MIICWgIBAAKBgQD0IlPlm21bOk4GKX3xA+Ugwk3CSmRHC+bLWC/sdw7o9cjiLygG
YT3Mv3RHkb9HQMpMmgG1b8LzUZFp9tBhYupwq/Mrd2nUh9uG82UITxr1x0g3ifPB
gE2K+L18f4ydDwbYKL4g2ndasDw+9VGdC5G0M7PR/mfIzuVImDepFgxyVQIDAQAB
An8tYIliOWwvc2bik6kVDeRIx9TW3Xzwt7BDm4tM0ymyTfzzYvsi3xrdiQ3T6liN
+zz0Kqv7+AoEWo+XYojY5nSB9SuSVefmHGf/DZfvEJWWIAsZOMatwAdCz0yjCv+F
RCsf7oab+ivbrYFefNsRr9KbGC6NxHsgXELdXxGjwKy5AkEA9Zq9MRD7IKgbZ9Mu
TMUSF7W+WBIt8p+qJ9jl9xTqvIW/3tPPzBeRX+w4EyCNa1IuxEBkR0SSPbg2qchE
vlFJTQJBAP53qBRBK854VculpgwZ5T+vwb5vyTZ8DZ+zHBbCrN1eQz0AEHq09Z1D
q3XUZe0MLnSgz0bd1+zLBKoyW+NECSkCQF0RL9Ph/WdYjFoBei/5FWwKoIA7E1I3
EoFa/XltYa3ieNx1Iu7Rl3LjzjPhR/V9BN+1Dsq6vzfIEF6x1urPXpkCQFxFXzkY
+J2BnPqfMjqpGSuiu4omVrve98G03LaUGMKcb50q7M7R104TP5UWU29FP4Mi3IZB
4w4F/8cHQ7KA9SECQQDMY/gXVNIAZi7KnKFcvGlGckXLjrrNSuOp5QxGXVoQSDUV
oO6nANxkfi81ZVos5jZJ4dS+BiF1L4iUkV8wJKdS
-----END RSA PRIVATE KEY-----
Enter a message:this message for encryption
Encrypted:  b'23299cf60684ef3dbe461c12091f7a010169f347a316fe4cdba1a1fdd5d215af678d83a94d7ced54fcb5321e6ba9689f1d15ea491bd8accdadab9c554c826d89aa27d26761ce9fe1d3726ab5f0c7d65f8fa6e37ecfc059652e54cc8da9f7c9fe16c5e74621b5da2a00df8c48ec7f1d1ba814b0e0e7c21552e2ba6560c6156f66'
Decrypted:  this message for encryption
"""