# 🚗 Concessionária de Carros - Projeto Django

Este é um projeto de estudo desenvolvido com **Django** que simula uma **concessionária de veículos**, com área administrativa para o dono da loja e uma página pública para os clientes visualizarem os carros disponíveis.

## 📚 Objetivo

Praticar os principais recursos do Django:

- Criação de modelos e relacionamento entre tabelas
- Admin customizado
- Upload e exibição de imagens
- Views públicas e privadas
- Templates com HTML + Django
- CRUD completo (Create, Read, Update, Delete)

## 🛠️ Tecnologias

- Python 3.10+
- Django 4.x
- SQLite (padrão do Django)
- HTML5 + CSS3 (com Bootstrap opcional)
- Pillow (para upload de imagens)

## ⚙️ Funcionalidades

### 👤 Área do Administrador (Dono da Concessionária)

- Login via Django Admin
- Adicionar novos carros com:
  - Marca
  - Modelo
  - Ano de fabricação e modelo
  - Preço
  - Imagem do carro
- Editar ou remover carros existentes

### 🌐 Área do Cliente (Público)

- Página com listagem de todos os carros disponíveis
- Visualização dos detalhes do carro (opcional)

## 📂 Estrutura de Pastas

```bash
cars_project/
├── cars/                 # App principal
│   ├── models.py         # Modelos: Car, Brand
│   ├── admin.py          # Admin customizado
│   ├── views.py          # Views públicas
│   ├── templates/
│   │   └── cars/         # Templates HTML
├── media/                # Imagens dos carros
├── static/               # Arquivos estáticos (opcional)
├── db.sqlite3            # Banco de dados
├── manage.py
▶️ Como rodar o projeto
Clone o repositório:

bash

git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
Crie um ambiente virtual e ative:

bash

python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
Instale as dependências:

bash

pip install -r requirements.txt
Execute as migrações:

bash

python manage.py migrate
Crie um superusuário:

bash

python manage.py createsuperuser
Inicie o servidor:

bash

python manage.py runserver
Acesse:

Admin: http://localhost:8000/admin
