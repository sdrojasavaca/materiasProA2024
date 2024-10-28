import sqlite3

class Estudiante:
    def __init__(self, DNI, nombre, apellido, curso):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso

    def agregar_estudiante(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('INSERT INTO estudiantes (DNI, nombre, apellido, curso) VALUES (?, ?, ?, ?)', 
                  (self.DNI, self.nombre, self.apellido, self.curso))
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

    def actualizar_estudiante(self, nuevo_nombre, nuevo_apellido, nuevo_curso):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('UPDATE estudiantes SET nombre = ?, apellido = ?, curso = ? WHERE DNI = ?', 
                  (nuevo_nombre, nuevo_apellido, nuevo_curso, self.DNI))
        conn.commit()
        conn.close()

    def eliminar_estudiante(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('DELETE FROM estudiantes WHERE DNI = ?', (self.DNI,))
        conn.commit()
        conn.close()
