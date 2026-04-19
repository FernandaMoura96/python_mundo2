somaidade = 0
mediaidade =0
nomehomem = ''
idademaior = 0
totmulher20 = 0
for p in range(1,5):
    print(f'-----{p}ªPESSOA------')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo= str(input('Sexo : [F/M]')).strip().upper()
    somaidade += idade
    if p ==1 and sexo == 'M':
        idademaior = idade
        nomehomem = nome
    if sexo == 'M' and idade > idademaior :
        idademaior = idade
        nomehomem = nome
    if sexo in 'F' and idade < 20 :
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos. ')
print(f'O homem mais velho tem {idademaior} anos, e se chama {nomehomem}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')