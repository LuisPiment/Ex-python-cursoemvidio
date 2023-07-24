def resp(*num,sit=False):
    l={}
    total=0
    total=sum(num)
    l["total"]=total
    maior=max(num)
    menor=min(num)
    l["maior"]=maior
    l["menor"]=menor
    media=sum(num)/len(num)
    l["media"]=media
    if sit:
        if media>=7:
            si="Boa"
        elif 5<media<7:
            si="Media"
        else:
            si="Ruim"
        l["Situação"]=si
    print(l)
print(resp(10,10,10,6,10,2,sit=True))