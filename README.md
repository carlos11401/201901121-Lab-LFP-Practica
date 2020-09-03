# Lab-LFP-Practica

MANUAL DE USUARIO DE SIMPLE QL

    Simple QL es una aplicacion en consola en donde el usuario pordra cargar a memoria 
	archivos en formato JSON y podra acceder a los registros que este archivo contenga.
	Para eso hay diversos comandos  los cuales son Case Insensitive(significa que puede
	reconocer el comando tanto en mayusculas o minusculas) que la aplicacion trae para 
	esto, los cuales son:
	
	CARGAR:
	    Al escribir este comando en la consola usted debera escribir los archivos que 
		desea cargar en memoria y al presionar ENTER, si encuentra los archivos que ha 
		escrito se mostrar un mensaje de los archivos que se han cargado con exito, de
		lo contrario si no llegara a encontrar un erchivo este mandara un mensaje del
		que no se encontro. Ejemplo de comando:
		
		    CARGAR archivo1, archivo2, archivo3, archivo4
			
			---> Se ha Cargado en Memoria : archivo1
			---> Se ha Cargado en Memoria : archivo2
			---> Se ha Cargado en Memoria : archivo3
			
	SELECCIONAR* :
	    Al escribir este comando y darle ENTER se mostrar cada registro que haya en todos
		los archivos que anteriormente haya cardado en momoria. Si por alguna razon se
		algun texto despues del comando, simplemente no hara nada ya que este comando no
		no debe llevar algun otro texto para funcionar. Ejemplo de Comando:
		     
			SELECCIONAR*

			Nombre           Edad       Activo       Promedio
			registro 1.1          10         True         14
			registro 2.1          20         True         24
			registro 2.2          21         True         26
			registro 3.1          30         True         35
			registro 3.2          300         True         36
			registro 3.3          32         True         38
			
	SELECCIONAR :
	    Con este comando podra buscar algun registro en especifico de todos los archivos y
		para esto al escribir el comando SELECCIONAR posteriormente debera escribir todos
		los datos que quiere obtener de los registros, despues de haber escrito los datos 
		debera escribir la palabra DONDE que forma parte del comando SELECCIONAR, des pues
		de haber escrito DONDE devera escribir el datos que quiere buscar en los registros.
		Al darle ENTER se mostrar los registros encontrados con el dato especificado y se 
		mostrara los datos que usted desea ver. Ejemplo Comando:
		    
			SELECCIONAR nombre, edad DONDE activo = true
			.......................................................................................................
			---> nombre :  registro 1.1
			---> edad :  10
			.......................................................................................................
			---> nombre :  registro 2.1
			---> edad :  20
			---> nombre :  registro 2.2
			---> edad :  21
			.......................................................................................................
			---> nombre :  registro 3.1
			---> edad :  30
			---> nombre :  registro 3.2
			---> edad :  300
			---> nombre :  registro 3.3
			---> edad :  32
			.......................................................................................................
	
    MAXIMO y MINIMO:
        Con estos comandos podra buscar entre los datos cual es el menor o el mayor de todos
		los registros. Para poder usar este comando, de primero escribe MAXIMO o MINIMO, y
		despues se escribe el dato que desea conocer su valor maximo o minimo. Esto solo aplica
		para la Edad y Promedio, si por alguna razon escribiera nombre o activo el programa le 
		mandara un mensaje de error. Ejemplo Comando:
		
		    MAXIMO edad

			---> edad  MAX :  300

			MINIMO promedio

			--> promedio  MIN :  14
			
	SUMA:
	    Con este comando se podra hacer la suma total de las edades o promedios de todos los
        registros. Ejemplo Comando:

            SUMA edad

			---> Suma de  edad  :  413

    CUENTA: 
        Con este comando se puede saber cuantos registros hay en total por todos los archivos
        cargados en memoria. Si por alguna razon se llegara a escribir algun texto despues de 
        de este comando, simplemente no hara nada ya que este comando funciona solo escribiendo
        CUENTA.	Ejemplo Comando:

			CUENTA

			---> Cantidad de Registros:  6

			
    REPORTAR n:
        La funcionalidad de este comando es crear un documento HTML donde se podra visualizar
        de forma organizada la cantidad de registros que el usuario desee. Para esto el usuario
        debera escribir el comando REPORTAR y seguido de esto ingresar el numero de registros 
        que quiera visualizar en el documento. Si el usuario escribi un numero que sea mayor al    
        numero de registros que se hayan cargado en memoria, se mostrar un mensaje de error en 
        la consola. Pasara lo mismo si ingresa algun caracter o letra. De lo contrario si todos
        ha salido bien se mostrara un mensaje en consola confirmando la creacion del HTML y este
        se abrira automaticamente en su navegador.	Ejemplo Comando:
		
			REPORTAR 4

			-----------------------> Archivo HTML Creado con Exito :) <------------------------------

    SALIR :
        Al escribir el comando SALIR el programa terminara de ejecutarse.