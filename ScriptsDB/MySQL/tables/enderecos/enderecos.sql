--------------------------------------------------------
--  DDL for Table enderecos
--------------------------------------------------------

CREATE TABLE enderecos(
    id INTEGER NOT NULL auto_increment,
    cep VARCHAR(8),
    endereco VARCHAR(255),
    numero INTEGER,
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cidade VARCHAR(255),
    estado VARCHAR(255),
    PRIMARY KEY (id)
);

-- necessario trocar caso o numero apresente uma letra '123-C'
alter table enderecos change column numero numero VARCHAR(12);
