
while True:
    n=int(input("Qual tabuada deseja "))
    if n<0:
        break
    for c in range(1,11):
        r=n*c
        print(n," x ",c," = ",r)
print("acabou")

