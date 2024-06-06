# Juego de Piedra, Papel, Tijera en Pygame

Este es un juego interactivo de "Piedra :fist: , Papel :hand: , Tijera :v: " creado usando Pygame. El primer jugador en ganar 2 de 3 rondas es el ganador. Los jugadores pueden seleccionar su elección haciendo clic en los botones correspondientes.



## Requisitos

- Python 3.x
- Pygame

## Instalación

1. **Clonar el repositorio**:
    ```sh
    git clone https://github.com/danielcardenasparra/yankenpon
    cd piedra-papel-tijera-pygame
    ```

2. **Crear y activar un entorno virtual (opcional pero recomendado)**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    ```

3. **Instalar las dependencias**:
    ```sh
    pip install pygame
    ```

## Uso

1. **Ejecutar el juego**:
    ```sh
    python main.py
    ```

2. **Interacción**:
    - Haz clic en los botones "Piedra", "Papel" o "Tijera" para hacer tu elección.
    - El juego mostrará el resultado de cada ronda y el marcador actual.
    - El primer jugador en ganar 2 de 3 rondas será el ganador.
    - Después de declarar al ganador, el juego se reiniciará automáticamente.

## Código

El código del juego se encuentra en `main.py`. Aquí hay una breve descripción de su funcionamiento:

1. **Inicialización**:
    - Se inicializa Pygame y se configura la pantalla.
    - Se definen colores y fuentes para el texto.

2. **Funciones del Juego**:
    - `choice(a)`: Devuelve la elección (Piedra, Papel, Tijera) basada en el número dado.
    - `determine_winner(usuario, pc)`: Compara las elecciones del jugador y la computadora, actualiza las victorias y devuelve el resultado de la ronda.
    - `reset_game()`: Reinicia las variables del juego para comenzar una nueva partida.

3. **Variables del Juego**:
    - Se utilizan variables globales para llevar el conteo de las victorias, el número de rondas y el estado del juego.

4. **Interacción del Usuario**:
    - Se definen rectángulos para los botones de "Piedra", "Papel" y "Tijera".
    - Se manejan eventos de clic del mouse para detectar cuándo el jugador hace una elección.
    - Se calcula la elección de la computadora y se determina el resultado de la ronda.
    - Si un jugador gana 2 rondas, se muestra un mensaje de victoria y el juego se reinicia automáticamente después de 3 segundos.

5. **Bucle Principal**:
    - Dibuja la interfaz del juego, incluyendo los botones y el texto que muestra el estado del juego.
    - Maneja los eventos de Pygame, incluyendo la detección de clics y el cierre del juego.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para discutir cualquier cambio que desees hacer.

## Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

## Autor

- [Daniel Cardenas :alien:](https://github.com/danielcardenasparra)
