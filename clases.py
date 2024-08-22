class Ejercito:     
    identificador = 0
    jugador = 0
    coordenadaX = 0
    coordenadaY = 0
    numeroSoldados = 0
    bonusDefensivo = 0
    soldados = []


    def __init__(self, identificador, jugador ,numeroSoldados):
        self.identificador = identificador
        self.jugador = jugador
        self.numeroSoldados = numeroSoldados
        self.soldados = []
        
        self.inicializarSoldados()
    
    def __repr__(self):
        fuerzaMedia = estadoMedia = experienciaMedia = 0

        infoEjercito = f" Ejercito {self.identificador}. Jugador: {self.jugador}. Posicion [{self.coordenadaX}][{self.coordenadaY}]."
        infoSoldados = f"  Soldados: {self.numeroSoldados}."
        fuerzaMedia,estadoMedia,experienciaMedia = self.calcularMediaEjercito()
        infoMedias = f"  Fuerza: {fuerzaMedia}, Estado: {estadoMedia}, Exp: {experienciaMedia}"
        return  f"{infoEjercito} {infoSoldados} {infoMedias}"
    

    '''
        Metodo que mueve un ejercito a unas coordenadas en particular. 
    '''
    def moverEjercito(self, x, y):
        self.coordenadaX = x
        self.coordenadaY = y

    def getPosicionEjercito(self):
        return self.coordenadaX, self.coordenadaY

    def getJugador(self):
        return self.jugador

    def inicializarSoldados(self):        
        for soldado in range(self.numeroSoldados):
            s = Soldado(soldado)
            #print (s)
            self.soldados.append(s)

    def calcularMediaEjercito(self):
        
        fuerzaEjercito = 0
        estadoEjercito = 0
        experienciaEjercito = 0
        #print (f" --> [1] {fuerzaEjercito} {estadoEjercito} {experienciaEjercito} {self.numeroSoldados}")
        for soldado in self.soldados:   
            #print (soldado)         
            fuerzaEjercito += soldado.fuerza
            estadoEjercito += soldado.estado
            experienciaEjercito += soldado.experiencia

        #print (f" --> [2] {fuerzaEjercito} {estadoEjercito} {experienciaEjercito} {self.numeroSoldados}")
        fuerzaMedia = round(fuerzaEjercito/self.numeroSoldados,2)
        estadoMedia = round(estadoEjercito/self.numeroSoldados,2)
        experienciaMedia = round(experienciaEjercito/self.numeroSoldados,2)

        #print (f" --> [3] {fuerzaMedia} {estadoMedia} {experienciaMedia}")

        return fuerzaMedia,estadoMedia,experienciaMedia
    
    def getNumeroJugador(self):
        return self.jugador

    def getNumeroSoldados(self):
        return self.numeroSoldados    

class Soldado: 
    identificador = 0
    fuerza = 0
    estado = 0
    experiencia = 0
    tiempoDescanso = 0
    
    def __init__(self,identificador):
        self.identificador = identificador
        self.fuerza = 50
        self.estado = 100
        self.experiencia = 0
        self.tiempoDescanso = 0

    def __repr__(self):
        return f"   Soldier => [{self.identificador}] Fuerza: {self.fuerza} / Estado: {self.estado} / Exp: {self.experiencia} / Tiempo: {self.tiempoDescanso}"

