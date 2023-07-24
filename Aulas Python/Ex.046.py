import time
te=int(input("Digite o tempo desejado para a esplosão acontecer "))
ten=float(input("Digite o tempo entre os numeros "))
for c in range(te,0,-1):
    time.sleep(ten)
    print(c)
print("BOM BOM BOM SPLASH")

