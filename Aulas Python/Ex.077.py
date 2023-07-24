p="palavras","linguas","tabuadas","origem","lista","maneiro","poder","soco","gostar","livro"
for c in p:
    v1=c.count('a')
    v2=c.count('e')
    v3=c.count('i')
    v4=c.count('o')
    v5=c.count('u')
    if v1>0:
        vo1=v1*"a "
    else:
        vo1=""
    if v2>0:
        vo2=v2*"e "
    else:
        vo2=""
    if v3>0:
        vo3=v3*"i "
    else:
        vo3=""
    if v4>0:
        vo4=v4 * "o "
    else:
        vo4=""
    if v5 > 0:
        vo5 = v5 * "u "
    else:
        vo5=""
    print(f"A palvra {c} contem {vo1}{vo2}{vo3}{vo4}{vo5}")
    
