import matplotlib.pyplot as plt
def menu():
    print("""
    Gestão de Polinómios: 
(1) Criar um polinómio;
(2) Simplificar polinómio;
(3) Calcular derivada de um polinómio;
(4) Calcular tabela;
(5) Ordenar o polinómio;
(6) Fazer o gráfico da função polinomial
(0) Sair""")
    
def criarTermo(c, e):
    return(c, e)

def criarPol():
    return []

def inserirTermo(p,t):
    return p.append(t)

def verTermo(t):
    c, e = t
    if e == 0:
        return str(c)
    elif e==1:
        return str(c) +'x'
    else:
        return str(c)+"x^"+ str(e)
    
def verPol(p):
    res = " "
    for t in p:
        if res == " ":
            res = verTermo(t)
        else:
            res = res + " + " + verTermo(t)
    print(res)
    
def chaveOrd(t):
    (c, e) = t 
    return e

def ordenarPol(p):
    p.sort(reverse = True, key = chaveOrd)
    return p
    
def simplificarPol (p):
    pord= ordenarPol(p)
    psimp=[]
    coef= []
    coeficiente=0
    n=1
    for i in pord: 
        while n<len(pord):
            c,e= i
            if (e == pord[n][1] ):
                coef.append(c)
            else:
                if len(coef)>0:
                    for i in coef:
                        coeficiente= coeficiente+i
                else:
                    coeficiente=c
            psimp.append((coeficiente, e))
            n=n+1
    return (psimp)

def derivarPol(p):
    res = []
    for (c, e) in p:
            if e > 0:
                res.append((c*e, e-1))
    return res    
    
def calcPol(p, x):
    res = 0
    for t in p:
       res = res + t[0]*(x**t[1])
    return res

def tabela(p, nlinhas):
    print("x  | Resultado")
    print("______________")
    for x in range (nlinhas+1):
        print(x, str(" | "), calcPol(p, x))
        
def grafico(p):
    x=[i for i in range(-100,100)]
    y=[]
    for n in x:
        y.append(calcPol(p,n))
        
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Função polinomial')
    plt.show()
    
op = "4"
while (op != "0"):
      menu()
      op = input("Qual é a sua opção?")
      if op == "1":
         poli = []
         termos = int(input("Quantos termos tem o polinómio?"))
         for i in range(termos):
             politup = input("Introduza o termo sem o x colocando uma , no seu lugar: ")
             politup2 = tuple(int(x) for x in politup.split(","))
             poli.append(politup2)
         polin = verPol(poli)
         print (polin)
         print ("            ")
        

      elif op == "2":
        try:
            print(simplificarPol(poli))
            print("      ")
        except:
            print ("Ainda não foi criado nenhum polinómio.")
            print ("                  ")
            
      elif op =="3":
        try:
            deri = derivarPol(poli)
            ver = verPol(deri)
            print(ver)
            print("      ")
        except:
            print ("Ainda não foi criado nenhum polinómio.")
            print ("                  ")
            
      elif op =="4":
        try:
            nlinhas = int(input("Qual o número de linhas a adicionar à tabela?"))
            print("        ")
            poli2 = tabela(poli, nlinhas)
            print(poli2)
        except:
            print ("Ainda não foi criado nenhum polinómio.")
            print ("                  ")
            
      elif op =="5":
        try:
            orden = ordenarPol(poli)
            ver = verPol(orden)
            print(ver)
            print("      ")
        except:
            print ("Ainda não foi criado nenhum polinómio.")
            print ("                  ")
      elif op =="6":
        try:
            grafico(poli)
            print("      ")
        except:
            print ("Ainda não foi criado nenhum polinómio.")
            print ("                  ")
            
      elif op == "0":
            print("Até à próxima!")
            print ("            ")
      else:
         print("Opção inválida!")
         print ("             ")
