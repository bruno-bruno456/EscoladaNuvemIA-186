"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação).
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

Exemplo de palíndromo:
Ana 
Arara
A cara rajada da jararaca
"""

def verifica_palindromo(texto):
    # Remover espaços e converter para minúsculo
    texto_limpo = ''.join(char.lower() 
                          for char in texto 
                          if char.isalnum())
    # Retorna o texto comparado com a sua versão invertida
    return texto_limpo == texto_limpo[::-1]

frase = input("Verificação do palíndromo: ")
resultado = verifica_palindromo(frase)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"O texto '{frase}' é um palíndromo? {resposta}.")        