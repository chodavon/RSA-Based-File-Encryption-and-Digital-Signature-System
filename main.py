# main.py
from keys import generate_keys
from encryptor import encrypt_file, decrypt_file
from signer import sign_file, verify_file_signature

def menu():
    print("\n==== RSA FILE SYSTEM ====")
    print("1. Generate RSA Keys")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Sign File")
    print("5. Verify Signature")
    print("6. Exit")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        generate_keys()

    elif choice == "2":
        file = input("Enter file to encrypt (e.g., message.txt): ")
        encrypt_file(file)

    elif choice == "3":
        input_file = input("Enter ciphertext file (default ciphertext.bin): ") or "ciphertext.bin"
        output_file = input("Enter output file (default decrypted.txt): ") or "decrypted.txt"
        decrypt_file(input_file, output_file)

    elif choice == "4":
        file = input("Enter file to sign: ")
        sign_file(file)

    elif choice == "5":
        file = input("Enter file to verify: ")
        sig = input("Enter signature file: ")
        verify_file_signature(file, sig)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
