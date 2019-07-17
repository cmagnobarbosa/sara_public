import mongo.mongo_db as db
import coletor_comentarios.coletor_comentarios as comment
import sys
"""
Coletor Web
Realiza a coleta dos comentários associados a determinado
Tweet.

Utiliza o selenium
"""


def main(banco_dados, colecao):
    """Coletor web"""
    cliente = db.inicia_conexao()
    conector = db.carregar_banco(cliente, banco_dados, colecao)
    tweets = conector.find({}) 

    for tweet in tweets:
        id_tweet = tweet['id_str']
        usuario_tweet = tweet['user']['screen_name']
        try:
            comment.get_data(usuario_tweet, id_tweet)
        except Exception as e:
            print("A coleta foi interrompida no usuário")
            print(e, f"Erro {e}")
            exit()


try:
    name_file = sys.argv[0]
    banco_dados = sys.argv[1]
    colecao = sys.argv[2]
except Exception as e:
    print("erro", e)
    print("Digite ", name_file, "<banco> <colecao>")
    exit()
main(banco_dados, colecao)