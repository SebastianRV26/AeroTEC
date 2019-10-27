ListaPuertas=[]
class PuertasAbordaje (): #An object is created for the boarding gates, these are located inside the airports, it will contain the attributes such as the door number, the state and the airport it belongs to.
    def __init__(self):
        self.NumeroPuerta=0
        self.EstadoPuerta:"" #available, not available, maintenance
        self.aeropuerto=""
    def set__info (self,ES, NP,a):
        self.EstadoPuerta=ES
        self.NumeroPuerta=NP
        self.aeropuerto=a
    def set__estado(self, EP):
        self.EstadoPuerta=EP
    def get__info (self):
        print ("Número de la Puerta", "\t","Estado de la Puerta","\t\t","aeropuerto")
        print ("\t",self.NumeroPuerta,"\t\t  ", self.EstadoPuerta, "\t\t",self.aeropuerto)
    def get__NumeroPuerta(self):
        return self.NumeroPuerta
    def get__estado (self):
        return self.EstadoPuerta
    def get__aeropuerto(self):
        return self.aeropuerto



def ValidaExistenciaPuertas(num, a):
    for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
        if i.get__nombre()==a: #If i.get_name equal a
            for pu in i.get__ListaPuertas(): #Seacrch for the variable pu in the i.get_ListasPuertas
                if pu.get__NumeroPuerta()==num: #if pu.get__NumeroPuerta equal num
                    return True
    return False
def CreaArchivoPuertas():
    archi=open('Puertas.txt','w') 
    archi.close()
def CreaPuertasAbordaje(estado, numero, aeropuerto):
    archi=open('Puertas.txt','a') #se abre el archivo en modo adjunción
    archi.write(str(estado)+", "+str(numero)+", "+str(aeropuerto)+", ")
    archi.write('\n') #cuando cambia de elemento va a hacer la identacion
    archi.close()

def CreaPuertasArchi():
    archi=open('Puertas.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        puerta=[]
        puerta=li.split(', ')
        p=PuertasAbordaje()
        p.set__info(puerta[0], puerta[1], puerta[2])
        ListaPuertas.append (p)
        if ValidaExistenciaPuertas(puerta[0], puerta[1])==True: #if valid existence is equal to true
            print ("La puerta ya existe")
        else:
            for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
                if i.get__nombre()==a: #If i.get_name equal a
                    i.set__ListaPuertas (puerta)
    archi.close()

CreaArchivoPuertas()
CreaPuertasAbordaje (1, "disponible", "Aeropuerto Nacional Juan Santamaría") #state number and airport
CreaPuertasAbordaje (2, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPuertasAbordaje (3, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPuertasAbordaje (4, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPuertasAbordaje (5, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPuertasAbordaje (6, "disponible", "Aeropuerto Nacional Juan Santamaría") 
CreaPuertasAbordaje (7, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPuertasAbordaje (8, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPuertasAbordaje (9, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPuertasAbordaje (10, "disponible", "Aeropuerto Nacional Juan Santamaría")
CreaPuertasAbordaje (1, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPuertasAbordaje (2, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPuertasAbordaje (3, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPuertasAbordaje (4, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPuertasAbordaje (5, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPuertasAbordaje (6, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPuertasAbordaje (7, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPuertasAbordaje (8, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPuertasAbordaje (9, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPuertasAbordaje (10, "disponible", "Aeropuerto Nacional Tobías Bolaños")
CreaPuertasAbordaje (1, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPuertasAbordaje (2, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPuertasAbordaje (3, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPuertasAbordaje (4, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPuertasAbordaje (5, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPuertasAbordaje (6, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPuertasAbordaje (7, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPuertasAbordaje (8, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPuertasAbordaje (9, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPuertasAbordaje (10, "disponible", "Aeropuerto Nacional De Pérez Zeledón")
CreaPuertasAbordaje (1, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPuertasAbordaje (2, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPuertasAbordaje (3, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPuertasAbordaje (4, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPuertasAbordaje (5, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPuertasAbordaje (6, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPuertasAbordaje (7, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPuertasAbordaje (8, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPuertasAbordaje (9, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPuertasAbordaje (10, "disponible", "Aeropuerto Internacional Jonh F. Kennedy")
CreaPuertasAbordaje (1, "disponible", "Aeropuerto Internacional De Osaka")
CreaPuertasAbordaje (2, "disponible", "Aeropuerto Internacional De Osaka")
CreaPuertasAbordaje (3, "disponible", "Aeropuerto Internacional De Osaka")
CreaPuertasAbordaje (4, "disponible", "Aeropuerto Internacional De Osaka")
CreaPuertasAbordaje (5, "disponible", "Aeropuerto Internacional De Osaka")
CreaPuertasAbordaje (6, "disponible", "Aeropuerto Internacional De Osaka")
CreaPuertasAbordaje (7, "disponible", "Aeropuerto Internacional De Osaka")
CreaPuertasAbordaje (8, "disponible", "Aeropuerto Internacional De Osaka")
CreaPuertasAbordaje (9, "disponible", "Aeropuerto Internacional De Osaka")
CreaPuertasAbordaje (10, "disponible", "Aeropuerto Internacional De Osaka")
CreaPuertasAbordaje (1, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPuertasAbordaje (2, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPuertasAbordaje (3, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPuertasAbordaje (4, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPuertasAbordaje (5, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPuertasAbordaje (6, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPuertasAbordaje (7, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPuertasAbordaje (8, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPuertasAbordaje (9, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPuertasAbordaje (10, "disponible", "Aeropuerto De París-Charles De Gaulle")
CreaPuertasAbordaje (1, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPuertasAbordaje (2, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPuertasAbordaje (3, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPuertasAbordaje (4, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPuertasAbordaje (5, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPuertasAbordaje (6, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPuertasAbordaje (7, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPuertasAbordaje (8, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPuertasAbordaje (9, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPuertasAbordaje (10, "disponible", "Aeropuerto Josep Tarradellas Barcelona-El Prat")
CreaPuertasAbordaje (1, "disponible", "Aeropuerto Internacional De Formosa")
CreaPuertasAbordaje (2, "disponible", "Aeropuerto Internacional De Formosa")
CreaPuertasAbordaje (3, "disponible", "Aeropuerto Internacional De Formosa")
CreaPuertasAbordaje (4, "disponible", "Aeropuerto Internacional De Formosa")
CreaPuertasAbordaje (5, "disponible", "Aeropuerto Internacional De Formosa")
CreaPuertasAbordaje (6, "disponible", "Aeropuerto Internacional De Formosa")
CreaPuertasAbordaje (7, "disponible", "Aeropuerto Internacional De Formosa")
CreaPuertasAbordaje (8, "disponible", "Aeropuerto Internacional De Formosa")
CreaPuertasAbordaje (9, "disponible", "Aeropuerto Internacional De Formosa")
CreaPuertasAbordaje (10, "disponible", "Aeropuerto Internacional De Formosa")
CreaPuertasArchi()









