--------------------------------------------------------
--  DDL for Table usuarios
--------------------------------------------------------

CREATE TABLE usuarios (
    id integer not null auto_increment,
    login VARCHAR(50) unique,
    senha VARCHAR(255),
    email VARCHAR(255) unique,
    ativo BOOLEAN DEFAULT TRUE,
    primary key (id)

  );
