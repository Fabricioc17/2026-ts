# Arquivo: 01b-debug.py
# ATENÇÃO: Este código continha 4 erros propositais. Todos foram corrigidos abaixo!

nome = input("Digite o nome do aluno: ") # 1.imput para input
nota1 = float(input("Digite a nota 1: ")) # 2. notal para nota1
nota2 = float(input("Digite a nota 2: "))

# 3. Adicionado parênteses 
media = (nota1 + nota2) / 2 

if media >= 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# 4. pront para print
print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")
