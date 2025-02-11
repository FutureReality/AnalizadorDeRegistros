#1. Leer Fichero

#Pre: Entrara un fichero de tipo log con una estructura generica

#Post: Enviara datos sobre los apartados deseados




#2. Analizar fichero de registro

#2.1. Contar el numero total de registros

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
