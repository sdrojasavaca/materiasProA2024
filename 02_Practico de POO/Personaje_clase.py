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
        if self.estado :
            danno = random.randint(0, self.ataque)
            if danno >= 1:
                if otro_jugador.defensa >=1:
                    otro_jugador.defensa -= danno 
                    print(f"{otro_jugador.nombre} se quedo con {otro_jugador.defesa} de defensa despues del ataque que recibio")
                else:
                    otro_jugador.vida -= danno
                    print(f"{otro_jugador.nombre} se quedo con {otro_jugador.vida} de vida despues del ataque que recibio")
            else:
                print(f"{self.nombre} no provoca nada de daño en su ataque")
        else:
            print (f"{self.nombre} no puede atacar, esta muerto")
            
    def recibirDano(self, otro_jugador):
        
        if otro_jugador.estado :
            danno = random.randint(0, otro_jugador.ataque)
            if danno >= 1:
                if self.defensa >=1:
                    self.defensa -= danno 
                    print(f"{self.nombre} se quedo con {self.defesa} de defensa despues del ataque que recibio")
                else:
                    self.vida -= danno
                    print(f"{self.nombre} se quedo con {self.vida} de vida despues del ataque que recibio")
            else:
                print(f"{otro_jugador.nombre} no provoca nada de daño en su ataque")
        else:
            print (f"{otro_jugador.nombre} no puede atacar, esta muerto")
        if self.vida <=0:
            self.estado=False
            print (f"{self.nombre} ha muerto")
        else:
            None
            #TIENE QUE RESTAR TAMBIEN Defensa
            #RANDOM para el ataque que sea que dentro de un paramentro segun la defensa del personaje sea mayor o menor la defensa. pero dentro de una aleatoriedad