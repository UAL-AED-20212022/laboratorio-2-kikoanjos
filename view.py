import controller
import model
from models import LinkedList

def main():
    lista_paises = LinkedList()
    while True:
        try:
            commands = input().split(" ")
        except EOFError:
            return

        if commands[0] == "RPI":
            lista_paises.insert_at_start(commands[1])
        if commands[0] == "RPF":
            lista_paises.insert_at_end(commands[1])
            pass
        if commands[0] == "RPDE":
            pass
        if commands[0] == "RPAE":
            pass
        if commands[0] == "RPII":
            pass
        if commands[0] == "VNE":
            pass
        if commands[0] == "VP":
            pass
        if commands[0] == "EPE":
            pass
        if commands[0] == "EUE":
            pass
        if commands[0] == "EP":
            pass
def registar_pais_inicio():
    pass
def registar_pais_fim():
    pass
def registar_pais_depois_de_outro():
    pass
def registar_pais_antes_de_outro():
    pass
def registar_pais_num_local_especifico():
    pass
def verificar_numero_elementos():
    pass
def verificar_pais_na_lista():
    pass
def eliminar_primeiro_pais():
    pass
def eliminar_ultimo_pais():
    pass
def eliminar_pais_especifico():
    pass
