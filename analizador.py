import re

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
    
def busqueda(ruta):
    cantidad = 0
    palabra_busca = input("Ingrese la palabra que desea buscar: ").strip().lower()  # Convertimos a minúsculas
    
    with open(ruta, "r") as fp:
        for linea in fp:
            palabras = linea.split()
            for palabra in palabras:
                if palabra.lower() == palabra_busca:
                    cantidad += 1

    print(f"La palabra '{palabra_busca}' aparece {cantidad} veces.")

    
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

    opcion = input("[1] mostrar [2] guardar en txt [3] buscar palabra [else] salir").strip()

    if opcion == "1":
        print(salida)
    elif opcion == "2":
        with open("informe.txt", "w") as archivo:
            archivo.write(salida)
        print("Guardado aqui mismo como: 'informe.txt'")
    elif opcion == "3":
        busqueda(ruta)
    else:
        print("Cancelando...")
    

while True:
    print("Bienvenido al lector de log's")
    ruta = input("Diga la ruta de su fichero: ")
    informe(ruta)
    