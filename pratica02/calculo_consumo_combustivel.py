"""
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

Distância percorrida: 300 km
Combustível gasto: 25 litros 

O programa deve calcular o consumo médio (km/l) e 
exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

# Cálculo do consumo de combutível

# Dados da viagem
distancia_percorrida = 300 # Em km
combustivel_gasto = 25 # Em litros

# Cálculo do consumo médio
consumo = distancia_percorrida / combustivel_gasto

# Exibição para o usuário
print("Dados da viagem:")
print("Distância percorrida: ", distancia_percorrida, "km")
print("Combustível gasto: ", combustivel_gasto, "litros")
print(f"Consumo médio: {consumo:.2f} km/l")
