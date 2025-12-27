from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"
DATA_FILE = "secret.txt"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print("🔑 Key generated and saved as key.key")

def load_key():
    if not os.path.exists(KEY_FILE):
        print("❌ Key not found. Generate a key first.")
        return None
    return open(KEY_FILE, "rb").read()

def encrypt_text():
    key = load_key()
    if not key:
        return

    cipher = Fernet(key)
    text = input("Enter text to encrypt:\n> ").encode()

    encrypted = cipher.encrypt(text)

    with open(DATA_FILE, "wb") as f:
        f.write(encrypted)

    print("🔒 Text encrypted and saved to secret.txt")

def decrypt_text():
    key = load_key()
    if not key:
        return

    if not os.path.exists(DATA_FILE):
        print("❌ No encrypted file found.")
        return

    cipher = Fernet(key)

    encrypted = open(DATA_FILE, "rb").read()
    decrypted = cipher.decrypt(encrypted)

    print("\n🔓 Decrypted text:")
    print(decrypted.decode())

def menu():
    print("\n=== Secure Text Tool ===")
    print("1. Generate Key (run once)")
    print("2. Encrypt Text")
    print("3. Decrypt Text")
    print("4. Exit")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        encrypt_text()
    elif choice == "3":
        decrypt_text()
    elif choice == "4":
        print("👋 Exiting")
        break
    else:
        print("❌ Invalid choice")
