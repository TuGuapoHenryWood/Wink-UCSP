# El primer mensaje de nuestro programa junto con el import random, para ya tener nuestra logica matematica implementada
print("\n- - - - [ W;NK ] - - - -")
import random


#_________________LISTAS Y DICCIONARIOS________________________________________________________________________________#


# Piropos que tienen lenguaje mas intenso, con contexto de mismo nivel (ha sido advertido profesor)
piropos_fuertes = {"Esta lloviendo o porque tan mojada?": "- Jean Marc Neadeau",
           "Ojala fuera Ukrania y yo misil... para bombardearte las nalgas": "- Carlos Huaylla",
           "A vecez quisiera olvidarte... pero sin el olvi": "- Bianca Diaz",
           "Yo nunca te pondria un dedo encima... adentro si como 3, pero nunca encima": "- Guillermo Aaron",
           "Amia pa ka charte": "- Rodrigo Sierra",
           "Juguemos al Titanic, yo soy el barco... y tu me la hundes": "- Alyson Perez",
           "Quisiera ser carro... para recorrer tus curvas": "- Matias Colan",
           "Eres un Ferrari? Que tal cola": "- Sebastian Chana",
           "Quisiera ser mariachi... para tocarte la Cucaracha": "- Gabriel Olaechea"}

# Piropos que tienen lenguaje menos intenso, con contexto de mismo nivel
piropos_suaves = {"La luna sale a caminar siguiendo tus pupilas": "- Renato Corales",
           "Me gustan tus ojos azules": "- Elmer Santiago",
           "Te quiero como la champions": "- Santiago Sotillo",
           "Hola :)": "- Oscar Zuniga",
           "Me gustas": "- Yorlenny Valdivia",
           "Si tu cuerpo fuera carcel, y tus labios condena, que bonita sentencia para mi": "- Elias Gonzales",
           "Eres como Google... porque en ti encuentro todo lo que busco": "- Walter Valdivia",
           "Juguemos Minecraft... yo consigo, tu construyes": "- Gabriel de la Colina",
           "Mejor que ella me hable": "- Alexis Raul",
           "Acaso te llamas luz? o por que iluminas mi vida?": "- Gabrielle Ore",
           "Desde que te vi... me di cuenta que mis ojos siempre han estado vacios": "- Nikolas Zuniga",
           "Tienes un diccionario, porque cuando te vi... me quede sin palabras": "- Franco Zegarra",
           "Con esos ojos mirandome... no me hace falta la luz del sol": "- Iair Suico",
           "Are you a rose... if not... you must be ugly": "- Abdu",
           "Quisiera ser una tabla de ajedrez... para tenerte como reina": "Kelvin Caya",
           "Si Adan por Eeva se comio una manzana... yo por ti me comeria una fruteria": "Renato Quispe",
           "Se te cayo un papel... el que te envuelve bonbon": "I.V.U"}

# Lista de piropos guardados segun el usuario
bookmarks = []

# Lista personal que se puede formar usando los piropos de la lista bookmarks
listaPersonal = []


#_________________FUNCIONES____________________________________________________________________________________________#


# Generador de piropos, extrae una llave de un diccionario segun el tipo elegido por el usuario, el tipo define si es suave o fuerte
def generarPiropo(tipo):
    global piropoActual
    global autorPiropoActual

    if (piropos_suaves == {}):
        print("\nYA NO QUEDAN PIROPOS SUAVES:(\n")
        quit()
    elif (piropos_fuertes == {}):
        print("\nYA NO QUEDAN PIROPOS FUERTES:(\n")
        quit()
    elif (piropos_suaves == {} and piropos_fuertes == {}):
        print("\nYA NO QUEDAN PIROPOS:(\n")
        quit()

    if(tipo == 0):
        gamaPiropo()
    elif (tipo == 1):
        piropoActual = random.choice(list(piropos_suaves.keys()))
        print("\n\n- - - [ GENERAR PIROPO ] - - -")
        print("\n" + str(piropoActual) + "\n")
    elif (tipo == 2):
        piropoActual = random.choice(list(piropos_fuertes.keys()))
        print("\n\n- - - [ GENERAR PIROPO ] - - -")
        print("\n" + str(piropoActual) + "\n")

# Gama piropo llama generarPiropo utilizando un input que lo convierte a el tipo que pido como parametro generarPiropo()
def gamaPiropo():
    intensidad = int(input("\nSUAVE [1] --- FUERTE [2] === "))
    generarPiropo(intensidad)

