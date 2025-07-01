"""
Crie um programa que receba o preço original de um produto e um percentual de desconto,
realizando o cálculo do preço final após a aplicação do desconto.

Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. 

Entrada esperada: preço do produto (exemplo: 250.75) 
e o percentual de desconto (exemplo: 10).
"""
# Definição da função para calcular os descontos
def calcula_desconto (preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return round(preco_final, 2) # retorno para o programa

while True:
    try: 
        # Solicitando os dados para o usuário
        preco_original = float(input("Digite o preço do produto: "))
        desconto = float(input("Digite o percentual do desconto: "))

        # Verificação dos valores sempre positivos
        if preco_original < 0 or desconto < 0:
            print("Erro. O preço e o desconto devem ter valores positivos.")
            continue
        break
    except ValueError:
        print("Por favor, insira um valor númerico.")
        continue

preco_com_desconto = calcula_desconto(preco_original, desconto)        
print(f"O preço final com desconto de {desconto}% é R${preco_com_desconto:.2f}")