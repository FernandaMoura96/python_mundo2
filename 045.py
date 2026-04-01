#Esse é um mini game de JokenPo
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print ('Faça sua jogada')

print('''Suas opções
 [0] Pedra
 [1] Papel
 [2] Tesoura''')

jogador = int(input(" Qual a sua escolha? "))

print('-*-*-*-*' *5)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print("PO!!!!")
sleep(1)
print('-*-*-*-*' *5)

print('==='*10)
print(f"Computador jogou {itens[pc]} ")
print(f"Você jogou {itens[jogador]} ")
print('==='*10)

if pc ==0: #PEDRA
    if jogador == 0:
     print('Empatou!! Tente de novo')
    elif jogador == 1:
        print("VOCÊ VENCEU!")
    elif jogador == 2:
        print("A MAQUINA VENCEU")
    else: print("****JOGADA INVÁLIDA****")

elif pc ==1:#PAPEL
    if jogador == 0:
        print("A MAQUINA VENCEU")
    elif jogador == 1:
        print('Empatou!! Tente de novo')
    elif jogador == 2:
        print("VOCÊ VENCEU!")
    else: print("****JOGADA INVÁLIDA****")


elif pc == 2:#TESOURA
    if jogador == 0:
        print("VOCÊ VENCEU!")
    elif jogador == 1:
        print("A MAQUINA VENCEU")
    elif jogador == 2:
        print('Empatou!! Tente de novo')
    else: print("****JOGADA INVÁLIDA****")


#else: