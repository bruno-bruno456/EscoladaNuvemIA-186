"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido
pelo usuário, utilizando a API ViaCEP. O programa deve exibir o
logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""

import requests

def consultar_cep(cep):
    # URL: viacep.com.br/ws/01001000/json/
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        if "erro" in dados:
            return "CEP não encontrado"

        return f"""
        Logradouro: {dados['logradouro']}
        Bairro: {dados['bairro']}
        Cidade: {dados['localidade']}
        Estado: {dados['uf']} 
        """
    except requests.RequestException as e:
        return f"Erro de consulta {e}"


cep = input("Digite o CEP para consulta (apenas numeros): ")
print("Consultando CEP...")
resultado = consultar_cep(cep)
print(resultado)