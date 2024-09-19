# Spaceship_Girl

**Spaceship_Girl** es un juego de acción donde el objetivo es guiar una nave espacial de regreso a la Tierra. El jugador debe recolectar puntos evitando asteroides y recolectando planetas para alcanzar los 30 puntos necesarios para ganar. Si la puntuación llega a 0, el juego termina.

## Objetivo del Juego

El objetivo es acumular 30 puntos para que la nave pueda regresar a la Tierra. Los puntos se obtienen al recolectar planetas y se pierden al colisionar con asteroides. Si la puntuación cae a 0, el juego finaliza y se muestra una pantalla de "GAME OVER". Si se alcanzan los 30 puntos, se muestra una pantalla de "WINNER!!!!".

## Controles

- **W**: Mover la nave hacia arriba.
- **S**: Mover la nave hacia abajo.
- **A**: Mover la nave hacia la izquierda.
- **D**: Mover la nave hacia la derecha.
- **4**: Reducir el volumen de la música de fondo.
- **5**: Aumentar el volumen de la música de fondo.

## Dinámica del Juego

- La nave debe evitar los asteroides y recoger los planetas.
- La velocidad de los asteroides aumenta con el tiempo, haciendo el juego más desafiante a medida que avanzas.
- La nave puede moverse libremente por la pantalla, pero debe evitar los asteroides y recoger los planetas para sumar puntos.

## Requisitos

- Python 3
- Pygame

## Instalación

1. Asegúrate de tener Python 3 y Pygame instalados.
2. Clona este repositorio o descarga el código.
3. Coloca los archivos de recursos (`fondo.png`, `musica_fondo.mp3`, `explosion.mp3`, `vida.mp3`, `explosion.png`, `astronave.png`, `asteroide.png`, `planeta-tierra.png`) en el mismo directorio que el archivo principal del juego.
4. Ejecuta el juego con el siguiente comando:

   ```bash
   python juego.py


## Explicación del Código
Inicialización de Pygame: Se inicializa Pygame y se configuran las dimensiones de la pantalla, colores, y recursos como imágenes y sonidos.

Clases:

Nave: Representa al jugador. Permite el movimiento basado en las teclas presionadas y maneja el estado de explosión.
Asteroide: Los asteroides que caen y que aumentan su velocidad con el tiempo. La velocidad se incrementa cada 5 segundos.
Planeta: Objetos que el jugador debe recoger. Se reposicionan aleatoriamente al ser recogidos.
Funciones:

mostrar_game_over(): Muestra una pantalla de "GAME OVER" en color rosado cuando la puntuación llega a 0.
mostrar_winner(): Muestra una pantalla de "WINNER!!!!" en verde limón cuando la puntuación alcanza 30.
Bucle Principal: Controla la lógica del juego, actualiza los sprites, maneja las colisiones, y muestra la puntuación. También maneja el incremento de la velocidad de los asteroides y controla el volumen de la música.
