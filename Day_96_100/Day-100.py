""""
Parte 6: Criando músicas, sons e placar de pontos
"""
# Importações necessárias para a criação da janela

import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Inicialização das váriaveis e funções do pygame

pygame.init()

#Criação da váriavel para tocar a música durante o jogo

pygame.mixer.music.set_volume(0.1)
music = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

#Criação da váriavel para tocar o som quando houver colisões

collision_sound = pygame.mixer.Sound('smw_coin.wav')
collision_sound.set_volume(1)
# Criação da tela

width = 640
height = 480
x = int(width / 2)
y = int(height / 2)

# Definindo a fonte e tamanho do texto

font = pygame.font.SysFont('arial', 40, True, True)

# Criando váriaveis para assumir diferentes valores para cada colisão
x_blue = randint(40, 600)
y_blue = randint(50, 430)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')
# Controlando a velocidade da movimentação do objeto

spots = 0
clock = pygame.time.Clock()

# Looping principal do jogo

while True:
    clock.tick(30)
    screen.fill((0, 0, 0))
    msg = f'Pontos: {spots}'  # Mensagem
    text = font.render(msg, True, (255, 255, 255))  # Texto formatado
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # Criando uma condição para mudar a movimentação de acordo com a tecla

        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20
    # Criando uma condição caso a tecla continue a ser pressionada

    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    # Desenhando Objetos dentro da Tela e movimentando
    ret_red = pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))  #
    ret_blue = pygame.draw.rect(screen, (0, 0, 255), (x_blue, y_blue, 40, 50))
    # Criando Condições para cada colisão
    if ret_red.colliderect(ret_blue):
        x_blue = randint(40, 600)
        y_blue = randint(50, 430)
#Adicionando os pontos
        spots = spots + 1
#Programando o som da colisão
        collision_sound.play()

    screen.blit(text, (450, 40))

    pygame.display.update()
