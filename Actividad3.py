import re
import datetime
import unicodedata

dicMeses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio",
8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

usuarioslista = []

mes30 = (4, 6, 9, 11)

def yearLeap(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

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

def fechaNacimiento():
    yearVal = True
    mesVal = True
    diaVal = True

    while yearVal == True:
        print("Ingresa fecha de nacimiento")
        _fyear=input("Ingresa el año: ")
        if re.findall("^\d+(\.\d+)?$", _fyear):
            if len(_fyear)>5 or len(_fyear)<=0:
                print("Año no encontrado")
            else:
                fyear = int(_fyear)
                while mesVal == True:
                    _imes=input("Ingresa el mes: ")
                    if re.findall("^\d+(\.\d+)?$", _imes):
                        imes = int(_imes)
                        if imes>=13 or imes<=0:
                            print("Mes no encontrado")
                        else:
                            if imes in dicMeses:
                                fmes = dicMeses[imes]
                            while diaVal == True:
                                _idia=input("Ingresa el dia: ")
                                if re.findall("^\d+(\.\d+)?$", _idia):
                                    idia = int(_idia)
                                    if imes in mes30:
                                        if idia >31 or idia<=0:
                                            print ("fecha no existente")
                                        else:
                                            fmes = dicMeses[imes]
                                            return idia, fmes, fyear
                                    elif imes == 2:
                                        _x = yearLeap(fyear)
                                        if _x != 1:
                                            if idia >28 or idia<=0:
                                                print ("fecha no existente")
                                            else:
                                                fmes = dicMeses[imes]
                                                return idia, fmes, fyear
                                        else:
                                            if idia >29 or idia<=0:
                                                print ("fecha no existente")
                                            else:
                                                fmes = dicMeses[imes]
                                                return idia, fmes, fyear
                                    else:
                                        if idia >32 or idia<=0:
                                            print ("Dia no existente")
                                        else:
                                            fmes = dicMeses[imes]
                                            return idia, fmes, fyear
                                else:
                                    print("Ingrese un valor númerico")
                    else:
                        print("Ingrese un valor númerico")
        else:
            print("Ingrese un valor númerico")

def pedirDatos():
    nameVal = True

    while nameVal == True:
        _nombre=input("Ingresa tu nombre completo: ")
        if re.findall("[a-zA-Z]", _nombre):
            nombre=quitarAcentos(_nombre)
            if len(nombre) < 10 or len(nombre)>40:
                print("El nombre es muy corto o muy largo")
            else:
                _fnacimiento = fechaNacimiento()
                matriculaVal = True
                while matriculaVal == True:
                    _matricula=input("Ingresa tu matricula [7 digitos]: ")
                    matricula= _matricula[0:6]
                    matricula=int(matricula)
                    if re.findall("^\d+(\.\d+)?$", _matricula):
                        correoVal = True
                        while correoVal == True:
                            correo=input("Ingresa tu correo electronico: ")
                            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', correo)

                            if match == None:
                                print("Correo invalido")
                                correo=""
                            else:
                                txt = "{0}/{1}/{2}"
                                #print("-" * 15)
                                #print("=== Datos ingresados ===")
                                #print(f"Nombre: {nombre}")
                                #print(f"Matricula: {'%.7s' % _matricula}")
                                #print(f"Correo: {correo}")
                                #print("-" * 15)
                                fnacimiento = str((txt.format(_fnacimiento[0], _fnacimiento[1], _fnacimiento[2])))
                                return nombre, fnacimiento, matricula, correo
                    else:
                        print("Matricula invalida\n")
                        _matricula=""
        else:
            print("Valores ingresados no validos\n")
            _nombre=""
# MENU ---
while True:
    print("---- Menu ----")
    print("1) Ingresar usuario -- 2) Mostrar usuarios -- 3) Salir")
    _opcion=input("Seleccione una opción: ")

    if re.findall("^\d+(\.\d+)?$", _opcion):
        opcion=int(_opcion)
        if opcion <= 2 and opcion >= 1:
            if opcion == 1:
                usuario = pedirDatos()
                usuarioslista.append(usuario)
                print("-" * 15)
                print("--- Datos del usuario ---")
                for dato in usuario:
                    print(dato)
                print("-" * 15)
            elif opcion == 2:
                n=0
                print("--- Usuarios ingresados ---")
                for u in usuarioslista:
                    for dato in u:
                        print(dato)
                    print("--")
                    n=n+1
            elif opcion == 3:
                print("Fin del programa")
                break
        else:
            print("Opción no encontrada\n")
    else:
	    print("Se requiere un número entre las opciones\n")