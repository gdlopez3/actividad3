"""
    Crear entidades en la base de datos
"""

from base_equipo import conn

cursor = conn.cursor()

cadena_sql = 'CREATE TABLE basegalo_equipo (nombre_equipo TEXT, ciudad_equipo TEXT, id_equipo TEXT)'

cursor.execute(cadena_sql)

cursor.close()