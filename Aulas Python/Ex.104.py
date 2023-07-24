def leaint(num):
   global n1
   while True:
        n1=str(input(num)).strip()
        if n1.isnumeric():
            break
        else:
            print("\033[1;31m ERRO digite um numero inteiro valido\033[m")


n=leaint("Digite um numero: ")
print(f"Voce acabou de digitar {n1}")
