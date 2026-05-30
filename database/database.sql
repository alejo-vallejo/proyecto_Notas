-- ============================================
-- SISTEMA DE NOTAS - BASE DE DATOS
-- PostgreSQL
-- ============================================

-- Crear la base de datos (ejecutar como superusuario)
-- CREATE DATABASE notas_db;

-- ============================================
-- TABLA: usuarios
-- ============================================
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

-- ============================================
-- TABLA: notas
-- ============================================
CREATE TABLE IF NOT EXISTS notas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    contenido TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Índice para búsquedas por usuario
CREATE INDEX IF NOT EXISTS idx_notas_usuario_id ON notas(usuario_id);

-- Índice para ordenar por fecha
CREATE INDEX IF NOT EXISTS idx_notas_fecha ON notas(fecha DESC);

-- ============================================
-- DATOS DE PRUEBA
-- ============================================
INSERT INTO usuarios (nombre, password) VALUES
('Juan', '123'),
('Maria', '123'),
('Carlos', '123'),
('Ana', '123'),
('Luis', '123')
ON CONFLICT (nombre) DO NOTHING;

INSERT INTO notas (titulo, contenido, usuario_id) VALUES
('Nota 1', 'Contenido de la primera nota', 1),
('Nota 2', 'Contenido de la segunda nota', 2),
('Nota 3', 'Contenido de la tercera nota', 3),
('Nota 4', 'Contenido de la cuarta nota', 4),
('Nota 5', 'Contenido de la quinta nota', 5)
ON CONFLICT DO NOTHING;
