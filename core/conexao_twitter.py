# -*- coding: utf-8 -*-
import twitter


"""
Inicia uma conexão com o twitter..
Remova as credencias ao realizar um upload para o git.
"""


def inicia_conexao():
    """Abre a conexão com a api do twitter"""
    api = twitter.Api(
        consumer_key='',
        consumer_secret='',
        access_token_key='',
        access_token_secret='',
        sleep_on_rate_limit=True,
        tweet_mode='extended',
    )
    return api
