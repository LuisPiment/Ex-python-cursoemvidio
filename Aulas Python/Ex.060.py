import math
f=int(input("Digite um numero para obter o seu fatorial "))
print("O fatorial de {}=".format(f,),end="")
f1=math.factorial(f)
while f!=0:
    print("{}x ".format(f,),end="")
    f-=1
print("={}".format(f1))


