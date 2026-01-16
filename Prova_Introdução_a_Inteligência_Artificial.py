qtd_alunos = int(input("Digite a quantidade de alunos: "))

soma_medias_turma = 0  # para calcular a média geral

for i in range(qtd_alunos):
    print(f"\nAluno {i+1}:")
    nome = input("Nome do aluno: ")

    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))

    media = (n1 + n2 + n3) / 3
    soma_medias_turma += media

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"\nAluno: {nome}")
    print(f"Notas: {n1}, {n2}, {n3}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

media_turma = soma_medias_turma / qtd_alunos
print(f"\nMédia geral da turma: {media_turma:.2f}")