# Pagina inicial donde se puede acceder a las funciones principales del programa
def menuPrincipal():
    while True:
        menu = input("\nINICIAR [ENTER]\n"
                     "PIROPOS GUARDADOS [1]\n"
                     "CREAR PIROPO [2]\n"
                     "CREAR LISTA [3]\n"
                     "CREDITOS [4]\n"
                     "CERRAR [5]\n"
                     "  [] = ")
        if (menu == "1"):
            input("\nPIROPOS GUARDADOS: " + str(bookmarks))
        elif (menu == "2"):
            crearPiropo()
        elif (menu == "3"):
            crearLista()
        elif (menu == "4"):
            creditos()
        elif (menu == "5"):
            quit()
        elif (menu == ""):
            return True

# Guarda el piropo actual en la lista vacia bookmarks[]
def guardarPiropo():
    bookmarks.append(piropoActual)
    input("\nPIROPOS GUARDADOS:\n" + "\n".join(bookmarks))

# Misma funcion que guardaPiropo, la unica diferencia es que aquel piropo guardado recien fue creado
def guardarPiropoPersonal():
    bookmarks.append(piropoPersonalizado)
    input("\nPIROPOS GUARDADOS:\n" + "\n".join(bookmarks))

# Borra el piropo actual del diccionario en el que se encuentra
def borrarPiropo():
    if (piropoActual in piropos_suaves):
        piropos_suaves.pop(piropoActual)
    elif (piropoActual in piropos_fuertes):
        piropos_fuertes.pop(piropoActual)

    input("\nBORRASTE ESTE PIROPO: " + str(piropoActual))

# Misma funcion que boorarPiropo, la unica diferencia es que aquel piropo borrado recien fue creado
def borrarPiropoPersonal():
    if(piropoPersonalizado in piropos_suaves):
        piropos_suaves.pop(piropoPersonalizado)
    elif (piropoPersonalizado in piropos_fuertes):
        piropos_fuertes.pop(piropoPersonalizado)

    input("\nBORRASTE ESTE PIROPO: " + str(piropoPersonalizado))

# Muestra el autor del piropo, osea el valor de la llave dentro del diccionario
def autorPiropo():
    if(piropoActual in piropos_suaves):
        input("\nAUTOR/A " + piropos_suaves.get(piropoActual))
    if (piropoActual in piropos_fuertes):
        input("\nAUTOR/A " + piropos_fuertes.get(piropoActual))

# Permite crear una lista personal donde de los piropos guardados, se pueden extraer ciertos, y meter en una lista personal
def crearLista():
    if(bookmarks == []):
        input("\nNO TIENES PIROPOS GUARDADOS AUN")
    else:
        seleccion = int(input(
            "\nCUAL [N°] DE PIROPO DE " + "\n".join(bookmarks) + "\nDESEAS TENER EN TU LISTA " + "\n".join(listaPersonal) + ": "))
        listaPersonal.append(bookmarks[seleccion - 1])
        input("\nLISTA PERSONAL = " + str(listaPersonal))

# Creditos del programa
def creditos():
    input("\nMUCHAS GRACIAS PROFESOR Y COMPAÑEROS\n"
          "En honor de Afrodita\n ...la diosa del AMOR\n\n"
          "Creador del Programa\n"
          " ... Henry Wood")

# A travez de un input, se puede crear un piropo con autor definido, y se puede guardar o borrar
def crearPiropo():
    global piropoPersonalizado
    intensidad = int(input("\nGAMA DE PIROPO:\nSUAVE [1] --- FUERTE [2] === "))
    piropoPersonalizado = input("\n- INSERTA TU PIROPO -\n")
    autorPiropoPersonalizado = input("\n- NOMBRE DE AUTOR -\n")

    manejo = input("\n" + piropoPersonalizado + "\n    -" + autorPiropoPersonalizado + "\n\nGUARDAR [1] --- BORRAR [2] --- CONTINUAR [ENTER] === ")
    if (manejo == "1"):
        guardarPiropoPersonal()
    elif (manejo == "2"):
        borrarPiropoPersonal()

    if(intensidad == 1):
        piropos_suaves.update({piropoPersonalizado: autorPiropoPersonalizado})
    elif(intensidad == 2):
        piropos_fuertes.update({piropoPersonalizado: autorPiropoPersonalizado})

# Inicamos el programa con menu principal, y esperar a que el usuario interactue con el programa
def inicoPrograma():
    menuPrincipal()
    generarPiropo(0)


#_________________PROGRAMA VISUALIZADO_________________________________________________________________________________#


# Desde este punto se visualiza el programa en la consola, y el loop mantiene el orden de las funciones, para una experiencia fluida
inicoPrograma()
while True:
    opcion = input("\nGUARDAR [1] --- BORRAR [2] --- AUTOR [3] --- MENU [4] --- CONTINUAR [ENTER] === ")
    if(opcion == "1"):
        guardarPiropo()
    elif(opcion == "2"):
        borrarPiropo()
        gamaPiropo()
    elif(opcion == "3"):
        autorPiropo()
    elif(opcion == "4"):
        inicoPrograma()
    else:
        gamaPiropo()