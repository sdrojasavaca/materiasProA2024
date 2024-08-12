listTask={}

def addTask():
    task= input("Ingrese la nueva tarea: ")
    if task not in listTask:
        listTask[task] = False
        print(f"Tarea {task} añadida a la lista")
    else:
        print(f"La tarea {task} ya existe en la lista")

def lookTask():
    if listTask:
        print("Lista de Tfareas")
        for task, completed in listTask.items():
            state = "Completada" if completed else "pendiente"
            print(f"- {task}: {state}")

    else:
        print("No hay tareas en la lista")

def markTask():
    completedTask = input("Ingrese el nombre de la tarea que ha completado: ")
    if completedTask in listTask:
        listTask[completedTask] = True
        print(f"Tarea {completedTask} marcada como completada.")
    else:
        print(f"La tarea {completedTask} no se encuentra en la lista.")


def eliminateTask():
    deleteTask = input("Ingrese el nombre de la tarea que desea eliminar: ")
    if deleteTask in listTask:
        del listTask[deleteTask]
        print(f"La tarea {deleteTask} fue eliminada de la lista")
    else:
        print(f"La tarea {deleteTask} no se esta en la lista")

while True:
    print('''
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
▐⑴ Añadir tarea         ▌
▐⑵ Ver tareas           ▌
▐⑶ Marcar completada una tarea      ▌
▐⑷ Elimiar Tarea        ▌  
▐⑸ Salir                ▌
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀''')
    option  = input("Ingrese el numero de la operación que desea realizar: ")

    if option == '1':
        addTask()
    elif option == '2':
        lookTask()
    elif option == '3':
        markTask()
    elif option == '4':
        eliminateTask()
    elif option == '5' :
      break
    else:
        print("Opción no válida")
print("chau, adios")





