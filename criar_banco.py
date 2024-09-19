from Pinterest import database,app
from Pinterest.models import Usuario,Foto

with app.app_context():
    database.create_all()


# bibliotecas usadas
# pip install flask-login flask-bcrypt -> login e criptografia da senha
# pip install flask-sqlalchemy -> trabalhar com sql
# pip install flask-wtf -> estrutura de formulários
# pip install email_validator -> validação de e-mail