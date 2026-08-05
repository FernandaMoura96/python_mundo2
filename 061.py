print("=-=-=-=-GERADOR DE P.A=-=-=-=-")
print('=-'*15)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input("Razão de PA : "))
termo = primeiro
cont =1
while cont <= 10:
    print(f"{termo} -> ", end = " ")
    termo += razao
    cont += 1
print('FIM')