#CRIANDO UMA LISTA
lista = [2,28,9, 'league of legends', 78, 12]
#ADICIONAMDO UM ELEMENTO A LISTA
lista[0] = 33
#PRINTANDO UMA LISTA
print(lista)

numeros = [3,5,9,1,7,5,9,3,1,7,5,9]
print(numeros[3])
#USANDO O OPERADOR - A LISTA PRINTA DE TRAS PARA FRENTE
print(numeros[-3])
#PRINTANDO O INTERVALO UMA LISTA
print(numeros[3:5])

#TESTANDO PARA SABR SE EXISTE UM VALOR NA LISTA
print(42 in lista)
#CEIANDO UMA LISTA QUE CONTEM OUTRA LISTA
colecao = ['casa', 25, 'dc,', 84, True, 'laranja', [6,5,7]]
#PRINTANDO A LISTA QUE ESTA DENTRO DA LISTA PELO INDEX
print(colecao[6])

# del deleta um alemento da lista de acordo com o indice informado
del colecao[2]
print(colecao)
# O operador + concatena lista 
combinacao = numeros + colecao
print(combinacao)
# O operador * repete a lista dado um número de vezes 
print(lista*2)
# Existem métodos que permitem alterar listas, como o append, que
# adiciona um elemento ao final da lista:
lista.append('adicionei elemento')
print(lista)
# Para inserir numa posição qualquer: list.insert(index, obj)
lista.insert(0, 'inserindo na posicao zero')
print(lista)
# extend recebe uma lista como argumento e adiciona todos seus elementos a outra:
teste = [1,3,6]
print(teste)
teste1 = [3,2,1]
print(teste1)
teste.extend(teste1)
print(teste)

# O método sort ordena os elementos da lista em ordem ascendente:
teste.sort()
print(teste)
# Para fazer uma cópia de uma lista, devemos usar o método copy:
l1 = ['copia', 'funcao', 'testando']
l2 = l1.copy()
print(l1)
print(l2)
l2.extend('adicionando')
print(l2)
l2.append('inserindo')
print(l2)

# uma nova lista
herois = ['superman', 'batman', 'wonder woman']
#varrendo uma lista inteira
for hero in herois:
    print(hero)
#trocando o ultimo elemento
herois[-1] = 'diana'
print(herois)

#incluido
herois.append('flash')
print(herois)
#removendo
herois.remove('batman')
print(herois)
#inverte a lista
herois.reverse()
print(herois)
#imprme numerado
# for i  in enumerate(herois):
#     print(herois[i])
  
# Em python existe a função embutida range(), com ela é possível produzir uma lista extensa de uma maneira bemsimples:
lista_grande = [3,3,3,5,6,9,4,2,8]
recebe = []
for i in range(len(lista_grande)):
    recebe.append(lista_grande[i])
    print(recebe)
# pritando a lista de 1 a 200 usando a funcao range
x = range(1, 200, 2)
for n in x:
    print (n)