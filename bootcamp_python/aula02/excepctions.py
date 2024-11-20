# # 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# try:
#     print('Exercicio 4 - Divisão inteira de dois números')
#     num1 = int(input('Digite o primeiro número: '))
#     num2 = int(input('Digite o segundo número: '))
#     print(num1 // num2)

# except ValueError:
#     print('Digite apenas números inteiros')
# except ZeroDivisionError:
#     print('Não é possível dividir por zero')
# except Exception as e:
#     print('Ocorreu um erro inesperado: ', e)


# # Exercicio 1 - Crie um programa que receba o nome do usuário e retorne o número de caracteres
# nome = 3
# try:
#     print(len(nome))
# except TypeError as e:
#     print('Erro de tipo:', e)

# except Exception as e:
#     print('Ocorreu um erro inesperado:', e)

# finally:
#     print('Fim do programa')


# numrto = int(input('Digite um número: '))

# if isinstance(numrto, int):
#     print('É um número inteiro')
# else:
#     print('Não é um número inteiro')


idade = 22
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
