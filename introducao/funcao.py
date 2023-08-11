# criando funcao em python. 
#sem argumento
def soma():
    print(1 +  1)
soma()

#xom return
def soma():
    return 1 +  1
print(soma())

# Queremos somar 3 com um número qualquer que insiro na função.
def soma_valor(x):
    return 2 + x
print(soma_valor(5))

# Bora lá, funcao com parametros:
def multiplicara(x,y):
    return x * y
print(multiplicara(2,3))

# def tabuada():
#     for i in range(1,11):
#         for j in range(1,11):
#             print("{} * {} = {}".format(i, j, i * j))

# tabuada()


#def tabuada(y, z):
 #       print(y * z)
        

#idade = int(input("Digite sua idade: "))
#print(idade)

#if idade >= 18:
#    tabuada(idade, idade)
#else:
#    tabuada(idade, 1)
    


#def tabuada_com_parametros(a,b):
 #   for i in range(a,b):
  #      for j in range(a,b):
   #         return("{} * {} = {}".format(i, j, i * j))


def tabuada_completa(a, b):
    for i in range(a,b+1):
        for j in range(a,b+1):
            print("{} * {} = {}".format(i, j, i * j))
            
resposta = bool(input("Você é bom em matematica: "))

if resposta == False:
    print("Você é bom em matematica!")
    
else:
    valor1 = int(input("Informe um numero: "))
    valor2= int(input("Informe um numero: "))
    tabuada_completa(valor1, valor2)