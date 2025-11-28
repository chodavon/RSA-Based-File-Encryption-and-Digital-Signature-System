# encryptor.py
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def encrypt_file(input_file, output_file="ciphertext.txt"):
    # Load public key
    with open("public.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Read plaintext from file
    with open(input_file, "rb") as f:
        plaintext = f.read()

    # Encrypt
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save ciphertext
    with open(output_file, "wb") as f:
        f.write(ciphertext)

    print(f"[+] File encrypted and saved as {output_file}")


def decrypt_file(input_file="ciphertext.txt", output_file="decrypted.txt"):
    # Load private key
    with open("private.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    # Read ciphertext
    try:
        with open(input_file, "rb") as f:
            ciphertext = f.read()
    except FileNotFoundError:
        print(f"[!] Error: File '{input_file}' not found!")
        print("[!] Make sure you encrypted a file first (option 2)")
        return

    # Decrypt
    try:
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    except ValueError:
        print(f"[!] Error: '{input_file}' is not a valid encrypted file!")
        print("[!] Make sure you're using a file that was encrypted with option 2")
        print("[!] The default encrypted file is 'ciphertext.bin'")
        return

    # Save decrypted message
    with open(output_file, "wb") as f:
        f.write(plaintext)

    print(f"[+] File decrypted and saved as {output_file}")
