'''Aqui temos um idenfiticador de palíndromos.
Um palíndromo é uma palavra, frase, número ou qualquer outra sequência de caracteres
que permanece igual quando lida de trás para frente.'''
frase = str(input('Digite uma frase: ')) .upper() .strip()
palavra= frase.split()
juntar = ''.join(palavra)
inverso = ''
for letra in range(len(juntar)-1 , -1, -1):
    inverso += juntar[letra]
print(f'O inverso de {juntar} é {inverso}')

if inverso == juntar:
    print('Temos um palindromo')
else:
    print('Não temos um palindromo')

