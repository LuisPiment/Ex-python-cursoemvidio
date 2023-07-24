import datetime
an=int(input("Digite o seu ano de nascimento "))
i= datetime.date.today().year-an
al=18-i
if i>18:
    print("Ja passou da {} anos que devias ter te alistado".format(al*-1))
elif i<18:
    print("Daqui a {} deves te alistar ".format(al))
else:
    print("Deves te alistar neste ano")









