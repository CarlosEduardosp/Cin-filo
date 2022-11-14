import requests
from bs4 import BeautifulSoup
import random
from flask import request





def comparar(resposta, nome):
    link = "https://cinefilo-938c9-default-rtdb.firebaseio.com/-NEmjtP_bkZLZfkK0yEL"
    requisicao = requests.get(f"{link}.json")
    dic_requisicao = requisicao.json()


    resposta = str(resposta).title()
    comp = str(dic_requisicao['nome'])
    for i in comp:
        if resposta == 'none' or resposta == 'None':
            return ''
        else:
            if resposta in comp:
                pontos = pontuacao(nome)
                return f"{nome},  Parabéns !! Você Acertou. Sua resposta foi: {resposta}, e o correto era: {comp}. {pontos} Pontos."
            #alterar os pontos no bd, neste campo.

            else:
                pontos = pegarpontos(nome)
                return f"Resposta errada {nome} !! Sua resposta foi: {resposta}, e o correto era: {comp}. {pontos} Pontos"


def receber(nome):
    resposta = str
    if request.method == "POST":
        if request.form.get(f"{nome}"):
            resposta = (request.form.get(f"{nome}").title())
            return resposta


def soup(pedido, escolha):

    link = pagina(escolha)

    page = requests.get(link)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}



    soup = BeautifulSoup(page.content, 'html.parser')
    if pedido == "titulo":
        #tag do titulo do filme
        titulos = soup.find_all("h2", class_='meta-title')
        return titulos
    elif pedido == "sinopse":
        sinopse = soup.find_all("div", class_='synopsis')
        return sinopse
    else:
        imagem = soup.find_all("img", class_="thumbnail-img")
        listadeimagens = []
        for link in imagem:
            listadeimagens.append(link.get('data-src'))
        return listadeimagens






def sort():
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    return random.choice(num)


def pagina(escolha):
    return f"https://www.adorocinema.com/filmes/melhores/?page={escolha}"

def acerto_numero(escolha):
    if escolha > 9:
        num = [0,1,2,3,4,5,6,7,8,9]
        novo_escolha = random.choice(num)
        return novo_escolha
    else:
        return escolha