l=("lapis",1.75,"Borracha",2.00,"Caderno",15.90,"Estonjo",25.00,
   "Transferidor",4.20,"Compasso",9.99,"Mochila",120.32,"Canetas",22.30,
   "Livro",34.90)
c0=0
c1=1
print(20*"-=-")
print(f"{'Listagem de preços':^55}")
print(20 * "-=-")
for p,c in enumerate(l):
    if c1<18:
        print(f"{l[c0]:.<30}{l[c1]:>6.2f}")
    c0+=2
    c1+=2

