# Gerenciador de Tarefas

Um gerenciador de listas de tarefas em Python para organização pessoal, permitindo criar múltiplas listas e gerenciar tarefas individualmente.

## 📋 Descrição

Este programa oferece uma interface CLI (Command Line Interface) para gerenciar múltiplas listas de tarefas. Ideal para organizar diferentes projetos ou categorias de atividades em listas separadas.

## ✨ Funcionalidades

- **Criar novas listas**  
  Organize tarefas em listas independentes (ex: "Estudos", "Compras")
  
- **Selecionar lista ativa**  
  Escolha qual lista deseja manipular no momento

- **Adicionar/Visualizar tarefas**  
  Gerencie itens individualmente dentro de cada lista

- **Exclusão granular**  
  Remova tarefas específicas ou listas inteiras

- **Interface amigável**  
  Menu interativo com feedback visual e operações confirmadas

## ⚙️ Instalação

1. Certifique-se de ter Python 3.x instalado
2. Clone o repositório ou faça download do arquivo `task_manager.py`

```bash
git clone https://github.com/seu-usuario/task-manager.git
```

## 🚀 Como Usar

Execute o programa:
```bash
python task_manager.py
```

Navegação no menu:
```
1 - Criar nova lista
2 - Selecionar lista existente
3 - Adicionar tarefa à lista atual
4 - Visualizar tarefas da lista
5 - Remover tarefa específica
6 - Excluir lista inteira
7 - Sair do programa
0 - Voltar ao menu anterior
```

## 🖥 Compatibilidade

- Testado em Windows (usa `cls` para limpar tela)
- Para Linux/Mac: substituir `os.system('cls')` por `os.system('clear')`

## 📄 Licença

Distribuído sob licença MIT. Veja o arquivo `LICENSE` para mais informações.

---

Desenvolvido com ❤️ por [Seu Nome]  
Contribuições são bem-vindas!
