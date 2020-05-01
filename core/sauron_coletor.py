# -*- coding: utf-8 -*-
# import codecs
# import os
# import sys
from pymongo import MongoClient

import core.conexao_twitter as conexao


class Sauron(object):
    """docstring for Sauron."""

    def __init__(self):
        # conexão com o banco de dados
        self.cliente = MongoClient()
        self.cliente = MongoClient('localhost', 27017)

        # inica a conexao com twitter
        self.api = conexao.inicia_conexao()
        # caminho = 'central_eleicoes/'
        # configuração do banco de dados MongoDB
        self.pos = ""
        self.collection = ""

    def banco(self, nome_banco, colecao):
        # # configura o local de salvamento no banco.
        banco = self.cliente[nome_banco]
        # coleção ...
        post = banco[colecao]
        return post

    def escreve_lista(self, nome_arquivo, lista):
        """Escreve no arquivo"""
        arq = open(nome_arquivo, "w")
        for i in lista:
            arq.write(str(i))
            arq.write('\n')
        arq.close()

    def save_data(self, name, data):
        """save data to file json"""
        arq = open(name + ".txt", "a")
        arq.write(str(data))
        arq.write("\n")
        arq.close()

    def salvar_mongo(self, tweet, post):
        """Salva o tweet no mongodb"""
        post.replace_one(tweet, tweet, True)
        self.save_data("dados_coletados", tweet)

    def monitor_twitter(self, termo_pesquisa, conexao_banco, limite=0):
        """Monitora as postagens em tempo real"""
        # print("TP",termo_pesquisa,"Limite",limite)
        retorno = self.api.GetStreamFilter(track=[termo_pesquisa])
        # print(list(retorno))
        print("Coletando dados", "Termo:", termo_pesquisa)
        contador = 0
        try:
            for i in retorno:
                print("Tweets Coletados", contador)
                contador += 1
                self.salvar_mongo(i, conexao_banco)
                if(contador == limite and limite != 0):
                    print("Coleta encerrada a partir do limite determinado.")
                    return
        except Exception as erro:
            print("error", erro)
            self.monitor_twitter(termo_pesquisa, conexao_banco, limite)

    def obtem_ids(self, lista_nomes):
        """Obtém ids de uma lista de nomes"""
        lista_ids = []
        for name in lista_nomes:
            try:
                info = self.api.GetUser(screen_name=name)
                id = info._json['id']
                lista_ids.append([name, id])
            except Exception as e:
                print(name + '\n')
                print("error", e)
        return lista_ids

    veiculos = ['@uol', '@uolnoticias', '@g1', '@veja',
                '@brasil247', '@cartacapital', '@exame', '@elpais_brasil',
                '@bbcbrasil', '@RevistaEpoca',
                '@folha', '@veja',
                '@estadao', '@tijolaco', '@o_antagonista', '@agenciabrasil']

    checadores_noticias = ['@agencialupa', '@aosfatos', '@agenciapublica']

    # nome da coleção
    def pesquisa(self, padrao_pesquisa, limite, colecao, nome_banco="eleicao"):
        """método de pesquisa"""
        print("Padrão de Busca:", padrao_pesquisa)
        print("Collection Onde os dados serão salvos?:", colecao)
        post = self.banco(nome_banco, colecao)
        self.monitor_twitter(padrao_pesquisa, post, limite)
