# -*- coding: utf-8 -*-
from pymongo import MongoClient


# import processamento.pre_processamento as pre_processamento
"""
Realiza a conexao com o MOngoDB
"""


def inicia_conexao():
    """Inicia a conexão com o mongoDb"""
    cliente = MongoClient()
    cliente = MongoClient('localhost', 27017)
    return cliente


def carregar_banco(cliente, nome, colecao):
    """Carrega um banco com uma colecao"""
    db = cliente[nome]
    return db[colecao]


def carregar_usuarios(nome_banco, colecao):
    """Carrega e retorna uma lista de usuários"""
    cliente = inicia_conexao()
    colecao = carregar_banco(cliente, nome_banco, colecao)
    usuarios = colecao.find({}, {"user": 1})
    lista_usuarios = []
    for i in usuarios:
        lista_usuarios.append(i)
    return lista_usuarios


def carrega_tweet_mongo(nome_base, colecao):
    """Carrega os tweets limpos"""
    cliente = inicia_conexao()
    colecao = carregar_banco(cliente, nome_base, colecao)
    tweets = colecao.find({})
    lista_tweets = []
    for tweet in tweets:
        try:
            full_tweet = tweet["extended_tweet"]["full_text"]
            if len(full_tweet) > 1:
                lista_tweets.append(full_tweet)
        except Exception as e:
            pass
    return lista_tweets
