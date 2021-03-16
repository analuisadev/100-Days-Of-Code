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
#Desenhando Objetos dentro da Tela
    pygame.draw.rect(screen, (255, 0, 0), (200, 300, 40, 50))#Responsável por criar o retangulo vermelho na tela
    pygame.draw.circle(screen, (0, 0, 255), (300, 260), 40)#Criação do circulo na tela (1° Cores, 2° Posição e raio do circulo)
    pygame.draw.line(screen, (255, 255, 0), (390, 0), (390, 600), 5)#Desenhando uma linha com posição inicial e final com expressura
    pygame.display.update()


