Passo 1
(O Banco de Dados): Crie um
banco de dados chamado zoologico. Em seguida, escreva o comando
para dizer ao MySQL que você quer usar (ativar) esse banco de dados
específico.

CREATE DATABASE rei_leao;
USE rei_leao;

--------------------------------------------------------------------------------

Passo 2
(A Tabela): Crie a
tabela animais dentro desse banco. Ela deve
conter:

id: número inteiro, chave primária
e incremento automático.                  

nome: texto (máx 50 carac.), obrigatório

especie: texto (máx 30 carac.), obrigatório

idade_anos: inteiro

reino: texto (máx 20 carac.) — ex: 'Savana', 'Répteis'

peso_kg: decimal (2 casas)

CREATE TABLE personagens (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    especie VARCHAR(30) NOT NULL,
    idade_anos INT,
    reino VARCHAR(20),
    peso_kg DECIMAL(10,2)
);

--------------------------------------------------------------------------------

Passo 3
(Inserção): Insira
os 5 animais na tabela:

INSERT INTO personagens (nome, especie, idade_anos, reino, peso_kg)
VALUES
('Simba', 'Leão', 5, 'Pedra do Rei', 190.50),
('Nala', 'Leoa', 5, 'Pedra do Rei', 160.20),
('Mufasa', 'Leão', 40, 'Pedra do Rei', 210.00),
('Timon', 'Suricato', 10, 'Selva', 15.50),
('Pumba', 'Javali', 12, 'Selva', 90.00),
('Scar', 'Leão', 8, 'Pedra do Rei', 180.00),
('Zazu', 'Ave', 7, 'Pedra do Rei', 1.50),
('Rafiki', 'Mandril', 15, 'Floresta', 35.00),
('Shenzi', 'Hiena', 6, 'Selva', 70.00),
('Banzai', 'Hiena', 5, 'Selva', 65.00);

--------------------------------------------------------------------------------

Passo 4
(Filtro por Setor): Escreva
uma consulta (SELECT) que mostre o nome e a idade_anos apenas
dos animais do setor 'Pedra do rei'.

SELECT nome, idade_anos
FROM personagens
WHERE reino = 'Pedra do Rei';

--------------------------------------------------------------------------------

Passo 5
(Filtro por Peso): Escreva
uma consulta que traga todos os dados dos animais que pesam menos de 50 kg.

SELECT *
FROM personagens
WHERE peso_kg < 50.00;

--------------------------------------------------------------------------------

Passo 6 (Ordenação): Escreva
uma consulta que liste todos os animais mostrando nome e especie,
ordenados do mais velho para o mais novo (idade decrescente).

SELECT nome, especie
FROM personagens
ORDER BY idade_anos DESC;

--------------------------------------------------------------------------------