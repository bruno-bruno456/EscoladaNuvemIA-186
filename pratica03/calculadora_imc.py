"""
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso" 
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
 Para os demais cenários: classificacao = "Obeso"

 IMC = peso / (altura ** 2)
 """

# Solicitação dos dados
peso = float(input("Digite seu peso em quilogramas (Kg): "))
altura = float(input("Digite sua altura em metros (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Categorização do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"  
else:
    classificacao = "Obeso"      

# Exibição do resultado para o usuário
print(f"""
Seu IMC é {imc:.1f}
Classificação: {classificacao}
""")    