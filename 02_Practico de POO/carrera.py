from Personaje_clase import Personaje
personajes = []
def crearPersonaje():
    nombre = input("Ingresa el nombre del personaje: ")
    while True:
        try:
            ataque = int(input(f"Ingresa el ataque de {nombre} 1/100: "))
            if 1 <= ataque <= 100:
                break
            else:
                print("el valor del ataque debe ser entre 1 y 100")
                print(f"Vuelva a ingresar el ataque de {nombre} 1/100")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")
    while True:
        try:
            defensa = int(input(f"Ingresa la defensa de {nombre} 1/100: "))
            if 1 <= defensa <= 100:
                break
            else:
                print("el valor de la defensa debe ser entre 1 y 100")
                print(f"Vuelva a ingresar la defensa de {nombre} 1/100")

        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")
    return Personaje(nombre, ataque, defensa)

def mostrarInformacion(personajes):
    for i, personaje in enumerate(personajes):
        estado = "Vivo" if personaje.estado else "Muerto"
        print(f"Personaje {i+1}: {personaje.nombre}, Ataque: {personaje.ataque}, Defensa: {personaje.defensa}, Estado: {estado}, Vida: {personaje.vida}")

def simular_ataque(personajes):
    if len(personajes) < 2:
        print("No hay suficientes personajes para simular un ataque.")
        return
    else:
        mostrarInformacion(personajes)
        print("\n")
        atacanteIndice = int(input("Elige el número del personaje que atacará: ")) - 1
        defensorIndice= int(input("Elige el número del personaje que recibirá el ataque: ")) - 1
        print("\n")

        if atacanteIndice == defensorIndice:
            print("No se puede atacar a si mismo el pesronaje")
            return
        else:
            atacante = personajes[atacanteIndice]
            defensor = personajes[defensorIndice]

            atacante.atacar(defensor)
            if defensor.estado:
                defensor.atacar(atacante)

            mostrarInformacion(personajes)

def juego():
        while True:
            print('''
                ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                ▐⑴ Jugar                ▌
                ▐⑵ Añadir jugador       ▌
                ▐⑶ Mostrar informacion  ▌
                ▐⑷ Salir                ▌  
                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀''')
            opcion = input("Elige una opción: ")

            if opcion == "1":
                if len(personajes) >= 2:
                    simular_ataque(personajes)
                else:
                    print("Tiene que haber minimo 2 personajes creados")

            elif opcion == "2":
                cantidad = int(input("¿Cuantos personajes queres crear? "))
                for i in range(cantidad):
                    personajes.append(crearPersonaje())
                    if i < cantidad - 1 : 
                        print("\n Crea el siguiente personaje \n")

            elif opcion == "3":
                if personajes:
                    mostrarInformacion(personajes)
                else:
                    print("Antes tenes que crear personajes")
            
            elif opcion == "4":
                print("Saliendo del juego.")
                break
            else:
                print("Opción no erronea, intenta de nuevo")
juego()