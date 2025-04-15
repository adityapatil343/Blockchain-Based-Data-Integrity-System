import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import hashlib
import base64
import os

# Function to generate encryption key from a user-defined 5-character string
def generate_key(user_key: str) -> bytes:
    # Validate the user key: must be 5 characters and alphanumeric
    if len(user_key) != 5 or not user_key.isalnum():
        raise ValueError("Key must be 5 characters long (letters and numbers only).")
    
    # Generate the encryption key using SHA256 hash and base64 encoding
    return base64.urlsafe_b64encode(hashlib.sha256(user_key.encode()).digest())

# Function to encrypt a file using the generated key
def encrypt_file(filepath: str, key: bytes):
    # Read the file's data in binary mode
    with open(filepath, 'rb') as file:
        data = file.read()

    # Initialize the Fernet encryption tool with the generated key
    fernet = Fernet(key)
    # Encrypt the file's data
    encrypted = fernet.encrypt(data)

    # Save the encrypted data to a new file with a '.enc' extension
    enc_filename = filepath + '.enc'
    with open(enc_filename, 'wb') as file:
        file.write(encrypted)

    # Notify the user that the file was encrypted successfully
    print(f"\n✅ File encrypted successfully: {enc_filename}")

# Function to decrypt a file using the generated key
def decrypt_file(filepath: str, key: bytes):
    # Ensure that the file is encrypted (ends with .enc)
    if not filepath.endswith('.enc'):
        raise ValueError("Decryption requires a file ending with .enc")

    # Read the encrypted file's data in binary mode
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()

    # Initialize the Fernet decryption tool with the generated key
    fernet = Fernet(key)
    try:
        # Decrypt the file's data
        decrypted = fernet.decrypt(encrypted_data)
    except Exception:
        # Handle decryption failure (wrong key or corrupted file)
        print("\n❌ Decryption failed: Invalid key or corrupted file.")
        return

    # Save the decrypted data to a new file with a '.dec' extension
    dec_filename = filepath.replace('.enc', '.dec')
    with open(dec_filename, 'wb') as file:
        file.write(decrypted)

    # Notify the user that the file was decrypted successfully
    print(f"\n✅ File decrypted successfully: {dec_filename}")

# Function to display a file dialog for the user to select a file
def select_file() -> str:
    try:
        # Create a Tkinter root window (which will not be displayed)
        root = tk.Tk()
        root.withdraw()  # Hide main window
        root.attributes('-topmost', True)  # Bring file dialog to front
        # Open the file selection dialog and get the file path
        filepath = filedialog.askopenfilename(title="Select a file")
        return filepath
    except Exception as e:
        # If there is an error opening the file dialog, print the error and return an empty string
        print(f"❌ Error opening file dialog: {e}")
        return ""

# Main entry point of the program
if __name__ == "__main__":
    # Display the tool's options for the user
    print("🔐 AES File Encrypt/Decrypt Tool")
    print("1️⃣  Encrypt a file")
    print("2️⃣  Decrypt a file")

    # Get the user's choice for encryption or decryption
    choice = input("Select an option (1 or 2): ").strip()

    # Check if the input choice is valid
    if choice not in ['1', '2']:
        print("❌ Invalid option. Please choose 1 or 2.")
        exit()

    # Ask the user to select a file
    print("\n📂 Please select a file...")
    filepath = select_file()

    # If no file was selected, exit the program
    if not filepath:
        print("❌ No file selected. Exiting.")
        exit()

    # Prompt the user for a 5-character key to be used for encryption/decryption
    user_key = input("🔑 Enter a 5-character key (letters & numbers only): ").strip()

    try:
        # Generate the encryption key from the user's input key
        key = generate_key(user_key)

        # Perform encryption or decryption based on user's choice
        if choice == '1':
            encrypt_file(filepath, key)  # Encrypt the file
        elif choice == '2':
            decrypt_file(filepath, key)  # Decrypt the file
    except Exception as e:
        # Handle any errors (e.g., wrong key, file errors, etc.)
        print(f"\n❌ Error: {e}")
