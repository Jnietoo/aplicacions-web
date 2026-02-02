import mysql.connector

# Configuración de conexión (basada en tu imagen de phpMyAdmin)
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="practica5"
    )

def insertar_usuario(nombre, mail):
    conn = conectar()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO usuarios (usuario, mails) VALUES (%s, %s)"
        cursor.execute(sql, (nombre, mail))
        conn.commit()
        return True
    except:
        return False
    finally:
        cursor.close()
        conn.close()

def buscar_mail(nombre):
    conn = conectar()
    cursor = conn.cursor()
    sql = "SELECT mails FROM usuarios WHERE usuario = %s"
    cursor.execute(sql, (nombre,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    # Devuelve el mail si existe, o None si no
    return resultado[0] if resultado else None