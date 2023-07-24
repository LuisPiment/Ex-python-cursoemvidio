from datetime import date
def voto(ano):
    """
    Digite seu ano de nacsimento que dira se
    é Obrigatorio,opcional,ou nao podes votar.
    Use o votod para usar a função dita
    """
    global votod
    global id
    aat=date.today().year
    id=aat-ano
    if id<16:
        votod="Nao podes"
    elif 16<=id<18 or id>65:
        votod="Opcional"
    else:
        votod="Obrigatorio"
    return votod



n1=int(input("Em qual ano nasceste: "))
voto(n1)
print(f"Com {id} anos:O seu voto é {votod}")