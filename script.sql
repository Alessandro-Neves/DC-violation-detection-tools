-- Task: Existe alguma maneira para forçar a interrupção da pesquisa/junção após encontrar 
-- a primeira tupla ? [Não]

CREATE TABLE T AS SELECT * FROM 'tax_100k_noisy_0.5.csv';

SELECT * FROM T t1 JOIN T t2 ON t1.State = t2.State AND t1.Salary > t2.Salary AND t1.Rate < t2.Rate;

SELECT t1.id, t2.id FROM T t1 JOIN T t2 ON t1.State = t2.State AND t1.Salary > t2.Salary AND t1.Rate < t2.Rate;


SELECT * FROM T t1 WHERE EXISTS ( 
  SELECT 1 FROM T t2 t1.State = t2.State AND t1.Salary > t2.Salary AND t1.Rate < t2.Rate
);

SELECT * FROM T t1 WHERE EXISTS ( 
  SELECT 1 FROM T t2 t1.State = t2.State AND t1.Salary > t2.Salary AND t1.Rate < t2.Rate 
);

SELECT CASE WHEN EXISTS (
  SELECT 1 FROM T t1 JOIN T t2 ON t1.State = t2.State AND t1.Salary > t2.Salary AND t1.Rate < t2.Rate
)
  THEN 'At least one combination exists'
  ELSE 'No combination exists'
END AS result;

SELECT * FROM T1 JOIN T2 ON T1.salary > T2.salary AND T1.ano > T2.ano LIMIT 1; -- ou TOP 1 (SQL Server)

-- Não encontrei uma maneira usando apenas SQL de instruir o DBMS para para de realizar o JOIN ou FILTER após 
-- encontrar a primeira combinação, a clausula para informar isso é LIMIT ou TOP (SQL Server), porém é responsabilidade 
-- do Query Optimizer e Execution Engine decidir a melhor maneira de executar a query, para o  DuckDB os 3 tipos de query 
-- com e sem LIMIT possuem praticamente o mesmo tempo de execução (tax_100k_noisy_0.5.csv / tax_dc4)

-- MySQL
CREATE TABLE IF NOT EXISTS T (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  salary DECIMAL,
  hiring_year INTEGER
);

-- PostgreSQL
CREATE TABLE IF NOT EXISTS EMPLOYEES (
  id SERIAL PRIMARY KEY,
  salary DECIMAL,
  hiring_year INTEGER
);

SELECT t1.id as id1, t2.id as id2  FROM T t1 JOIN T t2  ON t1.salary > t2.salary  AND t1.hiring_year > t2.hiring_year  AND t1.id <> t2.id LIMIT 1;
