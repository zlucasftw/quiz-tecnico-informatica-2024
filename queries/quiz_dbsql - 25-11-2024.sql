CREATE DATABASE quiz;

CREATE DATABASE quiz;
USE quiz;

CREATE TABLE categoria (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome varchar(150) NOT NULL
);

DROP TABLE contato;

CREATE TABLE contato (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    mensagem TEXT NOT NULL,
    telefone VARCHAR(45) DEFAULT NULL,
    data_envio DATETIME DEFAULT NOW()
);

ALTER TABLE contato
RENAME COLUMN ID TO id;

CREATE TABLE login (
	id_admin INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
    );
    
CREATE TABLE quiz (
	id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(40) NOT NULL,
    url_imagem VARCHAR(255) NOT NULL,
    quantidade_perguntas INT NOT NULL CHECK(quantidade_perguntas >= 5 OR quantidade_perguntas <= 8),
    categoria_id INT NOT NULL,
    pergunta_id INT NOT NULL
    );
    
DROP TABLE quiz;

CREATE TABLE pergunta (
	id INT PRIMARY KEY AUTO_INCREMENT,
    alternativas TEXT NOT NULL,
    resposta_correta BOOLEAN NOT NULL
);


    
	