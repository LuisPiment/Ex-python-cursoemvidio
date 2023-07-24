print("\033[1;35mConversor de bases numericas\nEscolha 1 para base binaria,escolha 2 para base octadecimal, escolha 3 para base hexadecimal")
n=int(input("Digite o numero para converter "))
m=int(input("Escolha a base de conversão(1,2,3): "))
if m==1:
    base="Binario"
    nc=bin(n)[2:]
elif m==2:
    base="Octadecimal"
    nc=oct(n)[2:]
elif m ==3:
    base="Hexadecimal"
    nc=hex(n)[2:]
else:
    print("Por favor digite 1,2 0u 3 e nao outro numero")
print("O seu numero na base {} é {}".format(base,nc))
