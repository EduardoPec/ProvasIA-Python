tarefas = []

def menu():

    while True:
        print("====================================")
        print("       Gerenciador de Tarefas       ")
        print("====================================")
        print("1 - Adicionar Tarefas")
        print("2 - Listar Tarefas")
        print("3 - Marcar Tarefas como Concluidas")
        print("4 - Exibir Tarefas por Prioridades")
        print("0 - Encerrar Gerenciador")

        opcao = int(input("Escolha a opção desejada: "))

        if opcao == 0:
            print("ENCERRANDO GERENCIADOR!")
            break
        elif opcao == 1:
            adicionar_tarefas()
        elif opcao == 2:
            listar_tarefas()
        elif opcao == 3:
            marcar_tarefas_concluidas()
        elif opcao == 4:
            exibir_prioridades()
        else:
            print("OPÇÃO INVÁLIDA!") 

def adicionar_tarefas():

    nome = input("Informe o nome da tarefa: ").lower()
    descricao = input("Informe a descrição da tarefa: ").lower()
    prioridade = input("Informe a prioridade da tarefa(alta, média ou baixa): ").lower()

    if nome == "":
        print("O NOME DA TAREFA NÃO PODE SER VAZIO!")
        return
    
    tarefa = {
        "nome": nome,
        "descrição": descricao,
        "prioridade": prioridade,
        "status": False
        }
    
    tarefas.append(tarefa)
    print(f"TAREFA {nome} ADICIONADA COM SUCESSO!") 

def listar_tarefas():
    
     if len(tarefas) == 0:
        print("NÃO HÁ TAREFAS CADASTRADAS!")
     else:
        print("--------- Lista de Tarefas ---------")
        for tarefa in tarefas:
            status = ("Concluído" if tarefa['status'] == True else "Pendente").lower()
            print(f"Nome: {tarefa['nome']}")
            print(f"Descrição: {tarefa['descrição']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Status: {status}")
            print("------------------------------------")
    
def marcar_tarefas_concluidas():
    
    tarefa_escolhida = input("Informe o nome da tarefa que deseja marcar como concluida: ").lower()

    if tarefa_escolhida not in [tarefa['nome'] for tarefa in tarefas]:
        print("TAREFA NÃO ENCONTRADA!")

    for tarefa in tarefas:
        if tarefa['nome'] == tarefa_escolhida:
            if tarefa['status']:
                print(f"A TAREFA {tarefa_escolhida} JÁ ESTÁ MARCADA COMO CONCLUÍDA!")
            else:
                tarefa['status'] = True
                print(f"TAREFA {tarefa_escolhida} MARCADA COMO CONCLUÍDA!")
            break

def exibir_prioridades():

    prioridade_escolhida = input("Informe a prioridade desejada (alta, média ou baixa): ").lower()

    if prioridade_escolhida not in ["alta", "media", "baixa"]:
        print("PRIORIDADE INVÁLIDA! USE (ALTA, MEDIA OU BAIXA), A TAREFA PRECISA TER SIDO CRIADA!")
        return

    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['prioridade'] == prioridade_escolhida]

    if not tarefas_filtradas:
        print(f"NÃO HÁ TAREFAS COM PRIORIDADE {prioridade_escolhida}!")

    for tarefa in tarefas_filtradas:
            status = ("Concluído" if tarefa['status'] == True else "Pendente").lower()
            print(f"--------- Lista de Tarefas por Prioridade {prioridade_escolhida} ---------")
            print(f"Nome: {tarefa['nome']}")
            print(f"Descrição: {tarefa['descrição']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Status: {status}")
            print("--------------------------------------------------------")

menu()

