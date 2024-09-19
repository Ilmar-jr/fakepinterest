# criar a estrutura do banco de dados


from Pinterest import database,login_manager
from datetime import datetime
from flask_login import UserMixin # qual classe vai gerenciar a estrutura de login

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model,UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String, nullable = False)
    email = database.Column(database.String, nullable = False, unique = True)
    senha = database.Column(database.String, nullable = False)
    fotos = database.relationship("Foto", backref="usuario",lazy=True)

class Foto(database.Model):
    imagem = database.Column(database.String, default = "default.png")
    data_criacao = database.Column(database.DateTime,nullable=False,default = datetime.utcnow())
    id = database.Column(database.Integer, primary_key = True)
    id_usuario = database.Column(database.Integer,database.ForeignKey('usuario.id'),nullable=False)