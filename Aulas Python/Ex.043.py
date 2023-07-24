print("\033[1;32mCalculadora e classificação de IMC")
kg=float(input("Digite o seu peso em kg "))
al=float(input("Digite o seu peso em m \033[m"))
imc=kg/(al**2)
if imc<=18.5:
    c= "Abaixo do peso"
elif 25>=imc>18.5:
    c="Peso ideal"
elif 30>=imc>25:
    c="Sobrepeso"
elif 40>=imc>30:
    c="Obsesidade"
else:
    c="Obesidade morbida"
print("A sua classe de imc é {}".format(c))
