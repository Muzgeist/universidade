CREATE DATABASE universidade;

use universidade;

CREATE TABLE alunos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(250) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    cpf CHAR(11) NOT NULL UNIQUE,
    telefone CHAR(12) UNIQUE,
    endereco VARCHAR(250),
    matricula BOOLEAN DEFAULT True

);