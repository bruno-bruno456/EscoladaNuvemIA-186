# Vericando a marioridade com if, else e elif

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 12:
    print("Você é adolescente.")
elif idade >= 4:
    print("Você é criança.")    
else:
    print("Você é um bebê.")