#comando de entrada de dados ja diretamente para a variavel
idade = input('informe sua idade: ')
peso = input('informe seu peso: ')
horas = input('horas dormidas: ')

if int(idade) > 16 and int(idade) <= 68 and int(peso) > 50 and int(horas) == 6:
    print('voce pode doar sangue')
else:
    print('voce nao pode doar sangue')
    

#estrtutura condicional
'''
if  int(idade) >= 12:
    print('você é maior de idade')
else:
    print('você é menor de idade')
    
#estrutura de repeticao
for n in range(3):
    print(n)
'''
#estrutura de repeticao com while
'''i = 0
while i < len('testando'):
    print(i)
    i += 1
'''   
#ultilizando operador ternario, no Python é conhecido como Expressão Condicional
a = input('informe um numero: ')
b = input('informe outro numero: ')
print ("a é maior" if a > b else "b e maior")

#converter sempre por que em python tudo é string
n1 = int (input('digite um numero: '))
n2 = int(input('digite outro numero: '))
soma = n1+n2
if int(soma) >= 20:
    print(int(soma)+8)
else:
    print(int(soma)-5)
    
#estruturas de repeticao
numero = int(input('digite algum numero: '))
acumulador =int(0)
while numero != 0:
    numero = int(input('digite algum numero: '))
    acumulador= int(numero+acumulador)
    aux = input('deseja finalizar? ')
    if aux == 'sim':
        print(acumulador)
        break
      