pi=[[],[]]
for c in range (0,7):
    n1=int(input(f"Digite um numero:"))
    if n1%2==0:
        pi[0].append(n1)
    else:
        pi[1].append(n1)
pi[0].sort()
pi[1].sort()
print(f"Os numeros pares são {pi[0]}")
print(f"Os numeros impares {pi[1]}")




