/* RETO2*/

#¿Cuál es el promedio de salario de los puestos?
select avg(salario) from puesto;

#¿Cuántos artículos incluyen la palabra Pasta en su nombre?
select count(*) FROM articulo WHERE nombre LIKE '%pasta%';

#¿Cuál es el salario mínimo y máximo?
select min(salario), max(salario) from puesto;

#¿Cuál es la suma del salario de los últimos cinco puestos agregados?
select sum(salario) from puesto order by id_puesto desc limit 5;

