
create table IF NOT EXISTS usuarios (
id INT primary key,
genero char(1),
edad int(3),
ocupacion int,
cp varchar(20)
);

CREATE TABLE IF NOT EXISTS peliculas (
   id INT PRIMARY KEY, 
   titulo VARCHAR(40), 
   generos VARCHAR(40)
); 

CREATE TABLE IF NOT EXISTS valoraciones (
   usuario_id INT,
   pelicula_id INT,
   valoracion INT,
   duracion BIGINT,
   FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
   FOREIGN KEY (pelicula_id) REFERENCES peliculas(id) 
   );