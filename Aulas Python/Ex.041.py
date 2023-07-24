print("\033[1;34mClasses de natação\033[m")
i=int(input("Digite a sua idade "))
if i<=9:
    c="Mirim"
elif 14>=i>9:
    c="Infantil"
elif 19>i>14:
    c="Junior"
elif i==19 or i==20:
    c="Senior"
elif i>20:
    c="Master"
print("A sua clase é {}".format(c))
