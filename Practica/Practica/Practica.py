import json
import sys
import re

print('Bienvenido usa Algun Comando --->  ')
print('(CARGAR)-(SELECCIONAR)-(SELECCIONAR*)-(SALIR)')
salir = False
while salir==False:
    global comando
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

    if ListaTextoComando[0] == "SELECCIONAR":
        if re.search("DONDE",comando):
            patron = r'"(.*?)"'     #para quitar comillas a algun texto
            palabraBuscada = re.findall(patron,comando)   #aqui se almacena la palabra que queremos buscar

            contador3 = 0
            while contador3 < len(listaArchivos):
                archivoJSON = listaArchivos[contador3] #recorriendo los archivos
                cantidadRegistros = len(archivoJSON)   #numero de registros
                contador = 0

                while contador < cantidadRegistros:    #recorriendo los registros de cada archivo
                    registro = archivoJSON[contador]      #en var "registro" estaran los registro de los archivos
                    if registro["nombre"] == palabraBuscada[0]:   #comparando las palabras
                        print(registro["nombre"],"     ",registro["edad"],"     ",registro["activo"],"     ",registro["promedio"])
                        contador= cantidadRegistros + 1
                        contador3 = len(listaArchivos)     #para que despues no siga buscando cuando ya encontro la coincidencia
                    contador = contador +1
                contador3 = contador3 + 1
        
        else:
            print("Ha ocurrido un error")
    if ListaTextoComando[0] == "SELECCIONAR*": 

        print("Nombre           Edad       Activo       Promedio")

        contador2 = 0
        
        while contador2 < len(listaArchivos):
            archivoJSON = listaArchivos[contador2] #recorriendo los archivos
            cantidadRegistros = len(archivoJSON)   #numero de registros

            contador = 0

            while contador < cantidadRegistros:    #recorriendo los registros de cada archivo
                registro = archivoJSON[contador]      #en var "registro" estaran los registro de los archivos
                print(registro["nombre"],'        ',registro["edad"],'       ',registro["activo"],'       ',registro["promedio"])
                contador= contador + 1
            contador2 = contador2 + 1

    if ListaTextoComando[0] == "SALIR":
        break