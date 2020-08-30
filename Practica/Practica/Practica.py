import json
import sys
from io import open

print('Bienvenido usa Algun Comando')
salir = False
while salir==False:
    comando = input()     # lo que va ha ingresar el usuario
    comando = comando.replace(",","")   #remplazando comas por nada jeje
    global ListaTextoComando 
    ListaTextoComando= comando.split(" ")     #separando cada palabra en una lista
    cantidadArchivos = len(ListaTextoComando)   #numero de palabras 

    if ListaTextoComando[0] == "CARGAR":         #verificar comando

        global listaArchivos   #lista donde se guardaran los archivos
        listaArchivos = []
        contador = 1
        while contador < cantidadArchivos:
            archivo = open(ListaTextoComando[contador]+".json").read()   #tomando de la lista de palabras el archivo omitiendo la posicion [0] que es de CARGAR
            datos_de_archivo = json.loads(archivo)

            listaArchivos.append(datos_de_archivo)     #guardando archivo en lista
            print("Se ha Cargado en Memoria : "+ListaTextoComando[contador])
            contador = contador+1
    print(len(listaArchivos))

    if ListaTextoComando[0] == "SELECCIONAR*": 

        print("Nombre           Edad       Activo       Promedio")

        contador2 = 0
        
        while contador2 < len(listaArchivos):
            archivoJSON = listaArchivos[contador2] #recorriendo los archivos
            cantidadRegistros = len(archivoJSON)   #numero de registros

            contador = 0

            while contador < cantidadRegistros: 
                registro = archivoJSON[contador]      #en var "registro" estaran los registro de los archivos
                print(registro["nombre"],'           ',registro["edad"],'       ',registro["activo"],'       ',registro["promedio"])
                contador= contador + 1
            contador2 = contador2 + 1

    if ListaTextoComando[0] == "SALIR":
        break