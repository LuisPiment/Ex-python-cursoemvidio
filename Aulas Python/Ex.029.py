k=int(input("Digite a velocidade do seu carro "))
if k>=80:
    m=(k-80)*7
    print("Voce deve pagar {} reais de multa".format(m))
else:
    print("Continue com a boa conduta na estrada")
print("Ate a proxima e tenha cuidado em estrada")
