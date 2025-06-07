



CUSTO_LATA = 80

metros_quadrados = int(input("Qtd de metros quadrados:"))

#Qtd de litros que vai gastar e o número decimal
#ex: 19 metros/ 3 metros que pode pintar: litros = 6; resto = 1

litros, resto = divmod(metros_quadrados, 3)

#Daria uma lata e um poquinho (100ml por exemplo), e
#Então se precisa mais do que 1 lata, some +1 litro para comprar a 2 lata
if resto > 0:
    litros += 1

latas, adicional = divmod(litros, 18)

if adicional > 0:
    latas += 1


custo = latas * CUSTO_LATA

print("Quantidade de latas: ", latas)
print(f"Custo total: R${custo}")