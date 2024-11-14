import sqlite3

class Calificacion:
    def __init__(self, id_estudiante, id_materia, nota):
        self.id_estudiante = id_estudiante
        self.id_materia = id_materia
        self.nota = nota

    def agregar_calificacion(self):
        conn = sqlite3.connect('escolar.sqbpro')
        c = conn.cursor()
        c.execute('INSERT INTO calificaciones (id_estudiante, id_materia, nota) VALUES (?, ?, ?)', 
                  (self.id_estudiante, self.id_materia, self.nota))
        conn.commit()
        conn.close()

    @staticmethod
    def ver_calificaciones():
        conn = sqlite3.connect('escolar.sqbpro')
        c = conn.cursor()
        c.execute('SELECT * FROM calificaciones')
        calificaciones = c.fetchall()
        conn.close()
        return calificaciones

    def actualizar_calificacion(self, nueva_nota):
        conn = sqlite3.connect('escolar.sqbpro')
        c = conn.cursor()
        c.execute('UPDATE calificaciones SET nota = ? WHERE id_estudiante = ? AND id_materia = ?', 
                  (nueva_nota, self.id_estudiante, self.id_materia))
        conn.commit()
        conn.close()

    def eliminar_calificacion(self):
        conn = sqlite3.connect('escolar.sqbpro')
        c = conn.cursor()
        c.execute('DELETE FROM calificaciones WHERE id_estudiante = ? AND id_materia = ?', 
                  (self.id_estudiante, self.id_materia))
        conn.commit()
        conn.close()