"""
A fórmula para calcular a área de uma circunferência é: área = π * raio * raio.
Considerando para este problema que π = 3.14159265: 

Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. 

Entrada: A entrada contém um valor de ponto flutuante (dupla precisão),
no caso, a variável raio.

Saída: Apresente a mensagem "A=" seguido pelo valor da variável area,
conforme exemplo abaixo, com 4 casas após o ponto decimal. 
Utilize variáveis de dupla precisão (double). 
Como em todos os problemas, não esqueça de imprimir o fim de linha após o resultado, 
caso contrário, você receberá "Presentation Error".
"""

# Definição do valor do π
PI = 3.14159265

# Solicitação dos dados ao usuário
raio = float(input("Favor, insira o valor do raio em cm: "))

# Cálculo da área da circunferência
area = PI * (raio ** 2)

# Exibindo o valor para o usuário
print(f"A área da circunferência é: {area:.4f} cm²")