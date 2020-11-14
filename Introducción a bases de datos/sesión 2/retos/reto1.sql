/* RETO1*/

/*¿Qué artículos incluyen la palabra Pasta en su nombre?*/
SELECT * FROM articulo WHERE nombre LIKE '%PASTA%';

/*2. ¿Qué artículos incluyen la palabra Cannelloni en su nombre?*/
SELECT nombre FROM articulo WHERE nombre LIKE '%Cannelloni%';

/* 3. ¿Qué nombres están separados por un guión (-) por ejemplo Puree - Kiwi?*/
SELECT nombre FROM articulo WHERE nombre LIKE '%-%';

/* 4. ¿Qué puestos incluyen la palabra Designer?*/
SELECT nombre FROM puesto WHERE nombre LIKE '%Designer%';

/*5. ¿Qué puestos incluyen la palabra Developer?*/
SELECT nombre FROM puesto WHERE nombre LIKE '%Developer%';
