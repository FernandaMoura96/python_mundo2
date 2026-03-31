a = float(input('Digite a medida da reta A:  '))
b = float(input('Digite a medida da reta B:  '))
c = float(input('Digite a medida da reta C:  '))

if a+b > c and b+c > a and a+c > b :
    print('É possível formar um triangulo com essas retas')
    if a==b and b==c:
        print("Equilatero")
    elif a!= b and  b != c and c != a :
         print('Escaleno')
    else :
        print('Isoceles')
else:
    print('Não é possível formar um triangulo com essas retas.')