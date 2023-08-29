# 1. Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor

def linha():
    print ('---------------------------------------')
    
    

class bola:
    #self e obrigatorio
    #construtor, e atributos
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material
      
      #metodos
    def mostrarCor(self):
          return self.cor
      
          
    def trocarCor(self, cor):
         self.cor = cor
         return self.cor
      
#instance do objeto e passando argumentos
bo= bola('branco','90','couro')

print(bo.trocarCor('azul'))

print(bo.mostrarCor())
linha()
# 2. Classe Quadrado: Crie uma classe que modele um quadrado:
# a. Atributos: Tamanho do lado
# b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado ** 2 
      
      
# Criando um objeto quadrado com lado igual a 5
meu_quadrado = Quadrado(5)

# Imprimindo o lado do quadrado
print("Lado do quadrado:", meu_quadrado.retornar_lado())  # Saída: Lado do quadrado: 5

# Mudando o valor do lado para 7
meu_quadrado.mudar_lado(7)

# Imprimindo o novo valor do lado
print("Novo lado do quadrado:", meu_quadrado.retornar_lado())  # Saída: Novo lado do quadrado: 7

# Calculando a área do quadrado
area = meu_quadrado.calcular_area()
print("Área do quadrado:", area)  # Saída: Área do quadrado: 49


# 3. Classe Retângulo: Crie uma classe que modele um retângulo:
# a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura,
# a escolher)
# b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área
# e calcular Perímetro;
# c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
# informe as medidas de um local. Depois, deve criar um objeto com as
# medidas e calcular a quantidade de pisos e de rodapés necessárias para
# o local.

class retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def mudarLados(self, novoLado):
        self = novoLado
        
        
        
    def getLado(self):
        print('altura ', self.altura, 'largura', self.largura)        

    def area(self):
        return self.base*self.altura
  
    
    
    def perimetro(self):
        p = 2*(self.base*self.altura)
        return p


base = float(input('informe a base: '))
altura = float(input('informe a altura: '))

rent = retangulo(base,altura)

print('a area', rent.area(), 'perimetro', rent.perimetro())

linha()

# 4. Classe Pessoa: Crie uma classe que modele uma pessoa:
# a. Atributos: nome, idade, peso e altura
# b. Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão,
# a cada ano que nossa pessoa envelhece, sendo a idade dela menor que
# 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer()
       
    def engordar(self):
        self.peso += self.peso
        
    def emagrecer(self, peso):
        self.peso -= peso
    
    def crescer(self):
        self.altura += self.altura
        
nome2 = input('Nome da pessoa: ')
idade2 = int(input('Sua idade: '))
peso2 = float(input('Seu peso: '))
altura2 = int(input('Sua altura: '))

pessoa = Pessoa(nome2, idade2, peso2, altura2)

# Imprimindo os atributos iniciais
print(pessoa.nome)    
print(pessoa.idade)   
print(pessoa.peso)    
print(pessoa.altura)


# Envelhecendo a pessoa
pessoa.envelhecer()

# Imprimindo a idade após envelhecer
print(pessoa.idade)  

# Crescendo a pessoa
pessoa.crescer()

# Imprimindo a altura após crescer
print(pessoa.altura)  

# Engordando e emagrecendo a pessoa
pessoa.engordar(5)
pessoa.emagrecer(3)

# Imprimindo o peso após engordar e emagrecer
print(pessoa.peso)    

# 5. Classe Conta Corrente: Crie uma classe para implementar uma conta
# corrente. A classe deve possuir os seguintes atributos: número da conta, nome
# do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e
# saque; No construtor, saldo é opcional, com valor default zero e os demais
# atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
            
            
# 6. Classe TV: Faça um programa que simule um televisor criando-o como um
# objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou
# diminuir o volume. Certifique-se de que o número do canal e o nível do volume
# permanecem dentro de faixas válidas.
    
class TV:
    def __init__(self):
        self.canal = 1  # Canal inicial
        self.volume = 50  # Nível de volume inicial

    def alterarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido.")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume máximo alcançado.")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume mínimo alcançado.")
            
                  
#  7. Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho
# Eletrônico):                   
class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, novo_nivel_fome):
        self.fome = novo_nivel_fome

    def alterarSaude(self, novo_nivel_saude):
        self.saude = novo_nivel_saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def retornarHumor(self):
        return self.fome + self.saude


# Exemplo de uso da classe BichinhoVirtual
bichinho = BichinhoVirtual("Tama")

print(bichinho.retornarNome())     
print(bichinho.retornarFome())     
print(bichinho.retornarSaude())   
print(bichinho.retornarIdade())    
print(bichinho.retornarHumor())    

bichinho.alterarNome("Tama Jr.")
bichinho.alterarFome(10)
bichinho.alterarSaude(90)
bichinho.alterarIdade(1)

print(bichinho.retornarNome())    
print(bichinho.retornarFome())     
print(bichinho.retornarSaude())    
print(bichinho.retornarIdade())    
print(bichinho.retornarHumor())    


