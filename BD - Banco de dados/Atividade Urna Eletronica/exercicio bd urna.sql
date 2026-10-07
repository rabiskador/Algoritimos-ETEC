create database eleicao;

CREATE TABLE partido (
    id_partido INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(10) NOT NULL,
    sigla VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE candidato (
    id_candidato INT PRIMARY KEY AUTO_INCREMENT,
    numero INT NOT NULL UNIQUE,
    nome VARCHAR(10) NOT NULL,
    id_partido INT NOT NULL,
    
    FOREIGN KEY (id_partido) REFERENCES partido(id_partido)
);

CREATE TABLE eleitor (
 id_eleitor INT PRIMARY KEY AUTO_INCREMENT,
 nome VARCHAR(10) NOT NULL,
 titulo VARCHAR(20) NOT NULL UNIQUE,
 cidade VARCHAR(50)
 );

    