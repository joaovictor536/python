usuario_correto = "admin"
senha_correta = "1234"

logado = False   # flag para saber se conseguiu logar

for tentativa in range(3):
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("\nLogin realizado com sucesso! Bem-vindo 👋")
        logado = True
        break
    else:
        restantes = 2 - tentativa
        if restantes > 0:
            print(f"Credenciais incorretas. Você ainda tem {restantes} tentativa(s).\n")

# Se não conseguiu logar:
if not logado:
    for i in range(3):
        print("Acesso bloqueado")
