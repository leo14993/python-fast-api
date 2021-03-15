--------------------------------------------------------
--  DDL for Table pessoa_fisica
--------------------------------------------------------

CREATE TABLE pessoa_fisica (
    id integer not null,
    cpf VARCHAR(11) unique,
    nome VARCHAR(255),
    data_nascimento DATE,
    primary key (id),
                        );


