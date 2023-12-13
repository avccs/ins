from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


key= RSA.generate(2048)
priv_key = key.export_key()
pub_key = key.publickey().export_key()


orignal_msg = b"This is original document content."
modified_msg = b"This is modified document content."


orignal_hash = SHA256.new(orignal_msg)
modified_hash = SHA256.new(modified_msg)


signature = pkcs1_15.new(RSA.import_key(priv_key)).sign(orignal_hash)


try:
    pkcs1_15.new(RSA.import_key(pub_key)).verify(modified_hash, signature)
    print("Valid Signature")
except (ValueError, TypeError):
    print("Invalid Signature")


"""
    OUTPUT:-
    Invalid Signature (if the document is modified)

    OR 
    
    OUTPUT:-
    Valid Signature (if the document is not modified)
"""