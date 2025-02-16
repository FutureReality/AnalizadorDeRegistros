import re

def contar(ruta):
    lineas = []
    #abre el archivo en modo de lectura, cuenta las lineas y las pasa
    #como variables de una en una
    with open(ruta, "r") as fp:
        for count, line in enumerate(fp):
            if line.strip():
                lineas.append(line.strip())
    return count + 1, lineas

def tipos(linea):
    #Se definen los tres tipos de log
    tipo_warning = []
    tipo_error = []
    tipo_info = []
    
    linea = linea.lower()
    palabras = linea.split()
    
    #Se organizan segun el tipo de log en las tres categorias anteriores
    for palabra in palabras:
        if palabra == "info:":
            tipo_info.append(linea)
        elif palabra == "error:":
            tipo_error.append(linea)       
        elif palabra == "warning:":
            tipo_warning.append(linea)
       
    #los devuelve com valores para ser utilizados de forma escalable
    return tipo_error, tipo_info, tipo_warning

def direcciones(frase):
    ips = []
    #Esta es la forma en la que se escriben las IP's
    CRITERIO_BUSQUEDA = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b" 

    #dividimos el log pasado en palabras que puedan ser comparadas con el criterio
    palabras = frase.split() 
    for palabra in palabras:
        if re.fullmatch(CRITERIO_BUSQUEDA, palabra): 
            ips.append(palabra)

    #Devolvemos las IP's encontradas
    return ips
    
def busqueda(ruta):
    cantidad = 0
    #Usamos el strip para eliminar espacios en blanco y el lower para volverlo a minusculas
    palabra_busca = input("Ingrese la palabra que desea buscar: ").strip().lower()
    
    #Realizamos una busqueda de las palabras, similar al modulo primero
    with open(ruta, "r") as fp:
        for linea in fp:
            palabras = linea.split()
            for palabra in palabras:
                if palabra.lower() == palabra_busca:
                    cantidad += 1

    print(f"La palabra '{palabra_busca}' aparece {cantidad} veces.")

    
def informe(ruta):
    #seteamos todas las variables
    total_registros, lineas = contar(ruta)
    errores = []
    warnings = []
    infos = []
    ips_encontradas = []
    
    NOMBRE_INFORME = "informe.txt"
    
    for linea in lineas:
        #Recopilamos toda la informacion
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

    opcion = input("[1] mostrar [2] guardar en txt [3] buscar palabra [else] salir").strip()

    #Opciones que puede elegir el usuario
    if opcion == "1":
        print(salida)
    elif opcion == "2":
        with open(NOMBRE_INFORME, "w") as archivo:
            archivo.write(salida)
        print(f"Guardado aqui mismo como: '{NOMBRE_INFORME}'")
    elif opcion == "3":
        busqueda(ruta)
    else:
        print("Cancelando...")
    

while True:
    print("Bienvenido al lector de log's")
    ruta = input("Diga la ruta de su fichero: ") #En windows funciona raro
    informe(ruta)
    
