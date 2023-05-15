"""
    Guarda información en las entidades en la base de datos
"""

from base_equipo import conn

cursor = conn.cursor()

nombre_equipo = "REAL MADRID"
ciudad_equipo = "Madrid"
id_equipo = "001M"
cadena_sql = """INSERT INTO basegalo_equipo (nombre_equipo, ciudad_equipo, id_equipo) \
VALUES ('%s', '%s', '%s');""" % (nombre_equipo, ciudad_equipo, id_equipo)

cursor.execute(cadena_sql)

nombre_equipo = "JUVENTUS"
ciudad_equipo = "Turin"
id_equipo = "002T"
cadena_sql = """INSERT INTO basegalo_equipo (nombre_equipo, ciudad_equipo, id_equipo) \
VALUES ('%s', '%s', '%s');""" % (nombre_equipo, ciudad_equipo, id_equipo)

cursor.execute(cadena_sql)

nombre_equipo = "LDU"
ciudad_equipo = "Quito"
id_equipo = "003Q"
cadena_sql = """INSERT INTO basegalo_equipo (nombre_equipo, ciudad_equipo, id_equipo) \
VALUES ('%s', '%s', '%s');""" % (nombre_equipo, ciudad_equipo, id_equipo)

cursor.execute(cadena_sql)

conn.commit()

cursor.close()
