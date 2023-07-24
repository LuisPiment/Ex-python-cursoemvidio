matriz=[[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3):
    for c in range (0,3):
        matriz [l] [c]=int(input(f"Digite um numero na posição[{l}:{c}]:  "))
s=0
s1=0
c1=0
maior=0
for l in range(0,3):
    for c in range (0,3):
        print(f"[ {matriz [l][c]} ]",end=" ")
        if matriz[l] [c]%2==0:
            s+=matriz[l][c]
        if c==2:
            s1+=matriz[l][2]
        if matriz[1][c]>maior:
            maior=matriz[1][c]
    print()
print(f"A soma dos valores pares {s}")
print(f"A soma dos valores da terceira coluna é {s1}")
print(f"O maior valor da segunda linha é {maior}")
