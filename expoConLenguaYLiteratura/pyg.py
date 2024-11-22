import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego con Personajes y Comederos Mejorado")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
RED = (255, 0, 0)
BUTTON_COLOR = (100, 200, 100)

# Fuentes
font = pygame.font.SysFont("arial", 48)
small_font = pygame.font.SysFont("arial", 24)

# Estados
STATE_MENU = "menu"
STATE_SELECTION = "selection"
STATE_GAME = "game"
current_state = STATE_MENU

# Cargar recursos
bark_sound = pygame.mixer.Sound("bark.mp3")
eat_sound = pygame.mixer.Sound("eat.mp3")
background_image = pygame.image.load("background.png")  # Añadir fondo decorativo
dog_images = [
    pygame.image.load("dog1.png"),
    pygame.image.load("dog2.png"),
    pygame.image.load("dog3.png")
]

# Clase del personaje
class Dog:
    def __init__(self, name, color, image):
        self.name = name
        self.color = color
        self.image = pygame.transform.scale(image, (80, 80))  # Redimensionar la skin
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = 40
        self.energy = 100

    def draw(self):
        screen.blit(self.image, (self.x - self.size, self.y - self.size))
        pygame.draw.rect(screen, BLUE, (10, 10, 200, 20))
        pygame.draw.rect(screen, RED, (10, 10, 2 * self.energy, 20))

    def move(self, dx, dy):
        self.x = max(self.size, min(WIDTH - self.size, self.x + dx))
        self.y = max(self.size, min(HEIGHT - self.size, self.y + dy))

    def bark(self):
        bark_sound.play()

    def eat(self):
        if self.energy < 100:
            eat_sound.play()
            self.energy += 20
            if self.energy > 100:
                self.energy = 100

# Clase del comedero
class Feeder:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 30
        self.used = False

    def draw(self):
        if not self.used:
            pygame.draw.circle(screen, RED, (self.x, self.y), self.size)

    def is_near(self, dog):
        if self.used:
            return False
        distance = ((self.x - dog.x) ** 2 + (self.y - dog.y) ** 2) ** 0.5
        if distance < self.size + dog.size:
            self.used = True
            return True
        return False

# Variables globales
characters = [
    {"name": "Doggo Dev", "color": (255, 200, 200), "image": dog_images[0]},
    {"name": "Puppy Pro", "color": (200, 255, 200), "image": dog_images[1]},
    {"name": "Coder Canine", "color": (200, 200, 255), "image": dog_images[2]},
]
selected_character = None
feeders = [Feeder(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(5)]

def draw_game(dog):
    screen.blit(background_image, (0, 0))  # Fondo decorativo
    dog.draw()
    for feeder in feeders:
        feeder.draw()

    # Dibujar botón de regresar
    button_width, button_height = 200, 50
    button_x = WIDTH - button_width - 20
    button_y = HEIGHT - button_height - 20
    pygame.draw.rect(screen, BUTTON_COLOR, (button_x, button_y, button_width, button_height))
    button_text = font.render("Regresar", True, BLACK)
    button_text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(button_text, button_text_rect)

    return button_x, button_y, button_width, button_height

# Modificación del bucle principal
def main():
    clock = pygame.time.Clock()

    while True:
        if current_state == STATE_MENU:
            draw_menu()
            handle_menu_events()
        elif current_state == STATE_SELECTION:
            draw_selection()
            handle_selection_events()
        elif current_state == STATE_GAME:
            draw_game(selected_character)
            handle_game_events(selected_character)
            # Reaparecer comederos si todos están usados
            if all(feeder.used for feeder in feeders):
                feeders.clear()
                feeders.extend(
                    [Feeder(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(5)]
                )

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
