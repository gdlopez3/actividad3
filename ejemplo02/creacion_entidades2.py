"""
    Crear entidades en la base de datos
"""

from base_jugador import conn

cursor = conn.cursor()

cadena_sql = 'CREATE TABLE basegalo_jugador (nombres TEXT, num_camiseta TEXT, id_equipo TEXT)'

cursor.execute(cadena_sql)

cursor.close()