# 8. Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos
# nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e
# digerir(). Faça um programa ou teste interativamente, criando pelo menos dois
# macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando
# o conteúdo do estomago a cada refeição.
           
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        if len(self.bucho) > 0:
            print(f"Conteúdo do bucho do macaco {self.nome}:")
            for alimento in self.bucho:
                print(alimento)
        else:
            print(f"O bucho do macaco {self.nome} está vazio.")

    def digerir(self):
        if len(self.bucho) > 0:
            print(f"O macaco {self.nome} está digerindo.")
            self.bucho = []
        else:
            print(f"O bucho do macaco {self.nome} já está vazio.")



# Exemplo de uso da classe Macaco
macaco1 = Macaco("Bob")
macaco2 = Macaco("Charlie")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco2.comer("Laranja")
macaco1.comer("Macaco")

macaco1.verBucho()  
macaco2.verBucho()  

macaco1.digerir()
macaco2.digerir()

macaco1.verBucho() 
macaco2.verBucho()    


# Classe Ponto e Retângulo: Faça um programa completo utilizando funções e
# classes que:
# a. Possua uma classe chamada Ponto, com os atributos x e y.
# b. Possua uma classe chamada Retângulo, com os atributos largura e
# altura.
# c. Possua uma função para imprimir os valores da classe Ponto
# d. Possua uma função para encontrar o centro de um Retângulo.
# e. Você deve criar alguns objetos da classe Retângulo.
# f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice
# inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
# g. A função para encontrar o centro do retângulo deve retornar o valor
# para um objeto do tipo ponto que indique os valores de x e y para o centro
# do objeto.
# h. O valor do centro do objeto deve ser mostrado na tela
# i. Crie um menu para alterar os valores do retângulo e imprimir o centro
# deste retângulo.
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Coordenadas do ponto: ({self.x}, {self.y})")


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)


def alterarRetangulo(retangulo):
    novo_x = float(input("Digite a coordenada x do ponto inicial: "))
    novo_y = float(input("Digite a coordenada y do ponto inicial: "))
    nova_largura = float(input("Digite a nova largura do retângulo: "))
    nova_altura = float(input("Digite a nova altura do retângulo: "))

    retangulo.ponto_inicial.x = novo_x
    retangulo.ponto_inicial.y = novo_y
    retangulo.largura = nova_largura
    retangulo.altura = nova_altura

    print("Valores do retângulo alterados com sucesso!")


def imprimirCentro(retangulo):
    centro = retangulo.encontrarCentro()
    centro.imprimir()


# Função para exibir o menu
def exibirMenu():
    print("======= MENU =======")
    print("1. Alterar valores do retângulo")
    print("2. Imprimir centro do retângulo")
    print("3. Sair")
    print("====================")


# Função principal
def main():
    ponto_inicial = Ponto(0, 0)
    retangulo = Retangulo(ponto_inicial, 5, 3)

    while True:
        exibirMenu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            alterarRetangulo(retangulo)
        elif opcao == "2":
            imprimirCentro(retangulo)
        elif opcao == "3":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
    
    
# Classe Bomba de Combustível: Faça um programa completo utilizando
# classes e métodos que:
# a. Possua uma classe chamada bombaCombustível, com no mínimo
# esses atributos:
# i. tipoCombustivel.
# ii. valorLitro
# iii. quantidadeCombustivel
# b. Possua no mínimo esses métodos:

# i. abastecerPorValor( ) – método onde é informado o valor a ser
# abastecido e mostra a quantidade de litros que foi colocada no
# veículo
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em
# litros de combustível e mostra o valor a ser pago pelo cliente.
# iii. alterarValor( ) – altera o valor do litro do combustível.
# iv. alterarCombustivel( ) – altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de
# combustível restante na bomba.

# OBS: Sempre que acontecer um abastecimento é necessário atualizar a
# quantidade de combustível total na bomba

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorLitro
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipoCombustivel}.")
        else:
            print("Não há combustível suficiente na bomba.")

    def abastecerPorLitro(self, litros):
        valor_pagar = litros * self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print(f"Valor a pagar: R$ {valor_pagar:.2f}")
        else:
            print("Não há combustível suficiente na bomba.")

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor
        print("Valor do litro alterado com sucesso.")

    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel
        print("Tipo de combustível alterado com sucesso.")

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade
        print("Quantidade de combustível alterada com sucesso.")


# Exemplo de uso da classe BombaCombustivel
bomba1 = BombaCombustivel("Gasolina", 4.5, 1000)

bomba1.abastecerPorValor(50)  # Saída: Foram abastecidos 11.11 litros de Gasolina.
bomba1.abastecerPorLitro(30)  # Saída: Valor a pagar: R$ 135.00

bomba1.alterarValor(4.8)  # Saída: Valor do litro alterado com sucesso.
bomba1.alterarCombustivel("Etanol")  # Saída: Tipo de combustível alterado com sucesso.
bomba1.alterarQuantidadeCombustivel(1500)  # Saída: Quantidade de combustível alterada com sucesso.