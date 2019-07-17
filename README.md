# sara_public
Framework para Análise e coleta de dados de redes sociais utilizando Redes complexas e Mineração de dados. 

Framework semi-automatizado,  permite uma coleta e uma análise rapida dos acontecimentos em redes sociais.

Devido a grande importância que as redes sociais como Twitter ganharam nos últimos anos uma análise do conteúdo que esta sendo propagado na mesma é essencial.

# Desenvolvimento

Desenvolvido no Laboratório de Modelagem Computacional e Inteligência Computacional (LABMIC) da Universidade Federal de São João del-Rei(UFSJ)

Estado : Em desenvolvimento
## Módulos

### Coletor

O módulo de coleta combina o coletor web e a API de coleta em tempo real do Twitter.

Módulos associados:
* saraColetor - Realiza as coletas de tweets em tempo real.
* saraColetorWeb - Coletor de comentários web, coleta os comentarios presente nos tweets coletados.
* conexao_twitter - Contém os dados de acesso da API twitter.
- Os dados são salvos no banco de dados.


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

## Visualização e Análise do conteúdo

A visualização e análise do conteúdo é realizada por meio da utilização da técnica de LDA combinada com uma núvem de palavras.

Módulos associados:

* SaraConteudo - Responsável pela geração da núvem de palavras.
* SaraSentimento - Responsável pela análise de sentimento.


## Depêndencias:

Em breve será disponibilizado um arquivo para facilitar a instação das depêndencias.
- python3.7
- pymongo.
- mongodb
- networkx
- gensim
- spacy
- matplot
- wordcloud
- nltk
- seaborn
- pandas

