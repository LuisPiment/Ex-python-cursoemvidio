n1=float(input("Digite o 1 numero "))
n2=float(input("Digite o 2 numero "))
n3=float(input("Digite o 3 numero "))
if n1> n2> n3:
    maior=n1
    menor=n3
if n1>n3>n2:
    maior=n1
    menor=n2
if n2> n1 > n3:
    menor=n3
    maior=n2
if n2 > n3 > n1:
    menor=n1
    maior=n2
if n3 > n1>n2:
    maior=n3
    menor=n2
if n3 > n2 > n1:
    menor=n1
    maior=n3
print("O maior numero é {} e o menor é {}".format(maior,menor))
