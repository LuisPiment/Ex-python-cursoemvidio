def escreva(texto,cor):
    tam=len(texto)+2
    if cor=="v":
        co="\033[1;;42m"
    elif cor=="a":
        co="\033[7;33;40m"
    elif cor=="az":
        co="\033[1;;44m"
    elif cor=="ve":
        co="\033[1;;41m"

    print(f"{co}~"*tam)
    print(f" {texto}")
    print("~"*tam)
def help2(com):
    while True:
        escreva("SISTEMA DE AJUDA PyHELP","v")
        print("\033[m")
        n1=str(input(com)).strip().lower()
        if n1=="fim":
            escreva("ATÉ LOGO","ve")
            break
        escreva(f"Acessando o manual do comando {n1}","a")
        print("\033[7;;44m~" * 50)
        print(f"{help(n1)}")
        print("~" * 50)
        print("\033[m")
n2=help2("Digite um comando: ")











