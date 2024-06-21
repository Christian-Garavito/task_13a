import psycopg2

host = "localhost"
database = "postgres"
user = "postgres"
password = "1802877"
port = 5432

def connect():
    return psycopg2.connect(dbname=database, user=user, password=password, host=host, port=port)

def read_contenidos():
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM public.tabla_contenido_imdb")# ejecuteme este sql
        rows = cursor.fetchall()# el cursor ejecuto su comando entoces traigame los resultados de la ejecucion
        return rows
    except psycopg2.Error as e:
        print("Error:", e)
    finally:# asi halla terminado bien o mal finalice la ejecucion 
        cursor.close()
        conn.close()


def create_contenido(pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula):
    conn = connect()
    cursor = conn.cursor()
    try:
        #comando sql para ingresar datos
        sql = "INSERT INTO public.tabla_contenido_imdb (pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula) VALUES (%s, %s, %s, %s, %s,%s)" # placeholders dejar informacion dumi miestras se pasa a la funcion 
        # espacio que va llenar
        cursor.execute(sql, (pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula))
        # la base de datos transaciones conn.commit() es agregarlos conn.rollback es devolverlos no los aplique 
        conn.commit()
        print("nuevo contenido")
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


def update_comando(pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula):
    conn = connect()
    cursor = conn.cursor()
    try:
        sql = "UPDATE public.tabla_contenido_imdb SET titulo_pelicula = %s, ano_pelicula = %s, fk_id_tipo_contenido = %s, director_pelicula = %s, valor_pelicula = %s WHERE pk_id_peliculas = %s"
        cursor.execute(sql, (titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula,pk_id_peliculas))
        conn.commit()
        print("contenido modificaod.")
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
