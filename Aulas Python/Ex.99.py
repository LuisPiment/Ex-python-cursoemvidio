t=0
def maior(*num):
    print("-="*30)
    print(f"Analisando valores:")
    for c in num:
        print(c,end=" ")
    print(f" foram informados {len(num)} valores ao todo")
    if len(num)>0:
            print(f"O maior valor informado foi {max(num)}")
    else:
        print(f"O maior valor informado foi 0 ")
maior(1,2,3,4,5)
maior(9,847,36,54)
maior(6)
maior()