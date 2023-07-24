import random
import time
s=[]
print(f"{'LOTERIA':*^30}")
n1=int(input("Quantos jogos queres que eu sorteie: "))
for c in range (0,n1):
    while True:
        t=random.randint(0,61)
        if t not in s:
            s.append(t)
        if len(s)==6:
            break
    s.sort()
    print(s)
    time.sleep(0.3)
    s.clear()
print(f"{'Boa sorte':*^30}")



