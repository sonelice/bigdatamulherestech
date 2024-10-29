-- criando meu primeiro banco de dados
CREATE DATABASE senac_copacabana;

-- criando minha primeira tabela/entidade
CREATE TABLE alunos (
  matricula INTEGER PRIMARY KEY,
  nome_aluno TEXT NOT NULL,
  genero TEXT NOT NULL
);
-- injeção de dados-teste
INSERT INTO alunos VALUES (1, 'Marina', 'F');
INSERT INTO alunos VALUES (2, 'Joana', 'F');


-- consultando as injeções realizadas
SELECT * FROM alunos WHERE matricula=1

-- criando meu primeiro banco de dados

CREATE DATABASE senac_copacabana;

-- criando minha segunda tabela/entidade
CREATE TABLE Professor (
  matricula INTEGER PRIMARY KEY,
  nome_professor TEXT NOT NULL,
  genero TEXT NOT NULL
);
-- injeção de dados-teste
INSERT INTO professor VALUES (1, 'Sonelice', 'F');
INSERT INTO professor VALUES (2, 'Mario', 'M');


-- consultando as injeções realizadas
SELECT * FROM Professor WHERE matricula=1


