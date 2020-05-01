# sara_public
Framework para coleta e Análise de dados de redes sociais utilizando Redes complexas e Mineração de dados.

Framework semi-automatizado,  permite uma coleta e uma análise rápida dos acontecimentos em redes sociais.


# Desenvolvimento

Desenvolvido no Laboratório de Modelagem Computacional e Inteligência Computacional (LABMIC) da Universidade Federal de São João del-Rei(UFSJ)

Estado : Em desenvolvimento
## Módulos

### Coletor

O módulo de coleta combina o coletor web e a API de coleta em tempo real do Twitter.

Módulos associados:
* saraColetor - Realiza as coletas de tweets em tempo real.
* saraColetorWeb - Realiza a coleta de comentários nos twitter.
* conexao_twitter - Contém os dados de acesso da API twitter.
- Os dados são salvos no mongodb, um banco de dados não relacional.


### Geração da Rede

A geração da rede é realizada por meio do módulo saraEstrutural.

* saraEstrutural - Gera uma rede direcionada ou não direcionada.

A rede gerada é salva no diretório redes.

## Análise de Centralidade

O framework identifica os vértices de maior importância de acordo com as seguintes métricas de centralidade:
- Betweenness, PageRank, Degree, Curtidas, Retweets.

A detecção de centralidade é realizada por meio da utilização do módulo saraImportancia.

O resultado deste módulo é salvo no diretório resultados_importancia

## Comunidade

A detecção de comunidade neste framework é realizada por meio do módulo Overlap.

Esta ferramenta procura encontrar ego comunidades formada em torno de determinados usuários.

- Detecção de comunidades - Realiza a detecção de comunidades sobrepostas, utilize o resultado de centralidade ou outro sequencia de importância para detecção de comunidades.

Modulo associado
> overlap.py

## Visualização e Análise do conteúdo

A visualização e análise do conteúdo é realizada por meio da utilização da técnica de LDA combinada com uma núvem de palavras.

Módulos associados:

* SaraConteudo - Responsável pela geração da núvem de palavras.
* SaraSentimento - Responsável pela análise de sentimento.


## Depêndencias:

Em breve será disponibilizado um arquivo para facilitar a instalação das dependências.
- python 3.7
- pymongo
- mongodb
- networkx
- gensim
- spacy
- matplot
- wordcloud
- nltk
- seaborn
- pandas
