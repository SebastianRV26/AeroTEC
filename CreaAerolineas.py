ListaAerolineas=[]
class Aerolineas: #An object is created for the airlines, which will contain attributes such as the name of the airline, the year of foundation, its type, the countries where it operates and the lists of aircraft, crew and flights that belong to said airport.
    def __init__(self):
        self.NombreAerolinea=""
        self.AñoFundacion=0
        self.TipoAerolinea="" #national or international
        self.PaisesQueOpera=0
        self.ListaAviones=[]
        self.ListaTripulacion=[]
        self.ListaVuelos=[]
    def set__info(self,NA,AF,TA,PQO):
        self.NombreAerolinea=NA
        self.AñoFundacion=AF
        self.TipoAerolinea=TA
        self.PaisesQueOpera=PQO
    def get__info (self):
        print (self.NombreAerolinea, "   \t",self.AñoFundacion,"\t\t", self.TipoAerolinea,"   \t",self.PaisesQueOpera)
    def get__nombre(self):
        return self.NombreAerolinea
    def set__ListaAviones (self, avion):
        self.ListaAviones.append(avion)
        return
    def get__ListaAviones(self):
        return self.ListaAviones
    def set__ListaTripulacion (self, tripulacion):
        self.ListaTripulacion.append (tripulacion)
        return
    def get__ListaTripulacion (self):
        return self.ListaTripulacion
    def set__ListaVuelos(self, vuelo):
        self.ListaVuelos.append (vuelo)
    def get__ListaVuelos(self):
        return self.ListaVuelos
    
def CreaArchivoAerolinea():
    archi=open('Aerolineas.txt','w') 
    archi.close()
def CreaAerolineas (nombre, anio, tipo, paises):
    archi=open('Aerolineas.txt','a') #se abre el archivo en modo adjunción
    archi.write(str(nombre)+", "+str(anio)+", "+str(tipo)+", "+str(paises)+", ")
    archi.write('\n') #cuando cambia de elemento va a hacer la identacion
    archi.close()
def CreaAerolineasArchi ():
    archi=open('Aerolineas.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        aerolinea=[]
        aerolinea=li.split(', ')
        a=Aerolineas()
        a.set__info(aerolinea[0], aerolinea[1], aerolinea[2], aerolinea[3])
        ListaAerolineas.append (a)   
    archi.close()

CreaArchivoAerolinea()
CreaAerolineas ("Avianca", 1945, "Local", 16) #name, year of foundation, type, number of countries that operates
CreaAerolineas ("Interjet", 2005, "Internacional", 54)
CreaAerolineas ("Volaris", 2006, "Internacional", 66)
CreaAerolineas ("Wingo", 2016, "Internacional", 15)
CreaAerolineas ("SANSA", 1979, "Local", 13)
CreaAerolineas ("Aeroméxico",1988,"Interncional",88)
CreaAerolineas ("Air France",1933,"Internacional",204)
CreaAerolineas ("Zennikku",1952,"Internacional",73)
CreaAerolineas ("Ticos Air",2012,"Local",4)
CreaAerolineas ("Silver Airways",2011,"Internacional",18)
CreaAerolineasArchi ()




