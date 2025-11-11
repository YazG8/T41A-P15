CREATE OR REPLACE FUNCTION calcular_desc(monto NUMERIC, descuento NUMERIC)
RETURNS NUMERIC AS $$
BEGIN
    IF descuento<=0 or descuento>=1 THEN
      RAISE NOTICE 'Formato erroneo(Debe ser decimal 50%%=>0.5)';
      RETURN Null;
    ELSE 
      RETURN monto*(1-descuento);
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION validar_correo(correo TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    IF POSITION('@' IN correo) > 0 THEN
      RETURN true;
    ELSE 
      RETURN false;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION stock_menor(cant_minima INT)
RETURNS SETOF productos AS $$
BEGIN
    RETURN QUERY SELECT * FROM PRODUCTOS WHERE cantidad<cant_minima;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION dia_semana(fecha DATE)
RETURNS TEXT AS $$
BEGIN
    RETURN UPPER(TRIM(TO_CHAR(fecha, 'Day')));
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION total_depEmpleados(dep INT)
RETURNS INT AS $$
BEGIN
    RETURN (SELECT COUNT(*) FROM empleado WHERE id_dep=dep);
END;
$$ LANGUAGE plpgsql;
