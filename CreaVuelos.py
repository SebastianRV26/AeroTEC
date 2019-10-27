ListaVuelos=[] 
class Vuelos(): #An object is created for the flights, which will contain the attributes such as the code, the airline to which it belongs, the departure date, departure and arrival time,
    def __init__(self): #departure and arrival airport, a list of the crew members that will participate in the flight, plane, tracks and doors
        self.codigo=""
        self.IndicaAerolineaVuelo=""
        self.FechaSalida=""
        self.HoraSalida=""
        self.HoraLlegada=""
        self.AeropuertoSalida=""
        self.AeropuertoLlegada=""
        self.ListaTripulantesParaVuelo=[] #two pilots, and three customer services
        self.avion=""
        self.pista=""
        self.puerta=""
        self.pistaLlegada=""
        self.puertaLlegada=""
    def set__info(self,cod,IAV,FS,HS,HL,AS,AL):
        self.codigo=cod
        self.IndicaAerolineaVuelo=IAV
        self.FechaSalida=FS
        self.HoraLlegada=HL
        self.HoraSalida=HS
        self.AeropuertoSalida=AS
        self.AeropuertoLlegada=AL
    def get__info (self):
        print ("Código del vuelo","\t","Aertolínea","\t","Fecha de Salida", "\t","Hora de Salida","\t", "Hora de llegada")
        print (self.codigo,"\t\t",self.IndicaAerolineaVuelo, "   \t   ",self.FechaSalida, "\t\t   ", self.HoraSalida, "\t\t   ",self.HoraLlegada)
        print ("\t","Aeropuerto de Salida", "\t\t\t","Aeropuerto de Llegada")
        print (self.AeropuertoSalida, "\t", self.AeropuertoLlegada)
        print ("  ","Avión", "\t","Pista","\t\t","Aeropuerto de la Pista salida","\t","Puerta","\t","Aeropuerto de la Puerta salida")
        print ((self.avion).get__nombre(),"\t  ",(self.pista).get__NumeroPista(),"\t",(self.pista).get__aeropuerto(), "\t  ", (self.puerta).get__NumeroPuerta(),"\t",(self.puerta).get__aeropuerto())
        print ("Pista \t Aeropuerto de la Pista de llegada \t puerta \t Aeropuerto de la Puerta de llegada")
        print ((self.pistaLlegada).get__NumeroPista(),"\t",(self.pistaLlegada).get__aeropuerto(), "\t  ", (self.puertaLlegada).get__NumeroPuerta(),"\t",(self.puertaLlegada).get__aeropuerto())
        print ("\t\t   ","Tripulantes")
        for i in self.ListaTripulantesParaVuelo:
            print ("  ","ID","\t\t", "Nombre", "\t","Nacimiento","\t","Rol")
            print (i.get__ID(), "\t",i.get__nombre(), "   \t", i.get__fecha(), "\t", i.get__rol())
        
    def set__tripulacion(self, lista):
        self.ListaTripulantesParaVuelo=lista
    def get__tripulacion(self):
        return self.ListaTripulantesParaVuelo
    def set__avion(self, a):
        self.avion=a
    def get__avion(self):
        return self.avion
    def set__pista(self, p):
        self.pista=p
    def get__pista (self):
        return self.pista
    def set__pistaLlegada(self, pista):
        self.pistaLlegada=pista
    def get__pistaLlegada(self):
        return self.pistaLlegada
    def set__puerta(self, pu):
        self.puerta=pu
    def get__puerta(self):
        return self.puerta
    def set__puertaLlegada(self, puerta):
        self.puertaLlegada=puerta
    def get__puertaLlegada(self):
        return self.puertaLlegada
    def get__aeropuerto(self):
        return self.AeropuertoSalida
    def get__fecha(self):
        return self.FechaSalida
    def get__HoraLlegada(self):
        return self.HoraLlegada
    def get__HoraSalida(self):
        return self.HoraSalida
    def get__codigo(self):
        return self.codigo
    def get__aerolinea(self):
        return self.IndicaAerolineaVuelo
        
def CreaArchivoVuelos():
    archi=open('Vuelos.txt','w') 
    archi.close()
