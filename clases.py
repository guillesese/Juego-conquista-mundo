class Ejercito:     
    identificador = 0
    coordenadaX = 0
    coordenadaY = 0
    numeroSoldados = 0
    soldados = []


    def __init__(self, identificador, numeroSoldados):
        self.identificador = identificador
        self.numeroSoldados = numeroSoldados
        self.inicializarSoldados()
    
    def __repr__(self):
        infoEjercito = f"Ejército {self.identificador}. Posición [{self.coordenadaX}][{self.coordenadaY}]."
        infoSoldados = f" Soldados: {self.numeroSoldados}."
        fuerzaMedia,estadoMedia,experienciaMedia = self.calcularMediaEjercito()
        infoMedias = f" Fuerza: {fuerzaMedia}, Estado: {estadoMedia}, Exp: {experienciaMedia}"
        return  infoEjercito & infoSoldados & infoMedias
    

    '''
        Método que mueve un ejército a unas coordenadas en particular. 
    '''
    def moverEjercito(self, x, y):
        self.coordenadaX = x
        self.coordenadaY = y

    def inicializarSoldados(self):
        for soldado in range(self.numeroSoldados):
            self.soldados.append(Soldado())

    def calcularMediaEjercito(self):
        for soldado in self.soldados:
            fuerzaTotal = soldado.fuerza
            estadoTotal = soldado.estado
            experienciaTotal = soldado.experiencia
        
        fuerzaMedia = fuerzaTotal/self.numeroSoldados
        estadoMedia = estadoTotal/self.numeroSoldados
        experienciaMedia = experienciaTotal/self.numeroSoldados
    
        return fuerzaMedia,estadoMedia,experienciaMedia
    
class Soldado: 
    fuerza = 50
    estado = 100
    experiencia = 0
    
    def __init__(self):
        pass