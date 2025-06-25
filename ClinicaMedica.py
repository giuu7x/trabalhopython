# Clínica Médica - Sistema Simples em Python

# Lista para armazenar os pacientes
pacientes = []

# Função para mostrar o menu
def mostrar_menu():
    print("\n--- MENU CLÍNICA MÉDICA ---")
    print("1. Cadastrar paciente")
    print("2. Visualizar fichas (visão do médico)")
    print("3. Sair")

# Função para cadastrar um paciente
def cadastrar_paciente():
    print("\n--- CADASTRO DE PACIENTE ---")
    nome = input("Nome completo: ")
    idade = input("Idade: ")
    genero = input("Gênero (M/F/Outro): ")
    sintomas = input("Informe os sintomas relatados: ")

    paciente = {
        "nome": nome,
        "idade": idade,
        "gênero": genero,
        "sintomas": sintomas
    }

    pacientes.append(paciente)
    print(" Paciente cadastrado com sucesso!")

# Função para visualizar fichas dos pacientes
def visualizar_fichas():
    print("\n--- FICHAS DOS PACIENTES ---")
    if not pacientes:
        print(" Nenhum paciente cadastrado.")
    else:
        for idx, p in enumerate(pacientes, start=1):
            print(f"\nPaciente {idx}")
            print(f"Nome: {p['nome']}")
            print(f"Idade: {p['idade']}")
            print(f"Gênero: {p['gênero']}")
            print(f"Sintomas: {p['sintomas']}")

# Função principal
def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_paciente()
        elif escolha == '2':
            visualizar_fichas()
        elif escolha == '3':
            print(" Encerrando o sistema. Obrigado!")
            break
        else:
            print(" Opção inválida. Tente novamente.")

# Executa o programa
main()
