# ¿Cuál es el nombre de los empleados que realizaron cada venta?
select venta.id_venta, venta.clave, empleado.nombre, empleado.apellido_paterno, empleado.apellido_materno
from empleado,venta,articulo where
venta.id_empleado=empleado.id_empleado and
venta.id_articulo=articulo.id_articulo order by clave;

#¿Cuál es el nombre de los artículos que se han vendido?
select venta.clave as claveProducto,articulo.nombre as nombreArticulo
from articulo,venta
where articulo.id_articulo=venta.id_articulo 
order by clave;

#¿Cuál es el total de cada venta?
SELECT venta.clave, sum(articulo.precio) as totalVenta
FROM venta ,articulo where
venta.id_articulo=articulo.id_articulo
group by clave
order by clave;


select clave,count(clave) from venta group by clave;