def CreaVuelos(codigo, aerolinea, FechaSalida, HoraSalida, HoraLlegada, AropuertoSalida, Aropuertollegada, precio):
    archi=open('Vuelos.txt','a') #se abre el archivo en modo adjunción
    archi.write(str(codigo)+", "+str(aerolinea)+", "+str(FechaSalida)+", "+str(HoraSalida)+", "+str(HoraLlegada)+", "+str(AropuertoSalida)+", "+str(Aropuertollegada)+", "+str(precio)+", ")
    archi.write('\n') #cuando cambia de elemento va a hacer la identacion
    archi.close() # se cierra el archivo
def CreaVuelosArchi():
    archi=open ('Vuelos.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        vuelo=[]
        vuelo=li.split(', ')
        v=Vuelos()
        v.set__info(vuelo[0], vuelo[1], vuelo[2], vuelo[3], vuelo[4], vuelo[5], vuelo[6], vuelo[7])
        ListaVuelos.append (v)
    archi.close()
def MuestraVuelos():
    for i in ListaVuelos:
        i.get__info()

CreaArchivoVuelos()
CreaVuelos ("V22JSFK11","Volaris", "06/06/19", "13:30","17:50", "Aeropuerto Nacional Juan Santamaría", "Aeropuerto Internacional Jonh F. Kennedy" , 250000) #Airline, Departure Date, Departure Time, Departure Airport, Arrival Airport
CreaVuelos ("A22JSOS23","Avianca", "06/06/19", "11:30","16:50", "Aeropuerto Nacional Juan Santamaría", "Aeropuerto Internacional De Osaka", 300000)
CreaVuelos ("I22JSPC14","Interjet", "06/06/19", "10:30","13:50", "Aeropuerto Nacional Juan Santamaría", "Aeropuerto De París-Charles De Gaulle", 450000)
CreaVuelos ("W22JS04BA","Wingo", "06/06/19", "13:20","18:50", "Aeropuerto Nacional Juan Santamaría", "Aeropuerto Josep Tarradellas Barcelona-El Prat", 400000) 
CreaVuelos ("SA22JS04FO","SANSA", "06/06/19", "09:20","12:50", "Aeropuerto Nacional Juan Santamaría", "Aeropuerto Internacional De Formosa", 400000) 
CreaVuelos ("V22TB04FK","Volaris", "06/06/19", "10:10", "13:30","Aeropuerto Nacional Tobías Bolaños", "Aeropuerto Internacional Jonh F. Kennedy", 150000)
CreaVuelos ("AV22TB04OS","Avianca", "06/06/19", "10:30", "13:30","Aeropuerto Nacional Tobías Bolaños", "Aeropuerto Internacional De Osaka", 200000)
CreaVuelos ("I22TB04PC","Interjet", "06/06/19", "12:00", "13:30","Aeropuerto Nacional Tobías Bolaños", "Aeropuerto De París-Charles De Gaulle", 450000)
CreaVuelos ("W22TB04BA","Wingo", "06/06/19", "11:30", "13:30","Aeropuerto Nacional Tobías Bolaños", "Aeropuerto Josep Tarradellas Barcelona-El Prat", 400000)
CreaVuelos ("SA22TB04FO","SANSA", "06/06/19", "12:10", "13:30","Aeropuerto Nacional Tobías Bolaños", "Aeropuerto Internacional De Formosa", 400000)
CreaVuelos ("VO22PZ04FK","Volaris", "06/06/19", "10:30", "13:30","Aeropuerto Nacional De Pérez Zeledón", "Aeropuerto Internacional Jonh F. Kennedy", 550000)
CreaVuelos ("AV22PZ04OS","Avianca", "06/06/19", "10:30", "13:30","Aeropuerto Nacional De Pérez Zeledón", "Aeropuerto Internacional De Osaka", 300000)
CreaVuelos ("IN22PZ04PC","Interjet", "06/06/19", "10:30", "13:30","Aeropuerto Nacional De Pérez Zeledón", "Aeropuerto De París-Charles De Gaulle", 450000)
CreaVuelos ("WI22PZ04BA","Wingo", "06/06/19", "10:30", "13:30","Aeropuerto Nacional De Pérez Zeledón", "Aeropuerto Josep Tarradellas Barcelona-El Prat", 400000)
CreaVuelos ("WI22PZ04FO","SANSA", "06/06/19", "10:30", "13:30","Aeropuerto Nacional De Pérez Zeledón", "Aeropuerto Internacional De Formosa", 400000)
CreaVuelos ("VO06FK10OS","Volaris", "06/06/19", "10:30","15:50", "Aeropuerto Internacional Jonh F. Kennedy", "Aeropuerto Internacional De Osaka", 425000) 
CreaVuelos ("AVI06OSPA1","Avianca", "06/06/19", "10:30","14:50", "Aeropuerto Internacional De Osaka", "Aeropuerto De París-Charles De Gaulle", 375000)
CreaVuelos ("INCH06JO10","Interjet", "06/06/19", "10:30","15:50", "Aeropuerto De París-Charles De Gaulle", "Aeropuerto Josep Tarradellas Barcelona-El Prat", 320000)
CreaVuelos ("WI06BA10FO","Wingo", "06/06/19", "10:30","14:50", "Aeropuerto Josep Tarradellas Barcelona-El Prat", "Aeropuerto Internacional De Formosa", 410000) 
CreaVuelos ("SA06FO13FK","SANSA", "06/06/19", "10:30","13:50", "Aeropuerto Internacional De Formosa", "Aeropuerto Internacional Jonh F. Kennedy", 553000) 
CreaVuelos ("VO06JK10JS","Volaris", "06/06/19", "10:30", "13:30","Aeropuerto Internacional Jonh F. Kennedy", "Aeropuerto Nacional Juan Santamaría", 350000)
CreaVuelos ("AV06OS10PZ","Avianca", "06/06/19", "10:30", "15:30","Aeropuerto Internacional De Osaka", "Aeropuerto Nacional De Pérez Zeledón", 305000)
CreaVuelos ("IN06CH10TB","Interjet", "06/06/19", "10:30", "14:30","Aeropuerto De París-Charles De Gaulle", "Aeropuerto Nacional Tobías Bolaños", 450000)
CreaVuelos ("WI06JO13JS","Wingo", "06/06/19", "10:30", "16:30","Aeropuerto Josep Tarradellas Barcelona-El Prat", "Aeropuerto Nacional Juan Santamaría", 500000)
CreaVuelos ("SA06FO10PZ","SANSA", "06/06/19", "10:30", "13:30","Aeropuerto Internacional De Formosa", "Aeropuerto Nacional De Pérez Zeledón", 400000)
CreaVuelos ("VO06FK10CH","Volaris", "06/06/19", "10:30", "13:30","Aeropuerto Internacional Jonh F. Kennedy", "Aeropuerto De París-Charles De Gaulle", 350000)
CreaVuelos ("AV06OSJT10","Avianca", "06/06/19", "10:30", "13:30","Aeropuerto Internacional De Osaka", "Aeropuerto Josep Tarradellas Barcelona-El Prat", 275000)
CreaVuelos ("IN06GUFO10","Interjet", "06/06/19", "10:30", "14:30","Aeropuerto De París-Charles De Gaulle", "Aeropuerto Internacional De Formosa", 300000)
CreaVuelos ("AV06BAFK10","Avianca", "06/06/19", "10:30", "15:30","Aeropuerto Josep Tarradellas Barcelona-El Prat", "Aeropuerto Internacional Jonh F. Kennedy", 425000)
CreaVuelos ("INFOOS2019","Interjet", "06/06/19", "10:30", "12:30","Aeropuerto Internacional De Formosa", "Aeropuerto Internacional De Osaka", 350000)

CreaVuelos ("A57JPJS20","Aeroméxico", "04/06/19", "17:30","23:50", "Aeropuerto Josep Tarradellas Barcelona-El Prat", "Aeropuerto Nacional Juan Santamaría",825000) 
CreaVuelos ("A57JSJP21","Aeroméxico", "04/06/19", "17:30","23:50", "Aeropuerto Nacional Juan Santamaría", "Aeropuerto Josep Tarradellas Barcelona-El Prat",825000)
CreaVuelos ("A57IFPC22","Aeroméxico", "04/06/19", "17:30","23:50", "Aeropuerto Internacional De Formosa", "Aeropuerto De París-Charles De Gaulle",700000)
CreaVuelos ("A58JFTB23","Air France", "04/06/19", "17:30","23:50", "Aeropuerto Internacional Jonh F. Kennedy", "Aeropuerto Nacional Tobías Bolaños",500000) 
CreaVuelos ("A58IAIF24","Air France", "04/06/19", "17:30","23:50", "Aeropuerto Internacional De Osaka", "Aeropuerto Internacional De Formosa",650000) 
CreaVuelos ("A58TBJF25","Air France", "04/06/19", "17:30", "23:30","Aeropuerto Nacional Tobías Bolaños", "Aeropuerto Internacional Jonh F. Kennedy",500000)
CreaVuelos ("Z59TBIO26","Zennikku", "04/06/19", "17:30", "23:30","Aeropuerto Nacional De Pérez Zeledón", "Aeropuerto Internacional De Osaka",700000)
CreaVuelos ("Z59IOPC27","Zennikku", "04/06/19", "17:30", "23:30","Aeropuerto Internacional De Osaka", "Aeropuerto De París-Charles De Gaulle",500000)
CreaVuelos ("Z59TBIF28","Zennikku", "04/06/19", "17:30", "23:30","Aeropuerto Nacional Tobías Bolaños", "Aeropuerto Internacional De Formosa",600000)
CreaVuelos ("T60JFIO29","Ticos Air", "04/06/19", "17:30", "23:30","Aeropuerto Internacional Jonh F. Kennedy", "Aeropuerto Internacional De Osaka",550000)
CreaVuelos ("T60PCPZ30","Ticos Air", "04/06/19", "17:30", "23:30","Aeropuerto De París-Charles De Gaulle", "Aeropuerto Nacional De Pérez Zeledón",775000)
CreaVuelos ("T60PZIO31","Ticos Air", "04/06/19", "17:30", "23:30","Aeropuerto Nacional De Pérez Zeledón", "Aeropuerto Internacional De Osaka",55000)
CreaVuelos ("S61JTPC32","Silver Airways", "04/06/19", "17:30", "23:30","Aeropuerto Josep Tarradellas Barcelona-El Prat", "Aeropuerto De París-Charles De Gaulle",600000)
CreaVuelos ("S61JSJT33","Silver Airways", "04/06/19", "17:30", "23:30","Aeropuerto Nacional Juan Santamaría", "Aeropuerto Josep Tarradellas Barcelona-El Prat",500000)
CreaVuelos ("S61JFIO34","Silver Airways", "04/06/19", "17:30", "23:30","Aeropuerto Internacional Jonh F. Kennedy", "Aeropuerto Internacional De Osaka",450000)
CreaVuelos ("1A57JPJS20", "Aeroméxico", "06/06/19", "20:30", "23:50", "Aeropuerto Internacional Jonh F. Kennedy", "Aeropuerto Internacional De Osaka", 825000) 
CreaVuelos ("2A57JPJS20", "Aeroméxico", "06/06/19", "20:30", "23:50", "Aeropuerto Internacional De Osaka", "Aeropuerto Internacional Jonh F. Kennedy", 825000)
CreaVuelos ("1A57JSJP21", "Aeroméxico", "06/06/19", "20:30", "23:50", "Aeropuerto Internacional De Osaka", "Aeropuerto De París-Charles De Gaulle", 775000)
CreaVuelos ("2A57JSJP21", "Aeroméxico", "06/06/19", "20:30", "23:50", "Aeropuerto De París-Charles De Gaulle", "Aeropuerto Internacional De Osaka", 775000)
CreaVuelos ("1A57IFPC22", "Aeroméxico", "06/06/19", "20:30", "23:50", "Aeropuerto De París-Charles De Gaulle", "Aeropuerto Josep Tarradellas Barcelona-El Prat", 720000)
CreaVuelos ("2A57IFPC22", "Aeroméxico", "06/06/19", "20:30", "23:50", "Aeropuerto Josep Tarradellas Barcelona-El Prat", "Aeropuerto De París-Charles De Gaulle", 720000)
CreaVuelos ("1A58JFTB22", "Air France", "06/06/19", "20:30", "23:50", "Aeropuerto Josep Tarradellas Barcelona-El Prat", "Aeropuerto Internacional De Formosa", 810000)
CreaVuelos ("2A58JFTB23", "Air France", "06/06/19", "20:30", "23:50", "Aeropuerto Internacional De Formosa", "Aeropuerto Josep Tarradellas Barcelona-El Prat", 810000) 
CreaVuelos ("1A58IAIF24", "Air France", "06/06/19", "20:30", "23:50", "Aeropuerto Internacional De Formosa", "Aeropuerto Internacional Jonh F. Kennedy", 953000)
CreaVuelos ("2A58IAIF24", "Air France", "06/06/19", "20:30", "23:50", "Aeropuerto Internacional Jonh F. Kennedy", "Aeropuerto Internacional De Formosa", 953000)
CreaVuelos ("1A58TBJF25", "Air France", "06/06/19", "20:30", "23:50", "Aeropuerto Internacional Jonh F. Kennedy", "Aeropuerto Nacional Juan Santamaría", 550000)
CreaVuelos ("2A58TBJF25", "Air France", "06/06/19", "20:30", "23:30", "Aeropuerto Nacional Juan Santamaría", "Aeropuerto Internacional Jonh F. Kennedy", 550000)
CreaVuelos ("1Z59TBIO26", "Zennikku", "06/06/19", "20:30", "23:30", "Aeropuerto Internacional De Osaka", "Aeropuerto Nacional De Pérez Zeledón", 605000)
CreaVuelos ("2Z59TBIO26", "Zennikku", "06/06/19", "20:30", "23:30", "Aeropuerto Nacional De Pérez Zeledón", "Aeropuerto Internacional De Osaka", 605000) 
CreaVuelos ("1Z59IOPC27", "Zennikku", "06/06/19", "20:30", "23:30", "Aeropuerto De París-Charles De Gaulle", "Aeropuerto Nacional Tobías Bolaños", 750000) 
CreaVuelos ("2Z59IOPC27", "Zennikku", "06/06/19", "20:30", "23:30", "Aeropuerto Nacional Tobías Bolaños", "Aeropuerto De París-Charles De Gaulle", 750000)
CreaVuelos ("1Z59TBIF28", "Zennikku", "06/06/19", "20:30", "23:30", "Aeropuerto Josep Tarradellas Barcelona-El Prat", "Aeropuerto Nacional Juan Santamaría", 700000) 
CreaVuelos ("2Z59TBIF28", "Zennikku", "06/06/19", "20:30", "23:30", "Aeropuerto Nacional Juan Santamaría", "Aeropuerto Josep Tarradellas Barcelona-El Prat", 700000)
CreaVuelos ("1T60JFIO29", "Ticos Air", "06/06/19", "20:30", "23:30", "Aeropuerto Internacional De Formosa", "Aeropuerto Nacional De Pérez Zeledón", 800000)
CreaVuelos ("2T60JFIO29", "Ticos Air", "06/06/19", "20:30", "23:30", "Aeropuerto Nacional De Pérez Zeledón", "Aeropuerto Internacional De Formosa", 800000)
CreaVuelos ("1T60PCPZ30", "Ticos Air", "06/06/19", "20:30", "23:30", "Aeropuerto Internacional Jonh F. Kennedy", "Aeropuerto De París-Charles De Gaulle", 650000)
CreaVuelos ("2T60PCPZ30", "Ticos Air", "06/06/19", "20:30", "23:30", "Aeropuerto De París-Charles De Gaulle", "Aeropuerto Internacional Jonh F. Kennedy", 650000)
CreaVuelos ("1T60PZIO31", "Ticos Air", "06/06/19", "20:30", "23:30", "Aeropuerto Internacional De Osaka", "Aeropuerto Josep Tarradellas Barcelona-El Prat", 575000)
CreaVuelos ("2T60PZIO31", "Ticos Air", "06/06/19", "20:30", "23:30", "Aeropuerto Josep Tarradellas Barcelona-El Prat", "Aeropuerto Internacional De Osaka", 575000)
CreaVuelos ("1S61JTPC32", "Silver Airways", "06/06/19", "20:30", "23:30", "Aeropuerto De París-Charles De Gaulle", "Aeropuerto Internacional De Formosa", 600000)
CreaVuelos ("2S61JTPC32", "Silver Airways", "06/06/19", "20:30", "23:30", "Aeropuerto Internacional De Formosa", "Aeropuerto De París-Charles De Gaulle", 600000)
CreaVuelos ("1S61JSJT33", "Silver Airways", "06/06/19", "20:30", "23:30", "Aeropuerto Josep Tarradellas Barcelona-El Prat", "Aeropuerto Internacional Jonh F. Kennedy", 725000)
CreaVuelos ("2S61JSJT33", "Silver Airways", "06/06/19", "20:30", "23:30", "Aeropuerto Internacional Jonh F. Kennedy", "Aeropuerto Josep Tarradellas Barcelona-El Prat", 725000)
CreaVuelos ("1S61JFIO34", "Silver Airways", "06/06/19", "20:30", "23:30", "Aeropuerto Internacional De Formosa", "Aeropuerto Internacional De Osaka", 650000)
CreaVuelos ("2S61JFIO34", "Silver Airways", "06/06/19", "20:30", "23:30", "Aeropuerto Internacional De Osaka", "Aeropuerto Internacional De Formosa", 650000)

CreaVuelosArchi()
#MuestraVuelos()





