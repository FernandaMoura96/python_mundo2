pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
dc = pt + (10-1) * rz

for c in range(pt, dc + rz, rz):
    print(c , end = " → ")

print("FIM")