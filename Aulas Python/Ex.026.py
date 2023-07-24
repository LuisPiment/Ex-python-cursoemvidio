f=str(input("Digite uma frase ")).strip()
f1=f.lower()
f2=f1.count("a")
f3=f1.find("a")+1
f4=f1.rfind("a")+1
print("A letra A aparece {} vezes \nA primerira aparição do A foi {} \nA ultima aparição do A foi {}".format(f2,f3,f4))
