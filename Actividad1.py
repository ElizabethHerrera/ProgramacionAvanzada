import re
import unicodedata

# Elaborar un programa que pregunte tres datos: matricula, nombre y correo
# [X] la matricula es un numero de 7 posiciones,
# [X] el nombre es un texto que contiene letras mayusculas y espacios, sin acentos no menor 10 a mayor a 40
# [X] el correo es un correo con formato valido

#Funcion para quitar acentos y respetar la
def quitarAcentos(a):
    x = (a.find("Ñ") == -1)
    y = (a.find("ñ") == -1)
    _accentString = a

    if x!=True or y!=True:
        _accentString=_accentString.replace('Ñ','-&-')
        _accentString=_accentString.replace('ñ','-%-')
        _accentString= str(unicodedata.normalize('NFKD', _accentString).encode('ascii','ignore'))[2:-1]
        _unaccentString = _accentString.replace('-&-','Ñ')
        _unaccentString = _unaccentString.replace('-%-','ñ')

        unaccentString=_unaccentString
        return unaccentString
    else:
        unaccentString= str(unicodedata.normalize('NFKD', _accentString).encode('ascii','ignore'))[2:-1]
        return unaccentString

# MENU ---
while True:
    print("---- Menu ----")
    print("1) Ingresar usuario -- 2) Salir")
    _opcion=input("Seleccione una opción: ")

    if re.findall("^\d+(\.\d+)?$", _opcion):
        opcion=int(_opcion)
        if opcion <= 2 and opcion >= 1:
            if opcion == 1:
                nameVal = True
                while nameVal == True:
                    _nombre=input("Ingresa tu nombre completo: ")
                    if re.findall("[a-zA-Z]", _nombre):
                        nombre=quitarAcentos(_nombre)
                        if len(nombre) < 10 or len(nombre)>40:
                            print("El nombre es muy corto o muy largo")
                        else:
                            matriculaVal = True
                            while matriculaVal == True:
                                _matricula=input("Ingresa tu matricula [7 digitos]: ")
                                if re.findall("^\d+(\.\d+)?$", _matricula):
                                    correoVal = True
                                    while correoVal == True:
                                        _correo=input("Ingresa tu correo electronico: ")
                                        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', _correo)

                                        if match == None:
                                            print("Correo invalido")
                                            _correo=""
                                        else:
                                            print("-" * 15)
                                            print("=== Datos ingresados ===")
                                            print(f"Nombre: {nombre}")
                                            print(f"Matricula: {'%.7s' % _matricula}")
                                            print(f"Correo: {_correo}")
                                            print("-" * 15)
                                            correoVal = False
                                            matriculaVal = False
                                            nameVal = False
                                            _correo=""
                                            _matricula=""
                                            _nombre=""
                                else:
                                    print("Matricula invalida\n")
                                    _matricula=""
                    else:
                        print("Valores ingresados no validos\n")
                        _nombre=""

            elif opcion == 2:
                print("Fin del programa")
                break
        else:
            print("Opción no encontrada\n")
    else:
	    print("Se requiere un número entre las opciones\n")