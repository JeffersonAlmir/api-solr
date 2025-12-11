CREATE TABLE IF NOT EXISTS tb_ocupacao (
    codigo INT PRIMARY KEY,
    titulo VARCHAR(200)
);

COPY tb_ocupacao(codigo, titulo)
FROM '/docker-entrypoint-initdb.d/cbo2002-ocupacao.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'LATIN1';