c1=0
n2=0
n1 = int(input("Digite o valor que deseja sacar "))
ced=50
total=n1
while True:
    if total>=ced:
        total-=ced
        c1+=1
    else:
        if c1>0:
            print(f"Voce vai sacar {c1} notas de {ced}")
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        c1=0





