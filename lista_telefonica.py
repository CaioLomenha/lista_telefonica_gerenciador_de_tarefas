
def adicionar_contato(lista_telefonica, nome_do_contato, telefone, email):
    contato = {"Nome do Contato": nome_do_contato, "Telefone": telefone, "Email": email, "Favorito": False}
    lista_telefonica.append(contato)
    print("Contato adicionado")
    return

def ver_contato(lista_telefonica):
    for indice, contato in enumerate(lista_telefonica, start=1):
        status = "★" if contato["Favorito"] else " "
        nome_do_contato = contato["Nome do Contato"]
        telefone = contato["Telefone"]
        email = contato["Email"]
        print("\nLista de Contatos")
        print(f"{indice}- [{status}] Nome: {nome_do_contato}, Telefone: {telefone}, Email: {email}")
    return

def editar_contato(lista_telefonica, indice_contato, novo_nome, novo_email, novo_telefone):
    indice_atualizado = int(indice_contato) - 1
    if indice_atualizado >= 0 and indice_atualizado < len(lista_telefonica):
        if novo_nome:
            lista_telefonica[indice_atualizado]["Nome do Contato"] = novo_nome
        if novo_telefone:        
            lista_telefonica[indice_atualizado]["Telefone"] = novo_telefone
        if novo_email:
            lista_telefonica[indice_atualizado]["Email"] = novo_email    
        print(f"Contato {indice_contato} atualizado")
    else:
        print("Contato não existe")

def contato_favorito(lista_telefonica, indice_contato):
    indice_atualizado = int(indice_contato) - 1
    if indice_atualizado >= 0 and indice_atualizado < len(lista_telefonica):
        if lista_telefonica[indice_atualizado]["Favorito"] == True:
            lista_telefonica[indice_atualizado]["Favorito"] = False
        elif lista_telefonica[indice_atualizado]["Favorito"] == False:
            lista_telefonica[indice_atualizado]["Favorito"] = True
    else:
        print("Contato não existe")

def ver_favorito(lista_telefonica):
    for indice, contato in enumerate(lista_telefonica):
        status = "★" if contato["Favorito"] else " "
        nome_do_contato = contato["Nome do Contato"]
        telefone = contato["Telefone"]
        email = contato["Email"]
        if contato["Favorito"] == True:
                print(f"{indice}- [{status}] Nome: {nome_do_contato}, Telefone: {telefone}, Email: {email}")

def apagar_contato(lista_telefonica, indice_contato):
    for indice, contato in enumerate(lista_telefonica):
        indice_atualizado = int(indice_contato) - 1
        if indice_atualizado >= 0 and indice_atualizado < len(lista_telefonica):
          if indice_atualizado == indice:
              lista_telefonica.remove(contato)
        else:
            print("Contato não existe")
    print(f"Contato {indice_contato} deletado")
        

lista_telefonica = []

while True:
    print("\nBem vindo a sua agenda, escolha a opção que deseja abaixo")
    print("\n1- Adicionar contato")
    print("2- Visualizar contato")
    print("3- Editar contato")
    print("4- Marcar/Desmarcar contato como Favorito")
    print("5- Visualizar lista de contatos Favoritos")
    print("6- Apagar contato")
    print("7- Sair da Agenda")
    escolha = input("\nDigite o número que deseja: ")

    if escolha == "1":
        nome_do_contato = input("Digite o nome do contato: ")
        telefone = input("Digite o número de telefone: ")
        email = input("Digite o email: ")
        adicionar_contato(lista_telefonica, nome_do_contato, telefone, email)

    elif escolha == "2":
        ver_contato(lista_telefonica)

    elif escolha == "3":
        ver_contato(lista_telefonica)
        indice_contato = input("Digite o número de qual contato deseja editar: ")
        novo_nome = input("Digite o Nome: ")
        novo_telefone = input("Digite o Telefone: ")
        novo_email = input("Digite o Email: ")
        editar_contato(lista_telefonica, indice_contato, novo_nome, novo_email, novo_telefone)
        
    elif escolha == "4":
        ver_contato(lista_telefonica)
        indice_contato = input("Digite o número de qual contato deseja marcar/desmarcar como Favorito: ")
        contato_favorito(lista_telefonica, indice_contato)

    elif escolha == "5":
        ver_favorito(lista_telefonica)
    
    elif escolha == "6":
        ver_contato(lista_telefonica)
        indice_contato = input("Qual contato deseja deletar? ")
        apagar_contato(lista_telefonica, indice_contato)
        
    elif escolha == "7": 
       break