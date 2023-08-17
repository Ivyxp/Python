def linha():
    print ('--------------------------------------------------------------------------------------------------')
 
 
# 1) Crie um dicionário d e coloque nele seus dados: nome, idade,
# telefone,endereço. Usando o dicionário d criado anteriormente, imprima
# seu nome.
linha()
dados = {'nome': 'ivy', 'idade': 20, 'telefone':'4002-8922', 'endereço': 'centro'}
print(dados)
linha()
# 2) Crie um dicionário d e coloque nele os dados fornecidos pelo usuário:
# nome, idade, telefone,endereço. Também usando d, imprima todos os
# itens do dicionário no formato chave : valor, ordenado pela chave
linha()
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
telefone = input('Digite seu telefone: ')
endereço = input('Digite seu endereço: ')
 
d = {'nome': nome, 'idade': idade, 'telefone': telefone, 'endereço': endereço}
print (d)
linha()
 
# 3) Crie um dicionário que é uma agenda e coloque nele os seguintes dados:
# chave (cpf), nome, idade, telefone. O programa deve ler um número
# indeterminado de dados, criar a agenda e imprimir todos os itens do
# dicionário no formato chave: nome-idade fone.
agenda =  {}
op = '1'
while op == '1':
 cpf = input('cpf: ')
 name = input('nome: ')
 age = input('idade: ')
 tel = input('telefone: ')
 linha()
 agenda[cpf] = {
    'nome': name,
    'idade':age,
    'telefone':tel
}
 op = input('deseja continuar? 1[sim] 2[nao]: ')
 
#printando os dados da agenda
for cpf, valor in agenda.items():
    print(cpf, valor['nome'], valor['idade'], valor['telefone'])
    linha()
   
# 4) Crie um programa que cadastre informações de várias pessoas (nome,
# idade e cpf) e depois coloque em um dicionário. Depois remova todas as
# pessoas menores de 18 anos do dicionário e coloque em outro dicionário.
# Criação de uma lista de dicionários para armazenar as informações das pessoas
pessoas = []

# Loop para cadastrar as informações das pessoas
while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    idade = int(input("Digite a idade da pessoa: "))
    cpf = input("Digite o CPF da pessoa: ")
    pessoa = {'nome': nome, 'idade': idade, 'cpf': cpf}
    pessoas.append(pessoa)

# Criação de dicionários para armazenar pessoas maiores e menores de 18 anos
maiores_de_18 = []
menores_de_18 = []

# Separando as pessoas maiores e menores de 18 anos
for pessoa in pessoas:
    if pessoa['idade'] >= 18:
        maiores_de_18.append(pessoa)
    else:
        menores_de_18.append(pessoa)

# Exibindo as informações das pessoas maiores de 18 anos
print("\nPessoas maiores de 18 anos:")
for pessoa in maiores_de_18:
    print(pessoa)

# Exibindo as informações das pessoas menores de 18 anos
print("\nPessoas menores de 18 anos: \n")
for pessoa in menores_de_18:
    print(pessoa)

#5) Considere um sistema onde os dados são armazenados em dicionários. 

#Nesse sistema existe um dicionario principal e o dicionário de backup. 

#Cada vez que o dicionário principal atinge tamanho 5, ele imprime os 

#dados na tela e apaga o seu conteúdo. Crie um programa que insira dados 

#em um dicionário, realizando o backup a cada dado e excluindo os dados 

#do dicionário principal quando ele atingir tamanho 5.

def principal():
    principal_dic = {}
    backup_dic = {}
    cc= 1
    
    while True:
        data = input("Insira um dado: ")
        principal_dic[cc] = data
        backup_dic[cc] = data
        
        if len(principal_dic) == 5:
            print("Dicionário principal:")
            print(principal_dic)
            principal_dic.clear()
            
            print("Backup:")
            print(backup_dic)
            
        cc+= 1

if __name__ == "__principal__":
    principal()
    

#6) Escreva uma função que conta a quantidade de vogais em um texto e 

#armazena tal quantidade em um dicionário, onde a chave é a vogal 

#considerada

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    vogais_contagem = {}
    
    for letra in texto:
        if letra in vogais:
            if letra in vogais_contagem:
                vogais_contagem[letra] += 1
            else:
                vogais_contagem[letra] = 1
    
    return vogais_contagem

texto = "Escreva uma função que conta a quantidade de vogais"
resultado = contar_vogais(texto)
print(resultado)

#7) Escreva um programa que lê duas notas de vários alunos e armazena tais

#notas em um dicionário, onde a chave é o nome do aluno. A entrada de 

#dados deve terminar quando for lida uma string vazia como nome. 

#Escreva uma função que retorna a média do aluno, dado seu nome

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def main():
    alunos = {}
    
    while True:
        nome = input("Digite o nome do aluno (ou vazio para sair): ")
        if nome == "":
            break
        
        notas_str = input(f"Digite as notas de {nome} separadas por espaço: ")
        notas = [float(nota) for nota in notas_str.split()]
        
        alunos[nome] = notas
    
    nome_busca = input("Digite o nome do aluno para calcular a média: ")
    if nome_busca in alunos:
        media = calcular_media(alunos[nome_busca])
        print(f"A média de {nome_busca} é: {media:.2f}")
    else:
        print(f"Aluno {nome_busca} não encontrado.")

if __name__ == "__main__":
    main()


#8) Uma pista de Kart permite 10 voltas para cada um de 6 corredores. 

#Escreva um programa que leia todos os tempos em segundos e os guarde 

#em um dicionário, onde a chave é o nome do corredor. Ao final diga de 

#quem foi a melhor volta da prova e em que volta; e ainda a classificação 

#final em ordem (1o o campeão). O campeão é o que tem a menor média 

#de tempos.
def calcularMediaTempos(tempos):
    soma = sum(tempos)
    media = soma / len(tempos)
    return media

corredores = ["Corredor1", "Corredor2", "Corredor3", "Corredor4", "Corredor5", "Corredor6"]
tempos_por_corredor = {}

for corredor in corredores:
    tempos = []
    for volta in range(1, 11):
        tempo = float(input(f"Digite o tempo em segundos da volta {volta} para o corredor {corredor}: "))
        tempos.append(tempo)
    tempos_por_corredor[corredor] = tempos

melhor_volta = float("inf")
nome_melhor_volta = ""
volta_melhor_volta = 0

for corredor, tempos in tempos_por_corredor.items():
    for volta, tempo in enumerate(tempos, start=1):
        if tempo < melhor_volta:
            melhor_volta = tempo
            nome_melhor_volta = corredor
            volta_melhor_volta = volta

classificacao = sorted(corredores, key=lambda corredor: calcularMediaTempos(tempos_por_corredor[corredor]))

print("Melhor volta:", nome_melhor_volta, "na volta", volta_melhor_volta)
print("Classificação:")
for posicao, corredor in enumerate(classificacao, start=1):
    print(f"{posicao}° lugar:", corredor)

