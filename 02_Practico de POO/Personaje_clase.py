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
            danno = self.ataque - otro_jugador.defensa
            if danno > 0:
                otro_jugador.vida -= danno
                print(f"{Personaje.nombre} ataca a {otro_jugador.nombre} causando {danno} de daño")
            else:
                print(f"{Personaje.nombre} ataca a {otro_jugador.nombre} sin causar daño")
        else:
            print (f"{Personaje.nombre} no puede atacar, esta muerto")
    def recibirDano(self, otro_jugador):
        if self.estado :
            danno = otro_jugador.ataque - self.defensa
            if danno > 0:
                self.vida -= danno
                print(f"{Personaje.nombre} ataca a {otro_jugador.nombre} causando {danno} de daño")
            else:
                print(f"{Personaje.nombre} ataca a {otro_jugador.nombre} sin causar daño")
        else:
            print (f"{Personaje.nombre} no puede recibir daño, esta muerto")