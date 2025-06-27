"""
Faça um programa que leia quatro números (N1, N2, N3, N4), 
cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. 
Calcule a média com pesos 2, 3, 4 e 1, respectivamente, 
para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". 

Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". 
Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". 
Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, 
o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame 
obtida pelo aluno. Imprima então a mensagem "Nota do exame: 
" acompanhada pela nota digitada. Recalcule a média 
(some a pontuação do exame com a média anteriormente calculada e divida por 2). 
e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais) 
ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). 

Para estes dois casos (aprovado ou reprovado após ter pego exame) 
apresente na última linha uma mensagem "Media final:
" seguido da média final para esse aluno.

Entrada: A entrada contém quatro números de ponto flutuante correspondentes às 
notas dos alunos.

Saída: Todas as respostas devem ser apresentadas com uma casa decimal. 
As mensagens devem ser impressas conforme a descrição do problema. 
Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá 
"Presentation Error".
"""

# Entrada das notas
N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a quarta nota: "))

# Cálculo da Média  => 2, 3, 4 e 1
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

# Exibição da Média para o Usuário
print(f"Média: {media:.1f}")


if media >= 7.0:
    print("Aluno aprovado")
elif media < 5.0:
    print("Aluno reprovado")   
else:
    print("Aluno em exame")     

    # Solicitar a nota do exame
    exame = float(input("Digite a nota do exame: "))
    print(f"A nota do exame é: {exame:.1f}")

    # Calcular a média final do aluno após o exame
    media_final = (media + exame) / 2

    # Define o status final do aluno
    if media_final >= 5.0:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")    

    print(f"Média final: {media_final:.1f}")    