print("=-=-=-=-GERADOR DE P.A=-=-=-=-")
print('=-'*15)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input("Razão de PA : "))
termo = primeiro
cont =1
total = 0
mais =10
while mais != 0:
    total += mais
    while cont <= total :
        print(f"{termo} -> ", end = " ")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input('Quantos termos a mais você deseja mostrar ?'))
print(f'Progressão finalizada com {total} termos')