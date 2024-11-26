CREATE DATABASE quiz;
USE quiz;

CREATE TABLE categoria (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome varchar(150) NOT NULL
);

CREATE TABLE contato (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    mensagem TEXT NOT NULL,
    telefone VARCHAR(45) DEFAULT NULL,
    data_envio DATETIME NOT NULL DEFAULT NOW(),
    data_atendimento DATETIME,
    data_expiracao DATETIME
    );

CREATE TABLE login (
	id_admin INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
    );
    
CREATE TABLE quiz (
	id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(40) NOT NULL,
    url_imagem VARCHAR(255) NOT NULL,
    quantidade_perguntas INT NOT NULL CHECK(quantidade_perguntas = 5),
    categoria_id INT NOT NULL,
    pergunta_id INT NOT NULL
    );
    
CREATE TABLE perguntas (
	id INT PRIMARY KEY AUTO_INCREMENT,
    alternativas TEXT NOT NULL
    resposta_correta INT NOT NULL CHECK(resposta_correta >= 0 OR resposta_correta <= 4)
    );

INSERT INTO login (email, senha)
VALUES
	('teste@teste.com', '5758@');