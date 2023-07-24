def metade(p1=0,form=False):
    s1=p1/2
    m = "€"
    if form:
        return f"{m}{s1:.2f}".replace(".", ",")
    else:
        return s1
def dobro(p1=0,form=False):
    s2=p1*2
    m = "€"
    if form:
        return f"{m}{s2:.2f}".replace(".", ",")
    else:
        return s2
def aumentar(p1=0,aum=0,form=False):
    s3=p1*(1+(aum/100))
    m = "€"
    if form:
        return f"{m}{s3:.2f}".replace(".", ",")
    else:
        return s3
def diminuir(p1=0,dim=0,form=False):
    s4=p1*(1-(dim/100))
    m = "€"
    if form:
        return f"{m}{s4:.2f}".replace(".", ",")
    else:
        return s4

def bonito(p1=0,m="€"):
    return f"{m}{p1:.2f}".replace(".",",")
def resumo(n1=0,aum=0,dim=0):
        t=[f"{'~'*30}\n"
         f"{'Resumo Do Valor':^30}\n"
         f"{'~'*30}\n"
         f"Preço analisado {bonito(n1):>14}\n"
         f"Dobro do Preço {dobro(n1,True):>15}\n"
         f"Metade do preço {metade(n1,True):>14}\n"
         f"{aum}% de aumento {aumentar(n1,aum,True):>15}\n"
         f"{dim}% de diminuição {diminuir(n1,dim,True):>12}\n"
         f"{'~' * 30}\n"]
        for c in t:
            return c