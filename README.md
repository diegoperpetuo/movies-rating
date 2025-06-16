# ⭐ Movies Rating - Avaliações de Filmes

### Membros:
- Danilo Santana
- Diego Perpétuo
- Luccas Pino
- Milton Kiefer

Este é o backend de avaliações da aplicação **Movies Reviews**, responsável por permitir que usuários logados realizem o CRUD (criação, leitura, atualização e remoção) de reviews de filmes.

## 📦 Tecnologias Utilizadas
- Python
- FastAPI
- JWT (validação de token)
- SQLite (ou outro banco de dados relacional)
- Pydantic

## 🚀 Como rodar localmente

1. Clone este repositório:
   ```bash
   git clone https://github.com/diegoperpetuo/movies-fastapi.git
   cd rating
   
2. Instale as dependências:
   ```bash
    pip install -r requirements.txt
    py -m pip install email-validator

3. Inicie o servidor:
   ```bash
    uvicorn app.main:app --reload --port 8001

### 🔐 Integração com Autenticação

Este serviço depende do backend movies-fastapi para autenticação. O usuário realiza login e recebe um token JWT, que deve ser incluído no cabeçalho das requisições para acessar as rotas protegidas.

## 📂 Estrutura do Projeto
   ```bash
    app/
    ├── main.py          # Ponto de entrada da aplicação
    ├── models.py        # Modelos de dados (Review, Usuário)
    ├── routes.py        # Rotas protegidas com autenticação JWT
    ├── auth.py          # Funções de verificação de token JWT
    └── database.py      # Configuração e acesso ao banco de dados
