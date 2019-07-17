# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import conteudo.lda.modelagem_topicos as modelagem_topicos
# import conteudo.tf_idf.bagwords as bagwords
import sys
"""
Central de Análise de conteúdo do Framework Sara.
Gera a Núvem de palavras
"""

try:
    name_file = sys.argv[0]
    banco = sys.argv[1]
    colecao = sys.argv[2]
except Exception as e:
    print("erro", e)
    print("Digite ", name_file, "<banco> <colecao>")
    exit()

print("Banco a ser utilizado:", banco, "\nColecao:", colecao)
path = "resultado_sentimento/"


# Análise de conteúdo
palavras = modelagem_topicos.main(banco, colecao, 1000)
# print("Modelagem ... OK\nSentimento Modelagem:")
# print("Sentimento Modelagem... ok")
