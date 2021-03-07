--------------------------------------------------------
--  DDL for Table pessoa_fisica
--------------------------------------------------------

CREATE TABLE pessoa_fisica (
    id integer not null,
    cpf VARCHAR(11),
    nome VARCHAR(255),
    nascimento DATE,
    endereco_id INTEGER,
    primary key (id),
    FOREIGN KEY (endereco_id) REFERENCES enderecos(id)
                        );

-- Foi identificado a necessidade de tratar a restrição de apenas um CPF por pessoa
alter TABLE pessoa_fisica change column cpf cpf VARCHAR(11) unique;
