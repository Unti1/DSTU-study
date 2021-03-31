import random

n = 100
i = 0
filename = 'nums.txt'
zerodown = 0

with open(filename, "w",encoding='utf8') as f:
    while i != n:
        print(f'{random.uniform(-100000,100000)}',file=f )
        i += 1

with open(filename,"r") as f:
    for i in range(n):
        a = f.readline()
        if float(a) < 0:
            zerodown += 1

print(zerodown)
