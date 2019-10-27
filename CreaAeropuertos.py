ListaAeropuertos=[]
class Aeropuertos: #An object is created for the airports, which will contain the attributes such as the name of the airport, the city, the country and the lists of tracks and doors that belong to said airport.
    def __init__(self):
        self.NombreAeropuerto=""
        self.CiudadActual=""
        self.PaisAeropuerto=""
        self.ListaPistas=[]
        self.ListaPuertasAbordaje=[]
    def set__info(self,n,CA,PA):
        self.NombreAeropuerto=n
        self.CiudadActual=CA
        self.PaisAeropuerto=PA
    def get__info(self):
        print (self.NombreAeropuerto, "\t",self.CiudadActual,"\t", self.PaisAeropuerto)
    def get__nombre(self):
        return self.NombreAeropuerto
    def set__ListaPistas (self, pista):
        self.ListaPistas.append(pista)
    def get__ListaPistas (self):
        return self.ListaPistas
    def set__ListaPuertas (self, puerta):
        self.ListaPuertasAbordaje.append (puerta)
    def get__ListaPuertas (self):
        return self.ListaPuertasAbordaje
    
def CreaArchivoAeropuerto():
    archi=open('Aeropuertos.txt','w') 
    archi.close()
def CreaAeropuertos (nombre, ciudad, pais):
    archi=open('Aeropuertos.txt','a') #se abre el archivo en modo adjunción
    archi.write(str(nombre)+", "+str(ciudad)+", "+str(pais)+", ")
    archi.write('\n') #cuando cambia de elemento va a hacer la identacion
    archi.close()
def CreaAeropuertoArchi ():
    archi=open('Aeropuertos.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        aeropuerto=[]
        aeropuerto=li.split(', ')
        a=Usuario()
        a.set__info(aeropuerto[0], aeropuerto[1], aeropuerto[2])
        ListaAeropuertos.append (a)   
    archi.close()

CreaArchivoAeropuerto()
CreaAeropuertos ("Aeropuerto Nacional Juan Santamaría", "Alajuela","Costa Rica") #Name, City, Country
CreaAeropuertos ("Aeropuerto Nacional Tobías Bolaños", "San José", "Costa Rica")
CreaAeropuertos ("Aeropuerto Nacional De Pérez Zeledón","San Isidro de El General", "Costa Rica")
CreaAeropuertos ("Aeropuerto Internacional Jonh F. Kennedy","Nueva York", "Estados Unidos")
CreaAeropuertos ("Aeropuerto Internacional De Osaka","Toyonaka","Japón")
CreaAeropuertos ("Aeropuerto De París-Charles De Gaulle","París","Francia")
CreaAeropuertos ("Aeropuerto Josep Tarradellas Barcelona-El Prat", "Barcelona", "España")
CreaAeropuertos ("Aeropuerto Internacional De Formosa", "Formosa", "Argentina")















