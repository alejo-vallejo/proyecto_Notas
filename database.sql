-- CREAR BASE DE DATOS
CREATE DATABASE notas_db;

-- TABLA USUARIOS
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    password VARCHAR(100)
);

-- TABLA NOTAS
CREATE TABLE notas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200),
    contenido TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_id INTEGER REFERENCES usuarios(id)
);



INSERT INTO usuarios (nombre, password) VALUES
('Juan', '123'),
('Maria', '123'),
('Carlos', '123'),
('Ana', '123'),
('Luis', '123');

INSERT INTO notas (titulo, contenido, usuario_id) VALUES
('Nota 1', 'Contenido 1', 1),
('Nota 2', 'Contenido 2', 2),
('Nota 3', 'Contenido 3', 3),
('Nota 4', 'Contenido 4', 4),
('Nota 5', 'Contenido 5', 5);