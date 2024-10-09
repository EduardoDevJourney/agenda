#uma agenda para salvar, editar, deletar e marcar um contato como favorito.
### Regras da aplicação
# - A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
# - Deve ser possível adicionar um contato
#     - O contato pode ter os dados:
#     - Nome
#     - Telefone
#     - Email
#     - Favorito (está opção é para poder marcar um contato como favorito)
# - Deve ser possível visualizar a lista de contatos cadastrados
# - Deve ser possível ver uma lista de contatos favoritos
# - Deve ser possível marcar/desmarcar um contato como favorito
# - Deve ser possível editar um contato
# - Deve ser possível apagar um contato
from os import system
from typing import Dict

list_agenda = []
type_contact = {
    "nome": "",
    "telefone": "",
    "email": "",
    "favorito": False
}


def clear_terminal():
    system('clear')

def pular_linha():
    print("\n \n")

def print_agenda(agenda: list):

    for contact in agenda:
        print( "################################" )
        print( f"nome: {contact["nome"]}" )
        print( f"telefone: {contact["telefone"]}" )
        print( f"email: {contact["email"]}" )
        print( f"favorito: { '[ X ]' if contact["favorito"] else '[  ]' }" )
        print( "################################" )


def view_contacts():
    if list_agenda:
        print_agenda(list_agenda)
    else:
        print("sua agenda esta vazia")

def view_favorite_contacts():
    filter_contacts = [contact for contact in list_agenda if contact["favorito"]]
    if filter_contacts:
        print_agenda(filter_contacts)
    else:
        print("sua agenda de favoritos esta vazia") 

def add_contact(new_contact: Dict[str, str]):
    if new_contact:
        valid_contact = [contact for contact in list_agenda if contact["nome"].lower() == new_contact["nome"].lower()]
        if not valid_contact:
            new_copy = new_contact.copy()
            list_agenda.append(new_copy)
            print(f"O contato {new_contact["nome"]}, foi adicionado a sua agenda")
        else:
            print("O nome para este contato ja existe")

def edit_contact(contact_name: str, field_name: str, new_value: str):
    for index, contact in enumerate(list_agenda):
        if contact["nome"].lower() == contact_name.lower():
            if field_name in contact:
                list_agenda[index][field_name] = new_value
                print(f"O {field_name} foi atualizado para {new_value}")
            else:
                print("Este campo que deseja editar não existe")
            return False
    print("Contato não encontrado.")

def remove_contact(contact_name: str):
    valid_contact = [contact for contact in list_agenda if contact["nome"].lower() == contact_name.lower()]
    if valid_contact:
        list_agenda.remove(valid_contact[0])
        print(f"o contato {contact_name}, foi removido")
    else:
        print("contato nao encontrado")

def mark_as_favorite(contact_name: str):
    for contato in list_agenda:
        if contato["nome"].lower() == contact_name.lower():
            contato["favorito"] = True
            print(f"O {contact_name} agora é seu favorito")
            return contato
    print("Contato nao encontrado")

def remove_as_favorite(contact_name: str):
    for contato in list_agenda:
        if contato["nome"].lower() == contact_name.lower():
            contato["favorito"] = False
            print(f"O {contact_name} agora nao é seu favorito")
            return contato
    print("Contato nao encontrado")


while True:
    
    print( "################################" )
    print("1 - Visualizar Contatos")
    print("2 - Visualizar Contatos Favoritos")
    print("3 - Adicionar Contato")
    print("4 - Editar um contato")
    print("5 - Marcar um contato como Favorito")
    print("6 - Remover um contato como Favorito")
    print("7 - Apagar um Contato")
    print("0 - sair")
    print( "################################" )
    
    options = input("Escolha uma opção: ")

    match options:

        case "0":
            break
            
        case "1":
            print("carregando todos os contatos")
            clear_terminal()
            view_contacts()
            pular_linha()
        
        case "2":
            print("carregando favoritos")
            clear_terminal()
            view_favorite_contacts()
            pular_linha()
        
        case "3":
            clear_terminal()
            print("adicionando contatos")
            type_contact["nome"] = input("Digite o nome do contato: ")
            type_contact["telefone"] = input("Digite o telefone do contato: ")
            type_contact["email"] = input("Digite o email do contato: ")
            clear_terminal()
            add_contact(type_contact)
            pular_linha()

        case "4":
            clear_terminal()
            print("voce esta editando um contato")
            contact_name = (input("Digite o nome do contato que deseja editar: "))
            contact_field = input("Digite o campo que deseja editar: ")
            value = input("Digite o novo valor para este campo: ")
            clear_terminal()
            edit_contact(
                contact_name=contact_name,
                field_name= contact_field,
                new_value=value
            )
            pular_linha()

        case "5":
            clear_terminal()
            print("voce esta escolhendo um novo favorito")
            contact_name = input("Digite o nome do contato que sera seu novo favorito: ")
            clear_terminal()
            mark_as_favorite(contact_name)
            pular_linha()

        case "6":
            clear_terminal()
            print("voce esta removendo um favorito")
            contact_name = input("Digite o nome do contato que deseja remover dos favoritos: ")
            clear_terminal()
            remove_as_favorite(contact_name)
            pular_linha()

        case "7":
            clear_terminal()
            print("voce esta removendo um contato")
            contact_name = input("Digite o nome do contato que deseja remover: ")
            clear_terminal()
            remove_contact(contact_name)
            pular_linha()
        
        case _:
            clear_terminal()
            print("digite uma opcao valida")
            pular_linha()
