--------------------------------------------------------
--  DDL for Table lista_dividas
--------------------------------------------------------

CREATE TABLE lista_dividas (
    id integer not null,
    devedor_id integer not null,
    credor_id integer,
    data_inicial_divida DATE,
    valor_divida INTEGER,
    primary key (id),
    FOREIGN KEY (devedor_id) REFERENCES pessoa_fisica(id),
    FOREIGN KEY (credor_id) REFERENCES pessoa_fisica(id)
                        );

-- trocando o nome da coluna, alterando o tipo de valro de inteiro para float
ALTER TABLE lista_dividas change COLUMN valor_divida valor FLOAT(20,2);

-- inserindo coluna de taxas de juros para caso seja necessário recalcular a divida
ALTER TABLE lista_dividas ADD COLUMN taxa_juros_mensal FLOAT(10,5) AFTER valor;
