#Concatenação de variáveis
x = 8.5
y = 'Marcos'

print('A média de ', y, ' foi: ', x)

#Comparando true e false
a = 1
b = 5

#resposta irá retornar False, pois a não é igual  (==) a b.
resposta = a == b

#r2 irá retornar true, pois a é diferente (!=) de b.
r2 = a != b
print(resposta, r2)

#Manipulação de String
frase = 'Olá, mundo'

#o print retornará apenas  o primeiro caractere da frase, ou seja : "O"
print(frase[1])
#Concatenação de string:
s1 = 'Lógica de programação'
s1 = s1 + ' e Algoritmos'
#o print abaixo retornará "Lógica de programação e algoritmos".
print(s1)

s2 = 'A' + '-' * 10 + 'B'
#O print abaixo retornará o string '-' multiplicado em 10x, ou seja: "A-------B".
print(s2)

#Concatenando string com variavel
nota = 8.5
# o %f irá retornar a variavel no final da variavel.
s3 = 'Você tirou %f na disciplina de Algoritmos' % nota
#Irá retornar com todas as casas decimais, ou seja, 8.50000
print (s3)

#Limitando casas decimais
s3 = 'Você tirou %.2f na disciplina de algoritmos' %nota

#Concatenação de string e variaveis
nota2 = 7
disc = 'Lógica de programação'
#Entre parenteses, sempre colocar em ordem as variáveis, ou
#seja, a primeira foi a nota e a segunda a disciplina
s4 = 'Você tirou %.2f na disciplina de %s' % (nota2, disc)
print(s4)
#Os tipos para delimitar as variaveis em % são:
# Inteiros: %d ou %i
# Float: %f
# String: %s

#Forma moderna de concatenação !!!USAR ESSA!!!

s5 = 'Você tirou {} na disciplina de {}.' .format(nota, disc)
print (s5)

#Pegar fatiamento de strings, ou seja: quero apenas os 6 primeiros caracteres:

s6 = 'Lógica de programação e algoritmos'

#Esse processo nos traz os 6 primeiros caracteres da variavel s6
#Ou seja, nos retorna "Lógica".
print(s6[0:6])

#Esse nos traz apenas "Algoritmos", pois nos retorna os caracteres de 24 à 34.
print(s6[24:34])

#Esse nos traz tudo até o 6 caractere.
print(s6[:6])

#E esse nos traz tudo após o caractere 24.
print(s6[24:])

#Para saber o tamanho de uma string, usamos o len
tamanho = len(s6)

#Nos retorna a quantidade de caracteres da variavel s6.
print(tamanho)

