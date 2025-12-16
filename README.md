# 🔐 RSA-Based File Encryption and Digital Signature System

## I. Introduction

In today’s digital world, important files such as photos, documents, IDs, and messages can be easily stolen, modified, or forged. This project, **"RSA-Based File Encryption and Digital Signature System"**, is a simple Python-based application that demonstrates how **RSA cryptography** (the same technology used by banks and secure messaging apps) can be used to protect files.

This system provides security in two main ways:

* **Encryption**: Locks a file so that only the person who owns the private key can open it.
* **Digital Signature**: Adds a secure seal to prove that a file is genuinely from the sender and has not been altered.

The goal of this project is to build an easy-to-use security tool while gaining hands-on experience with real RSA cryptography using a trusted professional library. The system is designed to be simple enough for non-technical users such as friends, family, teachers, and students.

---

## II. Design & Architecture

The system is divided into clear modules, each responsible for a specific task:

* **Key generation**
* **File encryption and decryption**
* **Digital signing and verification**
* **Menu-based user control**

The overall architecture follows a modular design to keep the code easy to understand, maintain, and extend.

<img width="806" height="1114" alt="System Architecture" src="https://github.com/user-attachments/assets/d37d1d4c-2da7-4660-b23c-b71c932fa6e9" />

---

## III. Implementation Details

### 1. Libraries Used

This project uses the **cryptography** Python library, which provides secure and well-tested cryptographic functions.

The library is used to:

* Generate RSA key pairs
* Encrypt and decrypt files
* Sign files and verify digital signatures

Standard Python file input/output is also used to read and write files.

---

### 2. RSA Key Generation

The function `generate_keys()` creates two cryptographic keys:

* **Private Key** → kept secret by the owner
* **Public Key** → shared with others

These keys are saved as:

* `private.pem`
* `public.pem`

Both keys are required for encryption, decryption, signing, and verification.

---

### 3. File Encryption

File encryption is performed using the **public key**.

**Function:** `encrypt_file()`

Steps:

1. Read the plaintext file
2. Encrypt the content using RSA
3. Save the encrypted output as `ciphertext.txt`

Only the corresponding private key can decrypt the encrypted file.

---

### 4. File Decryption

File decryption requires the **private key**.

**Function:** `decrypt_file()`

Steps:

1. Read the encrypted file (`ciphertext.txt`)
2. Decrypt the content using the private key
3. Save the original data as `decrypted.txt`

---

### 5. File Signing

Digital signatures are created using the **private key**.

**Function:** `sign_file()`

Steps:

1. Read the file
2. Generate a SHA-256 hash
3. Create a digital signature
4. Save the signature as a `.sig` file (example: `message.txt.sig`)

This proves the file was created by the legitimate sender.

---

### 6. Signature Verification

Signature verification is done using the **public key**.

**Function:** `verify_file_signature()`

Steps:

1. Read the original file
2. Read the signature file
3. Verify the signature using the public key

Results:

* **Valid** → File is authentic and unchanged
* **Invalid** → File was modified or signature is incorrect

---

### 7. Program Structure

```
main.py      → Menu and program controller
keys.py      → RSA key generation
encryptor.py → File encryption and decryption
signer.py    → Digital signing and verification
```

---

### 8. Cryptography Methods Used

* **RSA** → Encryption, decryption, signing, and verification
* **SHA-256** → Hashing during digital signing
* **OAEP & PSS Padding** → Improves RSA security and protects against attacks

---

## IV. Usage Guide

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

### Required Library Installation

Before running the program, install the required dependency:

```bash
pip install cryptography
```

---

## V. Conclusion and Future Work

This project demonstrates how RSA cryptography can be used to secure files through encryption and digital signatures. It provides a clear understanding of how public and private keys work together to ensure confidentiality and authenticity.

Possible future improvements include:

* Password protection for private keys
* Support for large files using hybrid encryption (AES + RSA)
* Graphical User Interface (GUI)
* Logging and auditing features
* Improved error handling

---

## VI. References

* [https://www.geeksforgeeks.org/computer-networks/cryptography-and-its-types/](https://www.geeksforgeeks.org/computer-networks/cryptography-and-its-types/)
* [https://stackoverflow.com/questions/20531474/decrypting-with-rsa-private-key](https://stackoverflow.com/questions/20531474/decrypting-with-rsa-private-key)
* [https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/](https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/)
* [https://www.askpython.com/python/examples/rsa-algorithm-in-python](https://www.askpython.com/python/examples/rsa-algorithm-in-python)
