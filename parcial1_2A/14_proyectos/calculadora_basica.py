from funciones_compartir import esperar_confirmacion
import math

def solicitarNumeros():
     global n1,n2
     n1=int(input("Numero # 1:"))
     n2=int(input("Numero # 2:"))


def calculadora(n1,n2,opcion):
     if opcion=="1" or opcion=="+" or opcion=="SUMA":
         return f"{n1}+{n2}={n1+n2}"
     
     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
         return f"{n1}-{n2}={n1-n2}"
     
     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
         return f"{n1}*{n2}={n1*n2}"
     
     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
         return f"{n1}/{n2}={n1/n2}"
     
     elif opcion=="5" or opcion=="**" or opcion=="POTENCIA":
         return f"{n1} a la{n2}={n1**n2}"
     
     elif opcion=="6" or opcion=="R" or opcion=="RAIZ":
         return f" La raiz de {n1} es {math.sqrt(n1)}"
        

opcion=True

while opcion:
     print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- Potencia \n 6.- Raiz \n 7.- SALIR ")
     opcion=input("\t Elige una opción: ").upper()
     if opcion != "7":
         solicitarNumeros()
         print(calculadora(n1,n2,opcion))
         esperar_confirmacion()
     else:
         opcion=False
         print("Gracias por utilizar el sistema ...")




