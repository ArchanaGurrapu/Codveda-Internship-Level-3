LEVEL 3 - ADVANCED 🔹 Task 1: Basic File Encryption/Decryption

I developed a Python-based file encryption and decryption system to secure data using cryptographic techniques. The program allows users to select a file, encrypt it using a secure encryption key, and decrypt it back to its original form. This task helped me understand file handling, data security concepts, and the use of cryptography libraries in Python.

    from cryptography.fernet import Fernet
    
    # Generate key (run only once)
    def generate_key():
        key = Fernet.generate_key()
        with open("secret.key", "wb") as f:
            f.write(key)
    
    def load_key():
        return open("secret.key", "rb").read()
    
    def encrypt_file(file):
        key = load_key()
        f = Fernet(key)
        with open(file, "rb") as f1:
            data = f1.read()
        encrypted = f.encrypt(data)
        with open(file + ".enc", "wb") as f2:
            f2.write(encrypted)
        print("File Encrypted Successfully")
    
    def decrypt_file(file):
        key = load_key()
        f = Fernet(key)
        with open(file, "rb") as f1:
            data = f1.read()
        decrypted = f.decrypt(data)
        with open("decrypted.txt", "wb") as f2:
            f2.write(decrypted)
        print("File Decrypted Successfully")
    
    # 🔹 Run this line ONLY ONCE
    generate_key()
    
    print("1 Encrypt")
    print("2 Decrypt")
    ch = input("Enter choice: ")
    
    if ch == "1":
        fname = input("Enter file name: ")
        encrypt_file(fname)
    
    elif ch == "2":
        fname = input("Enter encrypted file name: ")
        decrypt_file(fname)


LEVEL 3 - ADVANCED 🔹 Task 2: N-Queens Problem

Implemented the N-Queens problem using the backtracking algorithm in Python. The program places N queens on a chessboard such that no two queens attack each other. This task helped me strengthen my understanding of recursion, backtracking, and algorithmic problem-solving techniques.


