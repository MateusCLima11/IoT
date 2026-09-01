tarefas = []

while True:
    print("\n--- MENU DE TAREFAS ---")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Mostrar tarefas")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tarefa = input("Digite a tarefa a adicionar: ")
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    elif opcao == '2':
        tarefa = input("Digite a tarefa a remover: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print(f"Tarefa '{tarefa}' removida com sucesso!")
        else:
            print("Tarefa não encontrada na lista.")
    elif opcao == '3':
        if tarefas:
            print("\nTarefas cadastradas:")
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t}")
        else:
            print("Nenhuma tarefa cadastrada.")
    elif opcao == '0':
        print("Saindo do sistema... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")