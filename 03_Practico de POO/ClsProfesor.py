import sqlite3

class Profesor:
    def __init__(self, id_profesor, nombre, apellido, id_materia):
        self.id_profesor = id_profesor
        self.nombre = nombre
        self.apellido = apellido
        self.id_materia = id_materia

    def agregar_profesor(self):
        conn = sqlite3.connect('escolar.sqbpro')
        c = conn.cursor()
        c.execute('INSERT INTO profesores (id_profesor, nombre, apellido, id_materia) VALUES (?, ?, ?, ?)', 
                  (self.id_profesor, self.nombre, self.apellido, self.id_materia))
        conn.commit()
        conn.close()

    @staticmethod
    def ver_profesores():
        conn = sqlite3.connect('escolar.sqbpro.sql')
        c = conn.cursor()
        c.execute('SELECT * FROM profesores')
        profesores = c.fetchall()
        conn.close()
        return profesores

    def actualizar_profesor(self, nuevo_nombre, nuevo_apellido, nuevo_id_materia):
        conn = sqlite3.connect('escolar.sqbpro')
        c = conn.cursor()
        c.execute('UPDATE profesores SET nombre = ?, apellido = ?, id_materia = ? WHERE id_profesor = ?', 
                  (nuevo_nombre, nuevo_apellido, nuevo_id_materia, self.id_profesor))
        conn.commit()
        conn.close()

    def eliminar_profesor(self):
        conn = sqlite3.connect('escolar.sqbpro')
        c = conn.cursor()
        c.execute('DELETE FROM profesores WHERE id_profesor = ?', (self.id_profesor,))
        conn.commit()
        conn.close()
