import requests
import json


def incluirfilmenobd(filme_escolhido):
    link = "https://cinefilo-938c9-default-rtdb.firebaseio.com/-NEmjtP_bkZLZfkK0yEL"
    filme = {'nome': f'{filme_escolhido}'}
    requests.patch(f"{link}/.json", data=json.dumps(filme))

def incluirimagembd(imagem_certa):
    #link = "https://cinefilo-938c9-default-rtdb.firebaseio.com/imagem"
    link = "https://cinefilo-938c9-default-rtdb.firebaseio.com/imagem/-NFAox2A4Qjvz4FRp6yo"
    imagem = {'imagem': f"{imagem_certa}"}
    requests.patch(f"{link}/.json", data=json.dumps(imagem))



def incluirnomebd(nome):
    link = "https://cinefilo-938c9-default-rtdb.firebaseio.com/usuarios"
    if nome != None:
        add_nome = {'nome': f'{nome}', 'pontos': 0}
        requests.post(f"{link}/.json", data=json.dumps(add_nome))

def pegarbd():
    link = "https://cinefilo-938c9-default-rtdb.firebaseio.com/usuarios"
    requisicao = requests.get(f"{link}.json")
    dic_requisicao = requisicao.json()
    return dic_requisicao

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