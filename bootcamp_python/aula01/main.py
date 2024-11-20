# idade = 47
# nome = "Etore"

# print(idade)

# idade2 = idade + 1
# print(idade2)

# lista = [1,2,3,4,5]
# print(lista)

# lista_invertida = lista.reverse()
# print(lista_invertida)

print("Jornada de Dados")

# Exervicio 1 - Crie um programa que receba o nome do usuário e retorne o número de caracteres
# nome = input("Digite seu nome: ")
# print(len(nome))
# print(len(input("Digite seu nome: ")))

# Exervicio 2 -  Crie um programa onde o usuário digite dois valores e retorne a soma entre eles
# print(int(input("Digite o primeiro valor: ")) + int(input("Digite o segundo valor: ")))

# Tipos primitivos: int, float, str, list, tuple, dict, bool
# Python tem tipagem dinâmica

# Em python TUDO é objeto e estrutura de dados
# numero = 3
# print(type(numero))

# Exercicio 3 - Refac do exercicio 1
# name = input("Digite seu nome: ")
# # characteres = len(name)
# # print(f"Seu nome tem {characteres} caracteres")
# print(f"Seu nome tem {len(name)} caracteres")

# Exercicio 4 - Refac do exercicio 2
# value1 = int(input("Digite o primeiro valor: "))
# value2 = int(input("Digite o segundo valor: "))
# print(f"A soma entre {value1} e {value2} é {value1 + value2}")

# Desafio
CONSTANTE_BONUS = 1000.
# 1) Solicite ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")

# 2) Solicite ao usuário que digite o valor de seu salario
# Converter para float
salario_usuario = float(input("Digite o valor do seu salário: "))

# 3) Solicite ao usuário que digite a porcentagem do bonus recebido
# Converter para float
bonus_usuario = float(input("Digite a porcentagem do bonus recebido: "))

# 4) Calcule o valor do bonus final
bonus_final = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) imprima o cálculo do KPI para o usuário
# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bonus
print(f"O usuario {nome_usuario} tem um salário de R$ {salario_usuario} e um bonus de R$ {bonus_final}")


