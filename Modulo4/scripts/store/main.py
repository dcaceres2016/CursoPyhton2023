import modulos.bd as bd
from modulos.proceso import *
from pyfiglet import Figlet
import random

database=None

def mostrar_menu():
    print("Bienvenidos a store DatuxTec")
    print("1. Crear producto")
    print("2. Listar productos")
    print("3. Editar nombre de producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("2.1 Editar título del menú usando pyfiglet")

def bienvenido():
    bienvenida_texto = "¡Bienvenido al programa!"
    print(pyfiglet.figlet_format(bienvenida_texto))

def opcion_2_1():
    nuevo_titulo = input("Ingrese el nuevo título del menú: ")

    # Obtener la lista de fuentes disponibles
    fuentes_disponibles = Figlet().getFonts()

    # Seleccionar una fuente aleatoria
    fuente_seleccionada = random.choice(fuentes_disponibles)

    # Crear una instancia de Figlet con la fuente seleccionada
    figlet = Figlet(font=fuente_seleccionada)

    # Imprimir el nuevo título del menú con la fuente seleccionada
    titulo_formateado = figlet.renderText(nuevo_titulo)
    print(f"\nNuevo título del menú con fuente '{fuente_seleccionada}':\n{titulo_formateado}")

def main():
    global database
    salir=False
    init=True
    while not salir:
        #flag para que se inice solo una vez
        if init:
            user=input("ingrese su nombre de usuario temporal: ") 
            init=False
            config() ## ejecutar las consideraciones basicas al iniciar la aplicacion
        opciones="""
        Bienvenidos a store DatuxTec
        1. Crear producto
        2. Listar productos
        3. Editar nombre de producto 
        4. Eliminar producto
        5. Salir"""
        print(opciones)
        opc=int(input("ingrese una opcion: "))
        if opc==1:
            crear_producto(user)
        elif opc==2:
            listar_producto(user)
        elif opc==3:
            editar_nombre(user)
        elif opc==4:
            eliminar_producto(user)
        elif opc==5:
            salir=True
            print("terminando sesion....")
            break
        else:
            print("ingrese una opcion valida")

#funcion que configura la inicializacion de la aplicacion
def config():

    database=bd.Bd()
    query_products="""
        CREATE TABLE  IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL
                );
    """
    database.execute_query(query_products)


if __name__=='__main__':
    main()
