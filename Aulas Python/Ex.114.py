import urllib.request


try:
    site=urllib.request.urlopen("http://www.pudim.com.br")
except:
    print("O site nao esta acessivel")
else:
    print("Consegui acessar o site")
