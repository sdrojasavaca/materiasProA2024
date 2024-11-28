import pygame
import random
import os


class GameConfig:
    """Configuración central del juego"""
    VENTANA_ANCHO = 800
    VENTANA_ALTO = 600
    BASE_PATH = os.path.abspath(".")
    RESOURCES_PATH = os.path.join(BASE_PATH, 'resources')
    FPS = 60


class ResourceManager:
    """Manejador de recursos (imágenes, sonidos, etc.)"""

    @staticmethod
    def cargar_imagen(ruta, dimensiones=None):
        """Carga y redimensiona una imagen si es necesario"""
        if not os.path.exists(ruta):
            print(f"Advertencia: Archivo no encontrado -> {ruta}")
            return None
        try:
            imagen = pygame.image.load(ruta)
            if dimensiones:
                imagen = pygame.transform.scale(imagen, dimensiones)
            return imagen
        except pygame.error as e:
            print(f"Error cargando imagen: {e}")
            return None

    @staticmethod
    def cargar_sonido(ruta):
        """Carga un archivo de sonido"""
        if not os.path.exists(ruta):
            print(f"Advertencia: Archivo no encontrado -> {ruta}")
            return None
        try:
            return pygame.mixer.Sound(ruta)
        except pygame.error as e:
            print(f"Error cargando sonido: {e}")
            return None


class Personaje:
    """Clase base para personajes del juego"""
    def __init__(self, nombre, sprite_path, velocidad, vidas):
        self.nombre = nombre
        self.velocidad = velocidad
        self.vidas_maximas = vidas
        self.vidas_actuales = vidas
        self.sprite_original = ResourceManager.cargar_imagen(sprite_path, (100, 80))
        self.sprite = self.sprite_original
        self.x = GameConfig.VENTANA_ANCHO // 2
        self.y = GameConfig.VENTANA_ALTO - 150
        self.direccion = "derecha"

    def mover(self, direccion):
        """Mueve al personaje y actualiza el sprite si cambia de dirección"""
        if direccion == "izquierda":
            self.x -= self.velocidad
            if self.direccion != "izquierda":
                self.sprite = pygame.transform.flip(self.sprite_original, True, False)
                self.direccion = "izquierda"
        elif direccion == "derecha":
            self.x += self.velocidad
            if self.direccion != "derecha":
                self.sprite = self.sprite_original
                self.direccion = "derecha"

        # Limitar el movimiento dentro de la pantalla
        self.x = max(0, min(self.x, GameConfig.VENTANA_ANCHO - 100))


class Hueso:
    """Clase para manejar los huesos del juego"""
    TIPOS = ["normal", "chocolate", "dorado"]

    def __init__(self, tipo, x, velocidad_base):
        self.tipo = tipo
        self.rect = pygame.Rect(x, -50, 50, 50)
        self.velocidad = velocidad_base
        self.imagen = ResourceManager.cargar_imagen(
            os.path.join(GameConfig.RESOURCES_PATH, 'images', f'hueso_{tipo}.png'),
            (50, 50)
        )

    def mover(self):
        """Mueve el hueso hacia abajo"""
        self.rect.y += self.velocidad

    @staticmethod
    def generar_hueso(velocidad_base):
        """Genera un hueso aleatorio con probabilidades específicas"""
        tipo = random.choices(
            Hueso.TIPOS,
            weights=[70, 25, 5],  # Probabilidades: normal, chocolate, dorado
            k=1
        )[0]
        x = random.randint(50, GameConfig.VENTANA_ANCHO - 50)
        return Hueso(tipo, x, velocidad_base)


