"""
Classe Bichinho Virtual:
    Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
        Atributos: Nome, Fome, Saúde e Idade
        Métodos: Alterar Nome, Fome, Saúde e Idade;
        Retornar: Nome, Fome, Saúde e Idade
        Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""

class Tamagushi:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 100
        self.health = 100

    def get_name(self):
        return self.name

    def __set_name__(self, new_name):
        self.name = new_name

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def get_hunger(self):
        return self.hunger

    def set_hunger(self, new_hunger):
        self.hunger = new_hunger

    def get_health(self):
        return self.health

    def set_health(self, new_health):
        self.health = new_health

    def get_humor(self):
        if self.get_hunger() >= 70 and self.get_health() >= 70:
            return "Eu estou muito FELIZ!"
        elif self.get_hunger() >= 50 and self.get_health() >= 50:
            return "Eu não esotu me sentindo tão bem :("
        elif self.get_hunger() >= 30 and self.get_health() >= 30:
            return "Estou muito fraco e irritado! >:("
        else:
            return "Você me deixou morrer! :´("

bichinho = Tamagushi("Tamagushi", 2)
print(bichinho.get_name())
print(bichinho.get_age())
print(bichinho.get_humor())

bichinho.set_health(50)
bichinho.set_hunger(70)

print(bichinho.get_humor())

