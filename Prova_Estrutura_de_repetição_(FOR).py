inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

soma = 0
tem_par = False   # flag para verificar se existe par

for n in range(inicio, fim + 1):
    if n % 2 == 0:
        soma += n
        tem_par = True
else:
    if not tem_par:
        print("Não há números pares no intervalo.")

print("Soma dos números pares:", soma)
