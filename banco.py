import requests
import json
from banco_sql import db, user



def incluirfilmenobd(filme_escolhido):
    pessoa = user(filme_escolhido)
    db.session.add(pessoa)
    db.session.commit()

def incluirimagembd(imagem_certa):
    pessoa = user(imagem_certa)
    db.session.add(pessoa)
    db.session.commit()



def incluirnomebd(nome):
    pessoa = user(nome)
    db.session.add(pessoa)
    db.session.commit()

def pegarbd():
    users = db.session.execute(db.select(user)).all()
    return users

def trazernomebd():
    nomes = pegarbd()
    cont = len(nomes)
    for i in nomes:
        cont = cont - 1
        if cont == 0:
            nome = nomes[i]['nome']
            return nome

def pontuacao(nome):
    nomes = pegarbd()
    for i in nomes:
        if nome == nomes[i]['nome']:
            pontos = nomes[i]['pontos']
            pontos = int(pontos)
            pontos += 10
            pontos = str(pontos)
            dados = {'pontos': f'{pontos}'}
            id = i
            requests.patch(f"https://cinefilo-938c9-default-rtdb.firebaseio.com/usuarios/{id}.json", data=json.dumps(dados))
            return dados['pontos']

def pegarpontos(nome):
    nomes = pegarbd()
    for i in nomes:
        if nome == nomes[i]['nome']:
            pontos = nomes[i]['pontos']
            return pontos


def pegarimagembd():
    link = "https://cinefilo-938c9-default-rtdb.firebaseio.com/imagem/-NFAox2A4Qjvz4FRp6yo"
    requisicao = requests.get(f"{link}.json")
    dic_requisicao = requisicao.json()
    return dic_requisicao