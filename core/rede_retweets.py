import os
import sys

import networkx as nx

import conexao.conexao_twitter as conexao
import mongo.mongo_db as bd

"""
Gera a rede de Retweets.
"""
#########
"""Configuração inicial"""
# 0 define para usar toda a base..
# limite_tweets=0
# nome_rede="joaoamoedo_full"
# nome_base="eleicao"
# #caso seja informado uma coleção que não exista a mesma é criada..
# nome_colecao="temer"
######
caminho_base = "redes/"


def main(nome_rede, nome_base, nome_colecao, direcionada, limite_tweets):
    cliente = bd.inicia_conexao()
    colecao = bd.carregar_banco(cliente, nome_base, nome_colecao)
    # grafo não direcionado
    if("True" in direcionada):
        print("Gerando uma rede direcionada.")
        grafo = nx.DiGraph()
    else:
        print("Gerando uma rede não direcionada.")
        grafo = nx.Graph()
    # inica a conexao com twitter
    api = conexao.inicia_conexao()

    # utilizado para selecionar o titulo contendo a palavra senado maiusculo e minusculo.
    # retorno=colecao.find({"titulo":{"$regex":"senado","$options":"i"}})
    # for i in retorno:
    #     print(i)
    # carrega os tweets da coleção..
    try:
        # limitando o número de tweets utilizado..
        tweets = colecao.find().limit(limite_tweets)
    except Exception as e:
        print(e, "erro")
        exit()
    cont = 0
    for tweet in tweets:
        #print (tweet['user']['screen_name'])
        destino = None
        try:
            # print(tweet)
            cont += 1
            destino = tweet['user']['screen_name']
            # print(origem)
        except Exception as e:
            pass
        try:
            origem = tweet['retweeted_status']['user']['screen_name']
        except Exception as e:
            origem = None
        if(destino is not None and origem is not None):
            grafo.add_edge(origem, destino)
    print("------\nGerando a rede com: ", cont, "tweets")
    print("Nome da Rede:", nome_rede)
    print("Originada da Colecao:", nome_colecao, "\n--------")
    print("Sumário da Rede:\n", nx.info(grafo), "\n------")
    try:
        arquivo = open(caminho_base + "sumario_" + nome_rede, "w")
    except FileNotFoundError as e:
        os.mkdir(caminho_base)
        arquivo = open(caminho_base + "sumario_" + nome_rede, "w")
    arquivo.write(str(nx.info(grafo)))
    arquivo.close()
    nx.write_gml(grafo, caminho_base + nome_rede + ".gml")
    # nx.write_gexf(grafo,"retweets2.gexf")
