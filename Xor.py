import sys


################################### FUNCIONES PRINCIPALES ###################################################

"""Función que se encarga de descifrar con xor un arreglo y guardarlo en un archivo

file_bytes.- Arreglo donde cada elemento es un int equivalente a un byte
name.- Nombre del archivo de salida
"""
def decrypt(file_bytes,name):
    #Encuentra la llave por medio de fuerza bruta
    key = give_key_brute(file_bytes)
    #Verifica que se haya logrado encontrar la llave
    if key != -1:
        #Aplica la función xor a todo el arreglo utilizando la llave
        xor_bytes = xor(file_bytes,key)
        #index_c = get_index_two(xor_bytes,77,90)
        #Quitar la cabecera de xor_bytes
        #xor_bytes = xor_bytes[index_c:-1]
        #Crea un archivo nuevo o en caso de exitir uno con el mismo nombre elimina su contenido
        new_file = open(name,'wb')
        #Crea un arreglo de bytes a partir del arreglo de ints y lo escribe en el archivo
        a = bytearray(xor_bytes)
        new_file.write(a)
    else:
        #En caso de no haber encontrado una key notifica al usuario
        print("No fue posible encontrar la llave")

"""Dado un arreglo donde cada elemento representa un byte y se encuentra supuestamente cifrado, 
   obtiene por medio de fuerza bruta una llave de un byte para descifrar por xor este arreglo

bytes.- arreglo que representa los bytes supuestamnete cifrado bajo xor
"""
def give_key_brute(bytes):
    #itera probando todas las posibles llaves de 1 byte (En hexal 00 =0, FF = 255)
    for i in range(0,255):
        if is_key(bytes,i,windows_exec_identifier):
            #print("La llave es:")
            #print(i)
            return i
    #Si no encuentra ninguna llave valida regresa este valor
    return -1

################################## FUNCIONES SECUNDARIAS ###################################################

""""Recibe un archivo y lo convierte en un arreglo de ints donde cada entero representa un byte del archivo

file.- nombre del archivo que se abrira
"""
def file_to_bytes(file):
    #Se abre el archivo como binario y se lee todo su contenido en 'hexa_bytes'
    fileO = open(file,'rb')
    hexa_bytes = fileO.read()
    fileO.close()
    
    #Se convierte cada byte en su equivalente en int y se guarda en el arreglo dec_bytes
    dec_bytes = [byte for byte in hexa_bytes]
    return dec_bytes

"""Verifica si para un arreglo la llave pasada sirve para descifrarlo con la función xor.

bytes.- arreglo de ints donde cada int representa un byte.
key.- llave candidata
verify_arr.- un arreglo que debe encontrarse en el arreglo ya descifrado. En este arreglo cada elemeto
             esta en su forma hexadecimal y representa un byte
"""
def is_key(bytes,key,verify_arr):
    #se aplica la función xor a todo el arreglo
    file_bytes_dec = xor(bytes,key)
    #se convierte todos los elementos del arreglo a verificar a int para poder compararlo
    verify_arr_dec = [int(byte,16) for byte in verify_arr]
    #se regresa si este arreglo si fue encontradp
    return is_sublist(file_bytes_dec,verify_arr_dec)

"""Aplica xor a todos los elementos de un arreglo con una llave dada

bytes.- arreglo de ints donde cada int representa un byte
key.- llave de un byte
"""
def xor(bytes,key):
    xor_bytes = [byte ^ key for byte in bytes]
    return xor_bytes

##################################### FUNCIONES AUXILIARES ######################################

"""Dice si un arreglo es sub arreglo de otro
"""
def is_sublist(a,b):
    if len(a)>=len(b):
        i = 0
        for elem in a:
            if i == len(b):
                return True
            if elem == b[i]:
                i = i+1
            else:
                i = 0   
    return False

"""Encuentra la primera aparición de a en l

"""
def get_index(l,a):
    for i in range(len(l)):
        if l[i] == a:
            return i

"""Encuentra la primera aparición de a y b seguidos en l

"""
def get_index_two(l,a,b):
    index = get_index(l,a)
    if index:
        if l[index+1] == b:
            return index
        else:
            new_l = l[(index+1):-1]
            return get_index_two(new_l,a,b)




############################ EJECUCIÓN DEL PROGRAMA ############################################


""""Arreglo que representa una cadena común en archivos executables de Windows.

Cada elemento del arreglo es un byte de la cadena en su representación hexadecimal.
!This program cannot be run in DOS mode.

"""
windows_exec_identifier = ["21","54","68","69","73","20","70","72","6F","67","72","61","6D",
                           "20","63","61","6E","6E","6F","74","20","62","65","20","72","75",
                           "6E","20","69","6E","20","44","4F","53","20","6D","6F","64","65"]

"""Arreglo que sera utilizado para almacenar todos los bytes del archivo y poder manipularlos.

"""
file_bytes = []

"""Se almacenara el nombre del archivo que se quiere crear.

"""
new_file_name = ""

"""Verificamos que se haya ingresado el número de argumentos correcto

"""
if len(sys.argv) == 3:
    file_bytes= file_to_bytes(sys.argv[1])
    new_file_name = sys.argv[2]

    decrypt(file_bytes,new_file_name)

    print("Tarea completada!!")

else:
    print("No se ingreso el número de argumentos correctos.")
    print("Por favor ejecute:")
    print("\n /bin/python3/ Xor.py <Archivo cifrado> <Nombre del archivo de salida>\n")

    """
    file_bytes= file_to_bytes(sys.argv[1])
    key = give_key_brute(file_bytes)
    xor_bytes = xor(file_bytes,key)

    #print(xor_bytes)
    a = [1,2,3,4,5]
    b = get_index_two(a,3,6)
    if b:
        print(b)
        """