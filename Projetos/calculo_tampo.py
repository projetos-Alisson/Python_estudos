import os

remessa = int(input("Digite o valor da remessa: "))
remessa_restante = 0
medida = 160
qtd_pilha = 0

print("Contador de tampos - GRUPO LOPAS 🍀")
print("")
nome_peca = input("Qual peça irá trabalhar? ")
os.system('cls')
print("Peça de ", medida, "cm")
#tampos = input("Digite a quantidade desejada:")

#Enquanto houver peças a serem contadas
while remessa > 0:
    #Quantidade a distribuir em cada pilha
    tampos = 15 
    print("Número esocolhido: ", tampos)
    #Calcular tampos por pilha/ remessa
    qtd_pilha, sobra_tampo = divmod(remessa, tampos)

    #Se não houver sobra é porque todas as pilhas terão a mesma quantidade
    if sobra_tampo == 0:
        
        print("A quantidade de peças será", tampos ,"tampos com ", qtd_pilha ," pilhas")

    #Se houver sobra alterar valor das próximas pilhas
    elif (sobra_tampo > 0):
        
        remessa_restante = remessa - sobra_tampo
        #Quantidade de tampos das primeiras pilhas
        tampos_1 = tampos 
        #Quantidade sobrando de tampos
        tampos_2 = sobra_tampo
        qtd_pilha_2 = 0

     
        #Enquanto não distribuiu em pilhas...
        while remessa_restante < remessa:
           
           i = 1
           #Adicione até saciar o lote
           remessa_restante += i
        #Quando saciar...
        if remessa_restante >= remessa:
        #Adicionar quantas pilhas foram necessárias pra suprir
            qtd_pilha_2 = i
      
     
        print("A quantidade de peças do 1° conjunto de pilhas será", tampos_1 ,"tampos com ", qtd_pilha ," pilhas")
        print("A quantidade de peças do 2° conjunto de pilhas será", tampos_2 ,"tampos com ", qtd_pilha_2 ," pilhas")
    
    break

'''  for i in range(remessa_restante, remessa + 1):
           remessa_restante += tampos_2
           print(remessa_restante)
     '''