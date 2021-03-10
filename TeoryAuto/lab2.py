import itertools
#1 задание
n = 5
cout = 0
E = ['0','1']
posl = []
posl_c = []
for j in range(n):
    for i in itertools.combinations_with_replacement(E,j):
        for e in itertools.permutations(i):
            posl.append(e)

posl = list((set(posl)))
posl.sort()
print(posl)
word = ''

for i in posl:
    for j in i:
        word += j
    posl_c.append(word)
    word = ''
print(posl_c)

for i in posl_c:
    if '101' in i:
        posl_c.remove(i)
print(posl_c)

#2 задание