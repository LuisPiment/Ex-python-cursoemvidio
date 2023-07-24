def leiadinheiro(n3):
    valido = False
    while not valido:
        entrada = str(input(n3)).strip()
        if entrada.isalpha() or entrada=="":
            print("Erro: Valor invalido")
        else:
            valido=True
            return float(entrada.replace(",", "."))

def leaint1(num1,num2):
    while True:
        try:
            ni=int(input(num1))
        except:
            print("Erro, Digite um numero inteiro valido")
        else:
            break
    while True:
        try:
            nr=float(input(num2))
        except:
            print("Erro, Digite um numero real valido")
        else:
            break
    print(f"O numero inteiro digitado é {ni} e o real é {nr}")

def leaint(num1):
    while True:
        try:
            ni=int(input(num1))
        except:
            print("Erro, Digite um numero inteiro invalido")
        else:
            return ni
            break








