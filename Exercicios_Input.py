#Armazenando dados em variaveis com input

idade = input('Qual sua idade?')

#Ao printar, o usuário terá que retornar com a idade dele na linha de comando, que logo
#após, retornará o que o usuario digitou.
print(idade)

#Concatenando com variaveis de entrada
nome = input('Qual seu nome? ')

#O print irá retornar "Olá, (nome que veio do input), seja bem vindo!
print('Olá {}, seja bem vindo!' .format(nome))

#O input sempre retornará uma string, para retornar float ou string, precisamos
#converter o input, assim:

nota = float(input('Qual sua nota? '))
print('Você tirou {} ' .format(nota))

#Exercicio 1 : Ler 2 valores e printar a soma dos valores.
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

res = 'O resultado da soma de {} com {} é: {} ' .format(x,y, x+y)
print(res)

#Exercicio 2: algoritmo que solicite ao usuário uma quantidade de dias, de horas,
#de minutos e de segundos. Calcule o total de segundos resultante e imprima na tela para o usuário.

dia = int(input('Quantos dias? '))
hora = int(input('Quantas horas?'))
min = int(input('Quantos minutos? '))
seg = int(input('Quantos segundos? '))

total = seg + (min * 60) + (hora * 60 * 60) + (dia * 24 * 60 * 60)
resposta = 'O total de segundos é: {}' .format(total)
print(resposta)

#Exercicio 3: Preço de produto e percentual de desconto, mostrar o preço final do produto.
preco = float(input('Qual o preço do produto? '))
desc = float(input('Qual o desconto de 0 a 100? '))
pdesc = preco * (desc / 100)
fim = preco - pdesc


pfinal = 'O preço final do produto com o desconto de {}% é de: {}R$ ' .format(desc, fim)

print(pfinal)

#Exercicio 4: Transformar temperatura em Celsius para Fahrenheit
tc = float(input('Qual a temperatura em Celsius? '))
tf = (9 * tc) / 5 + 32

print ('Temperatura em Celsius: {}ºC. Fahrenheit: {}ºF' .format(tc, tf))








