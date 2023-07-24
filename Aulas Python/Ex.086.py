t=[[],[],[],[],[],[],[],[],[]]
c1=0
c2=0
for c in range (0,9):
    t[c].append(int(input(f"Digite o numero[{c1},{c2}]: ")))
    if c<2:
        c1=0
        c2+=1
    if c==2:
        c2=0
        c1=1
    if 2<c<5:
        c1=1
        c2+=1
    if c ==5:
        c2=0
        c1=2
    if 5<c:
        c1=2
        c2+=1
print(f"[ {t[0]} ] [ {t[1]} ] [ {t[2]} ]\n[ {t[3]} ] [ {t[4]} ] [ {t[5]} ]\n[ {t[6]} ] [ {t[7]} ] [ {t[8]} ]")




