import json, requests, random, re
from app.chatbot import setup
from app.chatbot import message_to_bot
import config

global learn_response
clf, learn_response = setup()

def handle(received_message):
    global learn_response
    send_message, learn_response = message_to_bot(received_message, clf, learn_response)                         #send received message to bot and retrieve appropriate response
    return send_message

if __name__ == '__main__':
    while True:
        message = input('>')
        response = handle(message)
        print(response)