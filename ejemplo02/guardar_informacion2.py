"""
    Guarda información en las entidades en la base de datos
"""

from base_jugador import conn

cursor = conn.cursor()
# nombres, num_camiseta, id_equipo
nombres = "LUCAS MODRICH"
num_camiseta = "10"
id_equipo = "001M"
cadena_sql = """INSERT INTO basegalo_jugador (nombres, num_camiseta, id_equipo) \
VALUES ('%s', '%s', '%s');""" % (nombres, num_camiseta, id_equipo)

cursor.execute(cadena_sql)

nombres = "JUAN GUILLERMO CUADRADO"
num_camiseta = "8"
id_equipo = "002T"
cadena_sql = """INSERT INTO basegalo_jugador (nombres, num_camiseta, id_equipo) \
VALUES ('%s', '%s', '%s');""" % (nombres, num_camiseta, id_equipo)

cursor.execute(cadena_sql)

nombres = "LUIS ANANGONO"
num_camiseta = "9"
id_equipo = "003Q"
cadena_sql = """INSERT INTO basegalo_jugador (nombres, num_camiseta, id_equipo) \
VALUES ('%s', '%s', '%s');""" % (nombres, num_camiseta, id_equipo)

cursor.execute(cadena_sql)

conn.commit()

cursor.close()
