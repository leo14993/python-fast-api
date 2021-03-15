--------------------------------------------------------
--  DDL for Table responsabilidades_usuarios
--------------------------------------------------------

CREATE TABLE responsabilidades_usuarios (
    id integer not null auto_increment,
    responsabilidade_id INTEGER,
    usuario_id  INTEGER,
    primary key (id),
    CONSTRAINT fk_resp_usuario_resp
    FOREIGN KEY (responsabilidade_id) REFERENCES responsabilidades(id),
    CONSTRAINT fk_resp_usuario_usuario
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)

  );

