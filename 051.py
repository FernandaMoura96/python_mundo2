pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
dc = pt + (10-1) * rz #essa linha eu não consegui fazer sozinha ainda.

for c in range(pt, dc + rz, rz):
    print(c , end = " → ")

print("FIM")