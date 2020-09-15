#Elaborar un programa que pregunte dos numeros enteros, que decida
# cual de los dos numeros es mayor, y que diga cual es el resultado de
# restarle al numero mayor el numero menor
# si son iguales el programa debe indicarlo

#10 and 15; 15+ diferencia = 5

import re


while True:
    _numero1=input("Ingresa el primer numero: ")
    if re.findall("^\d+(\.\d+)?$", _numero1):
        numero1 = int(_numero1)
        _numero2=input("Ingresa el segundo numero: ")
        if re.findall("^\d+(\.\d+)?$", _numero2):
            numero2 = int(_numero2)
            print(f"Los numeros ingresados fueron: {numero1}, {numero2}")
            print(f"--------------------------")
            if numero1 != numero2:
                if numero1 > numero2:
                    diferencia = numero1 - numero2
                    print(f"El numero {numero1} es mayor a {numero2}")
                    print(f"La diferencia entre los numeros es de: {diferencia}")
                    print(f"--------------------------")
                    break
                else:
                    diferencia = numero2 - numero1
                    print(f"El numero {numero2} es mayor a {numero1}")
                    print(f"La diferencia entre los numeros es de: {diferencia}")
                    print(f"--------------------------")
                    break
            else:
                print(f"Los numeros ingresados son iguales {numero1}, {numero2}")
                print(f"Los numeros no tienen diferencia")
                print(f"--------------------------")
                break
        else:
            print("No es un numero\n")
            break
    else:
        print("No es un numero\n")
        break