class SelectorPerro:
    """Clase para manejar la selección de perro"""
    def __init__(self, ventana):
        self.ventana = ventana
        self.fuente = pygame.font.SysFont("Arial", 36)
        self.perros = [
            Personaje("Hambriento", os.path.join(GameConfig.RESOURCES_PATH, 'images', 'dog1.png'), 4, 6),
            Personaje("Apetitoso", os.path.join(GameConfig.RESOURCES_PATH, 'images', 'dog2.png'), 5, 4),
            Personaje("Angurriento", os.path.join(GameConfig.RESOURCES_PATH, 'images', 'dog3.png'), 3, 8)
        ]
        self.tarjetas = self._crear_tarjetas()
        self.perro_seleccionado = None

    def _crear_tarjetas(self):
        tarjetas = []
        ancho_tarjeta = 200
        altura_tarjeta = 300
        espacio_entre_tarjetas = 50

        for i, perro in enumerate(self.perros):
            x = (GameConfig.VENTANA_ANCHO - (3 * ancho_tarjeta + 2 * espacio_entre_tarjetas)) // 2 + \
                i * (ancho_tarjeta + espacio_entre_tarjetas)
            y = (GameConfig.VENTANA_ALTO - altura_tarjeta) // 2
            tarjetas.append({'rect': pygame.Rect(x, y, ancho_tarjeta, altura_tarjeta), 'perro': perro})

        return tarjetas

    def dibujar(self):
        """Dibuja las tarjetas de selección de perro"""
        self.ventana.fill((200, 200, 200))
        texto_titulo = self.fuente.render("Selecciona tu Perro", True, (0, 0, 0))
        titulo_rect = texto_titulo.get_rect(center=(GameConfig.VENTANA_ANCHO // 2, 100))
        self.ventana.blit(texto_titulo, titulo_rect)

        for tarjeta in self.tarjetas:
            pygame.draw.rect(self.ventana, (255, 255, 255), tarjeta['rect'])
            pygame.draw.rect(self.ventana, (0, 0, 0), tarjeta['rect'], 3)
            if tarjeta['perro'].sprite:
                sprite_rect = tarjeta['perro'].sprite.get_rect(center=tarjeta['rect'].center)
                self.ventana.blit(tarjeta['perro'].sprite, sprite_rect)

    def manejar_eventos(self):
        """Maneja eventos de selección de perro"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "SALIR"
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for tarjeta in self.tarjetas:
                    if tarjeta['rect'].collidepoint(pos):
                        return tarjeta['perro']
        return None


class DogAdventure:
    """Clase principal del juego"""
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.ventana = pygame.display.set_mode((GameConfig.VENTANA_ANCHO, GameConfig.VENTANA_ALTO))
        pygame.display.set_caption("Dog Adventure")
        self.estado = "MENU_PERRO"
        self.perro = None
        self.selector_perro = SelectorPerro(self.ventana)
        self.huesos = []  # Lista de huesos activos
        self.puntuacion = 0
        self.velocidad_base_huesos = 3  # Velocidad inicial de caída
        self.fondo_menu = ResourceManager.cargar_imagen(
            os.path.join(GameConfig.RESOURCES_PATH, 'images', 'fondo_menu.jpg'),
            (GameConfig.VENTANA_ANCHO, GameConfig.VENTANA_ALTO)
        )
        self.fondo_juego = ResourceManager.cargar_imagen(
            os.path.join(GameConfig.RESOURCES_PATH, 'images', 'fondo.jpg'),
            (GameConfig.VENTANA_ANCHO, GameConfig.VENTANA_ALTO)
        )
        self.fondo_suelo = ResourceManager.cargar_imagen(
            os.path.join(GameConfig.RESOURCES_PATH, 'images', 'fondo_suelo.png'),
            (GameConfig.VENTANA_ANCHO, 50)
        )

    def actualizar_velocidad_huesos(self):
        """Aumenta la velocidad base de los huesos según la puntuación"""
        self.velocidad_base_huesos = 3 + (self.puntuacion // 10)

    def manejar_huesos(self):
        """Gestiona el movimiento y generación de huesos"""
        if random.randint(1, 150) <= 5:  # Probabilidad ajustada
            nuevo_hueso = Hueso.generar_hueso(self.velocidad_base_huesos)
            self.huesos.append(nuevo_hueso)

        for hueso in self.huesos[:]:
            hueso.mover()
            if hueso.rect.y > GameConfig.VENTANA_ALTO - 50:  # Eliminar huesos fuera del suelo
                self.huesos.remove(hueso)

    def bucle_principal(self):
        reloj = pygame.time.Clock()
        while True:
            if self.estado == "MENU_PERRO":
                self.ventana.blit(self.fondo_menu, (0, 0))
                self.selector_perro.dibujar()
                pygame.display.flip()
                resultado = self.selector_perro.manejar_eventos()
                if resultado == "SALIR":
                    break
                elif isinstance(resultado, Personaje):
                    self.perro = resultado
                    self.estado = "JUEGO"
            elif self.estado == "JUEGO":
                # Dibujar fondo principal del juego
                self.ventana.blit(self.fondo_juego, (0, 0))

                # Dibujar huesos
                for hueso in self.huesos:
                    if hueso.imagen:
                        self.ventana.blit(hueso.imagen, (hueso.rect.x, hueso.rect.y))

                # Dibujar suelo por encima de los huesos
                self.ventana.blit(self.fondo_suelo, (0, GameConfig.VENTANA_ALTO - 50))

                # Manejar eventos y generar huesos
                self.manejar_huesos()

                pygame.display.flip()

            reloj.tick(GameConfig.FPS)


if __name__ == "__main__":
    juego = DogAdventure()
    juego.bucle_principal()
    pygame.quit()