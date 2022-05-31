#ESCRIBE UNA FUNCIÓN QUE PIDA EL NOMBRE Y LO DEVUELVA EN MAYUSCULO

from tokenize import TokenInfo


def ejercicio1():
    
    nombre=input("Escribe un nombre")

    return nombre.upper()
    
print(ejercicio1())


#Crea una funcion que reciba un nombre y que diga cuantas palabras hay

def ejercicio2():

    cadena=input("Escribe un nombre")
    contador=0
    i=(" ")
    for i in cadena:
        if i==" ":
                contador=contador+1
    return(contador+1)    
                
print(ejercicio2()) 
            
 