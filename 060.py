from math import factorial
n = int(input( "Digite um número para calcular o fatorial : "))
c = n
while c > 0:
    print(f"{c} ", end=" ")
    print( "X " if c > 1 else "=", end=" ")
    c -= 1
#print(f"O Fatorial de {n} é = a {c}")
#termina na proxima aula