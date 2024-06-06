import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Chis Bum Papas")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
grey = (200, 200, 200)
yellow = (255, 255, 0)

# Fuentes
font_large = pygame.font.Font(None, 74)
font_medium = pygame.font.Font(None, 54)
font_small = pygame.font.Font(None, 36)

# Funciones del juego
def choice(a):
    choices = {1: 'Piedra', 2: 'Papel', 3: 'Tijera'}
    return choices.get(a, 'Opción inválida')

def determine_winner(usuario, pc):
    global master_wins, user_wins
    if usuario == pc:
        return 'Es un empate!'
    elif (usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2):
        user_wins += 1
        return 'Has ganado!'
    else:
        master_wins += 1
        return 'Has perdido!'

def reset_game():
    global master_wins, user_wins, rounds, result, usuario_choice, pc_choice, game_over
    master_wins = 0
    user_wins = 0
    rounds = 1
    result = ""
    usuario_choice = ""
    pc_choice = ""
    game_over = False

# Variables del juego
master_wins = 0
user_wins = 0
rounds = 1
running = True
result = ""
usuario_choice = ""
pc_choice = ""
game_over = False

# Coordenadas de los botones
button_piedra = pygame.Rect(50, 500, 150, 50)
button_papel = pygame.Rect(225, 500, 150, 50)
button_tijera = pygame.Rect(400, 500, 150, 50)

# Bucle principal del juego
while running:
    screen.fill(white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            if button_piedra.collidepoint(event.pos):
                usuario = 1
            elif button_papel.collidepoint(event.pos):
                usuario = 2
            elif button_tijera.collidepoint(event.pos):
                usuario = 3
            else:
                continue
            
            pc = random.randint(1, 3)
            result = determine_winner(usuario, pc)
            usuario_choice = choice(usuario)
            pc_choice = choice(pc)
            
            rounds += 1

            if user_wins == 2 or master_wins == 2:
                game_over = True
                if user_wins == 2:
                    result = "¡Has ganado la partida!"
                    result_color = green
                else:
                    result = "El master ha ganado la partida."
                    result_color = red
                pygame.time.set_timer(pygame.USEREVENT, 3000)  # Espera 3 segundos antes de reiniciar el juego

        if event.type == pygame.USEREVENT:
            reset_game()

    # Dibujar texto en la pantalla
    text = font_large.render(f'Round {rounds}', True, yellow)
    screen.blit(text, (320, 50))
    
    text = font_medium.render(f'Has elegido: {usuario_choice}', True, blue)
    screen.blit(text, (50, 150))
    
    text = font_medium.render(f'The master eligió: {pc_choice}', True, red)
    screen.blit(text, (50, 250))
    
    text = font_medium.render(result, True, result_color if game_over else (green if "ganado" in result else red))
    screen.blit(text, (50, 350))
    
    text = font_medium.render(f'Marcador: Tú {user_wins} - {master_wins} Master', True, black)
    screen.blit(text, (50, 450))
    
    # Dibujar botones
    pygame.draw.rect(screen, grey, button_piedra)
    pygame.draw.rect(screen, grey, button_papel)
    pygame.draw.rect(screen, grey, button_tijera)
    
    text = font_small.render('Piedra', True, black)
    screen.blit(text, (button_piedra.x + 50, button_piedra.y + 10))
    
    text = font_small.render('Papel', True, black)
    screen.blit(text, (button_papel.x + 50, button_papel.y + 10))
    
    text = font_small.render('Tijera', True, black)
    screen.blit(text, (button_tijera.x + 50, button_tijera.y + 10))
    
    pygame.display.flip()

pygame.quit()
