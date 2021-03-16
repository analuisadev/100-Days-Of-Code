""""
Parte 5: Criando Colisões
"""
#Importações necessárias para a criação da janela

import pygame
from pygame.locals import *
from sys import exit
from random import randint

#Inicialização das váriaveis e funções do pygame

pygame.init()

#Criação da tela

width = 640
height = 480
x = width/2
y = height/2

#Criando váriaveis para assumir diferentes valores para cada colisão
x_blue = randint(40, 600)
y_blue = randint(50, 430)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')
#Controlando a velocidade da movimentação do objeto

clock = pygame.time.Clock()

#Looping principal do jogo

while True:
    clock.tick(30)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
#Criando uma condição para mudar a movimentação de acordo com a tecla

        if event.type == KEYDOWN:
            if event.key == K_a:
               x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20
#Criando uma condição caso a tecla continue a ser pressionada

    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

#Desenhando Objetos dentro da Tela e movimentando
    ret_red = pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))#
    ret_blue = pygame.draw.rect(screen, (0, 0, 255), (x_blue, y_blue, 40, 50))

#Criando Condições para cada colisão
    if ret_red.colliderect(ret_blue):
        x_blue = randint(40, 600)
        y_blue = randint(50, 430)


    pygame.display.update()


