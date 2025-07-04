# Instruções para Executar o Projeto Django Localmente

Este projeto utiliza o framework Django e depende de um banco de dados PostgreSQL hospedado na Supabase. Siga os passos abaixo para configurá-lo e executá-lo localmente.

## Pré-requisitos

- Python 3.8+ instalado
- `pip` instalado
- `virtualenv` (opcional, mas recomendado)
- Acesso à internet

## Passos para Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```ini
# Banco de Dados
DB_NAME=postgres
DB_USER=postgres.[SEU_IDENTIFICADOR_SUPABASE]
DB_PASSWORD=[SUA_SENHA_SUPABASE]
DB_HOST=aws-0-us-east-2.pooler.supabase.com
DB_PORT=5432

# Supabase
SUPABASE_URL=[SUA_SUPABASE_URL]
SUPABASE_API_KEY=[SUA_SUPABASE_API_KEY]
```

> ⚠️ **Nunca compartilhe suas credenciais diretamente em repositórios públicos.** Use variáveis de ambiente e arquivos `.env` no `.gitignore`.

### 5. Execute as migrações
```bash
python manage.py migrate
```

### 6. Crie um superusuário (opcional, para acessar o admin e painel do vendedor)
```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor de desenvolvimento
```bash
python manage.py runserver
```

O projeto estará disponível em `http://127.0.0.1:8000/`.

---

## Observações

- Certifique-se de que a conexão com a Supabase está ativa e que seu IP tem permissão para acessar o banco.
- Em produção, use variáveis de ambiente seguras e configure um servidor WSGI como Gunicorn ou uWSGI.