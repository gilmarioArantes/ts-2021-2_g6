- Abra sua IDE diretamente na pasta tb_test

- Criar um ambiente
    Se não tiver o venv instalado: apt install pythonx.x-venv (python3.8-venv no meu caso)
    python -m venv venv
  
- Entrar no ambiente
    source ./venv/bin/activate
    No windows é diferente:
    ./venv/Scripts/Activate
    
- Instalar as bibliotecas: 
    pip install -r requirements.txt

- Rodar o pytest
    pytest -v
