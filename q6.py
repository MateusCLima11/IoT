notas = []

for x in range(8):
    n = float(input(f'Digite a {x+1}ª nota?  '))
    notas.append(n)

media = sum(notas)/len(notas)

for espiao in notas:
    if(espiao>=media):
        print(espiao,end='-')

print(f'A média da turma é {media:.1f}')
