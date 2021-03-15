--------------------------------------------------------
--  DDL for Table permissoes
--------------------------------------------------------


CREATE TABLE permissoes
(
    id          integer not null auto_increment,
    nome        VARCHAR(512),
    descricao   VARCHAR(1024),
    primary key (id)
);
