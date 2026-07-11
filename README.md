# 📚 Book API

API REST desenvolvida com **Python** e **Flask** para gerenciamento de livros.

O projeto foi criado com o objetivo de estudar o desenvolvimento de APIs backend utilizando boas práticas de organização de código, persistência de dados, validação, tratamento de exceções e versionamento de banco de dados.

## 🚀 Tecnologias

* Python 3
* Flask
* SQLAlchemy
* Flask-Migrate (Alembic)
* MySQL 8
* Docker
* PyMySQL
* Pydantic

---

## 📂 Estrutura do Projeto

```text
book-api/
│
├── app.py
├── config.py
├── database/
├── exceptions/
├── migrations/
├── models/
├── routes/
├── schemas/
├── services/
└── requirements.txt
```

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd book-api
```

### 2. Crie o ambiente virtual

Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🐳 Executando o MySQL com Docker

```bash
docker run -d \
  --name mysql-book-api \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=bookdb \
  -p 3306:3306 \
  mysql:8.4
```

---

## 🔧 Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto.

```properties
DB_HOST=localhost
DB_PORT=3306
DB_NAME=bookdb
DB_USER=root
DB_PASSWORD=root

SECRET_KEY=minha-chave
```

---

## 🗄️ Executando as migrações

Inicializar o Alembic (apenas na primeira vez)

```bash
flask db init
```

Criar uma migration

```bash
flask db migrate -m "Create books table"
```

Aplicar as migrations

```bash
flask db upgrade
```

---

## ▶️ Executando a aplicação

```bash
python app.py
```

A API ficará disponível em:

```
http://localhost:5000
```

---

## 📌 Endpoints

| Método | Endpoint      | Descrição             |
| ------ | ------------- | --------------------- |
| GET    | `/books`      | Lista todos os livros |
| GET    | `/books/{id}` | Busca um livro por ID |
| POST   | `/books`      | Cadastra um livro     |
| PUT    | `/books/{id}` | Atualiza um livro     |
| DELETE | `/books/{id}` | Remove um livro       |

---

## 📖 Exemplo de Requisição

### POST /books

```json
{
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "pages": 464
}
```

---

## 📈 Funcionalidades implementadas

* Estrutura modular em camadas
* CRUD completo
* Persistência com MySQL
* SQLAlchemy ORM
* Flask-Migrate
* Validação com Pydantic
* Tratamento global de exceções
* Docker para banco de dados

---

## 📚 Objetivo

Este projeto faz parte de uma trilha de estudos em desenvolvimento backend com Python e Flask, explorando conceitos utilizados em aplicações reais, desde a construção de uma API REST até recursos avançados como autenticação, documentação e testes automatizados.
