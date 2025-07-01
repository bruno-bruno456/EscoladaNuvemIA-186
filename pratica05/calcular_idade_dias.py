"""
Crie uma função que calcule a idade de uma pessoa em dias,
baseada no ano de nascimento.
"""

import datetime

# definindo a função
def calcular_idade_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias 

# Input do usuário
ano_nasc = int(input("Digite o ano do seu nascimento: "))

# Calcular o resultado
idade_em_dias = calcular_idade_dias(ano_nasc)

# Exibição ao usuário
print(f"Sua idade aproximada em dias é: {idade_em_dias} dias")