"""
Exercício: 
    Classe Bola: Crie uma classe que modele uma bola:
        a. Atributos: Cor, circunferência, material
        b. Métodos: trocaCor e mostraCor
"""

class Ball: 
    def __init__(self, color='unknown', circunf=0, material='unknown'): 
        self.color = color
        self.circunf = circunf
        self.material = material 
        
    def trocaCor(self): 
        troca = input(f'Deseja alterar a cor atual {self.color}? S/N ')
        
        troca = troca[0].lower()
        if troca == 'S':
            novacor = input('\n Nova cor: ')
            self.color = novacor
        else: 
            print('A cor não sofrerá alterações!')
            
    def mostraCor(self):
        print(f'\nA cor atual é {self.color}')
