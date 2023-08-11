#atividade um cotacao do dolar
dolar = 3.25
real = 65.00
conversao = real/dolar
print('Meu total em dolares',conversao)

#atividade dois 
celular = 299.99
chaleira = 23.37
gnomo = 66.66
adesivos = 1.42 #unidade
frete = 12.34

totalDolares = celular+chaleira+gnomo+(adesivos*6)+frete
print("total gasto em dolar: ",round(totalDolares))
IOF = 6.38/100

totalReais = (round(totalDolares*dolar,2))
print('total em reais sem IOF: ', totalReais)
#apenas IOF
print('calculo do IOF', round(totalReais*IOF,2))

totalComIOF = totalReais+IOF
print('total com IOF', round(totalComIOF))
