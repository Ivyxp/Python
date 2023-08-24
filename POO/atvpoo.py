import math


def linha():
    print ('--------------------------------------------------------------------------------------------------')


'''Crie um programa que utilize esta classe. Ele deve
pedir ao usuário que informe as medidas de um
triangulo. Depois, deve criar um objeto com as
medidas e imprimir sua área e maior lado.'''
class triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
       
    def calcularArea(self):
        p = (self.ladoA + self.ladoB + self.ladoC)/2
        area = math.sqrt(p*(p-self.ladoA)*(p-self.ladoB)*(p-self.ladoC))
        return area
    

    def getMaiorLado(self):
        maior_lado = max(self.ladoA,self.ladoB, self.ladoC)
        return maior_lado
   
lado1 = float(input('Digite o comprimento do primeiro triangulo: '))
lado2 = float(input('Digite o comprimento do segundo triangulo: '))
lado3 = float(input('Digite o comprimento do terceiro triangulo: '))

tri = triangulo(lado1,lado2,lado3)
area = tri.calcularArea()
print (f"A area do triangulo e: {area}")
       
print ('maior lado do triangulo: ',tri.getMaiorLado())
linha()


'''2. Classe Funcionário: Implemente a classe
Funcionário. Um funcionário tem um nome e um
salário. Escreva um construtor com dois parâmetros
(nome e salário) e o método aumentarSalario
(porcentualDeAumento) que aumente o salário do
funcionário em uma certa'''


class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
       
    def aumentarSalario(self,porcAumento):
        self.salario+= (porcAumento*100)/100
   
nome = input('qual e seu nome: ')
salario = float(input('informe seu salario: '))
func = Funcionario(nome,salario)

print(func.nome,'seu salario: ',func.salario)


aumento = float(input('informe o aumento do salario: '))
func.aumentarSalario(aumento)
print(func.nome,'seu salario com aumento: ',func.salario)
linha()
       
# 3. Crie uma classe Livro que possui os
# atributos nome, qtdPaginas, autor e preço. – Crie os métodos getPreco para obter o valor

# do preco e o método setPreco para setar
# um novo valor do preco.


class livro:
    def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco
       
    def getPreco(self):
        return self.preco
   
    def setPreco(self, preco):
        self.preco = preco
 
 
nome1 = input('nome do livro: ')
paginas = int(input('quantidades de paginas do livro: '))
autor = input('autor do livro: ')
preco = float(input('preco do livro: '))
lvro = livro(nome1, paginas, autor, preco)
print('nome: ',lvro.nome,'paginas: ', lvro.qtdPaginas, 'autor: ' ,lvro.autor,'preco',lvro.preco)
linha()


# 4. Implemente uma classe Aluno, que deve ter os
# seguintes atributos: nome, curso, tempoSemDormir
# (em horas). Essa classe deverá ter os seguintes
# métodos: – estudar (que recebe como parâmetro a qtd de horas de
# estudo e acrescenta tempoSemDormir ) – Dormir (que recebe como parâmetro a qtd de horas de

class aluno:
    def __init__(self, nome,curso,tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir
       
    def estudar(self,qqhorasEstudo):
        self.tempoSemDormir+=qqhorasEstudo
   
       
    def dormir(self,sono):
     self.tempoSemDormir -= sono

#solicitar dados
nome2 = input('nome do aluno: ')
curso = input('curso do aluno: ')
tempoSemDormir = int(input('tempo sem dormir do aluno: '))

#criar objeto
al = aluno(nome2,curso,tempoSemDormir)

#registrae horas de estudo e de sono
horasAcordado = int(input('quantas horas voce ficou acordado: '))
al.estudar(horasAcordado)
horasDotmindo = int(input('quantas horas de sono voce teve: '))
al.dormir(horasDotmindo)

# Imprimir o tempo sem dormir do aluno
print(f"O aluno {al.nome} está sem dormir há {al.tempoSemDormir} horas.")
linha()

# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
# •Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
# •O consumo é especificado no construtor e o nível de combustível inicial é 0.
# •Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina. Esse método recebe como parâmetro a distância em km.
# •Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
# •Forneça um método adicionarGasolina( ), para abastecer o tanque.
class carro:
    def __init__(self,consumo,):
        self.consumo = consumo
        self.nivelCombustivel = 0

    def andar(self,distancia):
        consumo = distancia/self.consumo
        if consumo <= self.nivelCombustivel:
            self.nivelCombustivel -= consumo
            return (f"O carro percorreu {distancia} km")
        else:
            return (f"Combustivel insuficiente ")
    
    def obterGasolina(self):
      return self.nivelCombustivel 
    
    def adicionarGasolina(self, qtidade):
        self.nivelCombustivel += qtidade

consumo = float(input('informe o consumo do carro: '))

car = carro(consumo)

gas = float(input('quantidade de gasolina: '))
car.adicionarGasolina(gas)

distancia = float(input('informe a distancia andada: '))
car.andar(distancia)

gasolina = car.obterGasolina()



print(f"O carro está com {gasolina} litros de gasolina no tanque.")

linha()

# Crie uma classe Aluno, que possui como atributo um nome e
# cpf. Crie outra classe chamada Equipe, que possui como
# atributo uma lista de participantes do tipo Aluno e outro
# atributo chamado projeto.
# Crie uma terceira classe chamada GerenciadorEquipes. Essa
# classe possui como atributo uma lista de todas as equipes
# formadas. Ela deverá possuir o método criarEquipe, que recebe
# uma lista de alunos de uma equipe e diz se a equipe pode se
# r
# formada ou não. Caso não haja nenhum aluno da equipe a ser
# formada em uma outra equipe com o mesmo projeto, então a
# equipe é criada e acrescentada à lista. Caso contrário é
# informada que a equipe não pode ser criada.

class Aluno:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
#EXISTEM DUAS CLASSES aluno e Aluno SAO DIFERENTES 
class Equipe:
    def __init__(self,projeto):
        self.alunos = []
        self.projeto = projeto


class gerenciadorEquipes:
    def __init__(self):
        self.equipes = []

    def criarEquipe(self,alunos,projeto):
        equipe_existente = None
        for equipe in self.equipes:
            if any(aluno in equipe.alunos for aluno in alunos):
                equipe_existente = equipe
                break
        if equipe_existente:
            print(f"O aluno {aluno.nome} ja esta em uma equipe")
        else:
            novaEquipe = Equipe(projeto)
            novaEquipe.alunos = alunos
            print("A equipe foi criada com sucesso!")


aluno1 = Aluno(input('nome do aluno: '),input('cpf do aluno: '))
aluno2 = Aluno(input('nome do aluno: '),input('cpf do aluno: '))
aluno3 = Aluno(input('nome do aluno: '),input('cpf do aluno: '))

ger = gerenciadorEquipes()
team = [aluno1,aluno2,aluno3]
projeto = input('digite o nome do projeto da equipe: ')

ger.criarEquipe(team,projeto)

for equipe in ger.equipes:
    if equipe.projeto == projeto:
        nomes_alunos = ', '.join([aluno.nome for aluno in Equipe.listar_alunos()])
        print(f"A equipe {nomes_alunos} possui o projeto {equipe.projeto}.")
    else:
        nomes_alunos = ', '.join([aluno.nome for aluno in Equipe.listar_alunos()]) 
        print(f"A equipe {nomes_alunos} não possuei o projeto {equipe.projeto}")




