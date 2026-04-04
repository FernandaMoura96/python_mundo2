#essa variavel "soma" refere- se a um acumulador
soma = 0 # soma um valor acumulado
contador = 0 #geralmente conta +1

for num in range (1,500 ,2):
    if num % 3 == 0:

        soma = soma + num
        contador += 1

print (f'A soma de todos os {contador} números impares, divisiveis por 3 é {soma} ')