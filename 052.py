# Esse programa deve ler um número e dizer se ele é ou não um número primo
primo = int(input("Digite o número que você deseja analizar: "))
tt = 0
for c in range (1,primo +1):
    if primo % c == 0:
        print('\033[34m',end = '')
        tt += 1
    else:
        print('\033[31m',end = '')
    print('{} ' .format(c), end='' )

print(f'\n \033[m {primo} foi dividido por {tt} vezes')
if tt ==2:
    print(f'{primo} é primo')
else:
    print(f"{primo} não é primo ")