import base64
from cryptography.fernet import Fernet
import sys

def decrypt_logs(log_file):
    try:
        with open("key.key", "rb") as f:
            key = f.read()
        cipher = Fernet(key)
        
        with open(log_file, "r") as f:
            for line in f:
                try:
                    encrypted_data = base64.b64decode(line.strip())
                    decrypted_data = cipher.decrypt(encrypted_data).decode()
                    print(decrypted_data)
                except Exception as e:
                    print(f"Error decrypting line: {e}")
    except FileNotFoundError:
        print("Error: key.key or log file not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decrypt_logs.py <log_file>")
        sys.exit(1)
    decrypt_logs(sys.argv[1])