"""
Framework de Análise de dados Politicos no twitter..
Central de Coleta Dados do Framework de Análise de Dados -
Sara - Sistema de Análise de Dados com Redes Complexas e Analytics
Focado em análises politicas no twitter.

Coletor API
"""
# -*- coding: utf-8 -*-


from Coleta.sauron_coletor import Sauron
import sys


# padrao_pesquisa,limite,colecao,nome_banco="eleicao"
# coletor de dados


# termo="haddad"
# n_tweets=0
# colecao="haddad_2310"
# nome_banco="eleicao"

# termo colecao numero_tweets
try:
    name_file = sys.argv[0]
    termo = sys.argv[1]
    n_tweets = sys.argv[2]
    colecao = sys.argv[3]
    nome_banco = sys.argv[4]
except Exception:
    print("ERRO!Digite", name_file,
        "<termo> <numero_tweets> <colecao> <banco de dados>")
    print("\nTermo: O termo a ser coletado" +
        "\nNúmero de Tweets: número de tweets a ser coletado." + 
        "0 para definir sem limite" +
        "\nColecao: A coleção onde os tweets serão salvos" +
        "\nBanco de Dados: O  banco onde os dados serão armazenados")
        
    exit()
# Termo: zika Colecao: doencas Número tweets:  0 Banco:  mineracao

print("Termo:", termo, "Colecao:", colecao,
"Número tweets: ", n_tweets, "Banco: ", nome_banco)

coletor = Sauron()
coletor.pesquisa(termo, n_tweets, colecao, nome_banco)

# odetalhista.detector_bots(nome_banco,colecao)
