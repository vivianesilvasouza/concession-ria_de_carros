# 🚗 Concessionária de Carros - Projeto Django

Este é um projeto de estudo desenvolvido com **Django** que simula uma **concessionária de veículos**, com área administrativa para o dono da loja e uma página pública para os clientes visualizarem os carros disponíveis.

---

## 📚 Objetivo

Praticar os principais recursos do Django:

- Criação de modelos e relacionamento entre tabelas
- Admin customizado
- Upload e exibição de imagens
- Views públicas e privadas
- Templates com HTML + Django
- CRUD completo (Create, Read, Update, Delete)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Django 4.x
- SQLite (banco de dados padrão do Django)
- HTML5 + CSS3
- Pillow (para upload e manipulação de imagens)

---

## ⚙️ Funcionalidades

### 👤 Área Administrativa (Dono da Concessionária)

- Login via Django Admin
- Adicionar novos carros com:
  - Marca
  - Modelo
  - Ano de fabricação e modelo
  - Preço
  - Imagem do carro
- Editar ou excluir carros existentes

### 🌐 Área Pública (Clientes)

- Visualização de todos os carros disponíveis
- (Opcional) Detalhes individuais de cada carro

---

## 📂 Estrutura de Pastas

```bash
cars_project/
├── cars/                 # App principal
│   ├── models.py         # Modelos: Car, Brand
│   ├── admin.py          # Admin customizado
│   ├── views.py          # Views públicas
│   ├── templates/
│   │   └── cars/         # Templates HTML
├── media/                # Imagens dos carros (upload)
├── static/               # Arquivos estáticos (opcional)
├── db.sqlite3            # Banco de dados local
├── manage.py
```

## ▶️ Como Rodar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

2. Crie um ambiente virtual e ative:

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

3. Instale as dependências:

```bash

pip install -r requirements.txt
```

4. Aplique as migrações:

```bash

python manage.py migrate
```

5. Crie um superusuário para acessar o admin:

```bash

python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento:

```bash

python manage.py runserver
```

7. Acesse no navegador:

Admin: <http://localhost:8000/admin>
