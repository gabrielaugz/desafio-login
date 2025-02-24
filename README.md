# Desafio-Login

Projeto em Django que implementa telas de **Login** e **Registro** com validações específicas, além de transição uma tela de exemplo de **Menu**. 

## Funcionalidades

- **Tela de Login**:
  - Validação de e-mail e senha (campos não podem estar vazios).
  - Erros tratados:
    - E-mail inexistente: "E-mail inexistente"
    - Senha inválida (quando e-mail existe, mas a senha não confere): "Senha inválida"
  - Redirecionamento para a tela de Registro (link "Registre-se").
  - Ao logar com sucesso, o usuário é direcionado para a tela de **Menu**.

- **Tela de Registro**:
  - Formulário com campos: **nome**, **e-mail**, **senha** e **confirmar senha**.
  - Validações:
    - Nome: apenas letras.
    - E-mail: formato válido com "@", etc.
    - Senha: ao menos 8 caracteres, 1 caractere especial, 1 número, 1 letra maiúscula.
    - Confirmar senha: deve ser idêntica à senha.
  - Botão "Registrar" (envia o formulário) e botão "Cancelar" (retorna à tela de Login).
  - Possibilidade de exibir ou ocultar os caracteres da senha (por meio de um pequeno script JS).

- **Tela de Menu**:
  - Exibida após login/registro com sucesso.  

## Pré-requisitos

- Python 3.11 (ou versão compatível com Django 5.x)
- Pip (gerenciador de pacotes do Python)
- MySQL (versão 8 ou superior) **ou** MariaDB 10.5 ou superior (caso vá realmente usar MySQL em produção). A versão é de extrema importância.

> Se preferir, você pode utilizar o SQLite (padrão do Django) apenas para teste local, alterando o `settings.py` para `'django.db.backends.sqlite3'`.

## Instalação

1. **Clonar o repositório**:
   ```console
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. **Criando e ativando ambiente virtual**
    ```console
    python -m venv .venv
    .venv\Scripts\activate
    ```
3. **Instalando as dependências**  
    ```console
    pip install -r requirements.txt
    ```
4. **Criação do Banco de Dados**
    ```console
    CREATE DATABASE desafio_login;
    ```
5. **Execute as migrações**
    ```console
    python manage.py makemigrations
    python manage.py migrate
    ```
6. **Execute o servidor localmente**
    ```console
    python manage.py runserver
    Acesse http://127.0.0.1:8000/ para ver a tela inicial 
    ```