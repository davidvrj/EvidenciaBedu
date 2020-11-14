
#Obtener el puesto de un empleado.
CREATE VIEW puestos AS
SELECT concat(e.nombre, ' ', e.apellido_paterno), p.nombre
FROM empleado e
JOIN puesto p
  ON e.id_puesto = p.id_puesto;

SELECT *
FROM puestos;

#Saber qué artículos ha vendido cada empleado.
CREATE VIEW empleado_articulo AS
SELECT v.clave, concat(e.nombre, ' ', e.apellido_paterno) nombre, a.nombre articulo
FROM venta v
JOIN empleado e
  ON v.id_empleado = e.id_empleado
JOIN articulo a
  ON v.id_articulo = a.id_articulo
ORDER BY v.clave;

SELECT *
FROM  empleado_articulo;

# Saber qué puesto ha tenido más ventas.
CREATE VIEW puesto_ventas AS
SELECT p.nombre, count(v.clave) total
FROM venta v
JOIN empleado e
  ON v.id_empleado = e.id_empleado
JOIN puesto p
  ON e.id_puesto = p.id_puesto
GROUP BY p.nombre;

SELECT *
FROM puesto_ventas
ORDER BY total DESC
LIMIT 1;


