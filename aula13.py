print('Aqui exibe contagem inserida pelo usiário')
n = int(input("Digite um número: "))
for c in range (0, n+1):
    print(c)
print('Fim')

#print("Aqui recebe um input do usurio que decice como o loop progredirá:")
#i = ('Digite o numero inicial:')
#f = ('Digite o numero final:')
#p = ('Digite o passo : ')
#for c in range (i, f+1, p):
#    print (c)
#print('Fim')



print('Aqui exibe um loop limitado')
for c in range (0,6):
    print('Oi')
print("Tchau")

print('Aqui exibe o proprio contador')
for c in range (0,6):
    print(c)
print ('Fim')


print('Aqui exibe o contador, condicionado a espaçamento delimitado pelo dev')
for c in range(0,11,2 ):
    print(c)
print('Fim')
#lembrando que o python ignora o ultimo numero da contagem, é sempre necessário adc +1 após