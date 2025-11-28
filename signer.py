# signer.py
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def sign_file(file_path):
    with open("private.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    with open(file_path, "rb") as f:
        message = f.read()

    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    sig_file = file_path + ".sig"
    with open(sig_file, "wb") as f:
        f.write(signature)

    print(f"[+] File signed! Signature saved as {sig_file}")


def verify_file_signature(file_path, sig_file):
    with open("public.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    with open(file_path, "rb") as f:
        message = f.read()
    with open(sig_file, "rb") as f:
        signature = f.read()

    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("[✓] Signature is valid!")
    except:
        print("[✗] Signature is invalid!")
