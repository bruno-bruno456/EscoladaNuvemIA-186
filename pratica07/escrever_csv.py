"""
Crie um script em Python que escreva dados em um arquivo CSV.
O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.
"""

import csv

def escrever_csv(nome_arquivo,dados):
    with open(nome_arquivo, 'w') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome','Idade','Cidade'])
        for linha in dados:
            escritor.writerow(linha)
    print(f"Dados salvos em {nome_arquivo}")        


dados = [
    ['Ana', 28, 'Rio de Janeiro'],
    ['Pedro', 34, 'São Paulo'],
    ['Maria', 30, 'Salvador']
]

nome_arquivo = input("Digite o nome do arquivo CSV: ")
escrever_csv(nome_arquivo,dados)