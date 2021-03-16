""""
Parte 3: Criando Obejetos que se movimentam
"""
#Importações necessárias para a criação da janela
import pygame
from pygame.locals import *
from sys import exit

#Inicialização das váriaveis e funções do pygame
pygame.init()

#Criação da tela
width = 640
height = 480
x = width/2
y = 0
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')
#Controlando a velocidade da movimentação do objeto
clock = pygame.time.Clock()

#Looping principal do jogo
while True:
    clock.tick(40)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

#Desenhando Objetos dentro da Tela e movimentando
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))#
    if y >= height:
        y = 0
    y = y + 5

    pygame.display.update()


