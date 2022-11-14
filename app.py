from flask import Flask, request, render_template, abort, redirect, url_for
from function import soup, sort, receber, comparar, acerto_numero
import random, json
import requests
#from banco_sql import incluirnomebd


DEBUG = True
app = Flask(__name__)
Debug = True


@app.route('/', methods=["GET", "POST"])
@app.route('/cinefilo', methods=["GET", "POST"])
def home():

    #recebe o nome do fomulario html, do arquivo cinefilo.html
    nome = receber('nome')

    #inclui o nome e pontos no banco de dados, com pontos zerados.


    #busca o ultimo nome do banco de dados, para mostrar na tela.


    #escolhe o numero para o sorteio do link entre 0-29
    escolha = sort()

    # função que recebe a resposta do usuário.
    resposta = receber('resposta')

    #faz a comparação entre a resposta obtida e o titulo do filme no Banco de dados.



    #lista com strings para buscar filmes e sinopses.
    imagem = str
    pedido = ["titulo", 'sinopse', imagem]

    #adicionando o link da imagem para mostrar no html, junto a resposta correta.
    #imagem = soup(pedido[2], escolha)

    #inclui filme na lista atraves do Beautifulsoup.
    filme = soup(pedido[0], escolha)

    #inclui sinopse na lista atraves do Beautiful soup.
    sinopse = soup(pedido[1], escolha)

    # condição para colocar o escolha abaixo de 9, precisa de melhoras.
    escolha = acerto_numero(escolha)



    #seleciona um filme e a sinopse, da lista de filmes, usando a variável escolha para fazer a seleção.
    filme = filme[escolha].text.title()
    sinopse = sinopse[escolha].text

    #incluir o titulo do filme no firebase(banco de dados)


    #render_template do arquivo html, e envia algumas variaveis para o html.
    return render_template("cinefilo.html", filme=filme, sinopse=sinopse, resposta=resposta, nome=nome)


@app.route('/sobre')
def sobre():
    return render_template("sobre.html")


@app.route('/contato')
def contato():
    return render_template("contato.html")

@app.route('/filmes')
def filme():
    filmes = soup('titulo', 5)
    sinopse = soup('sinopse', 5)
    return render_template('filmes.html', filmes=filmes, sinopse=sinopse)

if __name__ == "__main__":
    app.run(debug=True)
