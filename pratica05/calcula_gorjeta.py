"""
Crie uma função que calcule a gorjeta a ser deixada em um restaurante,
baseada no valor total da conta e na porcentagem de gorjeta desejada.

Calcule o valor da gorjeta baseado no total da conta e na porcentagem desejada.

Parâmetros: 
valor_conta (float): O valor total da conta 
porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna: 
float: O valor da gorjeta calculada
"""
# definiu a função calcular gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    # conversão da porcentagem para decimal e multiplicação pelo valor de conta
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    # Arredonda a variável gorjeta e retorna para o programa
    return round(gorjeta, 2)

# captura dos dados através da interação com o usuário
total_conta = float(input("Insira o valor total da conta: "))
porcentagem = float(input("Insira o valor percentual da gorjeta: "))

# chama a função 'calcular_gorjeta' e armazena na variável 'gorjeta' o que ela retorna 
gorjeta = calcular_gorjeta(total_conta, porcentagem)

# exibe esse conteúdo para o usuário
print(f"Para uma conta de R${total_conta:.2f}, a gorjeta de {porcentagem}% é de R$ {gorjeta:.2f}")