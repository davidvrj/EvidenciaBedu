#Querie 1)
#¿Cuál es el nombre de los empleados cuyo sueldo es menor a $10,000?
#Sin subquery
select empleado.nombre,apellido_paterno,apellido_materno from empleado,puesto where 
empleado.id_puesto=puesto.id_puesto and puesto.salario<10000;
#Con subquery
SELECT nombre, apellido_paterno,apellido_materno FROM empleado WHERE id_puesto IN
 (SELECT id_puesto FROM puesto WHERE salario <10000);
 
#Querie 2)
#¿Cuál es la cantidad mínima y máxima de ventas de cada empleado?
SELECT id_empleado,min(total_ventas), max(total_ventas)FROM
 (SELECT clave, id_empleado, count(*) total_ventas FROM venta
      GROUP BY clave, id_empleado) AS sq
GROUP BY id_empleado;

#Querie 3)
#¿Cuáles claves de venta incluyen artículos cuyos precios son mayores a $5,000?
SELECT clave, id_articulo FROM venta
 WHERE id_articulo IN (
 SELECT id_articulo FROM
 articulo WHERE precio > 5000);