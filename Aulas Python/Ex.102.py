def factorial(num,show=False):
    f=1
    global t
    t = num
    for c in range (num,0,-1):
        f*=c
        if show:
            print(c,end=" ")
            if c>1:
                print("x",end=" ")
            else:
                print("=",end=" ")
    return f





print(factorial(5,True))

