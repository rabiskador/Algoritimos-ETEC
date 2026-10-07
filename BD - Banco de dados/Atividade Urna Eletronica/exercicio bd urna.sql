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

 CREATE TABLE voto (
 id_voto INT PRIMARY KEY AUTO_INCREMENT,
 id_eleitor INT NOT NULL UNIQUE,
 id_candidato  INT NOT NULL,
 data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
 
 FOREIGN KEY (id_eleitor) REFERENCES eleitor(id_eleitor),
FOREIGN KEY (id_candidato) REFERENCES candidato(id_candidato)
);

INSERT INTO partido (nome, sigla) VALUES
('Partido MENINONEY', 'NEY'),
('Partido PAPAICRIS', 'CR7'),
('Partido ET', 'GOAT');

INSERT INTO candidato (nome, numero, id_partido) VALUES
('NEYMAR JUNIOR', 11, 7),
('CRISTIANO RONALDO', 7, 8),
('LIONEL MESSI', 10, 9);

SELECT * FROM partido