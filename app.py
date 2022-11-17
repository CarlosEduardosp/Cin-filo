from flask import Flask, request, render_template, abort, redirect, url_for, session, flash
from function import soup, sort, receber, comparar, acerto_numero
import random, json
import requests
from flask_sqlalchemy import SQLAlchemy
from tinydb import TinyDB, Query



app = Flask(__name__)

# criando instancia do sqllite
# Cria a extensão
db = SQLAlchemy()


# criar  a chave secreta com o comando = import os ; print(os.urandom(16))

app.secret_key = "b'\x10\xa2\x159\x94*\x03\xda{z\xb8.\x9f\xf0\x8b\xb2"

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projeto.db"

# initialize the app with the extension
db.init_app(app)

#criando banco nosql
banco = TinyDB('db.json')
query = Query()


def consultar_db():
    users = db.session.execute(db.select(user)).all()
    for nome in users:
        nomes = nome[0]
    return nomes

def incluirnomebd(nome, senha, pontos):
    if nome:
        pessoa = user(nome, senha, pontos)
        db.session.add(pessoa)
        db.session.commit()



class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String, unique=False, nullable=False)
    pontos = db.Column(db.Integer, unique=False, nullable=True)


    def __init__(self, nome, senha, pontos):
        self.nome = nome
        self.senha = senha
        self.pontos = pontos




@app.route("/cinefilo", defaults={'nome':'Usuário'})
@app.route('/cinefilo/<nome>', methods=["GET", "POST"])
def home(nome):

    #escolhe o numero para o sorteio do link entre 0-29
    escolha = sort()

    # função que recebe a resposta do usuário.
    resposta = receber('resposta')

    #faz a comparação entre a resposta obtida e o titulo do filme no Banco de dados.
    bancofilme = banco.all()
    resultado = comparar(resposta, bancofilme[0]['filme'])
    teste = len(str(resposta))
    if teste == 4:
        flash('Nenhuma resposta foi digitada.'.title())

    #lista com strings para buscar filmes e sinopses.
    imagem = str
    pedido = ["titulo", 'sinopse', imagem]

    #adicionando o link da imagem para mostrar no html, junto a resposta correta.
    imagem = soup(pedido[2], escolha)

    #inclui filme na lista atraves do Beautifulsoup.
    filme = soup(pedido[0], escolha)

    #inclui sinopse na lista atraves do Beautiful soup.
    sinopse = soup(pedido[1], escolha)

    # condição para colocar o escolha abaixo de 9, precisa de melhoras.
    escolha = acerto_numero(escolha)

    #seleciona um filme e a sinopse, da lista de filmes, usando a variável escolha para fazer a seleção.
    filme = filme[escolha].text.title()
    sinopse = sinopse[escolha].text
    imagem = imagem[escolha]

    #recupera os dados do banco de dados.
    bancofilme = banco.all()

    #salvando a imagem do filme anterio para mostrar junto a resposta
    imagem_anterior = bancofilme[0]['imagem']

    #atualizando o banco com a resposta, para a próxima pergunta
    banco.update({'filme': f'{filme}', 'imagem': f'{imagem}'})



    #render_template do arquivo html, e envia algumas variaveis para o html.
    return render_template("cinefilo.html", filme=filme,resultado=resultado , teste=teste, sinopse=sinopse, nome=nome, imagem=imagem_anterior)


@app.route('/sobre/<nome>')
def sobre(nome):
    return render_template("sobre.html", nome=nome)


@app.route('/contato/<nome>')
def contato(nome):
    return render_template("contato.html", nome=nome)

@app.route('/filmes/<nome>')
def filme(nome):
    filmes = soup('titulo', 5)
    sinopse = soup('sinopse', 5)
    return render_template('filmes.html', filmes=filmes, sinopse=sinopse,nome=nome)

@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=['GET', 'POST'])
def login():
    nome = receber('nome')
    senha = receber('password')
    pontos = 0
    if nome and senha:
        incluirnomebd(nome, senha, pontos)
        cadastro = f'{nome} foi cadastrado com sucesso.'
    else:
        cadastro = ''
    return render_template('login.html', nome=nome, senha=senha, cadastro=cadastro)

@app.route('/logar', methods=['GET', 'POST'])
def logar():
    nome = receber('nome')
    senha = receber('password')

    #fazer a verificação de usuário para entrada no sistema
    users = db.session.execute(db.select(user)).all()


    for pessoa in users:
        if nome:
            if nome.title() == pessoa[0].nome:
                if senha == pessoa[0].senha:
                    resultado = pessoa[0].nome
                    return redirect(f'cinefilo/{resultado}')
                else:
                    resultado = 'Senha Inválida !! tente outra vez !!'
            else:
                resultado = 'Usuário não cadastrado!! Favor cadastrar primeiro!!'
        else:
            resultado = 'Nenhum valor válido foi digitado'
    return render_template('login.html', users=users, resultado=resultado, nome=nome)




if __name__ == "__main__":
    app.run(debug=True)
    with app.app_context():
        db.create_all()

