# Para installar todas as libs
pip install -r requirements.txt
# Enviar versão das libs para requirements
pip freeze > requirements.txt
# Para importar arquivos a partir da raiz do projeto
obsoluct_path = os.path.abspath(os.curdir)
sys.path.insert(0, obsoluct_path)

# Modelagem
![alt text](image.png)

# Envio um comando para limpar o terminal
os.system('cls' if os.name == 'nt' else 'clear')