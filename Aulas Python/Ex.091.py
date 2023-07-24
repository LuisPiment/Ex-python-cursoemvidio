from random import randint
from operator import itemgetter
j={"P1":randint(1,6),
   "P2":randint(1,6),
   "P3":randint(1,6),
   "P4":randint(1,6)}
ranking={}
for k,c in j.items() :
    print(f"O {k} conseguiu {c} ")
ranking=sorted(j.items(),key=itemgetter(1),reverse=True)
for a,b in ranking:
    print(f"O {a} teve {b}")




