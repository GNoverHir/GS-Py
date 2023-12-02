# Criar um dicionário de usuários e senhas
usuarios = {"RM553461@fiap.com.br": "553461", "RM553873@fiap.com.br": "553873", "RM552570@fiap.com.br": "552570"}

# Criar uma lista de exames disponíveis
exames = ["EXAMES PRÉ NATAL", "EXAMES DO SEGUNDO SEMESTRE DE GRAVIDEZ", "EXAMES DO TERCEIRO SEMESTRE DE GRAVIDEZ", "PROCEDIMENTOS INVASIVOS", "TESTES GENÉTICOS PARA GRÁVIDAS"]

# Criar um dicionário de opções para cada exame
opcoes = {
    "EXAMES PRÉ NATAL": ["Ultrassom", "Exame de urina", "Glicemia, Hemograma", "Sorologia para DSTs", "Tipagem sanguínea"],
    "EXAMES DO SEGUNDO SEMESTRE DE GRAVIDEZ": ["Hemograma completo", "Sorologia para HIV", "Reação para toxoplasmose", "Reação para rubéola", "Hepatite B e C e Citomegalovírus", "Urina"],
    "EXAMES DO TERCEIRO SEMESTRE DE GRAVIDEZ": ["Hemograma completo", "VDRL", "Cultura vaginal e retal", "Exame de urina tipo I",],
    "PROCEDIMENTOS INVASIVOS": ["Biópsia de vilo corial", "Amniocentese"],
    "TESTES GENÉTICOS PARA GRÁVIDAS": ["CGH/SNP Array", "Pesquisa de mutação pontual pré-natal", "NGS", "Teste pré-natal por PCR",]
}

# Criar uma função para validar o login do usuário
def login():
    # Pedir o email e a senha do usuário
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")
    # Verificar se o email e a senha estão no dicionário de usuários
    if email in usuarios and senha == usuarios[email]:
        # Se estiverem, retornar True
        return True
    else:
        # Se não estiverem, retornar False
        return False

# Criar uma função para mostrar o menu principal
def menu():
    # Mostrar as opções do menu
    print("Escolha uma das opções abaixo:")
    print("1 - Exames")
    print("2 - Ver exames")
    print("3 - Apagar exames")
    print("4 - Sair do programa")
    # Pedir a escolha do usuário
    escolha = input("Digite o número da opção: ")
    # Retornar a escolha do usuário
    return escolha

# Criar uma função para mostrar os exames disponíveis
def mostrar_exames():
    # Mostrar os exames da lista de exames
    print("Escolha um dos exames abaixo:")
    for i, exame in enumerate(exames):
        print(f"{i+1} - {exame}")
    # Pedir a escolha do usuário
    escolha = input("Digite o número do exame: ")
    # Retornar a escolha do usuário
    return escolha

# Criar uma função para mostrar as opções de cada exame
def mostrar_opcoes(exame):
    # Mostrar as opções do exame escolhido
    print(f"Escolha uma das opções do exame {exame}:")
    for i, opcao in enumerate(opcoes[exame]):
        print(f"{i+1} - {opcao}")
    # Pedir a escolha do usuário
    escolha = input("Digite o número da opção: ")
    # Retornar a escolha do usuário
    return escolha

# Criar uma função para marcar um exame
def marcar_exame():
    # Mostrar os exames disponíveis
    escolha_exame = mostrar_exames()
    # Verificar se a escolha é válida
    if escolha_exame.isdigit() and 1 <= int(escolha_exame) <= len(exames):
        # Converter a escolha em um índice da lista de exames
        indice_exame = int(escolha_exame) - 1
        # Obter o nome do exame escolhido
        exame = exames[indice_exame]
        # Mostrar as opções do exame escolhido
        escolha_opcao = mostrar_opcoes(exame)
        # Verificar se a escolha é válida
        if escolha_opcao.isdigit() and 1 <= int(escolha_opcao) <= len(opcoes[exame]):
            # Converter a escolha em um índice da lista de opções
            indice_opcao = int(escolha_opcao) - 1
            # Obter o nome da opção escolhida
            opcao = opcoes[exame][indice_opcao]
            # Adicionar o exame e a opção escolhidos na lista de exames marcados
            exames_marcados.append((exame, opcao))
            # Mostrar uma mensagem de confirmação
            print(f"Você marcou o exame {exame} com a opção {opcao}.")
        else:
            # Se a escolha não for válida, mostrar uma mensagem de erro
            print("Opção inválida.")
    else:
        # Se a escolha não for válida, mostrar uma mensagem de erro
        print("Exame inválido.")

# Criar uma função para ver os exames marcados
def ver_exames():
    # Verificar se a lista de exames marcados está vazia
    if exames_marcados:
        # Se não estiver, mostrar os exames marcados
        print("Estes são os exames que você marcou:")
        for i, (exame, opcao) in enumerate(exames_marcados):
            print(f"{i+1} - {exame} com a opção {opcao}")
    else:
        # Se estiver, mostrar uma mensagem de aviso
        print("Você não marcou nenhum exame.")

# Criar uma função para apagar um exame marcado
def apagar_exame():
    # Verificar se a lista de exames marcados está vazia
    if exames_marcados:
        # Se não estiver, mostrar os exames marcados
        print("Escolha um dos exames que você marcou para apagar:")
        for i, (exame, opcao) in enumerate(exames_marcados):
            print(f"{i+1} - {exame} com a opção {opcao}")
        # Pedir a escolha do usuário
        escolha = input("Digite o número do exame: ")
        # Verificar se a escolha é válida
        if escolha.isdigit() and 1 <= int(escolha) <= len(exames_marcados):
            # Converter a escolha em um índice da lista de exames marcados
            indice = int(escolha) - 1
            # Obter o exame e a opção escolhidos
            exame, opcao = exames_marcados[indice]
            # Remover o exame e a opção escolhidos da lista de exames marcados
            exames_marcados.pop(indice)
            # Mostrar uma mensagem de confirmação
            print(f"Você apagou o exame {exame} com a opção {opcao}.")
        else:
            # Se a escolha não for válida, mostrar uma mensagem de erro
            print("Exame inválido.")
    else:
        # Se estiver, mostrar uma mensagem de aviso
        print("Você não marcou nenhum exame.")

# Criar uma lista vazia para armazenar os exames marcados
exames_marcados = []

# Criar uma variável para controlar o loop do programa
continuar = True

# Tentar fazer o login do usuário
logado = login()

# Verificar se o login foi bem sucedido
if logado:
    # Se foi, mostrar uma mensagem de boas-vindas
    print("Bem-vindo ao sistema de exames.")
    # Entrar no loop do programa
    while continuar:
        # Mostrar o menu principal
        escolha_menu = menu()
        # Verificar a escolha do usuário
        if escolha_menu == "1":
            # Se for 1, marcar um exame
            marcar_exame()
        elif escolha_menu == "2":
            # Se for 2, ver os exames marcados
            ver_exames()
        elif escolha_menu == "3":
            # Se for 3, apagar um exame marcado
            apagar_exame()
        elif escolha_menu == "4":
            # Se for 4, sair do programa
            continuar = False
            print("Obrigado por usar o sistema de exames. Até logo.")
        else:
            # Se for outra coisa, mostrar uma mensagem de erro
            print("Opção inválida.")
else:
    # Se não foi, mostrar uma mensagem de erro
    print("Login incorreto. Tente novamente.")