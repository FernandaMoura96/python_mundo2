maior= 0
menor= 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1:
     menor = peso
     maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O menor peso lido foi de {menor} kg e o maior foi de {maior} kg.")