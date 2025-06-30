notas = []
while True:
    try:    
        entrada = input("Digite a nota do aluno (ou fim para encerrar): ")
        if entrada == 'fim':
            break
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Por favor, digite uma nota válida entre 0 e 10.")
    except ValueError:
        print("Nota inválida. Digite um valor entre 0 e 10.")       

if notas:
    media = sum(notas) / len(notas)
    print(f"""A média da turma: {media:.2f}
O total de notas registradas é: {len(notas)}""")            
else:
    print("Nenhuma nota foi registrada.")    


