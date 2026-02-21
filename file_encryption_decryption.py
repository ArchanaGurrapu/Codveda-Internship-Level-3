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
# generate_key()

print("1 Encrypt")
print("2 Decrypt")
ch = input("Enter choice: ")

if ch == "1":
    fname = input("Enter file name: ")
    encrypt_file(fname)

elif ch == "2":
    fname = input("Enter encrypted file name: ")
    decrypt_file(fname)
