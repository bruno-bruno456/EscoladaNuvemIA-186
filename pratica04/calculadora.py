"""
Desenvolva uma calculadora em Python que realize as quatro operações básicas
(adição, subtração, multiplicação e divisão) entre dois números. 
A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. 
Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
Trate os seguintes erros:

Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida

Use try/except para capturar e tratar os erros apropriadamente.
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
"""
def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == "+":
                resultado = num1 + num2 
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2 
            elif operacao == "/":
                resultado = num1 / num2
            else:
                raise ValueError("Operação Inválida")
            print(resultado)
            break
        except ValueError as e:
            print(f"Erro {e}. Por favor, tente novamente.")
        except ZeroDivisionError:
            print("Erro: divisão por zero não é permitida. Por favor, tente novamente.")        

calculadora()            