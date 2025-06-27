"""
Crie um programa que solicite a idade do usuário
e classifique-o em uma das seguintes categorias:

Criança (0-12 anos),
Adolescente (13-17 anos),
Adulto (18-59 anos)
Idoso (60 anos ou mais).
"""

idade = int(input("Favor insira sua idade: "))

if idade < 0:
    print("Insira uma idade válida!")
elif idade <= 12:
    print("Você é uma criança.")
elif idade <= 17:         
    print("Você é adolescente.")
elif idade <= 59:
    print("Você é adulto.")    
else:
    print("Você é um idoso.")    