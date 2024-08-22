#IMPORTS
import clases
import numpy as np
import random
import os

#VARIABLES
NUM_JUGADORES = 4
DIMENSIONES_X = 20
DIMENSIONES_Y = 20
NUM_EJERCITOS = 4
FUERZAS_INICIALES = 100
#TABLERO = np.zeros((DIMENSIONES_X,DIMENSIONES_Y))
TABLERO = []
ejercitos = []

def main():
    inicializarTablero()
    turno = 1
    # Por cada jugador inicializo sus ejercitos
    for jugador in range(NUM_JUGADORES):
        errorGenerador = True
        while (errorGenerador):
            ejercitosJugador = []
            errorGenerador = generarEjercitos(jugador, ejercitosJugador)
        ejercitos.extend(ejercitosJugador)

    for ejercito in ejercitos:
        # Colocar los ejercitos en el tablero. 
        x,y = ejercito.getPosicionEjercito()
        TABLERO[x][y] = ejercito
    
    imprimirTablero()

    esEstadoFinal = comprobarEstadoFinal()
    while(not esEstadoFinal):
        #mientras no estemos en el estado final, ejecuto un turno.         
        turnoJugadores(turno)
        #ejecutarAccionesJugadores()


        #NOTA: Asigno un True al estado final para evitar bucles infinitos por error.
        esEstadoFinal = True #comprobarEstadoFinal()

# Cada jugador elige que hacer. 
def turnoJugadores(turno):
    for jugador in range(NUM_JUGADORES):
        accion = menuAccionesJugador(turno, jugador)
        match accion:
            case 1:
                print ("  ---> Accion: Mover ejercito")
            case 2:
                print ("  ---> Accion: Anular movimiento")
            case 3: 
                print ("  ---> Accion: Fusionar ejercitos")
            case 4: 
                print ("  ---> Accion: Dividir ejercitos")
            case 5: 
                print ("  ---> Accion: Tomar posiciones")
            case 6: 
                print ("  ---> Accion: Descansar")
            case 7: 
                print ("  ---> Accion: Entrenarse")
            case 8: 
                print ("  ---> Accion: Visualizar ejercitos")
            case 9: 
                #print ("  ---> Accion: Visualizar enemigos")
                imprimirTableroEnemigosJugador(jugador)
            case 10: 
                print ("  ---> Accion: Visualizar batallas")
            case 11: 
                print ("  ---> Accion: Pasar turno")

# Se ejecutan las acciones de todos los jugadores in orden. 
#  *Salvo aquellas que son las de mostrar que esas ya se han ejecutado. 
def ejecutarAccionesJugadores():
    pass




def menuAccionesJugador(turno,jugador) -> int:
    accion = 0
    #clear()
    print ("")
    print ("+-------------------------------------+")
    print (f"|  Turno: {turno}  Jugador: {jugador} [{chr(jugador+1)}] ")
    print ("+-------------------------------------+")
    print ("| 1- Mover ejercito.")
    print ("| 2- Anular movimiento.")
    print ("| 3- Fusionar ejercitos.")
    print ("| 4- Dividir ejercitos.")
    print ("| 5- Tomar posiciones.")
    print ("| 6- Descansar.")
    print ("| 7- Entrenarse.")
    print ("| 8- Visualizar ejercito.")
    print ("| 9- Visualizar enemigos.")    
    print ("| 10- Visualizar batallas.")
    print ("| 11- Pasar turno.")
    print ("+-------------------------------------+")
    
    try:
        accion = int(input("Opcion:"))
    except:
        accion = 0

    while(accion <1 or accion >11):
        try:
            accion = int(input("Opcion:"))
        except:            
            accion = 0

    return accion

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    

def generarEjercitos(jugador, ejercitosJugador) -> bool:
    soldadosJugador = FUERZAS_INICIALES
    for ejercito in range(NUM_EJERCITOS): 
        if ejercito < 3:
            if(soldadosJugador > 1):
                fuerzas_ejercito = random.randint(1,soldadosJugador)
            else:
                fuerzas_ejercito = 1
            soldadosJugador -= fuerzas_ejercito
        else:
            fuerzas_ejercito = soldadosJugador           
            if(fuerzas_ejercito <= 0):
                return True

        ej = clases.Ejercito(identificador=ejercito,jugador=jugador,numeroSoldados=fuerzas_ejercito)

        x,y = obtenerCoordenadaLibre()
        
        ej.moverEjercito(x,y)
        ejercitosJugador.append(ej)      
    
