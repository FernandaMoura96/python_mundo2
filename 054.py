from datetime import date
atual = date.today().year
maior =0
menor =0

for pepople in range( 1,8):
    nasc = int(input(f" Digite o ano de nascimento da {pepople}ª pessoa:  "))
    idade = atual - nasc
    if idade >= 18:
        maior +=1
    else:
        menor +=1
print(f'\033[1;33mAo todo tivemos {maior} pessoas maiores de idade,e \n {menor} pessoas menores de idade')