import sqlite3

class Materia:
    def __init__(self, id_materia, nombre, curso, id_profesor):
        self.id_materia = id_materia
        self.nombre = nombre
        self.curso = curso
        self.id_profesor = id_profesor

    def agregar_materia(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('INSERT INTO materias (id_materia, nombre, curso, id_profesor) VALUES (?, ?, ?, ?)', 
                  (self.id_materia, self.nombre, self.curso, self.id_profesor))
        conn.commit()
        conn.close()

    @staticmethod
    def ver_materia():
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('SELECT * FROM materias')
        materias = c.fetchall()
        conn.close()
        return materias

    def actualizar_materia(self, nuevo_nombre):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('UPDATE materias SET nombre = ? WHERE id_materia = ?', (nuevo_nombre, self.id_materia))
        conn.commit()
        conn.close()

    def eliminar_materia(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('DELETE FROM materias WHERE id_materia = ?', (self.id_materia,))
        conn.commit()
        conn.close()