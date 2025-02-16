from funciones import informe

while True:
    print("Bienvenido al lector de log's")
    ruta = input("Diga la ruta de su fichero: ") #En windows funciona raro
    try:
        informe(ruta)
    except FileNotFoundError:
        print(f"Error: No se encontro fichero en la ruta '{ruta}'")
    except Exception as e:
        print(f"Se produjo un error desconocido: {e}")