def obtenerCoordenadaLibre():
    #Las posiciones del tablero van desde 0 a DIMENSION -1 
    posicionX = random.randint(0,DIMENSIONES_X-1)
    posicionY = random.randint(0,DIMENSIONES_Y-1)
    valorPosicion = TABLERO[posicionX][posicionY]
    if(valorPosicion != None):        
        return obtenerCoordenadaLibre()
    else:
        return posicionX,posicionY

def comprobarEstadoFinal():
    #El estado final llega cuando solo quedan ejercitos de un solo jugador. 
    # Es decir, estaremos en el final, si no hay cambio de jugador
    hayCambioJugador = False
    primerJugador = ejercitos[0].getNumeroJugador() 
    for ejercito in ejercitos:
        if(primerJugador != ejercito.getNumeroJugador()):
            hayCambioJugador = True
    
    return not hayCambioJugador

def inicializarTablero():    
    for i in range(DIMENSIONES_X):
        lista = []
        for j in range(DIMENSIONES_Y):
            #TABLERO[i][j] = None
            lista.append(None)

        TABLERO.append(lista)

def imprimirTablero():
    primeraLinea = "    "
    for d in range(DIMENSIONES_Y):
        if(d<10):
            primeraLinea += f"{d}   "
        else:
            primeraLinea += f"{d}  "
    print(primeraLinea)

    for i in range(DIMENSIONES_X):
        #Hay que poner 10
        if(i<10):
            linea = f"{i}  "
        else:
            linea = f"{i} "
        
        for j in range(DIMENSIONES_Y):
            if(TABLERO[i][j]==None):
                linea += "[ ] "
            else:
                linea += f"[{chr(TABLERO[i][j].getJugador()+1)}] "

        print(linea)

'''
'''
def imprimirTableroEnemigosJugador(jugador):
    ejercitosJugador = obtenerEjercitosJugador(jugador)
    primeraLinea = "    "
    for d in range(DIMENSIONES_Y):
        if(d<10):
            primeraLinea += f"{d}   "
        else:
            primeraLinea += f"{d}  "
    print(primeraLinea)
    for i in range(DIMENSIONES_X):
        if(i<10):
            linea = f"{i}  "
        else:
            linea = f"{i} "
        
        for j in range(DIMENSIONES_Y):
            if(TABLERO[i][j] == None):
                linea += "[ ] "
            else:
                #Hay un ejercito
                ejercito = TABLERO[i][j]
                if(ejercito.getJugador()==jugador):
                    #Si el ejercito es del jugador, muestro su ejercito en el tablero
                    linea += f"[{chr(jugador+1)}] "
                else:
                    #Comprobar la visibilidad. 
                    if(determinarVisibilidadEjercito(ejercito,ejercitosJugador)):
                        linea += f"[{chr(ejercito.getJugador()+1)}] "
                    else:
                        linea += "[ ] "
        print(linea)
                    


def determinarVisibilidadEjercito(ejercito, ejercitosJugador):
    posXEnemigo,posYEnemigo=ejercito.getPosicionEjercito()
    for ejercitoJugador in ejercitosJugador:
        posX,posY = ejercitoJugador.getPosicionEjercito()
        soldados = ejercitoJugador.getNumeroSoldados()
        visibilidad = 0
        if(soldados < 100):
            #visibilidad una casilla.
            visibilidad = 1
        elif(soldados >= 100 and soldados <=999):
            #visibilidad dos casillas.
            visibilidad = 2
        else:
            #visibilidad tres casillas. 
            visibilidad = 3
        inicioX = posX - visibilidad
        finX = posX + visibilidad
        inicioY = posY - visibilidad
        finY = posY + visibilidad
        for i in range(inicioX,finX):
            for j in range(inicioY,finY):
                if(i==posXEnemigo and j==posYEnemigo):
                    #Si coincide, dicho ejercito es visible. 
                    return True
        #Si llego aqui, el ejercito no es visible por el jugador.
    return False

def obtenerEjercitosJugador(jugador):
    ejercitosJugador = []
    for ejercito in ejercitos:
        if(ejercito.getJugador()==jugador):
            ejercitosJugador.append(ejercito)
    return ejercitosJugador

if __name__ == "__main__":
    main()
