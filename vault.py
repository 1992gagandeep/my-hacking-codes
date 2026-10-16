import os
from cryptography.fernet import Fernet

# 1. Security Check
pin = input("Vault PIN Enter Karo: ")
if pin != "88921625":
    print("Galat PIN ! Bhag Jao.")
    exit()

# 2. Chabi (Key Banana)
if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as k:
        k.write(key)
else:
    with open("secret.key", "rb") as k:
        key = k.read()

cipher = Fernet(key)

# 3. Lock/Unlock Menu
print("\n---MyLifeLine Secret Vault ----")
print("Folder: mylifeline_data")
action = input("Type 'lock' or 'unlock': ")

name = input("File ka naam likho: ")
path = "mylifeline_data/" + name

if action == "lock":
    with open(path, "rb") as f:
        data = f.read()
    encrypted = cipher.encrypt(data)
    with open(path, "wb") as f:
        f.write(encrypted)
    print("File Lock (Encrypt) ho gayi")

elif action == "unlock":
    with open(path, "rb") as f:
        data = f.read()
    decrypted = cipher.decrypt(data)
    with open(path, "wb") as f:
        f.write(decrypted)
    print("File UNLOCK (Original) ho gayi")
