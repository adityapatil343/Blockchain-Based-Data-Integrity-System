import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import hashlib
import base64
import os

def generate_key(user_key: str) -> bytes:
    if len(user_key) != 5 or not user_key.isalnum():
        raise ValueError("Key must be 5 characters long (letters and numbers only).")
    return base64.urlsafe_b64encode(hashlib.sha256(user_key.encode()).digest())

def encrypt_file(filepath: str, key: bytes):
    with open(filepath, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    enc_filename = filepath + '.enc'
    with open(enc_filename, 'wb') as file:
        file.write(encrypted)

    print(f"\n✅ File encrypted successfully: {enc_filename}")

def decrypt_file(filepath: str, key: bytes):
    if not filepath.endswith('.enc'):
        raise ValueError("Decryption requires a file ending with .enc")

    with open(filepath, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(encrypted_data)
    except Exception:
        print("\n❌ Decryption failed: Invalid key or corrupted file.")
        return

    dec_filename = filepath.replace('.enc', '.dec')
    with open(dec_filename, 'wb') as file:
        file.write(decrypted)

    print(f"\n✅ File decrypted successfully: {dec_filename}")

def select_file() -> str:
    root = tk.Tk()
    root.withdraw()  # Hide main window
    filepath = filedialog.askopenfilename(title="Select a file")
    return filepath

if __name__ == "__main__":
    print("🔐 AES File Encrypt/Decrypt Tool")
    print("1️⃣  Encrypt a file")
    print("2️⃣  Decrypt a file")

    choice = input("Select an option (1 or 2): ").strip()

    if choice not in ['1', '2']:
        print("❌ Invalid option. Please choose 1 or 2.")
        exit()

    print("\n📂 Please select a file...")
    filepath = select_file()

    if not filepath:
        print("❌ No file selected. Exiting.")
        exit()

    user_key = input("🔑 Enter a 5-character key (letters & numbers only): ").strip()

    try:
        key = generate_key(user_key)

        if choice == '1':
            encrypt_file(filepath, key)
        elif choice == '2':
            decrypt_file(filepath, key)
    except Exception as e:
        print(f"\n❌ Error: {e}")
