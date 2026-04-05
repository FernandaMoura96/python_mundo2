print("Insira um número inteiro par e te darei a soma entre eles")
soma_pares = 0
conta_pares = 0

for c in range (1, 7):
    num =  int(input('Digite um número inteiro: '))

    if num % 2 == 0 :
        soma_pares += num
        conta_pares += 1
    else:
        print('Numero inválido: ')

print(f'Você informou {conta_pares} nuúmeros pares2 e a soma é  {soma_pares}')