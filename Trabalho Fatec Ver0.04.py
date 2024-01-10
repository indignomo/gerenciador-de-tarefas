import time
import os

#Função Menu
def menu():
    print("Gerenciador de Listas de Tarefas")
    print(10 * "*")
    print("1 - Incluir nova lista de tarefas\n"
          "2 - Selecionar lista de tarefas\n"
          "3 - Adicionar tarefa na lista atual\n"
          "4 - Ver lista de tarefas\n"
          "5 - Excluir tarefa\n"
          "6 - Excluir lista de tarefas\n"
          "7 - Sair\n"
          "0 - Voltar\n")
    print(10 * "*")

# Dicionário para armazenar múltiplas listas de tarefas
listasDeTarefas = {}

# Variável para armazenar o nome da lista atual
listaAtual = None

# Variável booleana para encerrar o programa
encerrarPrograma = False

#Enquanto NÃO se tratar do Laço de encerramento do programa
while not encerrarPrograma:
    menu()
    entrada = input("\nDigite a opção desejada: ")
#Comandos SE
    if entrada == "0":
        print("Selecione uma opção para poder voltar!\n")
    
    if not entrada.isdigit():
        print("\nDigite somente números para escolher a opção!\n")
        continue
    
    opcaoDoMenu = int(entrada)

    if opcaoDoMenu == 1:
        os.system('cls')
        print ('Carregando...')
        time.sleep(2)
        nomeLista = input("Digite o nome da nova lista de tarefas: ")
        if nomeLista == "0":

                continue
        listasDeTarefas[nomeLista] = []  # Cria uma nova lista vazia com o nome especificado
        print(f"Lista de tarefas '{nomeLista}' criada!\n",)
        time.sleep(1)
        print("Voltando ao MENU")
        time.sleep(2)
        
        

    elif opcaoDoMenu == 2:
        os.system('cls')
        print ('Carregando...')
        time.sleep (2)
        print("Opção escolhida: 2 - Selecionar lista de tarefas\n")
        print("Listas disponíveis:\n")
        for idx, lista in enumerate(listasDeTarefas, 1):
            print(f"{idx}. {lista}\n")

        entrada_lista = input("Digite o número da lista de tarefas desejada: ")
        if entrada_lista == "0":
                print("Voltando ao MENU")
                continue
        time.sleep(2)
        if not entrada_lista.isdigit():
            print("\nDigite somente números para escolher a lista desejada!")
            time.sleep(3)
            continue
        
        
        idxLista = int(entrada_lista)

        if 1 <= idxLista <= len(listasDeTarefas):
            listaAtual = list(listasDeTarefas.keys())[idxLista - 1]
            print(f"Lista '{listaAtual}' selecionada.\n")
            time.sleep(1)
            print("Voltando ao MENU")
            time.sleep(2)
        else:
            print("Número de lista inválido.\n")
            time.sleep(1)
            print("Voltando ao MENU")
            time.sleep (2)

       

    elif opcaoDoMenu == 3:
        os.system('cls')
        print ('Carregando...')
        time.sleep (2)
        if listaAtual:
            print(f"Opção escolhida: 3 - Adicionar tarefa na lista '{listaAtual}'\n")
            tarefa = input("Digite a tarefa a ser incluída: ")
            if tarefa == "0":
                print("Voltando ao MENU")
                time.sleep (2)
                continue
            listasDeTarefas[listaAtual].append(tarefa)
            print(f"Tarefa '{tarefa}' adicionada à lista '{listaAtual}'.\n")
            time.sleep (2)
            print('Voltando ao MENU')
            time.sleep(2)
        else:
            print("Por favor, selecione uma lista de tarefas primeiro.\n")
            time.sleep (1.5)
            print('Voltando ao MENU')
            time.sleep (2)

    elif opcaoDoMenu == 4:
        os.system('cls')
        print ('Carregando...')
        time.sleep (2)
        if listaAtual:
            print(f"Opção escolhida: 4 - Ver lista de tarefas '{listaAtual}'\n")
            print(f"Lista de tarefas '{listaAtual}':")
            for idx, tarefa in enumerate(listasDeTarefas[listaAtual], 1):
                print(f"{idx}. {tarefa}")
            time.sleep(5)
            print('Voltando ao MENU')
            time.sleep (2)

        else:
            print("Por favor, selecione uma lista de tarefas primeiro.\n")
            time.sleep(1)
            print('Voltando ao MENU')
            time.sleep (2)

    elif opcaoDoMenu == 5:
        os.system('cls')
        print ('Carregando...')
        time.sleep (2)
        if listaAtual:
            print(f"Opção escolhida: 5 - Excluir tarefa da lista '{listaAtual}'\n")
            if listasDeTarefas[listaAtual]:
                print("Tarefas disponíveis:")
                for idx, tarefa in enumerate(listasDeTarefas[listaAtual], 1):
                    print(f"{idx}. {tarefa}")

                entrada_tarefa = input("Digite o número da tarefa a ser removida: ")
                if entrada_tarefa == "0":
                    print("Voltando ao MENU")
                    continue
                if not entrada_tarefa.isdigit():
                    print("\nDigite somente números para escolher a lista a ser excluída.")
                    continue
                
                idxTarefa = int(entrada_tarefa)
                if 1 <= idxTarefa <= len(listasDeTarefas[listaAtual]):
                    tarefaRemovida = listasDeTarefas[listaAtual].pop(idxTarefa - 1)
                    time.sleep(0.5)
                    print(f"Tarefa '{tarefaRemovida}' removida da lista '{listaAtual}'.\n")
                    time.sleep(1.5)
                else:
                    print("Número de tarefa inválido.\n")
            else:
                print("A lista de tarefas está vazia.\n")
        else:
            print("Por favor, selecione uma lista de tarefas primeiro.\n")

    elif opcaoDoMenu == 6:
        os.system('cls')
        print ('Carregando...')
        time.sleep (2)
        print("Opção escolhida: 6 - Excluir lista de tarefas\n")
        print("Listas disponíveis para exclusão:")
        for idx, lista in enumerate(listasDeTarefas, 1):
            print(f"{idx}. {lista}")

        entrada_lista = input("Digite o número da lista de tarefas a ser excluída: ")

        if entrada_lista == "0":
                print("Voltando ao MENU")
                time.sleep(2)
                continue
        if not entrada_lista.isdigit():
            print("\nDigite somente números para escolher a lista a ser excluída.")
            time.sleep(1)
            print('Voltando ao MENU')
            time.sleep (2)
            continue
        
        idxLista = int(entrada_lista)
        if 1 <= idxLista <= len(listasDeTarefas):
            listaExcluir = list(listasDeTarefas.keys())[idxLista - 1]
            del listasDeTarefas[listaExcluir]
            print(f"Lista '{listaExcluir}' excluída.\n")
            time.sleep(1)
            print('Voltando ao MENU')
            time.sleep (2)
        else:
            print("Número de lista inválido.\n")
            time.sleep(1)
            print('Voltando ao MENU')
            time.sleep (2)

    elif opcaoDoMenu == 7:
        os.system('cls')
        #Enquanto de encerramento do sistema
        while True:
            print("Opção escolhida: 7 - Sair\n")
            sair = input("Deseja sair? S/N\n").upper()
            if sair == "S" or sair == "SIM":
                encerrarPrograma = True
                break
            elif sair == "N" or sair == "NAO":
                break
            else:
                print("Valor incorreto. Tente novamente.\n")
    else:
        print("\nPor favor digite outro número!\n")