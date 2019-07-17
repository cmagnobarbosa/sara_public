# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import Estrutural.rede_retweets as rede
import sys
"""
Central Estrutural -
Sara - Sistema de Análise de Dados com Redes Complexas e Analytics
Focado em análises politicas no twitter.
Geração da rede
"""


class Estrutural(object):
    """docstring for Estrutural."""

    def __init__(self):
        try:
            self.nome_rede = sys.argv[1]
            self.nome_base = sys.argv[2]
            self.nome_colecao = sys.argv[3]
            self.direcionada = sys.argv[4]
            self.limite = int(sys.argv[5])
            # limite de tweets a serem utilizados
        except Exception as e:
            print(e)
            print("ERRO!!\nDigite:\n>python3 saraEstrutural.py <nome_rede> <nome_base> <nome_colecao> <True||False> <limite>")
            print(
                "True: Rede direcionada, False: Rede não direcionada\nlimite:0 para utilizar a base completa")
            exit()

        rede.main(self.nome_rede, self.nome_base,
                  self.nome_colecao, self.direcionada, self.limite)


if __name__ == '__main__':
    estrutura = Estrutural()
