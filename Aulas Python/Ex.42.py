n1=float(input("Digite o 1 numero "))
n2=float(input("Digite o 2 numero "))
n3=float(input("Digite o 3 numero "))
if n1>= n2>= n3:
    maior=n1
    menor=n3
    menor2=n2
if n1>=n3>=n2:
    maior=n1
    menor1=n2
    menor2=n3
if n2>= n1 >= n3:
    menor1=n3
    menor2=n1
    maior=n2
if n2 >= n3 >= n1:
    menor1=n1
    maior=n2
    menor2=n3
if n3 >= n1>=n2:
    maior=n3
    menor2=n1
    menor1=n2
if n3 >= n2 >= n1:
    menor1=n1
    maior=n3
    menor2=n2
p=menor1+menor2

if n1==n2==n3:
    c="equilatero"
elif n1==n2 or n1==n3 or n2==n3:
    c="Isoceles"
elif n1!=n2!=n3:
    c="Escaleno"

if maior<p:
    print("O seu triangulo é possivel e é {}".format(c))

else :
    print("O seu triangulo n é possivel")
