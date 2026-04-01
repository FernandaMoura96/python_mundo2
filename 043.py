#Esta é uma cauculador de IMC, exercício 43 do mundo 2 do curso em vídeo.
altura = float(input("Qual a altura do paciente? "))
peso = float(input("Qual o peso do paciente? "))

indice = peso / (altura ** 2)

if indice < 18.5:
    print(f'Abaixo do peso com IMC de {indice:.1f}')
elif 18.5 <= indice < 25:
    print(f'Dentro do peso com IMC de {indice:.1f}')
elif 25 <= indice < 30:
    print(f'Sobrepeso, com IMC de {indice:.1f}')
elif 30 <= indice < 40:
    print(f'Obesidade, com IMC de {indice:.1f}')
else:
    print(f'Obesidade mórbida  com IMC de {indice:.1f}')