n1=int(input("Digite um valor "))
n2=int(input("Digite outro valor "))
op=99
m=""
while op!=5:
    print("-==-"*8)
    print("    [ 1 ] Somar\n    [ 2 ] Mutiplicar\n    [ 3 ] Maior\n    [ 4 ] Novos numeros\n    [ 5 ] Sair do pograma")
    op=int(input(">>>> Qual a sua opção  "))
    if op==1:
        print("A soma do valor {} e {} é {}".format(n1,n2,n1+n2))
    elif op==2:
        print("A mutiplicação de {} e de {} é {}".format(n1,n2,n1*n2))
    elif op==4:
        n1 = int(input("Digite um novo valor "))
        n2 = int(input("Digite outro novo valor "))
    elif op==3:
        if n1>n2:
            print("O maior valor é ".format(n1))
        elif n2>n1:
            print("O maior valor é {}".format(n2))
        else:
            print("Nao existe valor maior os dois sao iguais ")
    elif op!=5:
        print("Opção invalida tente novamente")

print("Espero que tenha gostado ")









