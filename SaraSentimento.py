from LeIA.leia import SentimentIntensityAnalyzer
import mongo.mongo_db as bd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
"""
Módulo Responsável pela Análise de sentimento
Utiliza o Leia para realizar a análise Léxica de Sentimento.
"""


class DetectorSentimento():
    """ Realiza a análise de sentimento Léxica"""
    def __init__(self):
        self.Leia = SentimentIntensityAnalyzer()

    def sentimento(self, score):
        if(score >= 0.5):
            return 1
        elif(score <= -0.5):
            return -1
        else:
            return 0

    def main(self, banco_dados, colecao):
        """Recebe como parâmetro o nome do banco e da colecao"""
        tweets = bd.carrega_tweet_mongo(banco_dados, colecao)
        sentimento = []
        sentimento_final = []
        final = []
        for i in tweets:
            resultado = self.Leia.polarity_scores(i)
            if(resultado['compound'] > 0):
                sentimento.append(resultado['compound'])
                sentimento_final.append("Positivo")
                final.append(1)
            elif(resultado['compound'] < 0):
                sentimento.append(resultado['compound'])
                sentimento_final.append("Negativo")
                final.append(-1)
            else:
                sentimento.append(resultado['compound'])
                sentimento_final.append("Neutro")
                final.append(0)

        Tweet = tweets

        tupla = list(zip(Tweet, sentimento, sentimento_final, final))
        df = pd.DataFrame(tupla,
        columns=['Tweet', 'Indice', 'Sentimento', 'Final'])

        print(df)

        fig, ax = plt.subplots(figsize=(7, 7))
        ax = sns.countplot(y="Sentimento", data=df, ax=ax)
        plt.show()
        fig.savefig("last_analise.png")


# --- chamada ----
detecta_sentimento = DetectorSentimento()

try:
    name_file = sys.argv[0]
    banco_dados = sys.argv[1]
    colecao = sys.argv[2]
except Exception as e:
    print("erro", e)
    print("Digite ", name_file, "<banco> <colecao>")
    exit()
detecta_sentimento.main(banco_dados, colecao)