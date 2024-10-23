import sqlite3

class Profesor:
    def __init__(self, id_profesor, nombre):
        self.id_profesor = id_profesor
        self.nombre = nombre

    def agregar_profesor(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('INSERT INTO profesores (id_profesor, nombre) VALUES (?, ?)', (self.id_profesor, self.nombre))
        conn.commit()
        conn.close()

    @staticmethod
    def ver_profesores():
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('SELECT * FROM profesores')
        profesores = c.fetchall()
        conn.close()
        return profesores

    def actualizar_profesor(self, nuevo_nombre):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('UPDATE profesores SET nombre = ? WHERE id_profesor = ?', (nuevo_nombre, self.id_profesor))
        conn.commit()
        conn.close()

    def eliminar_profesor(self):
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()
        c.execute('DELETE FROM profesores WHERE id_profesor = ?', (self.id_profesor,))
        conn.commit()
        conn.close()