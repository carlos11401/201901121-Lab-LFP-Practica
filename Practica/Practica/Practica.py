import json
import sys
import re
import webbrowser
import os

print('-----------------------> Bienvenido usa Algun Comando <------------------------------') 
print('\n(CARGAR)-(SELECCIONAR)-(SELECCIONAR*)-(SUMA)-(MAXIMO)-(MINIMO)-(REPORTAR)-(SALIR) \n')
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
    comandReportar = "reportar"
    comandSalir = "salir"
    
    try:
        if comand.lower() == comandCargar.lower():         #verificar comando CARGAR
        
            global listaArchivos   #lista donde se guardaran los archivos
            listaArchivos = []
            contador = 1

            print("")
        
            while contador < cantidadArchivos:
            
                try:
                    archivo = open(ListaTextoComando[contador]+".json").read()   #tomando de la lista de palabras el archivo omitiendo la posicion [0] que es de CARGAR
               
                    datos_de_archivo = json.loads(archivo)

                    listaArchivos.append(datos_de_archivo)     #guardando archivo en lista
                    print("---> Se ha Cargado en Memoria : "+ListaTextoComando[contador])
                
                except Exception as e:
                    print("\n         No se ha Podido Acceder al Archivo: ","'",ListaTextoComando[contador],".json","'"," :(  <----- (ERROR) \n") 
                contador = contador+1
            print("")

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
                if atributo == "activo":
                    numeroPalabrasTextoComando = len(ListaTextoComando)
                    palabraBuscada = ListaTextoComando[numeroPalabrasTextoComando-1]
                    palabraBuscada = str_to_bool(palabraBuscada)    #aqui se almacena el activo que queremos buscar ya convertido a bool
                if atributo == "edad" or atributo == "promedio":
                    numeroPalabrasTextoComando = len(ListaTextoComando)
                    palabraBuscada = int(ListaTextoComando[numeroPalabrasTextoComando-1])#aqui se almacena el numero que queremos buscar

                contador3 = 0
                print(".......................................................................................................")
                while contador3 < len(listaArchivos):
                    archivoJSON = listaArchivos[contador3] #recorriendo los archivos
                    cantidadRegistros = len(archivoJSON)   #numero de registros
                    contador = 0

                    while contador < cantidadRegistros:    #recorriendo los registros de cada archivo
                        registro = archivoJSON[contador]      #en var "registro" estaran los registro de los archivos
                        ponerPuntos = False

                        try:
                            if registro[atributo] == palabraBuscada:   #comparando las palabras
                                ponerPuntos = True     #para imprimir adorno
                                contador2 = 0
                        
                                while contador2 <(len(condiciones)-2):
                                    try:
                                        print("--->",condiciones[contador2],": ",registro[condiciones[contador2]])
                                    except Exception as e: print("       No se ha Encontrado el Atributo: ","'",condiciones[contador2],"'"," :(  <-----(ERROR)")
                    
                                    contador2 = contador2 + 1
                        except Exception as e: print("       No se ha Encontrado el Atributo: ","'",atributo,"'"," :(  <-----(ERROR)")
                        contador = contador +1
                            
                    if ponerPuntos==True: print(".......................................................................................................") 
                    else: ponerPuntos=False
                    contador3 = contador3 + 1
        
            else:
                print("No se Encontro el Comando DONDE")

        if comand.lower() == comandSeleccionarAll.lower(): #verificar comando SELECCIONAR*

            print("\nNombre           Edad       Activo       Promedio")

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

            print("")

        if comand.lower() == comandMax.lower():         #verificar comando MAXIMO
            if len(ListaTextoComando) > 2:
                print("       Ha Ocurrido un Error con el Atributo :(  <-----(ERROR)")
            else:
                try:
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
                    print("\n--->",atributo," MAX : ",listaNumeros[len(listaNumeros)-1],"\n")
                except Exception as e: print("\n       Ha Ocurrido un Error con el Atributo :(  <-----(ERROR)\n")

        if comand.lower() == comandMin.lower():         #verificar comando MINIMO
            if len(ListaTextoComando) > 2:
                print("\n       Ha Ocurrido un Error con el Atributo :(  <-----(ERROR)\n")
            else:
                try:
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
                    print("\n--->",atributo," MIN : ",listaNumeros[0],"\n")
                except Exception as e: print("\n       Ha Ocurrido un Error :(  <-----(ERROR)\n")

        if comand.lower() == comandSuma.lower():         #verificar comando SUMA
            if len(ListaTextoComando) > 2:
                print("\nHa Ocurrido un Error :(\n")
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

                print("\n---> Suma de ",atributo," : ",sumaAtributos,"\n")

        if comand.lower() == comandCuenta.lower():         #verificar comando CUENTA

            contador = 0
            cantidadRegistros = 0
            while contador < len(listaArchivos):
                archivoJSON = listaArchivos[contador] #recorriendo los archivos
                cantidadRegistros = cantidadRegistros + len(archivoJSON)   #numero de registros
                contador = contador + 1

            print("\n---> Cantidad de Registros: ",cantidadRegistros,"\n")

        if comand.lower() == comandReportar.lower():         #verificar comando REPORTAR
            if len(ListaTextoComando) > 2:
                print("\nHa Ocurrido un Error :(\n")
            else:
                numeroDeRegistrosUsuario = int(ListaTextoComando[1])  #numero de registros que quiere el usuario
                contadorRegistrosAcumulados = 0     #esta variable contara los registros que se vayan acumulando para generar el html

                # en esas listas se guardaran los datos de los atributos
                listaDatosRegistrosNombre = []   
                listaDatosRegistrosEdad = []
                listaDatosRegistrosActivo = []
                listaDatosRegistrosPromedio = []

                contador2 = 0
                while contador2 < len(listaArchivos):
                    archivoJSON = listaArchivos[contador2] #recorriendo los archivos
                    cantidadRegistros = len(archivoJSON)   #numero de registros

                    #contadorRegistrosAcumulados = contadorRegistrosAcumulados + cantidadRegistros   #acumulando los registros que encuentre por cada archivo
                    
                    contador = 0
                    while contador < cantidadRegistros:    #recorriendo los registros de cada archivo

                        if contadorRegistrosAcumulados < numeroDeRegistrosUsuario:

                            registro = archivoJSON[contador]      #en var "registro" estaran los registro de los archivos
                            listaDatosRegistrosNombre.append(registro['nombre'])
                            listaDatosRegistrosEdad.append(registro['edad'])
                            listaDatosRegistrosActivo.append(registro['activo'])
                            listaDatosRegistrosPromedio.append(registro['promedio'])

                            contador= contador + 1
                            contadorRegistrosAcumulados = contadorRegistrosAcumulados + 1
                        else: 
                            contador = contador + cantidadRegistros
                            contado2 = contador2 + len(listaArchivos)

                    contador2 = contador2 + 1

                print("")

                contador3 = 0
                guardarRegistro=""
                while contador3 < numeroDeRegistrosUsuario:

                    guardarRegistro=guardarRegistro+f"<tr><td>{listaDatosRegistrosNombre[contador3]}</td><td>{listaDatosRegistrosEdad[contador3]}</td><td>{listaDatosRegistrosActivo[contador3]}</td><td>{listaDatosRegistrosPromedio[contador3]}</td></tr>"
                    contador3 = contador3 + 1

                myFile = open("registros.html", "w")
                docHTML = f"""
                <DOCTYPE html>
                    <html>
                    <head>
	                    <title>REGISTROS</title>
	                    <link rel="stylesheet" type="text/css" href="plantilla.css">
                    </head>
                    <body>
                        <div class="container">
		                    <table>
			                    <thead>
				                    <tr>
					                    <td>nombre</td>
                                        <td>edad</td>
                                        <td>activo</td>
                                        <td>saldo</td>
				                    </tr>
			                    </thead> 
                            </table>
                            <table>
			                    <thead>
			                    </thead> 
                                </tbody>
                                    <tr>
					                    <td>---------------   ---------------   ---------------   ---------------</td>
				                    </tr>
			                    </tbody>
                            </table>
                            <table>
                                <thead>	 
                                </tbody>
                                    <tr>{guardarRegistro}</tr>
			                    </tbody>
		                    </table>
                    </div>
                    </body>
                    </html>
                    """

                myFile.write(docHTML)
                myFile.close()
                webbrowser.open_new_tab("registros.html")
                print('-----------------------> Archivo HTML Creado con Exito :) <------------------------------') 

        if comand.lower() == comandSalir.lower():         #verificar comando SALIR
            break

    except Exception as e: print("\n       Ha Ocurrido un Error :)  <-----(ERROR)\n")

    def str_to_bool(dato):   #para convertir el dato de texto activo a bool
        if dato == "true":
            return True
        if dato == "false": 
            return False
        
