CREATE TABLE productos(
  id SERIAL PRIMARY KEY,
  nombre TEXT,
  precio NUMERIC,
  cantidad INT
);

CREATE TABLE departamento(
  id SERIAL PRIMARY KEY,
  nombre TEXT
);

CREATE TABLE empleado(
  id SERIAL PRIMARY KEY,
  nombre TEXT,
  id_dep INT REFERENCES departamento(id)
);
