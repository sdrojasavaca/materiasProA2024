BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Materia" (
	"id"	INTEGER NOT NULL,
	"nombre"	INTEGER NOT NULL,
	"curso"	INTEGER NOT NULL,
	"id_profesor"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Profesor" (
	"id"	INTEGER NOT NULL,
	"nombre"	INTEGER NOT NULL,
	"apellido"	INTEGER NOT NULL,
	"id_materia"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("id_materia") REFERENCES "Materia"("id")
);
CREATE TABLE IF NOT EXISTS "Estudiante" (
	"id"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"apellido"	TEXT NOT NULL,
	"curso"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Calificacion" (
	"id_estudiante"	INTEGER NOT NULL,
	"id_materia"	INTEGER NOT NULL,
	"nota"	INTEGER,
	FOREIGN KEY("id_estudiante") REFERENCES "Estudiante"("id"),
	FOREIGN KEY("id_materia") REFERENCES "Materia"("id")
);
COMMIT;
