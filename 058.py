from random import randint
num = randint(1,10)
print("VAMOS JOGAR!")
print("----ADIVINHE O NÚMERO----")
jogador = int(input('Digite um número entre 1 e 10: '))
while jogador != num:
    if jogador < 1 or jogador > 10:
        print("  Digite um número VÁLIDO entre 1 e 10!")
    if jogador < num :
            print("Pra cima!")
    if jogador > num:
            print('Pra baixo!')
    else:
        print(' Tente novamente:')

    jogador = int(input('Digite um numero entre 1 e 10: '))

print(f'O NÚMERO É  {num}. VOCÊ VENCEU !!!')