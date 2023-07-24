n=input("Digite algo ")
t=(type(n))
n1=(n.isnumeric())
n2=(n.isalpha())
n3=(n.isalnum())
n4=(n.isupper())
n5=(n.islower())
print("""classe:{}
 É so numero {} 
 É so Letras {} 
 Contem Numero e Letra {} 
 Esta tudo em maiusculo {} 
 Esta tudo em minuscula {}""".format(t,n1,n2,n3,n4,n5))