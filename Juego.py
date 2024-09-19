import pygame, sys, random
from pygame.locals import *

#Inicialización
pygame.init()

# Dimensiones de la pantalla
ANCHO = 1000
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Spaceship_Girl')

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE_LIMON = (72, 254, 64)  # Color verde limón

# Fondo de la pantalla
fondo = pygame.image.load("fondo.png")

# Música de fondo
pygame.mixer.music.load('musica_fondo.mp3')
pygame.mixer.music.play(-1)

# Volumen inicial
volumen = 0.5
pygame.mixer.music.set_volume(volumen)

# Cargar el sonido de explosión
explosion_sonido = pygame.mixer.Sound('explosion.mp3')

# Cargar el sonido de vida
vida_sonido = pygame.mixer.Sound('vida.mp3')

# Imagen de explosión
explosion_imagen = pygame.image.load("explosion.png")

# Fuente para el marcador
fuente = pygame.font.SysFont('Gamer', 30)

# Inicializar puntuación
score = 10

# Clase Nave (jugador)
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cargar la imagen de la nave
        self.image = pygame.image.load("astronave.png").convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.explosion_tiempo = 0
        self.esta_explotando = False

    def update(self):
        teclas = pygame.key.get_pressed()
        self.velocidad_x = 0
        self.velocidad_y = 0

        # Si la nave no está en modo explosión, permitir el movimiento
        if not self.esta_explotando:
            # Movimiento con las teclas
            if teclas[pygame.K_a]:
                self.velocidad_x = -10
            if teclas[pygame.K_d]:
                self.velocidad_x = 10
            if teclas[pygame.K_w]:
                self.velocidad_y = -10
            if teclas[pygame.K_s]:
                self.velocidad_y = 10

            # Actualizar la posición
            self.rect.x += self.velocidad_x
            self.rect.y += self.velocidad_y

            # Limitar dentro de la pantalla
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > ALTO:
                self.rect.bottom = ALTO
            if self.rect.top < 0:
                self.rect.top = 0

        # Si está en modo explosión, revisar el tiempo
        if self.esta_explotando:
            if pygame.time.get_ticks() - self.explosion_tiempo > 500:  # 500 ms = 0.5 segundos
                self.image = pygame.image.load("astronave.png").convert()
                self.image.set_colorkey(NEGRO)
                self.esta_explotando = False

# Clase Asteroide
class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cargar la imagen del asteroide
        self.image = pygame.image.load('asteroide.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, ANCHO), 0)
        self.velocidad_base = 5  # Velocidad base del asteroide
        self.velocidad = self.velocidad_base  # Velocidad actual que irá incrementando
        self.tiempo_incremento = pygame.time.get_ticks()  # Registro del tiempo inicial

    def update(self):
        # Incrementar la velocidad del asteroide con el tiempo
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_incremento > 5000:  # Aumentar la velocidad cada 5 segundos
            self.velocidad += 1
            self.tiempo_incremento = tiempo_actual

        # Mover el asteroide hacia abajo
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            self.rect.bottom = 0
            self.rect.centerx = random.randint(0, ANCHO)

# Clase Planeta
class Planeta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cargar la imagen del planeta
        self.image = pygame.image.load('planeta-tierra.png')
        self.rect = self.image.get_rect()
        self.colocar_en_posicion_aleatoria()

    def colocar_en_posicion_aleatoria(self):
        # Nueva posición aleatoria, asegurándose que esté dentro de los límites de la pantalla
        self.rect.x = random.randint(0, ANCHO - self.rect.width)
        self.rect.y = random.randint(0, ALTO - self.rect.height)

# Crear instancias
nave = Nave()
asteroide = Asteroide()
planeta = Planeta()

# Grupo de sprites
sprites = pygame.sprite.Group()
sprites.add(nave)
sprites.add(asteroide)
sprites.add(planeta)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Función para mostrar el "Game Over"
def mostrar_game_over():
    fuente_game_over = pygame.font.Font('freesansbold.ttf', 100)  # Cambiar a fuente estilo videojuego
    texto_game_over = fuente_game_over.render('GAME OVER', True, (255, 105, 180))  # Color rosado
    texto_game_over = pygame.transform.scale(texto_game_over,
                                             (texto_game_over.get_width() + 20, texto_game_over.get_height() + 20))
    texto_rect = texto_game_over.get_rect(center=(ANCHO // 2, ALTO // 2))
    PANTALLA.blit(texto_game_over, texto_rect)
    pygame.display.update()
    pygame.time.wait(3000)  # Esperar 3 segundos
    pygame.quit()
    sys.exit()

# Función para mostrar el "WINNER!!!!"
def mostrar_winner():
    fuente_winner = pygame.font.Font('freesansbold.ttf', 100)  # Cambiar a fuente estilo videojuego
    texto_winner = fuente_winner.render('WINNER!!!!', True, VERDE_LIMON)  # Color verde limón
    texto_winner = pygame.transform.scale(texto_winner,
                                          (texto_winner.get_width() + 20, texto_winner.get_height() + 20))
    texto_rect = texto_winner.get_rect(center=(ANCHO // 2, ALTO // 2))
    PANTALLA.blit(texto_winner, texto_rect)
    pygame.display.update()
    pygame.time.wait(3000)  # Esperar 3 segundos
    pygame.quit()
    sys.exit()

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_4:
                volumen = max(0.0, volumen - 0.1)
                pygame.mixer.music.set_volume(volumen)
                print(f"Volumen bajado: {volumen:.1f}")

            if event.key == K_5:
                volumen = min(1.0, volumen + 0.1)
                pygame.mixer.music.set_volume(volumen)
                print(f"Volumen subido: {volumen:.1f}")

    # Detectar colisión entre la nave y el asteroide
    if pygame.sprite.collide_rect(nave, asteroide) and not nave.esta_explotando:
        nave.image = explosion_imagen
        explosion_sonido.play()
        nave.explosion_tiempo = pygame.time.get_ticks()
        nave.esta_explotando = True
        score -= 3

    # Detectar colisión entre la nave y el planeta
    if pygame.sprite.collide_rect(nave, planeta):
        planeta.colocar_en_posicion_aleatoria()
        vida_sonido.play()
        score += 1

    # Actualizar y dibujar sprites
    sprites.update()
    PANTALLA.blit(fondo, (0, 0))
    sprites.draw(PANTALLA)

    # Mostrar el marcador en la esquina superior derecha
    marcador = fuente.render(f'Score: {score}', True, BLANCO)
    PANTALLA.blit(marcador, (ANCHO - 150, 10))

    # Si el score llega a 0, mostrar la pantalla de "Game Over"
    if score <= 0:
        mostrar_game_over()

    # Si el score llega a 30, mostrar la pantalla de "WINNER!!!!"
    if score >= 30:
        mostrar_winner()

    # Actualizar la pantalla
    pygame.display.update()

    # Control de FPS
    clock.tick(FPS)
