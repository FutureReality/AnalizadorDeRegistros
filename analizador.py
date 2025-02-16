import re
#2. Analizar fichero de registro

#2.1. Contar el numero total de registros
#Este bloque de codigo fue sacado de: https://pynative.com/python-count-number-of-lines-in-file/


#Pre: Los registros siguen la misma estructura


        
#Post: Se dara el numero de registros totales sin contar lineas en blanco




#2.2. Detectar tipos de registro

#Pre: El fichero tendra siempre los mismos tipos



#Post: Se dividira segun el tipo de registro

#2.3. Identifica IP's

#Pre: Las direcciones IP seran IPv4
#Post: Se listaran todas las IPv4 al final

#2.4. Buscar por palabras clave

#Pre: El usuario no buscara simbolos ni caracteres no alfanumericos
#Post: Se dara la cantidad de veces que sale la palabra o letra.

#3. Generacion De Informe

#Pre: Se obtendran todos los datos anteriores


#Post: Se dara un fichero txt con todos los datos ateriores


#1. Leer Fichero

#Pre: Entrara un fichero de tipo log con una estructura generica



#Post: Enviara datos sobre los apartados deseados

# ---- Ya que me da algo de tiempo hare un pseudocodigo rapido

#2. Analizar fichero de registro

#2.1. Contar el numero total de registros
#Este bloque de codigo fue sacado de: https://pynative.com/python-count-number-of-lines-in-file/


#Pre: Los registros siguen la misma estructura

"""
Aqui ya se ha hecho el contador de lineas

"""

#Post: Se dara el numero de registros totales sin contar lineas en blanco




#2.2. Detectar tipos de registro



#Pre: El fichero tendra siempre los mismos tipos

"""
funcion tipos(frase):
    tipo1 = []
    tipo2 = []
    tipo3 = []
    
    palabras = dividir(frase)
    for palabra en palabras:
        si palabra == "tipo 1":
            añadir.tipo1(frase)
        si palabra == "tipo 2":
            añadir.tipo2(frase)
        si palabra == "tipo 3":
            añadir.tipo3(frase)
    
    print("Logs de -Tipo 1-")
        for frase en tipo1:
            print(frase)
    print("Logs de -Tipo 2-")
        for frase en tipo2:
            print(frase)
    print("Logs de -Tipo 3-")
        for frase en tipo3:
            print(frase)
    
"""

#Post: Se dividira segun el tipo de registro

#2.3. Identifica IP's

#Pre: Las direcciones IP seran IPv4

"""

funcion direcciones(frase):
    ips = []
    CRITERIO_BUSQUEDA = xxx.xxx.xxx.xxx #Esta constante deberia dar el patron de busqueda
    palabras = dividir(frase)
    por palabra en palabras:
        si palabra == CRITERIO_BUSQUEDA:
           añadir.ips(palabra)
    por ip en ips:
        print(ip)

"""
#Post: Se listaran todas las IPv4 al final

#2.4. Buscar por palabras clave

#Pre: El usuario no buscara simbolos ni caracteres no alfanumericos

"""

funcion busqueda(ruta):
    cantidad = 0
    palabra_busca = input()
    palabra_busca = minuscula.palabra_busca()
    
    abrir(ruta, leer) como linea:
        palabras = dividir(linea)
        por palabra en palabras:
            si palabra == palabra_busca:
                cantidad + 1
    print(cantidad)
        
    

"""

#Post: Se dara la cantidad de veces que sale la palabra o letra.

#3. Generacion De Informe

#Pre: Se obtendran todos los datos anteriores

"""
# IMPORTANTE: A los valores finales dados en las funciones se les otorga un return para devolver el valor

funcion fichero():
    cantidad = contar()
    tipo1, tipo2, tipo3 = tipos()
    direcciones = direcciones()
    print("Quieres mostrarlo en pantalla (1) o un fichero (2)")
    seleccion = input()
    si seleccion == 1:
        print(cantidad)
        print(tipo1)
        print(tipo2)
        print(tipo3)
        print(direcciones)
    si seleccion == 2:
        abrir(ruta, escribir) como archivo:
            archivo.escribir(cantidad)
            archivo.escribir(tipo1)
            archivo.escribir(tipo2)
            archivo.escribir(tipo3)
            archivo.escribir(direcciones)
            
"""

def contar(ruta):
    lineas = []
    with open(ruta, "r") as fp:
        for count, line in enumerate(fp):
            if line.strip():
                lineas.append(line.strip())
    return count + 1, lineas

def tipos(linea):
    tipo_error = []
    tipo_warning = []
    tipo_info = []
    
    linea = linea.lower()
    palabras = linea.split()
    
    for palabra in palabras:
        if palabra == "info:":
            tipo_info.append(linea)
        if palabra == "error:":
            tipo_error.append(linea)       
        if palabra == "warning:":
            tipo_warning.append(linea)
       
    return tipo_error, tipo_info, tipo_warning

def direcciones(frase):
    ips = []
    CRITERIO_BUSQUEDA = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b" 

    palabras = frase.split() 
    for palabra in palabras:
        if re.fullmatch(CRITERIO_BUSQUEDA, palabra): 
            ips.append(palabra)

    return ips
def informe(ruta):
    total_registros, lineas = contar(ruta)
    errores = []
    warnings = []
    infos = []
    ips_encontradas = []
    
    for linea in lineas:
        tipo_error, tipo_warning, tipo_info = tipos(linea)
        errores.extend(tipo_error)
        warnings.extend(tipo_warning)
        infos.extend(tipo_info)
        ips_encontradas.extend(direcciones(linea))
        
    salida = (
        f"Registros segun tupo: {total_registros}\n\n"
        
        f"Errores:\n{chr(10).join(errores)
        if errores else 'Ninguno'}\n\n"
        
        f"Warnings:\n{chr(10).join(warnings)
        if warnings else 'Ninguno'}\n\n"
        
        f"Informaciones:\n{chr(10).join(infos)
        if infos else 'Ninguna'}\n"
        
        f"\nDirecciones IP encontradas:\n{chr(10).join(ips_encontradas)
        if ips_encontradas else 'Ninguna'}\n"
    )

    opcion = input("Imprimir en pantalla (1) guardar en archivo (2) Cancelar cualquier otro").strip()

    if opcion == "1":
        print(salida)
    elif opcion == "2":
        with open("informe.txt", "w") as archivo:
            archivo.write(salida)
        print("Guardado aqui mismo como: 'informe.txt'")
    else:
        print("Cancelando...")
    

while True:
    print("Bienvenido al lector de log's")
    ruta = input("Diga la ruta de su fichero: ")
    informe(ruta)
    