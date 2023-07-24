n=str(input("Escreva um nome ")).strip()
t=n.split()


print(n.upper().strip())
print(n.lower().strip())
print("O seu nome tem {} letras".format(len(n)-n.count(" ")))
print("O seu primeiro tem  {} letras".format(n.find(" ")))
print("O seu primeiro nome é {} e tem {} letras ".format(t[0],len(t[0])))



