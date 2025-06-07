
''' 
notas =[]

for x in range(2): #range gera numeros a partir de 0
    
    codigo_aluno = input("RM: ")
    nota = float(input("Nota:"))
    resultado = [codigo_aluno, nota] #Ex:resultado = [1234 5.8]
    notas.append(resultado)

print("Quantidade de notas", len(notas))

for n in notas:

    codigo_aluno = n[0] 
    notas = n[1]
    print("O RM", codigo_aluno, "tirou nota:", nota) 


'''

#DIVISÕES SUCESSIVAS:
list_tampos = [15, 16, 17]

for divisor in list_tampos:
    resultado = 300 / divisor
    print("A divisão de:", divisor, "vai dar:", int(resultado))
