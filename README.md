# Task Django

Instruções para configurar e executar o projeto localmente.

## Pré-requisitos

* Python 3.10+ instalado
* Git

## Passo a Passo para Execução

1. **Acesse a pasta do projeto:**
   cd task_django

2. **Crie e ative o ambiente virtual (venv):**
   * Linux/macOS:
     python3 -m venv venv
     source venv/bin/activate
   * Windows:
     python -m venv venv
     .\venv\Scripts\activate

3. **Instale as dependências:**
   pip install -r requirements.txt

4. **Execute as migrações do banco de dados:**
   python manage.py migrate

5. **Crie um superusuário para acessar o painel administrativo:**
   python manage.py createsuperuser

6. **Inicie o servidor de desenvolvimento:**
   python manage.py runserver

7. **Acesse a aplicação:**
   Abra o seu navegador e acesse a área administrativa em http://127.0.0.1:8000/admin
