n = cont = soma = 0

n = int(input("SOMANDO NÚMEROS \n DIGITE 999 PARA SAIR :  "))
while n != 999:
    cont += 1
    soma += n
    n = int(input("SOMANDO NÚMEROS \n DIGITE 999 PARA SAIR :  "))

print(f"Você digitou {cont} números e a soma entre eles é de {soma}")


