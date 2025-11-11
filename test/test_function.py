import psycopg2

def test_descuento():
  conn = psycopg2.connect(
      dbname='test_db',
      user='postgres',
      password='postgres',
      host='localhost',
      port='5432'
  )
  conn.autocommit = False
  try:
      cur = conn.cursor()
      query="SELECT calcular_desc(%s,%s)"
      cur.execute(query,(50.0,1.5));
      result=cur.fetchone()[0];
      assert result is None;
      cur.execute(query,(50.0,0.5));
      result=cur.fetchone()[0];
      assert result==25.0;
      conn.commit()
  except Exception as e:
      raise e
  finally:
      conn.rollback()
      cur.close()
      conn.close()

  def test_correo():
    conn = psycopg2.connect(
        dbname='test_db',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )
    conn.autocommit = False
    try:
        cur = conn.cursor()
        query="SELECT validar_correo(%s)"
        cur.execute(query,('yazg8',));
        result=cur.fetchone()[0];
        assert result is False;
        cur.execute(query,('yazmin.guerreroguev@gmail.com',));
        result=cur.fetchone()[0];
        assert result is True;
        conn.commit()
    except Exception as e:
        raise e
    finally:
        conn.rollback()
        cur.close()
        conn.close()

def test_stock():
    conn = psycopg2.connect(
        dbname='test_db',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )
    conn.autocommit = False
    try:
        cur = conn.cursor()
        query="SELECT * from stock_menor(%s)"
        cur.execute(query,(5,));
        result=cur.fetchall();
        nombres=[row[1] for row in result]
        assert 'Mousepad' in nombres
        assert 'Tarjeta' in nombres
        conn.commit()
    except Exception as e:
        raise e
    finally:
        conn.rollback()
        cur.close()
        conn.close()

def test_fecha():
    conn = psycopg2.connect(
        dbname='test_db',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )
    conn.autocommit = False
    try:
        cur = conn.cursor()
        query="SELECT dia_semana(%s)"
        cur.execute(query,('2025-11-08',));
        result=cur.fetchone()[0];
        assert result=='SATURDAY'
        conn.commit()
    except Exception as e:
        raise e
    finally:
        conn.rollback()
        cur.close()
        conn.close()

def test_empleados():
    conn = psycopg2.connect(
        dbname='test_db',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )
    conn.autocommit = False
    try:
        cur = conn.cursor()
        query="SELECT total_depEmpleados(%s)"
        cur.execute(query,(1,));
        result=cur.fetchone()[0];
        assert result==1
        cur.execute(query,(2,));
        result=cur.fetchone()[0];
        assert result==1
        conn.commit()
    except Exception as e:
        raise e
    finally:
        conn.rollback()
        cur.close()
        conn.close()



