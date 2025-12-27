from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"
ENCRYPTED_DIR = "encrypted_files"


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

    filename = input("Enter output file name (e.g. note1.enc): ").strip()

    if not filename:
        print("❌ Invalid file name.")
        return

    os.makedirs(ENCRYPTED_DIR, exist_ok=True)
    file_path = os.path.join(ENCRYPTED_DIR, filename)

    encrypted = cipher.encrypt(text)

    with open(file_path, "wb") as f:
        f.write(encrypted)

    print(f"🔒 Text encrypted and saved as {file_path}")


def decrypt_text():
    key = load_key()
    if not key:
        return

    os.makedirs(ENCRYPTED_DIR, exist_ok=True)

    filename = input("Enter encrypted file name to decrypt: ").strip()
    file_path = os.path.join(ENCRYPTED_DIR, filename)

    if not os.path.exists(file_path):
        print("❌ Encrypted file not found.")
        return

    cipher = Fernet(key)

    with open(file_path, "rb") as f:
        encrypted = f.read()

    try:
        decrypted = cipher.decrypt(encrypted)
        print("\n🔓 Decrypted text:")
        print(decrypted.decode())
    except Exception:
        print("❌ Decryption failed. Wrong key or corrupted file.")


def menu():
    print("\n=== Encryption Learning Lab ===")
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
