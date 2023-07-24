print("\033[1;31mAprovação de emprestimo bancario\033[m \nPorfavor insira os seguintes dados:")
s=int(input("Insira o seu salario mensal: "))
e=int(input("Insira o valor do emprestimo desejado: "))
p=int(input("Insira a quantidade de anos que quer fazer as prestaões: "))
pm=e/(p*12)
if pm>(s*0.30):
    print("O seu salario é insuficiente para este numero de prestações/emprestimo")
else:
    print("Parabens o seu emprestimo é possivel pelo valor de {:.2f} por prestação mensal".format(pm))
