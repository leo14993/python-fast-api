--------------------------------------------------------
--  DDL for Table responsabilidades_permissoes
--------------------------------------------------------

CREATE TABLE responsabilidades_permissoes (
    id integer not null auto_increment,
    responsabilidade_id INTEGER,
    permissao_id  INTEGER,
    primary key (id),
    CONSTRAINT fk_resp_perm_resp
    FOREIGN KEY (responsabilidade_id) REFERENCES responsabilidades(id),
    CONSTRAINT fk_resp_perm_perm
    FOREIGN KEY (permissao_id) REFERENCES permissoes(id)
  );
