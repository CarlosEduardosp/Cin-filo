from flask_sqlalchemy import SQLAlchemy
from app import app

# criando instancia do sqllite
# Cria a extensão
db = SQLAlchemy()

# criar  a chave secreta com o comando = import os ; print(os.urandom(16))

app.secret_key ="b'\nQ\xc0\x10@\xea\xfcY\xd3<\x93\x9afH\x82f'"

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# initialize the app with the extension
db.init_app(app)

def consultar_db():
    users = db.session.execute(db.select(user)).all()
    return users

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String, unique=True, nullable=False)


    def __init__(self, nome):
        self.nome = nome


def incluirnomebd(nome):
    pessoa = user(nome)
    db.session.add(pessoa)
    db.session.commit()
