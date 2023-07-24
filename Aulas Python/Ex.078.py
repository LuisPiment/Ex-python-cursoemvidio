v=[]
o=[]
i=[]
for c in range(0,5):
    v.append(int(input("Digite um numero ")))
vmax=max(v)
vmin=min(v)
v1=v2=p1=p2=0
for p,t in enumerate(v):
    if t==vmax:
        o.append(p+1)
    if t==vmin:
        i.append(p+1)
print(f"Os seus numeros foram {v}")
print(f"Os maior numero é {vmax} e encomtrasse nas posições {o}")
print(f"Os menor numero é {vmin} e encomtrasse nas posições {i}")