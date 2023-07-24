n1=int(input("Tabuada de qual numero "))
n2=int(input("Quantas linhas a tabuada "))
for c in range(1,n2+1):
    print("{} x {} = {}".format(n1,c,n1*c))

