from models.LinkedList import LinkedList

def main():
    lista_paises = LinkedList()
    while True:
        try:
            commands = input().split(" ")
        except EOFError:
            return

        #Inserir país no início
        if commands[0] == "RPI":
            lista_paises.insert_at_start(commands[1])
            lista_paises.traverse_list()

        #Inserir país no fim
        if commands[0] == "RPF":
            lista_paises.insert_at_end(commands[1])
            lista_paises.traverse_list()

        #Inserir país depois de outro
        if commands[0] == "RPDE":
            lista_paises.insert_after_item(commands[2], commands[1])
            lista_paises.traverse_list()

        #Inserir país antes de outro
        if commands[0] == "RPAE":
            lista_paises.insert_before_item(commands[2], commands[1])
            lista_paises.traverse_list()

        #Inserir país num lugar especifico
        if commands[0] == "RPII":
            lista_paises.insert_at_index(int(commands[2]), commands[1])
            lista_paises.traverse_list()

        #Verificar quantos países existem
        if commands[0] == "VNE":
            print(f"O número de elementos são {lista_paises.get_count()}.")

        #Verificar se existe o país
        if commands[0] == "VP":
            resultado = lista_paises.search_item(commands[1])
            if resultado == False:
                print(f"O país {commands[1]} não se encontra na lista.")
            else:
                print(f"O país {commands[1]} encontra-se na lista.")

        #Eliminar o primeiro país
        if commands[0] == "EPE":
            print(f"O país {lista_paises.start_node.item} foi eliminado da lista.")
            lista_paises.delete_at_start()

        #Eliminar o ultimo país
        if commands[0] == "EUE":
            print(f"O país {lista_paises.get_last_node()} foi eliminado da lista.")
            lista_paises.delete_at_end()

        #Eliminar um país espexifico
        if commands[0] == "EP":
            if lista_paises.search_item(commands[1]) == False:
                print(f"O país {commands[1]} não se encontra na lista.")
            else:
                lista_paises.delete_element_by_value(commands[1])
                print(f"O país {commands[1]} foi eliminado da lista.")