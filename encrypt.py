import json
import requests
from cryptography.fernet import Fernet

def lambda_handler(event, context):

    key = Fernet.generate_key()
    
    cipher_suite = Fernet(key)
    
    cipher_text = cipher_suite.encrypt(b"123")
    
    print(f"Cipher text: {cipher_text}")
    
    original_text = cipher_suite.decrypt(cipher_text)
    
    print(f"Original text: {original_text}")