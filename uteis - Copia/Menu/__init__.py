from uteis import dados
def menup(num):
    while True:
        print(f"{'~'*30}\n{'Menu Principal':^30}\n{'~'*30}\n\033[1;33m1-\033[m\033[1;34mVer pessoas Cadastradas\033[m")
        print(f"\033[1;33m2-\033[m\033[1;34mCadastrar nova pessoa\033[m\n\033[1;33m3-\033[m\033[1;34mSair do pograma\033[m")
        try:
            n1=int(input(num.strip()))
        except:
            print("\033[1;31mErro tente opção invalida, tente novamente\033[m")
            continue
        else:
            if n1>3 or n1<0:
                print("\033[1;31mErro Opção Invalida\033[m")
            if n1==3:
                print("Saindo do pograma... Ate Logo")
                break
            if n1==1:
                if not arquivoexiste("novop"):
                    criararquivo("novop")
                lerarquivo("novop")
            if n1==2:
                no=str(input("Digite o seu nome: "))
                id=dados.leaint("Diga-me a sua idade: ")
                cadastrar("novop",no,id)



def arquivoexiste(nome):
    try:
        a=open(nome,"rt")
        a.close()
    except(FileNotFoundError):
        ex=False
    else:
        ex=True
    return ex

def criararquivo(nome):
    try:
        a=open(nome,"wt+")
        a.close()
    except:
        print(f"Teve uma falha na criação do seu arquivo")
    else:
        print(f"O seu arquivo foi criado com o nome {nome}")
def lerarquivo(nome):
    try:
        a=open(nome,"rt")
    except:
        print("Teve um erro ao ler o seu arquivo")
    else:
        print("~"*30)
        print("Pessoas Cadastradas")
        for c in a:
            dado=c.split(";")
            dado[1]=dado[1].replace("\n","")
            print(f"{dado[0]:<15}\t\t{dado[1]}")
        print("~"*30)
    finally:
        a.close()

def cadastrar (arq,nome,idd):
    try:
        a=open(arq,"at")
    except:
        print("Tivemos um erro na opção de adcionar arq")
    else:
        try:
            a.write(f"{nome};{idd}\n")
        except:
            print("Teve uma falha na escrita ")
        else:
            print("Cadastro feito com sucesso")
        finally:
            a.close()





