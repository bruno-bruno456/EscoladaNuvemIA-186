"""
Leia 2 valores inteiros e armazene-os nas variáveis A e B. 

Efetue a soma de A e B, atribuindo o seu resultado à variável X. 

Entrada: A entrada contém 2 valores inteiros informados pelo usuário. 

Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha.
"""

# Ler valores do usuário
A = int(input("Por favor, insira o primeiro número: "))
B = int(input("Por favor, insira o segundo número: "))

# Efetuando a soma
X = A + B

# Exibição
print(f"A soma dos valores é: X = {X}")