alunos = []
nota_aluno = {}

def funcao_menu():
    menu = {
        1 : 'Cadastrar Aluno',
        2 : 'Adicionar Notas',
        3 : 'Listar Alunos',
        4 : 'Verificar Notas',
        5 : 'Remover Aluno',
        6 : 'Sair'
    }
    for k, i in menu.items():
        print(f"{k}, {i}")

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ").strip().title()
    alunos.append(nome)
    nota_aluno[nome] = []
    print("Aluno cadastrado.")

def registrar_nota():
    atribuir_nota = input("Digite o nome do aluno para atribuir nota: ")
    if atribuir_nota not in alunos:
        print("Esse aluno não está cadastrado.")

    else:
        notas = int(input("Digite a nota do aluno: "))

        if notas < 0 or notas > 10:
            print("\nNota inválida")

        else:
            nota_aluno[atribuir_nota] = [notas]
            print(f"A nota {notas} foi adicionada pro aluno {atribuir_nota}.")

def mostrar_alunos():
    alunos.sort()
    print(f"\n{alunos}\n")

def ver_nota():
    verificar_nota = input("Digite o nome do aluno: ")
    if verificar_nota not in nota_aluno:
        print("Esse aluno não foi cadastrado.")
    else:
        print(f"\n{nota_aluno}\n")

def remover_aluno():
    remover_aluno = input("Digite o nome do aluno que deseja remover: ")
    if remover_aluno not in alunos:
        print("\nEsse aluno não está cadastrado\n")
    else:
        alunos.remove(remover_aluno)
        del nota_aluno[remover_aluno]
        print(f"\nO aluno {remover_aluno} foi removido.\n")

def encerrar_programa():
    print("\nPrograma encerrado.")

