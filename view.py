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

        if commands[0] == "RPDE":
        
        if commands[0] == "RPAE":

        if commands[0] == "RPII":

        if commands[0] == "VNE":

        if commands[0] == "VP":

        if commands[0] == "EPE":

        if commands[0] == "EUE":

        if commands[0] == "EP":
    
def registar_pais_inicio():

def registar_pais_fim():

def registar_pais_depois_de_outro():

def registar_pais_antes_de_outro():

def registar_pais_num_local_especifico():

def verificar_numero_elementos():

def verificar_pais_na_lista():

def eliminar_primeiro_pais():

def eliminar_ultimo_pais():

def eliminar_pais_especifico():

