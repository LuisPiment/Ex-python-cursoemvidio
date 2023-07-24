n1=(str(input("Digite uma conta ")))
t=n1.count("(")
p=n1.count(")")
if t==p:
    print("A sua conta é valida")
else:
    print("A sua conta nao é valida")

