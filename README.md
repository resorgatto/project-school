# ProjectSchool - API de Matrículas

Este projeto é uma API desenvolvida com **Django Rest Framework (DRF)** para gerenciar matrículas de alunos em cursos.

## 🚀 Funcionalidades
- CRUD de alunos e cursos
- Sistema de matrículas
- Autenticação e permissões
- Documentação automática com DRF

## 🛠 Tecnologias
- **Django** e **Django Rest Framework**
- **SQLite/PostgreSQL** (configurável)
- **Docker** (opcional)

## 📦 Como rodar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ProjectSchool.git
   cd ProjectSchool
   ```

2. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## 📖 Documentação
Após rodar o servidor, acesse `http://127.0.0.1:8000/api/docs/` para visualizar a documentação gerada automaticamente pelo DRF.

## 📝 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo!

