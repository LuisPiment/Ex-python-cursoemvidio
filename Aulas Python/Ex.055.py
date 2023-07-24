maior=0
menor=0
for c in range (0,5):
    n=float(input("Digite o seu peso "))
    if n>maior:
        maior=n
    if n*-1<menor:
        menor=n
print("O maior peso é {} e o menor peso  é {}".format(maior,menor))
