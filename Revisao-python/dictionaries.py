#Using dictionaries to store message informations

import os

messages = []

name = input("Nome: ")

while True:

    #Cleaning terminal
    os.system("cls")

    if len(messages) > 0:
        for m in messages:
            print(m['name'], "-", m["text"])

    print("_________________")



    #Getting texto
    text = input("mensagem: ")
    if text == "fim":
        break

    #Adding messages in list
    messages.append({
        "name": name,
        "text": text
    })

