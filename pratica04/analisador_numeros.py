def analisador_numeros ():
    pares = 0
    impares = 0

    while True:
        try:
            entrada = input("Digite um número inteiro (ou 'fim para encerrar): ")

            if entrada.lower() == "fim":
                break
            numero = int(entrada)    
            if numero % 2 == 0:
                print(f"O número {numero} é par.")
                pares = pares + 1 # pares += 1
            else:
                print(f"O número {numero} é ímpar.")
                impares += 1 # impares = impares + 1   
        except ValueError:
            print("Valor inválido. Por favor, insira apenas números inteiros.")        

    print(f"""
Resultado Final:
Quantidade de números pares: {pares}
Quantidade de números ímpares: {impares}""")        

analisador_numeros()    