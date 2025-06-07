

def characterDefinations():
     name = input("Nickname: ")
     typeCharacter = input("Type: ")
     print("Bem vindo " , name , "sua clase é " , typeCharacter)
       
characterDefinations()

print("________________")
print("Habilidades:")
print("")
print("1- Attack")
print("2- Defense")
print("3- Magic")

start_game = characterDefinations




options = [{"Attack": 10, "Defense": 20, "Magic": 15}]



while True:
    for op in options:
        choose =  int(input("O que você vai fazer?"))
        if choose == 1:
            print(op['Attack'])
            break    
        elif choose == 2:
            print(op['Defense'])
            break
        elif choose == 3:
            print(op['Magic'])
            break
        else: 
            print("Fugir")
            print("Arregou")
            exit()
 

           