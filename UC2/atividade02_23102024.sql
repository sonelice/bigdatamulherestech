CREATE TABLE cursos (
    curso_id INT PRIMARY KEY,
    nome_curso VARCHAR(100),
    duracao INT,
    nivel VARCHAR(50),
    professor_id INT,
    FOREIGN KEY (professor_id) REFERENCES professores(professor_id)
);

CREATE TABLE filiais (
    filial_id INT PRIMARY KEY,
    nome_filial VARCHAR(100),
    endereco VARCHAR(255),
    telefone VARCHAR(15),
    data_abertura DATE
);

INSERT INTO cursos (curso_id, nome_curso, duracao, nivel, professor_id) VALUES
(1, 'Engenharia da Computação', 60, 'Bacharelado', 1),
(2, 'Administração', 48, 'Bacharelado', 2),
(3, 'Design Gráfico', 30, 'Tecnólogo', 3),
(4, 'Ciência de Dados', 36, 'Pós-graduação', 1),
(5, 'Gestão de Recursos Humanos', 24, 'Tecnólogo', 2),
(6, 'Engenharia Civil', 60, 'Bacharelado', 4),
(7, 'Marketing Digital', 18, 'Pós-graduação', 5),
(8, 'Sistemas de Informação', 48, 'Bacharelado', 1),
(9, 'Pedagogia', 48, 'Bacharelado', 6),
(10, 'Cibersegurança', 36, 'Pós-graduação', 1);


INSERT INTO filiais (filial_id, nome_filial, endereco, telefone, data_abertura) VALUES
(1, 'Filial Centro', 'Av. Principal, 100', '(11) 1234-5678', '2020-01-15'),
(2, 'Filial Sul', 'Rua do Sul, 200', '(11) 9876-5432', '2019-06-20'),
(3, 'Filial Norte', 'Av. Norte, 300', '(11) 2345-6789', '2018-03-10'),
(4, 'Filial Leste', 'Rua da Leste, 400', '(11) 8765-4321', '2021-07-05'),
(5, 'Filial Oeste', 'Av. Oeste, 500', '(11) 3456-7890', '2017-11-25'),
(6, 'Filial Academia', 'Rua Acadêmica, 600', '(11) 4567-8901', '2022-09-15'),
(7, 'Filial Estudantes', 'Av. Estudantes, 700', '(11) 5678-9012', '2020-05-10'),
(8, 'Filial Professores', 'Rua dos Professores, 800', '(11) 6789-0123', '2019-12-01'),
(9, 'Filial Pesquisa', 'Av. Pesquisa, 900', '(11) 7890-1234', '2021-01-30'),
(10, 'Filial Tecnologia', 'Rua da Tecnologia, 1000', '(11) 8901-2345', '2023-03-15');

SELECT * FROM cursos WHERE duracao > 30;

SELECT * FROM filiais WHERE data_abertura > '2020-01-01';


import pandas as pd
import sqlite3

# Conectando ao banco de dados
conexao = sqlite3.connect('seu_banco_de_dados.db')

# Lendo a tabela 'cursos'
cursos_df = pd.read_sql_query("SELECT * FROM cursos", conexao)

# Lendo a tabela 'filiais'
filiais_df = pd.read_sql_query("SELECT * FROM filiais", conexao)

# Fechando a conexão
conexao.close()

# Exibindo os DataFrames
print(cursos_df)
print(filiais_df)

