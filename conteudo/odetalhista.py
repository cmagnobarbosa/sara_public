#coding:utf8
import mongo_db as bd
import re
from collections import Counter
"""
O detalhista extrai padrão dos dados usando estatistica e outras técnicas.
Módulo com objetivo de levantar informações sobre os usuários.
Detecção de perfis Fake.
"""

def detector_bots(nome_banco,colecao):
    """Detector de Bots no twitter"""
    lista=bd.carregar_usuarios(nome_banco,colecao)
    cont=0
    cont_geral=0
    possivel_fake=0
    lista_localizacao=[]
    print("Listagem perfis que provavelmente são bots:")
    for i in lista:
        #print(i['user']['lang'])
        try:
            idioma=i['user']['lang']
            if(idioma!="pt"):
                nome_perfil=i['user']['screen_name']
                nome=i['user']['name']

                if(re.search('(\w+(\d){4,})',nome_perfil)):
                    ano_criacao=i['user']['created_at'].split(" ")[-1]
                    mes_criacao=i['user']['created_at'].split(" ")[1]
                    if("2018" in ano_criacao):
                        print("-------------\n")
                        print("Nome",nome)
                        print("Nome Perfil:",nome_perfil)
                        print("Perfil Criado em:",mes_criacao,ano_criacao)
                        print("Seguidores:",i['user']['followers_count'])
                        print("Seguindo:",i['user']['friends_count'])
                        print("Número de tweets:",i['user']['statuses_count'])
                        #print("Localização:",i['user']['location'])
                        print("\n-------------")
                        possivel_fake+=1
                        #lista de localizações...
                        lista_localizacao.append(i['user']['location'])
                cont+=1
            cont_geral+=1
        except Exception as e:
            # print("Erro",e,"Tweet",i)
            pass

    print("Tweets idioma padrão não é português:",cont)
    print("Perfis provavelmente falsos:",possivel_fake)
    print("Tweets Linguagem padrão Português:",cont_geral)
    #print("Localização",Counter([lista_localizacao]))
        # print("-------------\n")
        # print("Perfil linguagem padrão não é em português")
        # print(i['user']['screen_name'])
        # print(i['user']['description'])
        # print("---------------\n")
    #print(i['user']['location'])
    #print(i['user']['description'])
