# Projeto: Criação de Ransomwqare utilizando o Python
Implementação da criptografia de vários arquivos em uma pasta.

## Criação da pasta para o projeto

```
mkdir projeto-ransomware
```

## Criação do ambiente virtual Python

```
python3 -m venv myenv
```

```
source myenv/bin/activate
```

## Instalação da biblioteca pyaes
[Biblioteca contendo a implementação do algoritmo de criptografia AES](https://pypi.org/project/pyaes/)

```
pip install pyaes
```

## Criação da pasta src

```
mkdir src
```

## Criação de pasta com documentos

```
cd src
```

```
mkdir docs
```

## Criação do arquivo encrypter.py

```
nano encrypter.py
```

![image](https://github.com/user-attachments/assets/897f0c94-80ec-4c5a-9734-f044fcf4a3f1)


### Criação do arquivo decrypter.py

```
nano decrypter.py
```

![image](https://github.com/user-attachments/assets/e779bba1-70e2-48a0-80b6-3b4d4fb48225)


### Criação dos arquivos alvo

```
mkdir docs
```

```
cd docs
```

```
nano senhas.txt
```

![image](https://github.com/user-attachments/assets/850c2c98-b8d7-4ef2-80d3-7f9ef476df0d)

```
nano importante.txt
```

![image](https://github.com/user-attachments/assets/93855255-9e85-4363-b123-05beb5daf923)

## Execução do ransomware

```
python encrypter.py
```

![image](https://github.com/user-attachments/assets/9fdf4ade-556a-41b0-a5c0-06e0821525bc)

![image](https://github.com/user-attachments/assets/2765151c-fd9d-41f7-a409-f1bf4a331ec8)

![image](https://github.com/user-attachments/assets/6f1172dd-b243-4275-9ae2-de245b9d681b)

```
python decrypter.py
```

![image](https://github.com/user-attachments/assets/69d633e8-eceb-4abe-8b79-d56c660db7f3)

![image](https://github.com/user-attachments/assets/c948e0e1-d295-4735-a2e9-0f344bc0755d)

![image](https://github.com/user-attachments/assets/742547d0-2909-40a9-9abe-cbcf578d1e13)


