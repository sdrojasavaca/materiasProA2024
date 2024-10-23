import sqlite3

class Estudiante:
    def __init__(self, DNI, nombre):
        self.DNI = DNI
        self.nombre = nombre

    def agregar_estudiante(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('INSERT INTO estudiantes (DNI, nombre) VALUES (?, ?, ?)', (self.DNI, self.nombre))
        conn.commit()
        conn.close()

    @staticmethod
    def ver_estudiantes():
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('SELECT * FROM estudiantes')
        estudiantes = c.fetchall()
        conn.close()
        return estudiantes

    def actualizar_estudiante(self, nuevo_nombre):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('UPDATE estudiantes SET nombre = ? WHERE DNI = ?', (nuevo_nombre, self.DNI))
        conn.commit()
        conn.close()

    def eliminar_estudiante(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('DELETE FROM estudiantes WHERE DNI = ?', (self.DNI,))
        conn.commit()
        conn.close()
