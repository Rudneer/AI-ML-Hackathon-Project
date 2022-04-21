from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer )

for files in os.listdir('C:/Users/hetan/PycharmProjects/pythonProjectDigit-Digit/english'):
    data=open('C:/Users/hetan/PycharmProjects/pythonProjectDigit-Digit/english/' +files,'r').readlines()
    bot.train(data)

while True:
    message = input("You: ")
    if message.strip() != 'bye':
        reply = bot.get_response(message)
        print("Chatbot: ", reply)
    if message.strip()=='ye':
        print("Chatbot:Bye")
        break