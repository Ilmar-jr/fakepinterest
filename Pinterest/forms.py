# criar os formulários do nosso site
from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm # estrutura da classe
from wtforms import StringField, PasswordField,SubmitField,FileField # estrutura dos campos
from wtforms.validators import DataRequired,Email,EqualTo,length,ValidationError
from Pinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(),Email()])
    senha = PasswordField("Senha",validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer login")
    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email= email.data).first()
        if not usuario:
            raise ValidationError("Usuário inexistente, crie uma conta")


class FormCriarConta(FlaskForm):
    email = StringField("E-mail",validators=[DataRequired(),Email()])
    username =StringField("Nome de usuário", validators=[DataRequired()])
    senha = PasswordField("Senha",validators=[DataRequired(),length(6,20)])
    confirmacao_senha = PasswordField("Confirmação de senha",validators=[DataRequired(),EqualTo("senha")])
    botao_confirmacao =  SubmitField("Criar Conta")

    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email= email.data).first()
        if usuario:
            raise ValidationError("E-mail ja cadastrado, faça login para cadastrar")
        
class FormFoto(FlaskForm):
    foto = FileField("Foto",validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")