# Crypto-basics-demo-project

A small Python-based learning project built to understand how **encryption works in practice**, and how it differs from hashing.

This project focuses on:
- Symmetric encryption
- Keys and reversibility
- Why encrypted data is unrecoverable without the correct key

This is **not a production-ready application**.  
It is a **learning and experimentation project**.

---

## 🧠 What This Project Demonstrates

- Difference between **hashing vs encryption**
- Use of **symmetric key encryption**
- Why encryption is reversible (with a key)
- Why losing a key means permanent data loss
- Basic secure file handling concepts

---

## 🛠 Tech Stack

- Python 3
- `cryptography` library (Fernet encryption)

---

## 📂 Project Structure
encryption-learning-lab/
│
├── secure_text.py
├── key.key
├── encrypted_files/
│ ├── note1.enc
│ ├── credentials.enc
│ └── example.enc
└── README.md


> The `encrypted_files/` folder can contain **any number of encrypted files**.

---

## 🔑 How Encryption Works in This Project

- A **single secret key** is generated once and stored in `key.key`
- The same key is used to:
  - encrypt text into a file
  - decrypt that file back into plaintext
- If the key is lost, encrypted data **cannot be recovered**

---

## 📦 Installation

Install the required dependency:

```bash
pip install cryptography

▶️ Usage

Run the program:

python secure_text.py


You will see a menu with options to:

Generate a key (run once)

Encrypt text

Decrypt text

Exit

📁 Working With Multiple Files

This project does NOT limit you to a single secret.txt file.

Encrypting multiple files

When encrypting, you can:

Choose a custom filename

Save each encrypted output as a separate .enc file

Example filenames:

note1.enc
api_keys.enc
journal.enc


Each encrypted file:

Is independent

Can be decrypted later using the same key

Decrypting a specific file

To decrypt:

Select the encrypted file you want

Provide the correct key

The original text will be restored

You can encrypt and decrypt any number of files, as long as:

The same key is used

The encrypted file is not modified

⚠️ Important Security Notes

❌ Losing key.key means permanent data loss

❌ Anyone with access to the key can decrypt all files

❌ This project does not store passwords or plaintext

✅ Encryption is local and file-based

🎯 Scope & Intent

This project is intentionally kept small to:

Focus on core cryptographic concepts

Avoid unnecessary features like authentication or databases

Reduce security anti-patterns

It is meant as a foundation for understanding secure systems, not as a finished product.

🚀 Possible Extensions (Future Work)

Password-based key derivation (PBKDF2)

File encryption (PDFs, images)

Client-side encryption using Web Crypto API

Secure note-sharing experiments

CLI arguments instead of menu-based input

📌 Disclaimer

This project is for educational purposes only.
Do not use it to store sensitive or real-world confidential data.
