"""
Desenvolva um programa que calcule o desconto em uma loja. Use as seguintes informações:

Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20% 

O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

"""

# Informações do Produto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Cálculo do desconto e do preço final
valor_desconto = preco_original * (porcentagem_desconto/100)
preco_final = preco_original - valor_desconto

# Exibição dos dados para o usuário
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor de desconto: {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")