# python-fast-api

Instalar as dependencias necessarias com o comando:

- pip install -r requirements.txt

rodar a aplicação:

- uvicorn main:app --reload

Armazenazenamento:
## BASE A ##

Para a base A, considerando as condições de umas base extremamente sensível e deve ser protegida com os maiores níveis de segurança, mas o acesso a esses dados não precisa ser tão performática.

De início foi escolhido usar o Oracle, mas por questões de complexidade desnecessária para configurar o docker-compose, foi decidido o MySQL, além de ser open source, possui comandos bem parecidos ao da base Oracle.

Os primeiros testes foram utilizando o comando no bash do docker:
    docker run --name mysql_demo -p 3306:3306 \
    -e MYSQL_ALLOW_EMPTY_PASSWORD=true \
    -e MYSQL_DATABASE=mysql_demo \
    -e MYSQL_USER=my_user_name \
    -e MYSQL_PASSWORD=somethingSecret
    -d mysql


## BASE B ##
Para a segunda base foi decidido usar o ElasticSearch em conjunto com o kibana para gerenciar visualmente os dados recebidos.

Para testes foram executados os comandos no bash do docker:

docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.11.1


Usando o Kibana para acessar o elasticSearch:

docker run --link <id_do_container>:elasticsearch -p 5601:5601 docker.elastic.co/kibana/kibana:7.11.1

## BASE C ##

Considerando que, essa base não possui nenhum tipo de dado crítico, mas precisa de um acesso extremamente rápido.
Foi decidido usar o Redis. Uma vez que é um banco alocado em memoria ram, que possui alto desempenho.

A aplicação foi baseada no framework fast-api.

a documentação encontra-se no endereço: localhost:8000/docs, neste endereço é possivel testar todos os métodos, e endpoints.

A aplicação é dividida nas seguintes camadas:
Dentro de /src temos:
 ### /bootloader ###

 Esta camada possui os pre requisitos para as conexões com as bases de dados, são carregadas as variaveis de ambiente, a sessão com o banco, e a instância da classe de conexão com redis.

 ### /domain ###

 Esta é subdividida em:

  ### /controller ###
    Responsável por acomodar as rotas de cada classe associada, recebe os métodos HTTP, e executa as funções pertinentes a cada endereço.

  ### /entity ###

    Responsável por acomodar as entidades que darão forma e instância aos objetos utilizados

  ### /repository ###

    Gera as querys para o banco de dados para cada entidade existente

  ### /schema ###

    Responsável por aplicar a regra de negócio onde as entidades serão aplicadas, limitando atributos das antidades dependendo de onde será aplicado, e fazendo o relacionamento entre as entidades.

  ### /service ###

    Gerencia a lógica da regra de negócio, são chamados logo após o controller, gerenciam a comunicação das entidades e dos repositórios,
    validando, ativando funções, e gerando exceções.


