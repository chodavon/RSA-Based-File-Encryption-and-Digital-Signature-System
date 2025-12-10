# RSA-Based-File-Encryption-and-Digital-Signature-System
# I. Introduction 
In today’s world, our important files (photos, documents, IDs, messages) can be easily stolen or changed. This project, “RSA-Based File Encryption and Digital Signature System”, is a simple Python program that uses RSA the same strong encryption used by banks and WhatsApp to keep files safe in two ways:
•	Encryption: Locks any file so only the person with the private key can open it.
•	Digital Signature: Adds a secure seal to prove the file is really from you and hasn’t been altered.
The goal I want to Build an easy tool that gives real security to everyone and I want to learn real RSA hands-on, use a trusted professional library, and make powerful protection simple enough for non-tech people (friends, family, teachers) to use safely.
# II. Design & Architecture
<img width="806" height="1114" alt="image" src="https://github.com/user-attachments/assets/d37d1d4c-2da7-4660-b23c-b71c932fa6e9" />

# III. implementation Detail
1. Libraries Used
The project uses the cryptography library.
This library helps us:
Create RSA keys
Encrypt and decrypt files
Sign and verify signatures
We also use normal Python file reading/writing to save data.

2. RSA Key Generation
The function generate_keys() creates two keys:
Private Key → kept secret
Public Key → shared with others
Both keys are saved into files:
private.pem
public.pem
These keys are required for encryption, decryption, signing, and verifying.

3. File Encryption
The public key is used to encrypt data.
Function: encrypt_file()
Steps:
Read the plaintext file.
Encrypt the content using RSA.
Save the result into ciphertext.bin.
Only the matching private key can decrypt it.

4. File Decryption
The private key is required to decrypt the file.
Function: decrypt_file()
Steps:
Read the encrypted file (ciphertext.bin)
Use the private key to decrypt the content
Save the original message into decrypted.txt

5. File Signing
The private key is used to sign a file.
Function: sign_file()
The program:
Reads the file
Creates a digital signature using SHA-256
Saves the signature as a new file (example: test.txt.sig)
This proves the file comes from the real sender.

6. Signature Verification
The public key is used to check if a signature is valid.
Function: verify_file_signature()
The program:
Reads the original file
Reads the .sig signature file
Uses the public key to verify it
Shows:
Valid → file is original and not changed
Invalid → file was changed or signature is wrong

7. Program Structure
main.py → Menu and program controller
keys.py → Generates RSA keys
encryptor.py → Encrypts and decrypts files
signer.py → Signs and verifies files

8. Cryptography Methods Used
RSA → for encryption, decryption, signing, verifying
SHA-256 → for hashing the message during signing
Padding (OAEP & PSS) → makes RSA safer from attacks

# IV. Usage Guide
Option 1 → Generate RSA Keys
Select 1
Program creates:
private.pem
public.pem
These two files must exist before doing encryption or signing.

Option 2 → Encrypt File
Create any plaintext file (example: message.txt)
Choose 2
Enter file name:
message.txt
Program outputs:
ciphertext.bin (encrypted file)

Option 3 → Decrypt File
Choose 3
Enter encrypted file name:
ciphertext.txt
Enter output file:
decrypted.txt
Program creates:
decrypted.txt (original message restored)

Option 4 → Sign File
Choose 4
Enter file to sign:
message.txt
Program creates:
message.txt.sig (digital signature)

Option 5 → Verify Signature
Choose 5
Enter file:
message.txt
Enter signature file:
message.txt.sig
Program displays:
[✓] Signature is valid!
or
[✗] Signature is invalid!

# V. Conclusion and Future Work
This project successfully demonstrates how RSA can be used for secure communication. It shows key generation, file encryption, file decryption, digital signatures, and verification. The implementation teaches how public and private keys work together to provide confidentiality and authenticity.

However, the system can still be improved. Future work may include:
Adding password protection for the private key
Supporting larger files using hybrid encryption (AES + RSA)
Creating a GUI version of the system
Adding logging to monitor activity
Improving error handling for missing files.

# VI. References


