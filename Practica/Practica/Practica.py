import json
import sys

print('Bienvenido usa Algun Comando')
salir = False
while salir==False:
    comando = input()     # lo que va ha ingresar el usuario
    comando = comando.replace(",","")   #remplazando comas por nada jeje
    ListaTextoComando = comando.split(" ")     #separando cada palabra en una lista
    cantidadArchivos = len(ListaTextoComando)   #numero de palabras 

    

    
         # donde se guardaran los archivos

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
        print(len(listaArchivos))

        print("Nombre                Edad               Activo            Promedio")

        contador2 = 0
        
        while contador2 < len(listaArchivos):
            print(listaArchivos[contador2])
            #archivoJSON = listaArchivos[contador2]
            #print(archivoJSON.get('nombre'))
            contador2 = contador2 + 1

    if ListaTextoComando[0] == "SALIR":
        break