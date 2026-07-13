# UXBlog

Blog institucional desenvolvido em Django, com painel administrativo customizado, API REST autenticada via JWT e frontend server-side renderizado. Projeto desenvolvido no módulo de Django do curso de Python do Senac-RS.

## Sumário

- [Visão geral](#visão-geral)
- [Stack técnica](#stack-técnica)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Configuração do ambiente](#configuração-do-ambiente)
- [Executando o projeto](#executando-o-projeto)
- [API REST](#api-rest)
- [Licença](#licença)

## Visão geral

O UXBlog permite a publicação e listagem de artigos organizados por categoria, com paginação incremental ("carregar mais"), página de detalhes do artigo, formulário de contato e um painel administrativo com tema visual próprio. Também expõe uma API REST somente leitura para artigos e categorias, além de um endpoint autenticado para criação de artigos.

Principais funcionalidades:

- Listagem de artigos com filtro por categoria e paginação via `fetch()` (sem reload de página).
- Página de detalhes de artigo.
- Formulário de "Fale conosco" que persiste mensagens no banco.
- Painel Django Admin com tema visual customizado (`admin_theme.css`).
- API REST com autenticação JWT (`djangorestframework-simplejwt`).
- Upload de imagens de artigos com armazenamento em `media/`.

## Stack técnica

| Camada | Tecnologia |
| --- | --- |
| Backend | Django 6.0 |
| API | Django REST Framework + Simple JWT |
| Banco de dados | PostgreSQL (`psycopg2-binary`) / MySQL (`mysqlclient`) |
| Arquivos estáticos | WhiteNoise |
| Servidor de aplicação | Gunicorn |
| Imagens | Pillow |

## Estrutura do projeto

```
dev_blog/
├── core/                  # Configuração do projeto (settings, urls, wsgi)
├── blog/
│   ├── models.py          # Categoria, Artigo, MensagemContato
│   ├── views.py           # Views HTML + endpoints da API REST
│   ├── forms.py           # Formulário de contato
│   ├── admin.py           # Customização do Django Admin
│   ├── templates/         # Templates HTML (site + admin)
│   └── static/blog/       # CSS, JS e imagens do frontend
├── media/                 # Uploads de usuário (git-ignored)
├── manage.py
└── requirements.txt
```

## Pré-requisitos

- Python 3.12+
- PostgreSQL ou MySQL em execução (dependendo do `DATABASE_ENGINE` escolhido)

## Configuração do ambiente

1. Clone o repositório e acesse a pasta do projeto:

   ```bash
   git clone https://github.com/gustavo-ross/dev_blog.git
   cd dev_blog
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Linux/macOS
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto com as variáveis abaixo:

   ```env
   SECRET_KEY=sua-chave-secreta
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1

   DATABASE_ENGINE=django.db.backends.postgresql
   DATABASE_NAME=nome_do_banco
   DATABASE_USER=usuario
   DATABASE_PASSWORD=senha
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   ```

   > `ALLOWED_HOSTS` aceita múltiplos hosts separados por vírgula. Para MySQL, use `django.db.backends.mysql` e a porta `3306`.

5. Aplique as migrações e crie um superusuário:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

## Executando o projeto

```bash
python manage.py runserver
```

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## API REST

| Método | Endpoint | Descrição | Autenticação |
| --- | --- | --- | --- |
| `GET` | `/api/artigos/` | Lista todos os artigos | Não |
| `GET` | `/api/categorias/` | Lista todas as categorias | Não |
| `POST` | `/api/artigos/novo` | Cria um novo artigo | JWT |
| `POST` | `/api/token/` | Obtém par de tokens (access/refresh) | Não |
| `POST` | `/api/token/refresh/` | Renova o access token | Não |

Exemplo de autenticação:

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "seu_usuario", "password": "sua_senha"}'
```

Use o `access` token retornado no cabeçalho `Authorization: Bearer <token>` para acessar endpoints protegidos.

## Licença

Distribuído sob a licença MIT. Consulte [LICENSE](LICENSE) para mais detalhes.
