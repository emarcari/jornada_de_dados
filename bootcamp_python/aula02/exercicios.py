import math

# #### Inteiros (`int`)
print('int')
# print(1+2)
# print(3-1)
# print(2*3)
# print(5/4)
# print(5//4) # divisao inteira
# print(6%4) # resto da divisão - modulo 

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
print('Exercicio 1 - Soma de dois números inteiros')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print(num1 + num2)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
print('Exercicio 2 - Resto da divisão por 5')
num = int(input('Digite um número: '))
print(num % 5)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
print('Exercicio 3 - Multiplicação de dois números')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print(num1 * num2)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print('Exercicio 4 - Divisão inteira de dois números')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print(num1 // num2)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
print('Exercicio 5 - Quadrado de um número')
num = int(input('Digite um número: '))
print(num ** 2)

# #### Números de Ponto Flutuante (`float`)
print('float')
# print(1.0+2.4)
# print(3.2-1.0)
# print(2.1*3.0)
# print(5.0/4.0)
# print(5.5**2) # potenciacao

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
print('Exercicio 6 - Adição de dois números flutuantes')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
print(num1 + num2)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
print('Exercicio 7 - Média de dois números flutuantes')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
print((num1 + num2) / 2)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
print('Exercicio 8 - Potência de um número')
base = float(input('Digite a base: '))
expoente = float(input('Digite o expoente: '))
print(base ** expoente)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
print('Exercicio 9 - Conversão de temperatura')
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
print('Exercicio 10 - Área de um círculo')
raio = float(input('Digite o raio do círculo: '))
area = math.pi * (raio ** 2)
print(f'Area do círculo:', '{:.2f}'.format(area))
print(f'Area do círculo: {area:.2f}')

#### Strings (`str`)
# print('str')
# print('Hello World '.upper())
# print('Hello World  '.lower())
# print('Hello World  '.strip())
# print('Hello World  '.split(' '))
# print('Hello' + ' World')

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
print('Exercicio 11 - Conversão para maiúsculas')
st = input('Digite uma string: ')
print(st.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
print('Exercicio 12 - Conversão para minúsculas')
nome = input('Digite seu nome completo: ')
print(nome.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
print('Exercicio 13 - Remoção de espaços em branco')
frase = input('Digite uma frase: ')
print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
print('Exercicio 14 - Separação de data')
data = input('Digite uma data no formato "dd/mm/aaaa": ')
dia, mes, ano = data.split('/')
print(f'Dia: {dia}')
print(f'Mês: {mes}')
print(f'Ano: {ano}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
print('Exercicio 15 - Concatenação de strings')
str1 = input('Digite a primeira string: ')
str2 = input('Digite a segunda string: ')
print(str1 + str2)


# #### Booleanos (`bool`)
# print('bool')
# print(True and False)
# print(True or False)
# print(not False)
# print(1 == 1)
# print(2 != 1)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
print('Exercicio 16 - Operação AND')
exp1 = True
exp2 = False
print(exp1 and exp2)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
print('Exercicio 17 - Operação OR')
print(exp1 or exp2)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
print('Exercicio 18 - Inversão de valor booleano')
exp = True
print(not exp)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
print('Exercicio 19 - Comparação de números')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print(num1 == num2)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
print('Exercicio 20 - Verificação de diferença entre números')
print(num1 != num2)

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação

