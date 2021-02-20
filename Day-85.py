#Importação do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
#speech recognition
import speech_recognition as sr

#speech synthesis
import pyttsx3

bot = ChatBot('Ei Dev') #inicia o bot

chats = ['Hi', 'Hello', 'How are you?', 'How are you going?', 'What are you going?'] #conversas

bot.set_trainer(ListTrainer) #define o método de treinamento
bot.train(chats) #define a lista de conversas

while True:
    request = input('Enter a text: ')
    print(bot.get_response(request))
