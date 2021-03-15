--------------------------------------------------------
--  DDL for Table pessoa_endereco
--------------------------------------------------------

CREATE TABLE pessoa_endereco (
    id integer not null auto_increment,
    pessoa_id INTEGER NOT NULL,
    endereco_id INTEGER NOT NULL,
    primary key (id),
    CONSTRAINT fk_pessoa_endereco_pessoa
        FOREIGN KEY  (pessoa_id) REFERENCES pessoa_fisica(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_pessoa_endereco_endereco
        FOREIGN KEY  (endereco_id) REFERENCES enderecos(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
