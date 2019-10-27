ListaPistas=[]
class Pistas: #An object is created for the tracks, these are inside the airports, it will contain the attributes such as the track number, the state and the airport to which it belongs
    def __init__(self):
        self.NumeroPista=0 
        self.EstadoPista="" #available, not available, maintenance
        self.aeropuerto=""
    def set__info(self, ES, NP,a):
        self.EstadoPista=ES
        self.NumeroPista=NP
        self.aeropuerto=a
    def set__estado(self, EP):
        self.EstadoPista=EP
    def get__info (self):
        print ("Número de la Pista", "\t","Estado de la Pista", "\t\t", "Aeropuerto")
        print ("\t",self.NumeroPista, "\t\t ", self.EstadoPista, "\t\t",self.aeropuerto)
    def get__NumeroPista(self):
        return self.NumeroPista
    def get__estado(self):
        return self.EstadoPista
    def get__aeropuerto(self):
        return self.aeropuerto
def CreaArchivo():
    archi=open('Pistas.txt','w') 
    archi.close()
def CreaPistas(estado, numero, aeropuerto):
    archi=open('Pistas.txt','a') #se abre el archivo en modo adjunción
    archi.write(str(estado)+", "+str(numero)+", "+str(aeropuerto)+", ")
    archi.write('\n') #cuando cambia de elemento va a hacer la identacion
    archi.close()

def CreaPistasArchi():
    archi=open('Pistas.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        pista=[]
        pista=li.split(', ')
        p=Pistas()
        p.set__info(pista[0], pista[1], pista[2])
        ListaPistas.append (p)   
    archi.close()

CreaArchivo()
CreaPistas (1, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPistas (2, "disponible", "Aeropuerto Nacional Juan Santamaría") #state number and airport
CreaPistas (3, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPistas (4, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPistas (5, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPistas (6, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPistas (7, "disponible", "Aeropuerto Nacional Juan Santamaría") 
CreaPistas (8, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPistas (9, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPistas (10, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPistas (1, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPistas (2, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPistas (3, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPistas (4, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPistas (5, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPistas (6, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPistas (7, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPistas (8, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPistas (9, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPistas (10, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPistas (1, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPistas (2, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPistas (3, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPistas (4, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPistas (5, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPistas (6, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPistas (7, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPistas (8, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPistas (9, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPistas (10, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPistas (1, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPistas (2, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPistas (3, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPistas (4, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPistas (5, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPistas (6, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPistas (7, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPistas (8, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPistas (9, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPistas (10, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPistas (1, "disponible", "Aeropuerto Internacional De Formosa")
CreaPistas (2, "disponible", "Aeropuerto Internacional De Formosa")
CreaPistas (3, "disponible", "Aeropuerto Internacional De Formosa")
CreaPistas (4, "disponible", "Aeropuerto Internacional De Formosa")
CreaPistas (5, "disponible", "Aeropuerto Internacional De Formosa")
CreaPistas (6, "disponible", "Aeropuerto Internacional De Formosa")
CreaPistas (7, "disponible", "Aeropuerto Internacional De Formosa")
CreaPistas (8, "disponible", "Aeropuerto Internacional De Formosa")
CreaPistas (9, "disponible", "Aeropuerto Internacional De Formosa")
CreaPistas (10, "disponible", "Aeropuerto Internacional De Formosa")
CreaPistas (1, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPistas (2, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPistas (3, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPistas (4, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPistas (5, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPistas (6, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPistas (7, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPistas (8, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPistas (9, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPistas (10, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPistas (1, "disponible", "Aeropuerto Internacional De Osaka")
CreaPistas (2, "disponible", "Aeropuerto Internacional De Osaka")
CreaPistas (3, "disponible", "Aeropuerto Internacional De Osaka")
CreaPistas (4, "disponible", "Aeropuerto Internacional De Osaka")
CreaPistas (5, "disponible", "Aeropuerto Internacional De Osaka")
CreaPistas (6, "disponible", "Aeropuerto Internacional De Osaka")
CreaPistas (7, "disponible", "Aeropuerto Internacional De Osaka")
CreaPistas (8, "disponible", "Aeropuerto Internacional De Osaka")
CreaPistas (9, "disponible", "Aeropuerto Internacional De Osaka")
CreaPistas (10, "disponible", "Aeropuerto Internacional De Osaka")
CreaPistas (1, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPistas (2, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPistas (3, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPistas (4, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPistas (5, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPistas (6, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPistas (7, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPistas (8, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPistas (9, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPistas (10, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPistasArchi()









