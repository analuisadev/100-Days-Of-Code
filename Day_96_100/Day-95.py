"""
Parte 1: Criando uma Janela Vazia
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
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')

#Looping principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()


