ListaAviones=[]
class Avion (): #An object is created for the aircraft, which will contain attributes such as an identification, aircraft model, year of construction, airline to which it belongs, passenger capacity and status
    def __init__(self):
        self.ID=0
        self.ModeloAvion=""
        self.AñoConstrucciónAvion=""
        self.AerolineaPerteneciente=""
        self.CapacidadPasajeros=0
        self.Estado="" #available, not available
    def set__info (self,ES,ID,MA,AC,AP,CP):
        self.Estado=ES
        self.ID=ID
        self.ModeloAvion=MA
        self.AñoConstruccion=AC
        self.AerolineaPerteneciente=AP
        self.CapacidadPasajeros=CP
    def set__estado(self, E):
        self.Estado=E
    def get__estado(self):
        return self.Estado
    def get__info (self):
        print ("ID","\t","Modelo", "\t", "Año Construcción", "\t","Aerolínea", "\t","Cant. pasajeros","","Estado")
        print (self.ID, "\t",self.ModeloAvion, "  \t\t", self.AñoConstruccion, "\t\t", self.AerolineaPerteneciente, "\t\t",self.CapacidadPasajeros, "\t", self.Estado)
    def get__ID(self):
        return self.ID
    def get__nombre(self):
        return self.ModeloAvion
    
def CreaArchivoAviones():
    archi=open('Aviones.txt','w') 
    archi.close()
def CreaAviones(ID, modelo, anio, aerolinea, pasajeros, estado):
    archi=open('Aviones.txt','a') #se abre el archivo en modo adjunción
    archi.write(str(ID)+", "+str(modelo)+", "+str(anio)+", "+str(aerolinea)+", "+str(pasajeros)+", "+str(estado)+", ")
    archi.write('\n') #cuando cambia de elemento va a hacer la identacion
    archi.close()
def CreaAvionesArchi():
    archi=open('Aviones.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        avion=[]
        avion=li.split(', ')
        print(avion)
        a=Avion()
        a.set__info(avion[0], avion[1], avion[2], avion[3], avion[4], avion[5])
        ListaAviones.append (a)   
    archi.close()

CreaArchivoAviones()
CreaAviones (319, "Airbus A319", 1995, "Avianca", 320, "disponible")#ID, model, Construction, airline, passengers, state
CreaAviones (330, "Airbus A330", 1992, "Avianca", 330, "disponible")
CreaAviones (326, "Airbus A326", 1992, "Avianca", 330, "disponible")
CreaAviones (747, "Boeing 747", 1969, "Interjet", 400, "disponible")
CreaAviones (204, "Túpolev Tu-204", 1989, "Interjet", 340, "disponible")
CreaAviones (306, "Túpolev Tu-306", 1991, "Interjet", 300, "disponible")
CreaAviones (456, "Túpolev Tu-456", 1980, "Interjet", 320, "disponible")
CreaAviones (200, "Bombardier CRJ100/200", 1992, "Volaris", 200, "disponible")
CreaAviones (805, "Bombardier Q Series", 1984, "Volaris", 470, "disponible")
CreaAviones (208, "Bombardier XLR8", 1984, "Volaris", 470, "disponible")
CreaAviones (960, "Ilyushin Il-96",1988, "Wingo", 320, "disponible")
CreaAviones (190, "Ilyushin Il-90",1990, "Wingo", 400, "disponible")
CreaAviones (120, "Ilyushin Il-100",2000, "Wingo", 400, "disponible")
CreaAviones (228, "Dornier Do 228", 1982, "Wingo", 270, "disponible")
CreaAviones (937,"Mitsubishi Regional Jet", 2015, "SANSA", 430, "disponible")
CreaAviones (777, "Fokker 70", 1993, "SANSA", 370, "disponible")
CreaAviones (999, "Fokker 99", 1999, "SANSA", 370, "disponible")
CreaAviones (190,"Embraer E-Jets E2",2013,"Aeroméxico",114,"disponible")
CreaAviones (100,"Airbus A220",2013,"Aeroméxico",133,"disponible")
CreaAviones (847,"Túpolev Tu-204.",1993,"Aeroméxico",180,"disponible")
CreaAviones (737,"Dassault Mercure",1967,"Air France",140,"disponible")
CreaAviones (667,"Pilatus PC-12",1990,"Air France",120,"disponible")
CreaAviones (765,"Ilyushin Pl-97",2007,"Air France",165,"disponible")
CreaAviones (402,"NAMC YS-11",1962,"Zennikku",150,"disponible")
CreaAviones (919,"COMAC C919",2011,"Zennikku",162,"disponible")
CreaAviones (620,"Bombardier CRJ200",1991,"Zennikku",62,"disponible")
CreaAviones (717,"COMAC ARJ21",2010,"Ticos Air",230,"disponible")
CreaAviones (186,"Xian MA600",2008,"Ticos Air",500,"disponible")
CreaAviones (398 ,"Boeing 777",1994,"Ticos Air",550,"disponible")
CreaAviones (900,"Boeing 737 MAX",2016,"Silver Airways",230,"disponible")
CreaAviones (217,"Boeing 787",2009,"Silver Airways",323,"disponible")
CreaAviones (572,"Boeing 646",1969,"Silver Airways",233,"disponible")

CreaAvionesArchi()
