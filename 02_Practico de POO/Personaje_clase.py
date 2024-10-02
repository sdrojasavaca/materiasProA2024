import random
class Personaje:
    #atributo de clase
    estado = True #define el estado del personaje como vivo mientras sea True
    vida = 100

    #constructor / atributo de instancia
    def __init__(self, nombre, ataque, defensa):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.estado = Personaje.estado
        self.vida = Personaje.vida

    def atacar(self, otro_jugador):
        if self.estado:
            danno = random.randint(0, self.ataque)
            if danno >= 1:
                if otro_jugador.defensa > 0:
                    if danno > otro_jugador.defensa:
                        danno_restante = danno - otro_jugador.defensa
                        otro_jugador.defensa = 0
                        otro_jugador.vida -= danno_restante
                    else:
                        otro_jugador.defensa -= danno
                    print(f"{otro_jugador.nombre} se quedó con {otro_jugador.defensa} de defensa y {otro_jugador.vida} de vida después del ataque")
                else:
                    otro_jugador.vida -= danno
                    print(f"{otro_jugador.nombre} se quedó con {otro_jugador.vida} de vida después del ataque")
                
                if otro_jugador.vida <= 0:
                    otro_jugador.estado = False
                    otro_jugador.vida = 0
                    print(f"{otro_jugador.nombre} ha muerto")
            else:
                print(f"{self.nombre} no provoca nada de daño en su ataque")
        else:
            print(f"{self.nombre} no puede atacar, está muerto")

    def recibirDano(self, otro_jugador):
        if otro_jugador.estado:
            danno = random.randint(0, otro_jugador.ataque)
            if danno >= 1:
                if self.defensa > 0:
                    if danno > self.defensa:
                        danno_restante = danno - self.defensa
                        self.defensa = 0
                        self.vida -= danno_restante
                    else:
                        self.defensa -= danno
                    print(f"{self.nombre} se quedó con {self.defensa} de defensa y {self.vida} de vida después del ataque")
                else:
                    self.vida -= danno
                    print(f"{self.nombre} se quedó con {self.vida} de vida después del ataque")
                
                if self.vida <= 0:
                    self.estado = False
                    self.vida = 0
                    print(f"{self.nombre} ha muerto")
            else:
                print(f"{otro_jugador.nombre} no provoca nada de daño en su ataque")
        else:
            print(f"{otro_jugador.nombre} no puede atacar, está muerto")
            #TIENE QUE RESTAR TAMBIEN Defensa
            #RANDOM para el ataque que sea que dentro de un paramentro segun la defensa del personaje sea mayor o menor la defensa. pero dentro de una aleatoriedad