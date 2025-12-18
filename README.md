# RSA-Based File Encryption and Digital Signature System
## 1. Introduction

In today’s digital world, important files such as documents, photos, IDs, and messages can be stolen, modified, or forged. This project, **RSA-Based File Encryption and Digital Signature System**, is a Python-based application that demonstrates how **RSA public-key cryptography** can be used to protect files.

The system provides security in two ways:
- **Encryption**: Protects file confidentiality
- **Digital Signature**: Ensures file authenticity and integrity

This project is designed to be simple, educational, and suitable for students and beginners.

---

## 2. Features

- RSA key pair generation
- File encryption and decryption
- Digital signature creation
- Digital signature verification
- Menu-based command-line interface
- Uses secure cryptographic standards

---

## 3. Technologies and Algorithms

- **Language**: Python 3.12
- **Library**: cryptography
- **Algorithms**:
  - RSA
  - SHA-256
  - OAEP Padding (Encryption)
  - PSS Padding (Signature)

---

## 4. System Architecture

The system follows a modular design:

- `main.py` – Program controller and menu
- `keys.py` – RSA key generation
- `encryptor.py` – Encryption and decryption
- `signer.py` – Digital signing and verification

---

## 5. Project Structure
RSA_File_Security/
│
├── main.py # Main program and menu controller
├── keys.py # RSA key pair generation
├── encryptor.py # File encryption and decryption logic
├── signer.py # Digital signature and verification
│
├── message.txt # Sample plaintext file
├── private.pem # Generated RSA private key
├── public.pem # Generated RSA public key
├── ciphertext.txt # Encrypted output file
├── decrypted.txt # Decrypted file (original content)
├── message.txt.sig # Digital signature file

## 6. Usage Guide

### Option 1: Generate RSA Keys

1. Select option **1**
2. The program creates:

   * `private.pem`
   * `public.pem`

These files must exist before encryption or signing.

---

### Option 2: Encrypt a File

1. Create a plaintext file (example: `message.txt`)
2. Select option **2**
3. Enter the file name

Output:

* `ciphertext.txt` (encrypted file)

---

### Option 3: Decrypt a File

1. Select option **3**
2. Enter encrypted file name: `ciphertext.txt`
3. Enter output file name: `decrypted.txt`

Result:

* Original content is restored

---

### Option 4: Sign a File

1. Select option **4**
2. Enter file name: `message.txt`

Output:

* `message.txt.sig` (digital signature file)

---

### Option 5: Verify a Signature

1. Select option **5**
2. Enter file name
3. Enter signature file

Program displays:

* `[✓] Signature is valid!`
* `[✗] Signature is invalid!`

---

### 7. Required Library Installation

Before running the program, install the required dependency:

```bash
pip install cryptography
```
### 8. System Requirements

- Operating System: Windows / Linux / macOS
- Python Version: **Python 3.12**

