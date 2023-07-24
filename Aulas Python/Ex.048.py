a1=int(input("Digite a quantidade de numeros que  quer "))
m=int(input("Digite o numero de mutiplo "))
s=0
for c in range(1,a1+1,2):
 if c%m==0:

  s+=c
print(s)


