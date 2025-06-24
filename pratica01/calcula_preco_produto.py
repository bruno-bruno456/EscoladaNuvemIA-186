"""
Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 

O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

# Esse código tem objetivo de calcular o preço total de um produto

# Variáveis com detalhes do produto
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

# Variável com o cálculo do valor toral
preco_total = quantidade * preco_unitario

# Exibição das informações do produto e do valor total
print(f"Produto: {nome_produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço total: R$ {preco_total:.2f}")


# :.2f => seja exibido duas casas decimais, como utilizamos em representação monetária.