CREATE DATABASE quiz;
USE quiz;

CREATE TABLE pergunta (
    id INT PRIMARY KEY AUTO_INCREMENT,
    alternativas TEXT NOT NULL,
    resposta_correata BOOLEAN NOT NULL
    );

CREATE TABLE categoria (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
    );

CREATE TABLE quiz (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(40) NOT NULL,
    url_imagem VARCHAR()
    );
