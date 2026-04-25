from cryptography.fernet import Fernet
import os

# 1. Initialize the Key (The "Master Key")
def initialize_key():
    if not os.path.exists("master.key"):
        key = Fernet.generate_key()
        with open("master.key", "wb") as key_file:
            key_file.write(key)

# 2. Load the Key
def load_key():
    return open("master.key", "rb").read()

# 3. Encrypt Function
def encrypt_val(passthrough_text):
    f = Fernet(load_key())
    return f.encrypt(passthrough_text.encode()).decode()

# 4. Decrypt Function
def decrypt_val(encrypted_text):
    f = Fernet(load_key())
    return f.decrypt(encrypted_text.encode()).decode()