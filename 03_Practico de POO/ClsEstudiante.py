import sqlite3

class Estudiante:
    def __init__(self, id, nombre, apellido, curso):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso

    def agregar_estudiante(self, id, nombre, apellido, curso):
        conn = sqlite3.connect('escolar.sqbpro')
        c = conn.cursor()
        c.execute('INSERT INTO estudiantes (id, nombre, apellido, curso) VALUES (?, ?, ?, ?)', 
                  (self.id, self.nombre, self.apellido, self.curso))
        conn.commit()
        conn.close()

    @staticmethod
    def ver_estudiantes():
        conn = sqlite3.connect('escolar.sqbpro')
        c = conn.cursor()
        c.execute('SELECT * FROM estudiantes')
        estudiantes = c.fetchall()
        conn.close()
        return estudiantes

    def actualizar_estudiante(self, id, nuevo_nombre, nuevo_apellido, nuevo_curso):
        conn = sqlite3.connect('escolar.sqbpro')
        c = conn.cursor()
        c.execute('UPDATE estudiantes SET nombre = ?, apellido = ?, curso = ? WHERE id = ?', 
                  (nuevo_nombre, nuevo_apellido, nuevo_curso, self.id))
        conn.commit()
        conn.close()

    def eliminar_estudiante(self, id):
        conn = sqlite3.connect('escolar.sqbpro')
        c = conn.cursor()
        c.execute('DELETE FROM estudiantes WHERE id = ?', (self.id,))
        conn.commit()
        conn.close()
