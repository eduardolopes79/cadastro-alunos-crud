from funcoes import (
    alunos, nota_aluno, funcao_menu, cadastrar_aluno, registrar_nota,
    mostrar_alunos, ver_nota, remover_aluno, encerrar_programa
)


while True:

    funcao_menu()
    opcao = int(input("\nEscolha uma opção: "))
    if opcao == 1:
        cadastrar_aluno()

    elif opcao == 2:
        registrar_nota()

    elif opcao == 3:
        mostrar_alunos()

    elif opcao == 4:
        ver_nota()

    elif opcao == 5:
        remover_aluno()

    elif opcao == 6:
        encerrar_programa()
        break

    else:
        print("\nOpção inválida.\n")
