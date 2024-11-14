from ClsEstudiante import Estudiante
from ClsProfesor import Profesor
from ClsMateria import Materia
from ClsClasificacion import Calificacion

idEstuidante, idProfesor, idMateria= 0

def menuEstudiantes():
    while True:
        print('''
                MENU DE ESTUDIANTES
            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
            ▐⑴ Crear o añadir       ▌
            ▐⑵ Leer                 ▌
            ▐⑶ Actualizar/Editar    ▌
            ▐⑷ Borrar               ▌
            ▐⑸ Volver               ▌    
            ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀''')
        
        opcionEstudiantes = input("Elige una opción en estudiantes: ")
        
        if opcionEstudiantes =="1":
            idEstudiante= idEstudiante + 1
            nombre=input("Ingrese el nombre del estudiante que añadira")
            apellido= input("Ingrese el apellido del estudiante que añadira")
            while True: #input curso
                try: 
                    curso= int(input('''
                    Ingrese el numero del curso que pertenece el estudiante que añadira
                    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▐ 1 Primer Año      ▌
                    ▐ 2 Segundo Año     ▌
                    ▐ 3 Tercer Año      ▌
                    ▐ 4 Cuarto Año      ▌
                    ▐ 5 Quinto Año      ▌  
                    ▐ 6 Sexto Año       ▌ 
                    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀'''))
                except ValueError:
                    print  ("Valor incorrecto, ingresa de nuevo")
                    continue
                else:
                    break
            estudiante =Estudiante(idEstudiante, nombre, apellido, curso)
            estudiante.agregar_estudiante()
            print("El estudiante fue ingresado con exito")
        elif opcionEstudiantes == "2":
            print(Estudiante.ver_estudiantes)
        elif opcionEstudiantes == "3":             
             Estudiante.actualizar_estudiante
        elif opcionEstudiantes == "4":
            Estudiante.eliminar_estudiante
        elif opcionEstudiantes == "5":
            break
        else:
            print ("Opción no erronea, intenta de nuevo")
def menuProfesores():
    while True:
        print('''
                MENU DE PROFESORES
            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
            ▐⑴ Crear o añadir       ▌
            ▐⑵ Leer                 ▌
            ▐⑶ Actualizar/Editar    ▌
            ▐⑷ Borrar               ▌
            ▐⑸ Volver               ▌    
            ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀''')
        
        opcionEstudiantes = input("Elige una opción en estudiantes: ")
        
        if opcionEstudiantes =="1":
            Profesor.agregar_profesor
        elif opcionEstudiantes == "2":
            Profesor.ver_profesores
        elif opcionEstudiantes == "3":
             Profesor.actualizar_profesor
        elif opcionEstudiantes == "4":
            Profesor.eliminar_profesor
        elif opcionEstudiantes == "5":
            break
        else:
            print("Opción no erronea, intenta de nuevo")
def menuMaterias():
    while True:
        print('''
                MENU DE MATERIAS
            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
            ▐⑴ Agregar              ▌
            ▐⑵ Leer                 ▌
            ▐⑶ Actualizar           ▌
            ▐⑷ Borrar               ▌
            ▐⑸ Volver               ▌    
            ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀''')
        
        opcionEstudiantes = input("Elige una opción en estudiantes: ")
        
        if opcionEstudiantes =="1":
            Materia.agregar_materia
        elif opcionEstudiantes == "2":
            Materia.ver_materia
        elif opcionEstudiantes == "3":
            Materia.actualizar_materia
        elif opcionEstudiantes == "4":
            Materia.eliminar_materia
        elif opcionEstudiantes == "5":
            break
        else:
            print("Opción no erronea, intenta de nuevo")                            
def menuCalificaciones():
    while True:
        print('''
                MENU DE CALIFICACIONES
            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
            ▐⑴ Crear o añadir           ▌
            ▐⑵ Leer                     ▌
            ▐⑶ Actualizar/Editar        ▌
            ▐⑷ Borrar                   ▌
            ▐⑸ Volver                   ▌    
            ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀''')
        
        opcionEstudiantes = input("Elige una opción en estudiantes: ")
        
        if opcionEstudiantes =="1":
            Calificacion.agregar_calificacion
        elif opcionEstudiantes == "2":
            Calificacion.ver_calificaciones
        elif opcionEstudiantes == "3":
            Calificacion.actualizar_calificacion
        elif opcionEstudiantes == "4":
            Calificacion.eliminar_calificacion
        elif opcionEstudiantes == "5":
            break
        else:
            print("Opción erronea, intenta de nuevo")

def menu():
        while True:
            print('''
                        MENU
                ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                ▐⑴ Estudiantes          ▌
                ▐⑵ Profesores           ▌
                ▐⑶ Materias             ▌
                ▐⑷ Calificaciones       ▌
                ▐⑸ Salir                ▌    
                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀''')

            opcion = input("Elige la entidad: ")

            if opcion == "1":
                menuEstudiantes()
            elif opcion == "2":
                menuProfesores()
            elif opcion == "3":
                menuMaterias()
            elif opcion == "4":
                menuCalificaciones()
            elif opcion == "5":
                break
            else:
                print("Opción erronea, intenta de nuevo")
menu()