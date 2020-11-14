/* RETO3*/

#¿Cuántos registros hay por cada uno de los puestos?
select nombre, count(*) from puesto group by nombre;

#¿Cuánto dinero se paga en total por puesto?
select nombre, sum(salario) from puesto group by nombre;

#¿Cuál es el número total de ventas por vendedor?
select id_empleado, count(clave) as ventas from venta group by id_empleado;

#¿Cuál es el número total de ventas por artículo?
select id_articulo, count(*) from venta group by id_articulo;