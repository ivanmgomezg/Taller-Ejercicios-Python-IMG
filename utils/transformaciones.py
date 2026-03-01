# Funciones con transformaciones de texto y datos
import codecs #Para la decodificación ROT13

#Defino una función para decodificar el texto usando ROT13
def rot13(texto): 
    return codecs.decode(texto, "rot13")