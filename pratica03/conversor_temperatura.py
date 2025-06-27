"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura,
a unidade de origem e a unidade para qual deseja converter.

Celsius para Fahrenheit: °F = (°C * 1.8) + 32
Fahrenheit para Celsius: °C = (°F - 32) / 1.8
Celsius para Kelvin: K = °C + 273.15
Kelvin para Celsius: °C = K - 273.15 
Fahrenheit para kelvin K = (5/9 x (ºF - 32)) + 273,15
Kelvin para Fahrenheit: F = (1.8 x (k -273.15) +32) 
"""

# Solicitar a temperatura ao usuário
temperatura = float(input("Digite a temperatura: "))

# Fornecer as escalas
origem = input("Insira a unidade de origem (C, F, K): ").upper()
destino = input("Insira a unidade de destino (C, F, K): ").upper()

# Conversão da temperatura
# Escala de origem é a mesma do destino
if origem == destino:
    resultado = temperatura

# Conversão quando a origem for Celsius (C)
elif origem == "C":
    if destino == "F": # origem C, destino F
        resultado = (temperatura * 1.8) + 32
    else:  # origem C, destino K
        resultado = temperatura + 273.15

# Conversão quando a origem for Fahrenheit (F)
elif origem == "F":
    if destino == "C": # origem F, destino C
        resultado = (temperatura - 32) / 1.8
    else: # origem F, destino K
        resultado = ((temperatura - 32 ) * 1.8) + 273.15

# Conversão quando a origem for Kelvin (K)
else:
    if destino == "C":
        resultado = temperatura - 273.15
    else:
        resultado = ((temperatura - 273.15) * 1.8) + 32
    

# Exibição da conversão
print(f"{temperatura} {origem} é igual a {resultado:.1f} {destino}")    