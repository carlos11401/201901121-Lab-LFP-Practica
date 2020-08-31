import json
import sys
import re

print('Bienvenido usa Algun Comando --->  ') 
print('(CARGAR)-(SELECCIONAR)-(SELECCIONAR*)-(SALIR)-(CUENTA)')
salir = False
while salir==False:
    global comando
    comando = input()     # lo que va ha ingresar el usuario
    comando = comando.replace(",","")   #remplazando comas por nada jeje
    global ListaTextoComando 
    ListaTextoComando= comando.split(" ")     #separando cada palabra en una lista
    cantidadArchivos = len(ListaTextoComando)   #numero de palabras 

    comand = ListaTextoComando[0]    #guardando los comandos
    comandCargar = "cargar"
    comandSeleccionarAll = "seleccionar*"
    comandSeleccionar = "seleccionar"
    comandCuenta = "cuenta"
    comandMax = "maximo"
    comandMin = "minimo"
    comandSuma = "suma"
    

    if comand.lower() == comandCargar.lower():         #verificar comando CARGAR

        global listaArchivos   #lista donde se guardaran los archivos
        listaArchivos = []
        contador = 1
        while contador < cantidadArchivos:
            archivo = open(ListaTextoComando[contador]+".json").read()   #tomando de la lista de palabras el archivo omitiendo la posicion [0] que es de CARGAR
            datos_de_archivo = json.loads(archivo)

            listaArchivos.append(datos_de_archivo)     #guardando archivo en lista
            print("Se ha Cargado en Memoria : "+ListaTextoComando[contador])
            contador = contador+1

    if comand.lower() == comandSeleccionar.lower():  #verificar comando SELECCIONAR
        Donde = "donde"
        condiciones = re.findall(r' (.*?) =',comando)   #obtener las condiciones para la busqueda
        condiciones = " ".join(condiciones)
        condiciones = condiciones.split(" ")  #recordar omitir los ultimos 2 datos de la lista que sera DONDE ATRIBUTO

        comandDonde = condiciones[len(condiciones)-2]  #obteniendo el comando DONDE

        if Donde.lower()==comandDonde.lower():

            atributo = condiciones[len(condiciones)-1]  #obteniendo el tipo de atributo que vamos a buscar

            if atributo== "nombre":
                patron = r'"(.*?)"'     #para quitar comillas a algun texto               
                palabraBuscada = re.findall(patron,comando)   #aqui se almacena el nombre que queremos buscar
                palabraBuscada = palabraBuscada[0]
            else:
                if atributo == "activo":
                    numeroPalabrasTextoComando = len(ListaTextoComando)
                    palabraBuscada = ListaTextoComando[numeroPalabrasTextoComando-1]
                    palabraBuscada = str_to_bool(palabraBuscada)    #aqui se almacena el activo que queremos buscar ya convertido a bool
                else:
                    numeroPalabrasTextoComando = len(ListaTextoComando)
                    palabraBuscada = int(ListaTextoComando[numeroPalabrasTextoComando-1])#aqui se almacena el numero que queremos buscar

            contador3 = 0
            print("......................................")
            while contador3 < len(listaArchivos):
                archivoJSON = listaArchivos[contador3] #recorriendo los archivos
                cantidadRegistros = len(archivoJSON)   #numero de registros
                contador = 0

                while contador < cantidadRegistros:    #recorriendo los registros de cada archivo
                    registro = archivoJSON[contador]      #en var "registro" estaran los registro de los archivos
                    ponerPuntos = False
                    if registro[atributo] == palabraBuscada:   #comparando las palabras
                        ponerPuntos = True     #para imprimir adorno
                        contador2 = 0
                        while contador2 <(len(condiciones)-2):
                            print(condiciones[contador2],": ",registro[condiciones[contador2]])
                            contador2 = contador2 + 1
                    contador = contador +1
                if ponerPuntos==True: print("......................................") 
                else: ponerPuntos=False
                contador3 = contador3 + 1
        
        else:
            print("Ha ocurrido un error")

    if comand.lower() == comandSeleccionarAll.lower(): #verificar comando SELECCIONAR*

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

    if comand.lower() == comandMax.lower():         #verificar comando MAXIMO
        if len(ListaTextoComando) > 2:
            print("Ha Ocurrido un Error :(")
        else:
            atributo = ListaTextoComando[1]
            contador3 = 0
            
            listaNumeros  = []  #lista donde se guardara cada dato del atributo
            while contador3 < len(listaArchivos):
                archivoJSON = listaArchivos[contador3] #recorriendo los archivos
                cantidadRegistros = len(archivoJSON)   #numero de registros
                
                contador = 0
                
                while contador < cantidadRegistros:    #recorriendo los registros de cada archivo
                    registro = archivoJSON[contador]      #en var "registro" estaran los registro de los archivos
                    listaNumeros.append(registro[atributo])   #agregando cada dato del atributo a una lista para despues ordenarla
                    contador = contador + 1
                contador3 = contador3 + 1

            listaNumeros = sorted(listaNumeros)   #se ordeno la lista, donde el valor MAX esta en la ultima posicion
            print("-->",atributo," MAX : ",listaNumeros[len(listaNumeros)-1])

    if comand.lower() == comandMin.lower():         #verificar comando MINIMO
        if len(ListaTextoComando) > 2:
            print("Ha Ocurrido un Error :(")
        else:
            atributo = ListaTextoComando[1]
            contador3 = 0
            
            listaNumeros  = []  #lista donde se guardara cada dato del atributo
            while contador3 < len(listaArchivos):
                archivoJSON = listaArchivos[contador3] #recorriendo los archivos
                cantidadRegistros = len(archivoJSON)   #numero de registros
                
                contador = 0
                
                while contador < cantidadRegistros:    #recorriendo los registros de cada archivo
                    registro = archivoJSON[contador]      #en var "registro" estaran los registro de los archivos
                    listaNumeros.append(registro[atributo])   #agregando cada dato del atributo a una lista para despues ordenarla
                    contador = contador + 1
                contador3 = contador3 + 1

            listaNumeros = sorted(listaNumeros)   #se ordeno la lista, donde el valor MIN esta en la primera posicion
            print("-->",atributo," MIN : ",listaNumeros[0])

    if comand.lower() == comandSuma.lower():         #verificar comando SUMA
        if len(ListaTextoComando) > 2:
            print("Ha Ocurrido un Error :(")
        else:
            atributo = ListaTextoComando[1]
            contador3 = 0
            
            sumaAtributos = 0  #en esta variable se iran sumando los datos
            while contador3 < len(listaArchivos):
                archivoJSON = listaArchivos[contador3] #recorriendo los archivos
                cantidadRegistros = len(archivoJSON)   #numero de registros
                
                contador = 0
                
                while contador < cantidadRegistros:    #recorriendo los registros de cada archivo
                    registro = archivoJSON[contador]      #en var "registro" estaran los registro de los archivos
                    sumaAtributos = sumaAtributos + int(registro[atributo])   #agregando cada dato del atributo a la lista
                    contador = contador + 1
                contador3 = contador3 + 1

            print("Suma de ",atributo," : ",sumaAtributos)

    if comand.lower() == comandCuenta.lower():         #verificar comando
        print("funciona")
        contador = 0
        cantidadRegistros = 0
        while contador < len(listaArchivos):
            archivoJSON = listaArchivos[contador] #recorriendo los archivos
            cantidadRegistros = cantidadRegistros + len(archivoJSON)   #numero de registros
            contador = contador + 1

        print("Cantidad de Registros: ",cantidadRegistros)

    if ListaTextoComando[0] == "SALIR":
        break


    def str_to_bool(dato):   #para convertir el dato de texto activo a bool
        if dato == "true":
            return True
        else:
            return False
