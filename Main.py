"""
Segunda etapa - Proyecto taller de programación
Autores:
        Sebastián Rojas Vargas
        César Enrique Acuña Pérez
"""
import time #The system time is imported
from datetime import datetime, timedelta #The system date is imported
import operator
ListaUsuarios=[] #The main lists are created
ListaAeropuertos=[]
ListaAerolineas=[]
ListaEscalas=[]
class Usuario: #An object is created for the users, it will contain the attributes such as name, ID, age, password, email and its type (administrator or guest)
    def __init__(self):
        self.NombreCompleto=""
        self.ID=0
        self.edad=0
        self.CorreoElectronico=""
        self.contraseña=""
        self.tipo=""
        self.HistorialDeViajes=[]
        #el nombre de usuario será la cédula
    def set__info (self,n,ID,e,correo,contra,t):
        self.nombre=n
        self.ID=ID
        self.edad=e
        self.CorreoElectronico=correo
        self.contraseña=contra
        self.tipo=t
    def get__nombre(self):
        return self.nombre
    def get__info(self):
        print ("\nNombre ID Edad Correo Cotraseña Tipo")
        print (self.nombre,self.ID,self.edad,self.CorreoElectronico,self.contraseña,end=" ")
        if self.tipo==1:
            print ("Administrador")
        elif self.tipo==2:
            print ("Invitado")
        elif self.tipo==3:
            print ("Pasajero")
    def get__ID (self):
        return self.ID
    def get__contraseña(self):
        return self.contraseña
    def get__tipo(self):
        return self.tipo
    def set__historial(self,viaje):
        self.HistorialDeViajes.append(viaje)
        
    def get__historial(self):
        for viajes in self.HistorialDeViajes:
            if len (viajes)==1:
                #print ("\n\t\tVuelos Directos") 
                print ("Salida:",viajes[0].get__aeropuerto(), "\tFecha Salida:", viajes[0].get__fecha(), "\tHora de salida",viajes[0].get__HoraSalida())
                print ("Destino:",viajes[0].get__AeropuertoLlegada(),"\tHora de llegada",viajes[0].get__HoraLlegada())
                print ("precio:",viajes[0].get__precio())
                print("\n")
            if len(viajes)==2:
                #print ("\n\t\tEscala (2 vuelos)")    
                #for i in viajes:
                precio=int(viajes[0].get__precio())+int(viajes[1].get__precio())
                print ("Salida:",viajes[0].get__aeropuerto(),"\tFecha Salida:",viajes[0].get__fecha(), "\tHora de salida",viajes[0].get__HoraSalida())
                print ("Aeropuerto Intermedio:", viajes[1].get__aeropuerto(),"\tFecha Salida (vuelo 2):", viajes[1].get__fecha(),"\tHora de salida:", viajes[1].get__HoraSalida(),"\tDestino:",viajes[1].get__AeropuertoLlegada())
                print ("Precio:", precio)
                print ("\n")
            if len(viajes)==3:
                #print ("\n\t\tEscala (3 vuelos)")
                #for k in viajes[2]:
                precio=int(viajes[0].get__precio())+int(viajes[1].get__precio())+int(viajes[2].get__precio())
                print ("Salida:",viajes[0].get__aeropuerto(),"\tFecha Salida:",viajes[0].get__fecha(), "\tHora de salida",viajes[0].get__HoraSalida())
                print ("Aeropuertos Intermedios:", viajes[1].get__aeropuerto(), viajes[1].get__AeropuertoLlegada(),"\tFecha Salida (vuelo 2):", viajes[1].get__fecha(),"\tHora de salida:", viajes[1].get__HoraSalida(),"\tDestino:",viajes[2].get__AeropuertoLlegada())
                print("\n")
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
    
class Pistas: #An object is created for the tracks, these are inside the airports, it will contain the attributes such as the track number, the state and the airport to which it belongs
    def __init__(self):
        self.NumeroPista=0 
        self.EstadoPista="" #available, not available, maintenance
        self.aeropuerto=""
    def set__info(self,NP,ES,a):
        self.NumeroPista=NP
        self.EstadoPista=ES
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

class PuertasAbordaje (): #An object is created for the boarding gates, these are located inside the airports, it will contain the attributes such as the door number, the state and the airport it belongs to.
    def __init__(self):
        self.NumeroPuerta=0
        self.EstadoPuerta:"" #available, not available, maintenance
        self.aeropuerto=""
    def set__info (self,NP,ES,a):
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

class Avion (): #An object is created for the aircraft, which will contain attributes such as an identification, aircraft model, year of construction, airline to which it belongs, passenger capacity and status
    def __init__(self):
        self.ID=0
        self.ModeloAvion=""
        self.AñoConstrucciónAvion=""
        self.AerolineaPerteneciente=""
        self.CapacidadPasajeros=0
        self.Estado="" #available, not available
    def set__info (self,ID,MA,AC,AP,CP,ES):
        self.ID=ID
        self.ModeloAvion=MA
        self.AñoConstruccion=AC
        self.AerolineaPerteneciente=AP
        self.CapacidadPasajeros=CP
        self.Estado=ES
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
    
class Tripulacion (): #An object is created for the crew, which will contain attributes such as an identification, the name of the crew, the date of birth, the airline to which it belongs, its role and the state
    def __init__(self):
        self.ID=""
        self.NombreTripulante=""
        self.FechaNacimiento=""
        self.AerolineaPatrona=""
        self.RolDelTripulante="" #pilot or customer service
        self.Estado="" #available, not available
        self.contador=0
    def set__info (self,ID,NT,FN,AP,AT,ES):
        self.ID=ID
        self.NombreTripulante=NT
        self.FechaNacimiento=FN
        self.AerolineaPatrona=AP
        self.RolDelTripulante=AT
        self.Estado=ES
    def set__estado(self, E):
        self.Estado=E
    def get__info (self):
        print ("  ","ID","\t\t", "Nombre", "\t","Nacimiento","\t", "Aerolinea", "\t","Rol", "\t\t\t","Estado")
        print (self.ID, "\t",self.NombreTripulante, "   \t", self.FechaNacimiento, "\t", self.AerolineaPatrona, "\t", self.RolDelTripulante, "   \t",self.Estado)
    def get__ID(self):
        return self.ID
    def get__rol (self):
        return self.RolDelTripulante
    def get__estado(self):
        return self.Estado
    def get__nombre(self):
        return self.NombreTripulante
    def get__fecha(self):
        return self.FechaNacimiento
    def set__contador(self, num):
        self.contador=self.contador+num
    def get__contador(self):
        return self.contador
    
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
        self.precio=0
    def set__info(self,cod,IAV,FS,HS,HL,AS,AL,p):
        self.codigo=cod
        self.IndicaAerolineaVuelo=IAV
        self.FechaSalida=FS
        self.HoraLlegada=HL
        self.HoraSalida=HS
        self.AeropuertoSalida=AS
        self.AeropuertoLlegada=AL
        self.precio=p
    def get__info (self):
        print ("Código del vuelo","\t","Aertolínea","\t","Fecha de Salida", "\t","Hora de Salida","\t", "Hora de llegada")
        print (self.codigo,"\t\t",self.IndicaAerolineaVuelo, "   \t   ",self.FechaSalida, "\t\t   ", self.HoraSalida, "\t\t   ",self.HoraLlegada)
        print ("\t","Aeropuerto de Salida", "\t\t\t","Aeropuerto de Llegada", "\t\t\t","Precio")
        print (self.AeropuertoSalida, "\t", self.AeropuertoLlegada,"   \t", self.precio)
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
    def get__AeropuertoLlegada(self):
        return self.AeropuertoLlegada
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
    def get__precio(self):
        return self.precio
    def get__info__viajes(self):
        print ("\nCódigo del vuelo","\t","Aertolínea","\t","Fecha de Salida", "\t","Hora de Salida","\t", "Hora de llegada")
        print (self.codigo,"\t\t",self.IndicaAerolineaVuelo, "   \t   ",self.FechaSalida, "\t\t   ", self.HoraSalida, "\t\t   ",self.HoraLlegada)
        print ("\t","Aeropuerto de Salida", "\t\t\t","Aeropuerto de Llegada", "\t\t\t","Precio")
        print (self.AeropuertoSalida, "\t", self.AeropuertoLlegada,"   \t", self.precio)
        
class Escala ():
    def __init__(self):
        self.AeroOrigen=""
        self.AeroIntermedio=""
        self.AeroDestino=""
        self.ListaEscalas=[]
        self.VuelosDirectos=[]
    def set__info(self, AO, AI, AD):
        self.AeroOrigen=AO
        self.AeroIntermedio=AI
        self.AeroDestino=AD
    def set__Escalas(self, e1, e2):
        self.ListaEscalas.append ([e1, e2])
    def set__Directos(self, d):
        self.VuelosDirectos.append (d)
    def get__Escalas(self):
        return self.ListaEscalas
    def get__Directos(self):
        return self.VuelosDirectos
    def get__AeroOrigen(self):
        return self.AeroOrigen
    def get__AeroIntermedio(self):
        return self.AeroIntermedio
    def get__AeroDestino(self):
        return self.AeroDestino
    def get__info(self):
        cont=1
        if len (self.VuelosDirectos)!=0:
            print ("\n\t\tVuelos Directos") 
            for j in self.VuelosDirectos:
                print (cont,"- Salida:",self.AeroOrigen, "\tFecha Salida:", j.get__fecha(), "\tHora de salida",j.get__HoraSalida())
                print ("Destino:",self.AeroDestino,"\tHora de llegada",j.get__HoraLlegada())
                cont+=1
                print ("")
        if len(self.ListaEscalas)!=0:
            print ("\n\t\tEscalas")    
            for i in self.ListaEscalas:
                print (cont,"- Salida:",self.AeroOrigen,"\tFecha Salida:",i[0].get__fecha(), "\tHora de salida",i[0].get__HoraSalida())
                print ("Aeropuerto Intermedio:", self.AeroIntermedio,"\tFecha Salida (vuelo 2):", i[1].get__fecha(),"\tHora de salida:", i[1].get__HoraSalida(),"\tDestino:",self.AeroDestino)
                cont+=1
    def get__escala(self, viaje):
        cont=0
        if len (self.VuelosDirectos)!=0:
            for j in self.VuelosDirectos:
                if viaje==cont:
                    print (j)
                    return [j]
                cont+=1
        if len(self.ListaEscalas)!=0:
            for i in self.ListaEscalas:
                if viaje==cont:
                    print (i)
                    return i
                cont+=1
def CreaArchivoUsuario():
    archi=open('Usuarios.txt','w') 
    archi.close()

def CreaUsuario(nombre, ID, edad, correo, contra, tipo):
    usuario1=Usuario() #Set a variable as an object.
    usuario1.set__info(nombre, ID, edad, correo, contra, tipo)
    ListaUsuarios.append(usuario1)
    archi=open('Usuarios.txt','a') #se abre el archivo en modo adjunción
    archi.write(str(nombre)+", "+str(ID)+", "+str(edad)+", "+str(correo)+", "+str(contra)+", "+str(tipo))
    archi.write('\n') #cuando cambia de elemento va a hacer la identacion
    archi.close()

def CreaUsuarios():
    archi=open('Usuarios.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        usuario=[]
        usuario=li.split(', ')
        u=Usuario()
        u.set__info(usuario[0], int(usuario[1]), int(usuario[2]), usuario[3], usuario[4], int(usuario[5]))
        ListaUsuarios.append (u)
    archi.close()

def RegistraUsuario ():
    n=input("Ingrese el nombre completo: ")
    ID=int(input ("Ingrese el número de cédula o pasaporte: "))
    e=int(input ("Ingrese la edad: "))
    correo=input ("ingrese el correo electrónico: ")
    contra=input ("Ingrese la contraseña: ")
    t=int(input ("Ingrese el tipo (1- administrador, 2- invitado, 3-Pasajero)"))
    CreaUsuario (n,ID,e,correo,contra,t)
    print ("Usuario registrado")
    return IniciarSesion () 
def IniciarSesion (): 
    valor=True #The value variable is set as truth
    while valor==True: #There has been a while cycle while the value is equal to true
        try: #The reserved word try prevents the system from falling in case of error with the input
            ID=int (input ("Ingrese su nombre de usuario (número de cédula/pasaporte): ")) 
            contra=input ("Ingrese su contraseña: ")
            for i in ListaUsuarios: #Seacrch for the variable i in the user lists
                if i.get__ID()==ID and i.get__contraseña()==contra:
                    print ("sesión iniciadada, bienvenido",i.get__nombre()) #If the parameters match, "Welcome" is printed
                    return i #return the type attribute
            print ("Los datos no coinciden ¿Desea registrarse? (1.Si - 2.No)")
            comando=0
            comando=int(input ("Ingrese la opción que desea realizar: "))
            if comando==1:
                return RegistraUsuario ()
        except:
            print ("Error en datos, vuelve a intentarlo!")
            
def BuscarAeropuertos (nombre): #Seacrch for the variable i in the airport lists, if the name attribute within i matches name, it will return true
    for i in ListaAeropuertos:
        if i.get__nombre()==nombre: #If i is get_name equal to name
            return True
    return False
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
        a=Aeropuertos()
        a.set__info(aeropuerto[0], aeropuerto[1], aeropuerto[2])
        if BuscarAeropuertos(aeropuerto[0])==True: 
            print ("El aeropuerto ya existe")
        else:
            ListaAeropuertos.append (a)   
    archi.close()

def MuestraAeropuertos(): 
    print ("\t\t","Nombre","\t\t","Ciudad","\t  ","País")
    for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
        i.get__info () #i is airports get_info
def ModificaAeropuerto (nombre):
    for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
        if i.get__nombre()==nombre: #If i is get_name equal to name
            n=input ("Ingrese el nombre del aeropuerto: ") #Ask for the data
            c=input ("Ingrese el nombre de la ciudad actual: ")
            p=input ("Ingrese el país en el que opera: ")
            if i.get__nombre()==nombre: #If i is get_name equal to name
                i.set__info (n, c, p) #The values ​​of i.set_info are set
                print (n, "se modificó correctamente")
                return
            else:
                print (n, "no se pudo modificar")
def EliminaAeropuertos(nombre):
    valor=True #The value variable is set as true
    for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
        if i.get__nombre()==nombre: #If i is get_name equal to name
            ListaAeropuertos.remove(i) #Removed i from the airports list
            print (nombre, "Se eliminó correctamente")
            valor=False #The value variable is set as false
    if valor==True: 
        print ("el aeropuerto no se ha podido eliminar")
            
def ValidaExistenciaPistas(num, a):
    for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
        if i.get__nombre()==a: #If i.get_name equal a
            for pi in i.get__ListaPistas(): #Seacrch for the variable pi in the i.get_ListasPistas
                if pi.get__NumeroPista()==num: #if pi.get__NumeroPista equal num
                    return True
    return False

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
        p.set__info(int(pista[0]), pista[1], pista[2])
        if ValidaExistenciaPistas(pista[0], pista[2])==True: 
            print ("La pista ya existe")
        else:
            for i in ListaAeropuertos:
                if i.get__nombre()==pista[2]: 
                    i.set__ListaPistas (p)
    archi.close()
def MuestraPistas ():
    for i in ListaAeropuertos:#Seacrch for the variable i in the airport lists
        for j in i.get__ListaPistas(): #Seacrch for the variable j in i.get__ListaPistas
            j.get__info ()
def ModificaPistas (num, a):
    valor=True #The value variable is set as true
    for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
        if i.get__nombre()==a: #If i.get_name equal a
            for j in i.get__ListaPistas(): #Seacrch for the variable j in i.get__ListaPistas
                if j.get__NumeroPista()==num: #If j.get__NumeroPista equal num
                    n=int(input("ingrese el número de la pista: "))
                    e=input("ingrese el estado de la pista: ")
                    a=input ("ingrese el aeropuerto de la pista: ")
                    j.set__info (n,a)
                    j.set__estado(e)
                    print ("Pista",num,"se modificó correctamente")
                    valor=False #The value variable is set as false
    if valor==True: #if valor equal true
        print ("Pista",num," no se pudo modificar correctamente")
        
def EliminaPistas(num, a):
    valor=True #The value variable is set as true
    for i in ListaAeropuertos:#Seacrch for the variable i in the airport lists
        if i.get__nombre()==a: #If i.get_name equal a
            for pi in i.get__ListaPistas(): #Seacrch for the variable pi in the i.get_ListasPistas
                if pi.get__NumeroPista()==num: #if pi.get__NumeroPista equal num
                    i.get__ListaPistas().remove(pi) #Remove pi from i.get__ListaPistas
                    print (num,"ha sido eliminada")
                    valor=False #The value variable is set as false
    if valor==True: #if valor equal true
        print ("Pista",num,"no se pudo eliminar")
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
    archi=open ('Puertas.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        puerta=[]
        puerta=li.split(', ')
        p=PuertasAbordaje()
        p.set__info(int(puerta[0]), puerta[1], puerta[2])
        if ValidaExistenciaPuertas(puerta[0], puerta[2])==True: #if valid existence is equal to true
            print ("La puerta ya existe")
        else:
            for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
                if i.get__nombre()==puerta[2]: #If i.get_name equal a
                    i.set__ListaPuertas (p)
                    
    archi.close()
def MuestraPuertas():
    for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
        for j in i.get__ListaPuertas():#Seacrch for the variable j in i.get__ListaPuertas
            j.get__info ()
def ModificaPuertas(num,a):
    valor=True #The value variable is set as true
    for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
        if i.get__nombre()==a: #If i.get_name equal a
            for j in i.get__ListaPuertas(): #Seacrch for the variable j in i.get__ListaPuertas
                if j.get__NumeroPuerta()==num: #If j.get__NumeroPuerta equal num
                    n=int(input("ingrese el número de la puerta: "))
                    e=input("ingrese el estado de la puerta: ")
                    a=input ("ingrese el aeropuerto de la puerta: ")
                    j.set__info (n,a)
                    j.set__estado(e)
                    print ("Puerta",n,"se modificó correctamente")
                    valor=False #The value variable is set as false 
    if valor==True: #if valor equal true
        print ("Puerta",n," no se pudo modificar correctamente")
def EliminaPuertas(num, a):
    for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
        if i.get__nombre()==a: #If i.get_name equal a
            for pu in i.get__ListaPuertas(): #Seacrch for the variable pu in the i.get_ListasPuertas
                if pu.get__NumeroPuerta()==num: #if pu.get__NumeroPuerta equal num
                    i.get__ListaPuertas().remove(pu) #Remove pu from i.get__ListaPuertas
                    print (num,"ha sido eliminada")
                    
def BuscaAerolineas(nombre): #Seacrch for the variable i in the airlines lists, if the name attribute within i matches name, it will return true
    for i in ListaAerolineas: 
        if i.get__nombre()==nombre: #If i is get_name equal to name
            return True
    return False
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
        if BuscaAerolineas(aerolinea[0])!=True: 
            ListaAerolineas.append (a)
        else:
            print ("La aerolínea ya existe")
    archi.close()
def MuestraAerolineas():
    print ("nombre","\t", "año de fundación", "\t","tipo","\t", "cantidad de países donde opera")
    for i in ListaAerolineas: #Seacrch for the variable i in the airport lists
        i.get__info()
def ModificaAerolineas(nombre):
    valor=True #The value variable is set as true
    for i in ListaAerolineas:  #Seacrch for the variable i in the airlines lists
        if i.get__nombre()==nombre: #If i is get_name equal to name
            nombre=input ("Ingrese el nuevo nombre de la aerolínea: ")
            año=int (input ("Ingrese el año de fundación de la aerolínea: "))
            tipo=input ("Ingrese el tipo (internacional o local): ")
            paises=int (input ("Ingrese la cantidad de paises que opera: "))
            i.set__info(nombre, año, tipo, paises)
            print (nombre, "se modificó correctamente")
            valor=False #The value variable is set as false
    if valor==True: #if valor equal true
        print (nombre,"no se pudo modificar")
def EliminaAerolineas(nombre):
    valor=True #The value variable is set as true
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        if i.get__nombre()==nombre: #If i is get_name equal to name
            ListaAerolineas.remove(i) #Removed i from the airlines list
            print (nombre,"se eliminó correctamente")
            valor=False #The value variable is set as false
    if valor==True: #if valor equal true
        print (nombre,"no se pudo eliminar")

def ValidaExistenciaAviones(ID,aerolinea):
    valor=True #The value variable is set as true
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        if i.get__nombre()==aerolinea: #If i is get_name equal to aerolinea
            valor=False #The value variable is set as false
            for j in i.get__ListaAviones(): #Seacrch for the variable j in i.get__ListaAviones
                if j.get__ID()==ID: #if j.get__ID equal ID
                    if j.get__ID()==ID: #if j.get__ID equal ID
                        return True #returns True if it found an equal ID
    if valor==True: #if valor equal true
        return -1 #If you did not find an existing airline equal to the one entered, it will not change the value by False, then it will return -1
    else:
        return False #if False returns it is because the airline does exist but it did not find an ID equal to the one it was looking for
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
        a=Avion()
        a.set__info(int(avion[0]), avion[1], int(avion[2]), avion[3], int(avion[4]), avion[5])
        validacion=ValidaExistenciaAviones(int(avion[0]), avion[3])
        if validacion==True: 
            print ("El avión ya existe")
        elif validacion==-1: 
            print ("El avión", avion[0],"no se pudo agregar")
        else:
            for i in ListaAerolineas: 
                if i.get__nombre()==avion[3]: 
                    i.set__ListaAviones(a)
    archi.close()
def MuestraAviones ():
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        for j in i.get__ListaAviones(): #Seacrch for the variable j in i.get__ListaAviones
            j.get__info()
def ModificaAviones (ID):
    contador=0
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        for j in i.get__ListaAviones(): #If j in i.get__ListaAviones
            if j.get__ID()==ID: #If j.get__ID equal ID
                ID=int (input ("Ingrese el ID del avión: "))
                modelo=input ("Ingrese el modelo del avión: ")
                AñoConstruccion=int (input ("Ingrese el año de fundación: "))
                aerolinea=input ("Ingrese el nombre de la aerolínea perteneciente: ")
                aerolinea=aerolinea.title()
                pasajeros=int (input ("Ingrese la cantidad de pasajeros del avión: "))
                estado=input ("Ingrese el estado (disponible o en uso): ")
                estado=estado.lower() #everything is changed to lowercase to avoid errors
                j.set__info (ID, modelo, AñoConstruccion, aerolinea, pasajeros)
                j.set__estado(estado)
                print ("Avion",ID,"se modificó correctamente")
                contador=1
    if contador==0: #If the counter stays at zero, it could not be changed
        print (ID,"no se ha podido modificar")
def EliminaAviones (ID):
    valor=True #The value variable is set as true
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        for j in i.get__ListaAviones(): #If j in i.get__ListaAviones
            if j.get__ID()==ID: #If j.get__ID equal ID
                if j.get__ID()==ID: #If j.get__ID equal ID
                    print (j.get__nombre(),"ha sido eliminado")
                    i.get__ListaAviones().remove(j) #Removed j from i.get__ListaAviones
                    valor=False #The value variable is set as false
    if valor==True: #if validacion equal true
        print ("Avión",ID,"no se ha podido eliminar")

def ValidaExistenciaTripulante (ID, aerolinea):
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        if i.get__nombre()==aerolinea: #If i is get_name equal to aerolinea
            for j in i.get__ListaTripulacion(): #Search for the variable j in the i.get__ListaTripulacion
                if j.get__ID()==ID: #If j.get__ID equal ID
                    return True
    return False
def CreaArchivoTripulacion():
    archi=open('Tripulacion.txt','w') 
    archi.close()
def CreaTripulacion(ID, nombre, nacimiento, aerolinea, rol, estado):
    archi=open('Tripulacion.txt','a') #se abre el archivo en modo adjunción
    archi.write(str(ID)+", "+str(nombre)+", "+str(nacimiento)+", "+str(aerolinea)+", "+str(rol)+", "+str(estado)+", ")
    archi.write('\n') #cuando cambia de elemento va a hacer la identacion
    archi.close()
def CreaTripulacionArchi():
    archi=open('Tripulacion.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        tripu=[]
        tripu=li.split(', ')
        t=Tripulacion()
        t.set__info(int(tripu[0]), tripu[1], tripu[2], tripu[3], tripu[4], tripu[5])
        if ValidaExistenciaTripulante (tripu[0], tripu[3])==True: #If ValidaExistenciaTripulante equal true
            print ("El tipulante", tripu[1], "ya existe con el mismo ID")
        else:
            for i in ListaAerolineas:
                if i.get__nombre()==tripu[3]: 
                    i.set__ListaTripulacion(t) 
    archi.close()
def MuestraTripulacion():
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        for j in i.get__ListaTripulacion(): #Search for the variable j in the i.get__ListaTripulacion
            j.get__info()
def ModificaTripulacion (ID): 
    valor=True #The value variable is set as true
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        for j in i.get__ListaTripulacion(): #Search for the variable j in the i.get__ListaTripulacion
            if j.get__ID()==ID: #If j.get__ID equal ID
                ID=int (input ("Ingrese el ID del tripulante: "))
                nacimiento=input ("Ingrese la fecha de nacimiento del tripulante: ")
                nombre=input ("Ingrese el nombre del tripulante: ")
                aerolinea=input ("Ingrese la aerolínea para la cual trabaja: ")
                rol=input ("Ingrese el rol del tripulante (piloto o servicio al cliente): ")
                estado=input ("Ingrese el estado del tripulante (disponible o en servicio): ")
                j.set__info (ID, nombre, nacimiento, aerolinea, rol)
                j.set__estado(estado)
                print ("Avion",ID,"se modificó correctamente")
                valor=False #The value variable is set as false
    if valor==True: #if validacion equal true
        print (ID,"no se ha podido modificar")
def EliminaTripulacion (ID):
    valor=True #The value variable is set as true
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        for j in i.get__ListaTripulacion(): #Search for the variable j in the i.get__ListaTripulacion
            if j.get__ID()==ID: #If j.get__ID equal ID
                print (j.get__nombre(),"ha sido eliminado")
                i.get__ListaTripulacion().remove(j) #Removed j from i.get__ListaTripulacion
                valor=False #The value variable is set as false
    if valor==True: #if validacion equal true
        print (ID,"no ha podido eliminarse")

def SumarHora(hora1):
        HoraSeparada=hora1.split(":") #Gives a list with the time separated from the minutes in the form of a string
        hora=int(HoraSeparada[0])+1 #The hour is passed to the whole and it is added 1 hour 
        if hora<10:
            hora=str(hora) 
            hora=hora.zfill(2) #If I have a character string, zfill (2) adds a 0 to the left
        else:
            hora=str(hora) #Then it is passed to string and then joined with join
        minuto=HoraSeparada[1]
        Lista=[hora, minuto]
        resultado=':'.join(Lista) #The hour and minutes are joined by means of the join
        return resultado
def ComparaFechas (fecha1,fecha2):
    f1=[]
    f2=[]
    f1=fecha1.split("/")
    f2=fecha2.split("/") 
    if f1[0]<=f2[0] and f1[1]<=f2[1] and f1[2]==f2[2]:
        return "menorigual"
    elif f1[1]<=f2[1] and f1[2]==f2[2]:
        return "menorigual"
    elif f1[0]>f2[0] and f1[1]>=f2[1] and f1[2]==f2[2]:
        return "mayorigual"
    else:
        return "mayorigual"
def RecorreTripulacion (aerolinea, FechaSalida, HoraSalida):
    FechaActual=time.strftime("%d/%m/%y") #The current date is called
    HoraActual=time.strftime("%H:%M") #It is called the current time
    HoraActual=SumarHora(HoraActual) #The function is called SumarHora
    ListaParaVuelo=[] #An empty list is created
    contador=0
    #print (ComparaFechas (FechaActual,FechaSalida))
    if ComparaFechas (FechaActual,FechaSalida)=="menorigual": #If the departure date matches the current date and the departure time matches the current time
        for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
            if i.get__nombre()==aerolinea: #If i is get_name equal to aerolinea
                for j in i.get__ListaTripulacion(): #Search for the variable j in i.get__ListaTripulacion
                    if j.get__rol()=="piloto" and contador<2: #if j.get__rol() equal "piloto" and j.get__estado() equal "disponible" and contador is less than 2
                        ListaParaVuelo.append(j) #j is added to the ListaParaVuelo
                        j.set__estado("no disponible") #the status changes to not available
                        contador+=1 #one is added to the contador
                        j.set__contador(1)
                    elif j.get__rol()=="servicio al cliente" and contador<5: #and j.get__estado()=="disponible"  #if j.get__rol() equal "servicio al cliente" and j.get__estado() equal "disponible" and contador is less than 5
                        ListaParaVuelo.append(j) #j is added to the ListaParaVuelo
                        j.set__estado("no disponible") #the status changes to not available
                        contador+=1 #one is added to the contador
                        j.set__contador(1)
                        if contador==5: #if contador equal 5, break
                            break
    if len(ListaParaVuelo)<5: #If len(ListaParaVuelo) less than 5
        return -1
    else:
        return ListaParaVuelo
    
def RecorreAvion(FechaSalida, HoraSalida):
    avion=""
    contador=0
    FechaActual=time.strftime("%d/%m/%y") #The current date is called
    HoraActual=time.strftime("%H:%M") #It is called the current time
    HoraActual=SumarHora(HoraActual) #The function is called SumarHora
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        if contador==0: #If contador equal 0
            for j in i.get__ListaAviones(): #Search for the variable j in i.get__ListaAviones
                #if j.get__estado()=="disponible": #If j.get__estado equal "disponible"
                 #   if ComparaFechas (FechaActual,FechaSalida)=="menorigual":
                        j.set__estado("no disponible") #the status changes to not available
                        avion=j
                        contador=1
                        break
        if contador==1:
            break
    if contador!=1: #If contador different to 1, return -1
        return -1
    else:
        return avion
def RecorrePistaSalida(AropuertoSalida, FechaSalida, HoraSalida):
    pista=""
    contador=0
    FechaActual=time.strftime("%d/%m/%y") #The current date is called
    HoraActual=time.strftime("%H:%M") #It is called the current time
    HoraActual=SumarHora(HoraActual) #The function is called SumarHora
    if contador==0: #If contador equal 0
        for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
            if i.get__nombre()==AropuertoSalida: #if i.get__nombre() equal AropuertoSalida
                for j in i.get__ListaPistas(): #Search for the variable j in i.get__ListaPistas
                    #if j.get__estado()=="disponible": #If j.get__estado equal "disponible"
                     #   if ComparaFechas (FechaActual,FechaSalida)=="menorigual":
                            j.set__estado("no disponible") #the status changes to not available
                            pista=j
                            contador=1
                            break
            if contador==1:
                break
        
    if contador!=1: #If contador different to 1, return -1
        return -1
    else:
        return pista
def RecorrePistaLlegada(Aropuertollegada, FechaSalida, HoraSalida):
    pista=""
    contador=0
    FechaActual=time.strftime("%d/%m/%y") #The current date is called
    HoraActual=time.strftime("%H:%M") #It is called the current time
    HoraActual=SumarHora(HoraActual) #The function is called SumarHora
    if contador==0: #If contador equal 0
        for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
            if i.get__nombre()==Aropuertollegada: #if i.get__nombre() equal AropuertoLlegada
                for j in i.get__ListaPistas(): #Search for the variable j in i.get__ListaPistas
                    #if j.get__estado()=="disponible": #If j.get__estado equal "disponible"
                     #   if ComparaFechas (FechaActual,FechaSalida)=="menorigual":
                            j.set__estado("no disponible")#the status changes to not available
                            pista=j
                            contador=1
                            break
            if contador==1: 
                break
        
    if contador!=1: #If contador different to 1, return -1
        return -1
    else:
        return pista
def RecorrePuertaSalida(AropuertoSalida, FechaSalida, HoraSalida):
    puerta=""
    contador=0
    FechaActual=time.strftime("%d/%m/%y") #The current date is called
    HoraActual=time.strftime("%H:%M") #It is called the current time
    HoraActual=SumarHora(HoraActual) #The function is called SumarHora
    if contador==0: #If contador equal 0
        for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
            if i.get__nombre()==AropuertoSalida: #if i.get__nombre() equal AropuertoSalida
                for j in i.get__ListaPuertas(): #Search for the variable j in i.get__ListaPuertas
                   # if j.get__estado()=="disponible":  #If j.get__estado equal "disponible"
                    #    if ComparaFechas (FechaActual,FechaSalida)=="menorigual":
                            j.set__estado("no disponible") #the status changes to not available
                            puerta=j
                            contador=1
                            break
            if contador==1: 
                break
        
    if contador==1: #If contador equal to 1, return puerta
        return puerta
    else:
        return -1
def RecorrePuertaLlegada(Aropuertollegada, FechaSalida, HoraSalida):
    puerta=""
    contador=0
    FechaActual=time.strftime("%d/%m/%y")#The current date is called
    HoraActual=time.strftime("%H:%M") #It is called the current time
    HoraActual=SumarHora(HoraActual) #The function is called SumarHora
    if contador==0: #If contador equal 0
        for i in ListaAeropuertos: #Seacrch for the variable i in the airport lists
            if i.get__nombre()==Aropuertollegada: #if i.get__nombre() equal AropuertoLlegada
                for j in i.get__ListaPuertas(): #Search for the variable j in i.get__ListaPuertas
                   # if j.get__estado()=="disponible": #If j.get__estado equal "disponible"
                    #    if ComparaFechas (FechaActual,FechaSalida)=="menorigual":
                            j.set__estado("no disponible") #the status changes to not available
                            puerta=j
                            contador=1
                            break
            if contador==1:
                break
        
    if contador==1: #If contador equal to 1, return puerta
        return puerta
    else:
        return -1
def ValidaExistenciaVuelos(codigo):
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        for j in i.get__ListaVuelos(): #Seacrch for the variable j  in i.get__ListaVuelos
            if j.get__codigo()==codigo: #if j.get__codigo() equal codigo, return true 
                return True
    return False

def CreaVuelosArchi():
    archi=open ('Vuelos.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        vuelo=[]
        vuelo=li.split(', ')
        codigo=vuelo[0]
        aerolinea=vuelo[1]
        FechaSalida=vuelo[2]
        HoraSalida=vuelo[3]
        HoraLlegada=vuelo[4]
        AropuertoSalida=vuelo[5]
        Aropuertollegada=vuelo[6]
        precio=vuelo[7]
        contador=0
        vuelo=Vuelos()
        vuelo.set__info(codigo, aerolinea, FechaSalida, HoraSalida, HoraLlegada, AropuertoSalida, Aropuertollegada, precio)
        ListaTripulacion = RecorreTripulacion (aerolinea, FechaSalida, HoraSalida)
        AvionParaVuelo = RecorreAvion (FechaSalida, HoraSalida)
        PistaParaVueloSalida = RecorrePistaSalida (AropuertoSalida, FechaSalida, HoraSalida)
        PuertaParaVueloSalida = RecorrePuertaSalida (AropuertoSalida, FechaSalida, HoraSalida)
        PistaParaVueloLlegada = RecorrePistaLlegada (Aropuertollegada, FechaSalida, HoraSalida)
        PuertaParaVueloLlegada = RecorrePuertaLlegada (Aropuertollegada, FechaSalida, HoraSalida)
        if ValidaExistenciaVuelos(codigo)==True: #if ValidaExistenciaVuelos(codigo) equal true:
            print ("Ya existe un vuelo con el código", codigo)
        else:
            for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
                if i.get__nombre()==aerolinea: #If i is get_name equal to aerolinea
                    if ListaTripulacion != -1: #If ListaTripulacion different -1
                        vuelo.set__tripulacion(ListaTripulacion)
                    else:

                        contador+=1 #A contador is added 1
                        print ("No hay tripulantes disponibles a esta hora")
                    if AvionParaVuelo != -1: #If AvionParaVuelo different -1
                        vuelo.set__avion(AvionParaVuelo)
                    else:
                        contador+=1 #A contador is added 1
                        print ("No hay un avión disponible a esta hora")
                    if PistaParaVueloSalida != -1: #If PistaParaVueloSalida different -1
                        vuelo.set__pista(PistaParaVueloSalida)
                    else:
                        contador+=1 #A contador is added 1
                        print ("No hay pista disponible a esta hora")
                    if PistaParaVueloLlegada != -1: #If PistaParaVueloLlegada different -1
                        vuelo.set__pistaLlegada(PistaParaVueloLlegada)
                    else:
                        contador+=1 #A contador is added 1
                        print ("No hay pista disponible a esta hora")
                    if PuertaParaVueloSalida != -1: #If PuertParaVueloSalida different -1
                        vuelo.set__puerta (PuertaParaVueloSalida)
                    else:
                        contador+=1 #A contador is added 1
                        print ("No hay una puerta de abordaje de salida lista para esta hora")
                    if PuertaParaVueloLlegada != -1: #If PuertaParaVueloLlegada different -1
                        vuelo.set__puertaLlegada (PuertaParaVueloLlegada)
                    else:
                        contador+=1 #A contador is added 1
                        print ("No hay una puerta de abordaje de llegada lista para esta hora")
            if contador==0: #If contador equal 0
                i.set__ListaVuelos (vuelo)
            else:
                print ("No se pudo realizar el vuelo", codigo)
                ModificaEstado(codigo)
    archi.close()
def CreaArchivoVuelos():
    archi=open('Vuelos.txt','w') 
    archi.close()
def CreaVuelos(codigo, aerolinea, FechaSalida, HoraSalida, HoraLlegada, AropuertoSalida, Aropuertollegada, precio):
    archi=open('Vuelos.txt','a') #se abre el archivo en modo adjunción
    archi.write(str(codigo)+", "+str(aerolinea)+", "+str(FechaSalida)+", "+str(HoraSalida)+", "+str(HoraLlegada)+", "+str(AropuertoSalida)+", "+str(Aropuertollegada)+", "+str(precio)+", ")
    archi.write('\n') #cuando cambia de elemento va a hacer la identacion
    archi.close() # se cierra el archivo


def MuestraVuelos ():
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        for j in i.get__ListaVuelos(): #Seacrch for the variable j in i.get__ListaVuelos
            j.get__info()
def ModificaEstado(codigo):
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        for j in i.get__ListaVuelos(): #Seacrch for the variable j in i.get__ListaVuelos
            if j.get__codigo()==codigo: #If j.get__codigo equal to codigo
                (j.get__pista()).set__estado("disponible") #the status changes to available
                (j.get__puerta()).set__estado("disponible") #the status changes to available
                (j.get__avion()).set__estado("disponible") #the status changes to available
                for k in i.get__tripulacion(): #Seacrch for the variable k in i.get__tripulacion
                    k.set__estado("disponible") #the status changes to available
def ModificaVuelos (codigo):
    ModificaEstado(codigo) #se cambia el estado a disponible de la tripulación, pistas y puertas
    contador=0
    ListaTripulacion=RecorreTripulacion (aerolinea, FechaSalida, HoraSalida)
    AvionParaVuelo=RecorreAvion(FechaSalida, HoraSalida)
    PistaParaVuelo=RecorrePistaSalida(AropuertoSalida, FechaSalida, HoraSalida)
    PuertaParaVuelo=RecorrePuertaSalida(AropuertoSalida, FechaSalida, HoraSalida)
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        for j in i.get__ListaVuelos(): #Seacrch for the variable j in i.get__ListaVuelos
            if j.get__codigo()==codigo: #If j.get__codigo equal to codigo
                codigo=input("Ingrese el código que reprsentará al vuelo: ")
                aerolinea=input("Ingrese la aerolinea a la que pertenece: ")
                FechaSalida=input ("Ingrese la Fecha de Salida: ")
                HoraSalida=input ("Ingrese la Hora de Salida: ")
                AropuertoSalida=input ("Ingrese el aeropuerto de Salida: ")
                Aropuertollegada=input ("Ingrese el aeropuerto de llegada: ")
                for k in ListaAerolineas: #Seacrch for the variable k in the airlines lists
                    if k.get__nombre()==j.get__aerolinea(): #Seacrch for the variable k in i.get__aerolinea
                        if ListaTripulacion == -1: #If ListaTripulacion equal -1
                            contador+=1 #A contador is added 1
                            print ("No hay tripulantes disponibles a esta hora")
                        if AvionParaVuelo == -1: #If AvionParaVuelo equal -1
                            contador+=1 #A contador is added 1
                            print ("No hay un avión disponible a esta hora")
                        if PistaParaVuelo == -1: #If PistaParaVuelo equal -1
                            contador+=1 #A contador is added 1
                            print ("No hay pista disponible a esta hora")
                        if PuertaParaVuelo == -1: #If PuertaParaVuelo equal -1
                            contador+=1 #A contador is added 1
                            print ("No hay una puerta de abordaje lista para esta hora")
    if contador!=0: #If contador different to 0
        print ("Vuelo", codigo, "no se pudo modificar")
    else:
        j.set__info (codigo, aerolinea, FechaSalida, HoraSalida, AropuertoSalida, Aropuertollegada)
        j.set__tripulacion(ListaTripulacion)
        j.set__avion(AvionParaVuelo)
        j.set__pista(PistaParaVuelo)
        j.set__puerta (PuertaParaVuelo)
        print ("Vuelo",codigo,"se modificó correctamente")
def EliminaVuelo (codigo):
    valor=True #The value variable is set as true
    for i in ListaAerolineas: #Seacrch for the variable i in the airlines lists
        for j in i.get__ListaVuelos(): #Seacrch for the variable j in i.get__ListaVuelos
            if j.get__codigo()==codigo: #If j.get__codigo equal to codigo
                print ("Vuelo",codigo,"se eliminó correctamente")
                (i.get__ListaVuelos()).remove(j) #Removed j from i.get__ListaVuelos
                valor=False #The value variable is set as false
    if valor==True: #if valor equal true
        print ("Vuelo",codigo, "no se pudo eliminar")

def CambiaEstadoEmpiezaVuelo():
    #function that changes the state of the runway and boarding gate when the flight starts
    FechaActual=time.strftime("%d/%m/%y")
    HoraActual=time.strftime("%H:%M")
    for i in ListaAerolineas:
        for j in i.get__ListaVuelos():
            if FechaActual==j.get__fecha() and HoraActual<=j.get__HoraSalida():
                (j.get__pista()).set__estado("disponible")
                (j.get__puerta()).set__estado("disponible")
def CambiaEstadoTerminaVuelo():
    #function that will change the state of the plane and the crew when the flight ends
    FechaActual=time.strftime("%d/%m/%y")
    HoraActual=time.strftime("%H:%M")
    for i in ListaAerolineas:
        for j in i.get__ListaVuelos():
            if FechaActual==j.get__fecha() and HoraActual>=j.get__HoraLlegada():
                (j.get__avion()).set__estado("disponible")
                (j.get__pistaLlegada()).set__estado("disponible")
                (j.get__puertaLlegada()).set__estado("disponible")
                for k in i.get__tripulacion():
                    k.set__estado("disponible")

def ReporteVueloPorFechas(FechaInicial, FechaFinal): #Function that shows flight reports in a range of dates.
    for i in ListaAerolineas:
        for j in i.get__ListaVuelos():
            if j.get__fecha()>=FechaInicial and j.get__fecha()<=FechaFinal:
                j.get__info()
def ReportePuertas(puerta, aeropuerto): #Function that shows flight reports flights at a boarding gate.
    for i in ListaAerolineas:
        for j in i.get__ListaVuelos():
            if (j.get__puerta()).get__NumeroPuerta()==puerta and (j.get__puerta()).get__aeropuerto()==aeropuerto:
                j.get__info()
def ReporteAeropuertos(): #Function that shows the reports of the ranking of airports with the most registered flights showing name and amount.
    ContadorAeropuertoMayor=-999999
    AeropuertoMayor=[]
    for i in ListaAeropuertos:
        for j in ListaAerolineas:
            contador=0
            for k in j.get__ListaVuelos():
                if k.get__aeropuerto()==i.get__nombre():
                    contador+=1
                    if contador>ContadorAeropuertoMayor:
                        ContadorAeropuertoMayor=contador
    for i in ListaAeropuertos:
        for j in ListaAerolineas:
            contador=0
            for k in j.get__ListaVuelos():
                if k.get__aeropuerto()==i.get__nombre():
                    contador+=1
                    if contador==ContadorAeropuertoMayor:
                        AeropuertoMayor.append(i)
    print ("\n","El/los aeropuerto(s) con más vuelos registrados es(son):")                
    for m in AeropuertoMayor:
        print (m.get__nombre())
    print ("Con",ContadorAeropuertoMayor,"vuelos registrados")
                
def ReporteTripulacion(): #Function that shows the reports of the ranking of crew members with the most flights made.
    ContadorTripulacionMayor=-999999
    TripulacionMayor=[]
    for i in ListaAerolineas:
        for j in i.get__ListaVuelos():
            for k in j.get__tripulacion():
                if k.get__contador()>ContadorTripulacionMayor:
                    ContadorTripulacionMayor=k.get__contador()

    for n in ListaAerolineas:
        for s in n.get__ListaVuelos():
            for t in s.get__tripulacion():
                if t.get__contador()==ContadorTripulacionMayor:
                        TripulacionMayor.append (t)
    print ("\n","Los tripuantes con más vuelos registrados son:")
    for trip in TripulacionMayor:
        print (trip.get__nombre())
    print ("Con",ContadorTripulacionMayor,"vuelos registrados")

#etapa 2
def RangodeFechas (FechaSalida, FechaVuelo, FechaLlegada):
    #Function that compares that the date of the flight is in the range of the dates entered by the user
    f1=[]
    f2=[]
    f3=[]
    f1=FechaSalida.split("/")
    f2=FechaVuelo.split("/")
    f3=FechaLlegada.split ("/")
    if f1[1]<=f2[1] and f2[1]<=f3[1] and f1[2]==f2[2]:
        return True
    else:
        return False
def ValidaVuelosDirectos(AeroOrigen, AeroDestino, FechaSalida, FechaLlegada):
    #function that verifies that a flight already exists in the list of the following function, this in order that the flight does not repeat
    VuelosDirectos=[]
    for i in ListaAerolineas:
        for j in i.get__ListaVuelos():
            if RangodeFechas (FechaSalida, j.get__fecha(), FechaLlegada)==True:
                if j.get__aeropuerto()==AeroOrigen and j.get__AeropuertoLlegada()==AeroDestino:
                    VuelosDirectos.append([j])
    return VuelosDirectos

def CreaEscalas (AeroOrigen, AeroDestino, FechaSalida, FechaLlegada):
    """
    Function that runs through the list of flights, if you find a direct flight within the indicated time range, add it
    to the list of direct flights of the Escala class, but will create scales by going through the list of flights again
    and if the airport of arrival of the first coincides with the departure airport of the second, the arrival airport
    of the second with the destination airport, add flights to a sublist of the list of stopovers
    """
    VD=[]
    AS=[]
    AL=[]
    escalas2=[]
    escala=[]
    escglobal=[]
    valor=False
    for i in ListaAerolineas:
        for j in i.get__ListaVuelos():
            if RangodeFechas (FechaSalida, j.get__fecha(), FechaLlegada)==True:
                if j.get__aeropuerto()==AeroOrigen and j.get__AeropuertoLlegada()==AeroDestino:
                    VD.append([j])
                elif j.get__aeropuerto()==AeroOrigen:
                    AS.append(j)
                elif j.get__AeropuertoLlegada()==AeroDestino:
                    AL.append(j)
    for i in ListaAerolineas:
        for j in i.get__ListaVuelos():
            for k in AS:
                for m in AL:
                    if j.get__aeropuerto()==k.get__AeropuertoLlegada() and j.get__AeropuertoLlegada()==m.get__aeropuerto():
                        escalas2.append([k,j,m])
                    elif k.get__AeropuertoLlegada()==m.get__aeropuerto():
                        if ValidaEscalas(escala, k.get__codigo(), m.get__codigo())!=True:
                            escala.append([k,m])
    escglobal=[VD, escala, escalas2]
    #print (escglobal)
    return escglobal
def ValidaEscalas(lista, codvuelo1, codvuelo2):
    for i in lista:
        if i[0].get__codigo()==codvuelo1 and i[1].get__codigo()==codvuelo2:
            return True
    return False

def MostrarEscalas(viajes):
    """
    function that travels the list of trips and shows first the information of the direct flights and then
    shows the scales, has a counter that will allow the user to choose which trip to choose
    """
    cont=1
    if len (viajes[0])>0:
        print ("\n\t\tVuelos Directos") 
        for j in viajes[0]:
            print (cont,"- Salida:",j[0].get__aeropuerto(), "\tFecha Salida:", j[0].get__fecha(), "\tHora de salida",j[0].get__HoraSalida())
            print ("Destino:",j[0].get__AeropuertoLlegada(),"\tHora de llegada",j[0].get__HoraLlegada())
            print ("Precio:", j[0].get__precio())
            cont+=1
            print("\n")
    if len(viajes[1])>0:
        print ("\n\t\tEscala (2 vuelos)")    
        for i in viajes[1]:
            precio=int(i[0].get__precio())+int(i[1].get__precio())
            print (cont,"- Salida:",i[0].get__aeropuerto(),"\tFecha Salida:",i[0].get__fecha(), "\tHora de salida",i[0].get__HoraSalida())
            print ("A. Intermedio:", i[1].get__aeropuerto(),"\thora Salida (vuelo 2):", i[1].get__HoraSalida(),"\tHora de salida:", i[1].get__HoraSalida(),"\tDestino:",i[1].get__AeropuertoLlegada())
            print ("Precio:", precio)
            cont+=1
            print ("\n")
    if len(viajes[2])>0:
        print ("\n\t\tEscala (3 vuelos)")
        for k in viajes[2]:
            precio=int(k[0].get__precio())+int(k[1].get__precio())+int(k[2].get__precio())
            print (cont,"- Salida:",k[0].get__aeropuerto(),"\tFecha Salida:",k[0].get__fecha(), "\tHora de salida",k[0].get__HoraSalida())
            print ("Aeropuertos Intermedios:", k[1].get__aeropuerto(), k[1].get__AeropuertoLlegada(),"\tFecha Salida (vuelo 2):", k[1].get__fecha(),"\tHora de salida:", k[1].get__HoraSalida(),"\tDestino:",k[2].get__AeropuertoLlegada())
            print ("Precio:", precio)
            cont+=1
            print("\n")
    if cont==1:
        return False
    else:
        return True
def EscribeHistorial(ID, vuelo):
    #Go through the list of users and if the IDs match, add the trip to the passenger's flight history
    for i in ListaUsuarios:
        if i.get__ID()==ID:
            if len(vuelo)==1:
                i.set__historial(vuelo)
                archi=open("Historial.txt","a")
                archi.write(str(ID)+", "+str(vuelo[0].get__codigo()))
                archi.close()
            elif len(vuelo)==2:
                i.set__historial(vuelo)
                archi=open("Historial.txt","a")
                archi.write(str(ID)+", "+str(vuelo[0].get__codigo())+", "+str(vuelo[1].get__codigo()))
                archi.close()
            elif len(vuelo)==3:
                i.set__historial(vuelo)
                archi=open("Historial.txt","a")
                archi.write(str(ID)+", "+str(vuelo[0].get__codigo())+", "+str(vuelo[1].get__codigo())+", "+str(vuelo[2].get__codigo()))
                archi.close()
def SeleccionarViaje(ID,viajes,v):
    #the flights are sent in a list, this function travels the flights and compares that the number that the user entered is equal to the trip that was shown    
    cont=1
    if len (viajes[0])>0:
        for j in viajes[0]:
            if cont==v:
                print ("Su vuelo directo ha sido agregado a su historial de viajes!")
                return EscribeHistorial(ID, j)
            cont+=1
    if len(viajes[1])>0:
        for i in viajes[1]:
            if cont==v:
                print ("Su viaje ha sido agregado a su historial de viajes!")
                return EscribeHistorial(ID, i)
            cont+=1
    if len(viajes[2])>0:
        for k in viajes[2]:
            if cont==v:
                print ("Su viaje ha sido agregado a su historial de viajes!")
                return EscribeHistorial(ID, k)
            cont+=1
    print ("Su viaje no se ha podido agregar al historial, verifique que sí exista tal viaje")
    
def MuestraVuelosPrecio():
    """
    function that saves the flight object and the price of such in a dictionary, the values are ordered ascending
    what are the prices, then they are added to a list and the information of the object is displayed
    """
    precios={} 
    preciosordenados=[]
    for i in ListaAerolineas: 
        for j in i.get__ListaVuelos():
            precios[j]=j.get__precio()

    ordenados=sorted(precios.items(), key=lambda x: x[1])
    for k in ordenados:
        preciosordenados.append(k[0])
    for m in preciosordenados:
        m.get__info__viajes()
def MuestraVuelosFecha():
    """
    Passes the hours to minutes, adds the object and the result to a dictionary, it is sorted, added to a list,
    then the list is scanned and the flight information is displayed
    """
    horas={}
    horasordenadas=[]
    for i in ListaAerolineas:
        for j in i.get__ListaVuelos():
            h1=[]
            h2=[]
            h1=(j.get__HoraSalida()).split(":")
            h2=(j.get__HoraLlegada()).split(":")
            min1=int(h1[0])*60+int(h1[1])
            min2=int(h2[0])*60+int(h2[1])
            resultado=min2-min1
            horas[j]=resultado
    ordenado = sorted(horas.items(), key=operator.itemgetter(1))
    for k in ordenado:
        horasordenadas.append(k[0])
    for m in horasordenadas:
        m.get__info__viajes()
        
def MostrarHistorialPasajero(IDPasajero):
    #go through the users list and show the flight history of a passenger
    for i in ListaUsuarios:
        if i.get__ID()==IDPasajero:
            i.get__historial()
    
def BusquedaInteligentePrecio (AeropuertoSalida,AeropuertoLlegada,FechaSalida,FechaLlegada):
    """
    Go through the list of flights, if the airports match, add the flight to a dictionary, where the key is the object
    and the value is the price, then order the dictionary from lowest to highest with the value and then show them
    """
    precios={}
    preciosordenados=[]
    contador=0
    valor=True
    while contador <= 5 and valor==True:
        for i in ListaAerolineas:
            for j in i.get__ListaVuelos():
                if RangodeFechas (FechaSalida, j.get__fecha(), FechaLlegada)==True:
                    if j.get__aeropuerto()==AeropuertoSalida and j.get__AeropuertoLlegada()==AeropuertoLlegada:
                        precios[j]=j.get__precio()
                        contador+=1
        valor=False                        
    ordenado= sorted (precios.items(), key=operator.itemgetter(1))
    for k in ordenado:
        preciosordenados.append (k[0])
    for m in preciosordenados:
        m.get__info__viajes()
def BusquedaInteligenteTiempo(AeropuertoSalida,AeropuertoLlegada,FechaSalida,FechaLlegada):
    """
    Passes the hours to minutes, adds the object and the result to a dictionary, it is sorted, added to a list,
    then the list is scanned and the flight information is displayed
    """
    horas = {}
    horasordenadas = []
    contador = 0
    valor=True
    while contador <= 5 and valor==True:
        for i in ListaAerolineas:
            for j in i.get__ListaVuelos():
                if RangodeFechas (FechaSalida, j.get__fecha(), FechaLlegada)==True:
                    if j.get__aeropuerto() == AeropuertoSalida and j.get__AeropuertoLlegada() == AeropuertoLlegada:
                        if j.get__HoraSalida() < j.get__HoraLlegada():
                            h1 = []
                            h2 = []
                            h1 = (j.get__HoraSalida()).split(":")
                            h2 = (j.get__HoraLlegada()).split(":")
                            min1 = int(h1[0])*60+int(h1[1])
                            min2 = int(h2[0])*60+int(h2[1])
                            resultado = min2-min1
                            horas[j] = resultado
                            contador+=1
        valor=False        
    ordenado = sorted(horas.items(), key=operator.itemgetter(1))
    for k in ordenado:
        horasordenadas.append(k[0])
    for m in horasordenadas:
        m.get__info__viajes()
            
def MuestraMatriz(AeroOrigen, AeroDestino, FechaSalida, FechaLlegada):
    fechas=[]
    precios=[]
    viajes=CreaEscalas (AeroOrigen, AeroDestino, FechaSalida, FechaLlegada)
    for i in viajes:
        for j in i:
            if len(j)==1:
                fechas.append(j[0].get__fecha())
                precios.append(j[0].get__precio())
            elif len(j)==2:
                fechas.append(j[0].get__fecha())
                costo=int(j[0].get__precio())+int(j[1].get__precio())
                precios.append(costo)
            elif len(j)==3:
                fechas.append(j[0].get__fecha())
                costo=int(j[0].get__precio())+int(j[1].get__precio())+int(j[2].get__precio())
                precios.append(costo)
    matriz=[fechas,precios]
    for k in fechas:
        print (k, end="  ")
    print("")
    for m in precios: 
        print (m, end="    ")
    print("")
    for k in fechas: 
        print (k,end="  ")
    print ("")
def MostrarUsuarios():
    #function that shows users to the administrator
    for i in ListaUsuarios:
        i.get__info()
def ValidaExistenciaUsuario(ID):
    for i in ListaUsuarios:
        if i.get__ID()==ID:
            return True
    return False
def MostrarInformacionPasajero(IDPasajero):
    #function that shows the information of the passenger who wishes to see his own information
    for i in ListaUsuarios:
        if i.get__ID()==IDPasajero:
            i.get__info()
def ModificaPasajeros(IDPasajero):
    #allows to modify passenger information
    for i in ListaUsuarios:
        if i.get__ID()==IDPasajero:
            n=input("Ingrese el nombre completo: ")
            ID=int(input ("Ingrese el número de cédula de la siguiente manera: #0###0###: "))
            e=int(input ("Ingrese la edad: "))
            correo=input ("ingrese el correo electrónico: ")
            contra=input ("Ingrese la contraseña: ")
            if ValidaExistenciaUsuario(ID)!=True:
                i.set__info(n,ID,e,correo,contra,3)
            else:
                print ("El ID ya existe, los datos no se modificaron")
def ModificaUsuarios(ID):
     #allows to modify user information
    for i in ListaUsuarios:
        if i.get__ID()==ID:
            n=input("Ingrese el nombre completo: ")
            ID=int(input ("Ingrese el número de cédula de la siguiente manera: #0###0###: "))
            e=int(input ("Ingrese la edad: "))
            correo=input ("ingrese el correo electrónico: ")
            contra=input ("Ingrese la contraseña: ")
            t=int(input ("Ingrese el tipo (1- administrador, 2- invitado, 3-pasajero)"))
            i.set__info(n,ID,e,correo,contra,t)

def RecorrerArchiVuelo ():
    archi=open('Vuelos.txt','w')
    archi.close()
    archi=open ('Vuelos.txt','a')
    for i in ListaAerolineas:
        for j in i.get__ListaVuelos():
            cod=j.get__codigo()
            IAV=j.get__aerolinea()
            FS=j.get__fecha()
            HS=j.get__HoraSalida()
            HL=j.get__HoraLlegada()
            AS=j.get__aeropuerto()
            AL=j.get__AeropuertoLlegada()
            p=j.get__precio()
            archi.write(str(cod)+", "+str(IAV)+", "+str(FS)+", "+str(HS)+", "+str(HL)+", "+str(AS)+", "+str(AL)+", "+str(p)+", ")
            archi.write('\n') 
    archi.close()

def RecorrerArchiHistorial():
    archi=open("Historial.txt","w")
    for i in ListaUsuarios:
        if i.get__historial()!="None" or len(i.get__historial())!=0:
            for j in i.get__historial():
                if len(j)==1:
                    archi.write (str(i.get__ID())+", ",str(j[0].get__codigo()))
                elif len(j)==2:
                    archi.write (str(i.get__ID())+", ",str(j[0].get__codigo())+", "+str(j[1].get__codigo()))
                elif len(j)==3:
                    archi.write (str(i.get__ID())+", ",str(j[0].get__codigo())+", "+str(j[1].get__codigo())+", "+str(j[2].get__codigo()))
                archi.write ("\n")
    archi.close()
def Menu():
    valor=False
    while valor==False or valor==True:
        objeto=IniciarSesion ()
        tipo=objeto.get__tipo()
        IDPasajero=objeto.get__ID()
        comando=0
        if tipo==1:
            valor=True
            while comando!=-1 and valor==True:
                #try:
                    CambiaEstadoEmpiezaVuelo()
                    CambiaEstadoTerminaVuelo()
                    print ("\n","\t","Menú de opciones")
                    print ("1-Registrar un usuario")
                    print ("2-Aeropuertos (Aeropuertos, Pistas, Puertas de Abordaje)")
                    print ("3-Aerolineas (Aerolíneas, Aviones, Tripulación, Vuelos)")
                    print ("4-Ver reportes de vuelos")
                    print ("5-Ver información de los usuarios")
                    print ("6-Modificar la información de un usuario")
                    print ("7-Refrescar datos (vuelos)")
                    print ("8-Cerrar sesión")
                    comando=int(input ("Ingrese la opción que desea realizar: "))
                    if comando==1:
                        n=input("Ingrese el nombre completo: ")
                        ID=int(input ("Ingrese el número de cédula de la siguiente manera: #0###0###: "))
                        e=int(input ("Ingrese la edad: "))
                        correo=input ("ingrese el correo electrónico: ")
                        contra=input ("Ingrese la contraseña: ")
                        t=int(input ("Ingrese el tipo (1- administrador, 2- invitado, 3-pasajero)"))
                        CreaUsuario (n,ID,e,correo,contra,t)
                        print ("Usuario registrado")
                        
                    elif comando==2:
                        print ("1-Aeropuertos", "\n","2-Pistas", "\n","3-Puertas de Abordaje")
                        opcion=int(input ("Ingrese la opción que desea realizar: "))
                        if opcion==1:
                            print ("1-Agregar Aeropuertos","\n","2-Ver Aeropuertos","\n","3-Modificar Aeropuertos","\n","4-Eliminar Aeropuertos")
                            decision=int(input ("Ingrese la opción que desea realizar: "))
                            if decision==1:
                                nombre=input ("Ingrese el nombre del aeropuerto: ")
                                nombre=nombre.title()
                                ciudad=input ("Ingrese el nombre de la ciudad actual: ")
                                ciudad=ciudad.title()
                                pais=input ("Ingrese el país en el que opera: ")
                                pais=pais.title()
                                CreaAeropuertos (nombre, ciudad, pais)
                            elif decision==2:
                                MuestraAeropuertos()
                            elif decision==3:
                                nombre=input("Ingrese el nombre del aeropuerto que desea modificar: ")
                                ModificaAeropuerto (nombre)
                            elif decision==4:
                                nombre=input("Ingrese el nombre del aeropuerto que desea eliminar: ")
                                nombre=nombre.title()
                                EliminaAeropuertos(nombre)
                        elif opcion==2:
                            print ("1-Agregar Pistas","\n","2-Ver Pistas","\n","3-Modificar Pistas","\n","4-Eliminar Pistas")
                            decision=int(input ("Ingrese la opción que desea realizar: "))
                            if decision==1:
                                num=int(input("ingrese el número de la pista: "))
                                e=input ("Ingrese el estado de la pista (disponible, no disponible o en mantenimiento): ")
                                e=e.lower()
                                a=input ("Ingrese el nombre del Aeropuerto al que pertenecerá la pista: ")
                                CreaPistas(num, e, a)
                            elif decision==2:
                                MuestraPistas ()
                            elif decision==3:
                                num=int (input ("Ingrese el número de pista que desea modificar: "))
                                a=input("Ingrese el aeropuerto de la pista que desea modificar: ")
                                a=a.title()
                                ModificaPistas (num, a)
                            elif decision==4:
                                num=int (input ("Ingrese el número de pista que desea eliminar: "))
                                a=input("Ingrese el aeropuerto de la pista que desea eliminar: ")
                                a=a.title()
                                EliminaPistas(num, a)
                                
                        elif opcion==3:
                            print ("1-Agregar Puertas de Abordaje","\n","2-Ver Puertas de Abordaje","\n","3-Modificar Puertas de Abordaje","\n","4-Eliminar Puertas de Abordaje")
                            decision=int(input ("Ingrese la opción que desea realizar: "))
                            if decision==1:
                                num=int(input("ingrese el número de la puerta de abordaje: "))
                                e=input ("Ingrese el estado de la puerta de abordaje (disponible o en uso): ")
                                e=e.lower()
                                CreaPuertasAbordaje(num, e)
                            elif decision==2:
                                MuestraPuertas()
                            elif decision==3:
                                num=int(input("ingrese el número de la puerta de abordaje que desea modificar: "))
                                a=input("Ingrese el aeropuerto de la puerta de abordaje que desea modificar: ")
                                a=a.title()
                                ModificaPuertas(num,a)
                            elif decision==4:
                                num=int(input("ingrese el número de la puerta de abordaje que desea eliminar: "))
                                a=input("Ingrese el aeropuerto de la puerta de abordaje que desea eliminar: ")
                                a=a.title()
                                EliminaPuertas(num,a)
                                
                    elif comando==3:
                        print ("1-Aerolíneas","\n","2-Aviones","\n","3-Tripulación","\n","4-Vuelos")
                        opcion=int(input ("Ingrese la opción que desea realizar: "))
                        if opcion==1:
                            print ("1-Agregar Aerolíneas","\n","2-Ver Aerolíneas","\n","3-Modificar Aerolíneas","\n","4-Eliminar Aerolíneas")
                            decision=int(input ("Ingrese la opción que desea realizar: "))
                            if decision==1:
                                nombre=input ("Ingrese el nombre de la aerolínea: ")
                                nombre=nombre.title ()
                                año=int (input ("Ingrese el año de fundación de la aerolínea: "))
                                tipo=input ("Ingrese el tipo (internacional o local): ")
                                tipo=tipo.capitalize()
                                paises=int (input ("Ingrese la cantidad de paises que opera: "))
                                CreaAerolineas(nombre, año, tipo, paises)
                            elif decision==2:
                                MuestraAerolineas ()
                            elif decision==3:
                                nombre=input("Ingrese el nombre de la aerolínea que desea modificar: ")
                                nombre=nombre.title()
                                ModificaAerolineas (nombre)
                            elif decision==4:
                                nombre=input("Ingrese el nombre de la aerolínea que desea eliminar: ")
                                nombre=nombre.title()
                                EliminaAerolineas (nombre)
                            
                        elif opcion==2:
                            print ("1-Agregar Aviones","\n","2-Ver Aviones","\n","3-Modificar Aviones","\n","4-Eliminar Aviones")
                            decision=int(input ("Ingrese la opción que desea realizar: "))
                            if decision==1:
                                ID=int (input ("Ingrese el ID del avión: "))
                                modelo=input ("Ingrese el modelo del avión: ")
                                AñoConstruccion=int (input ("Ingrese el año de fundación: "))
                                aerolinea=input ("Ingrese el nombre de la aerolínea perteneciente: ")
                                aerolinea=aerolinea.title()
                                pasajeros=int (input ("Ingrese la cantidad de pasajeros del avión: "))
                                estado=input ("Ingrese el estado (disponible o en uso): ")
                                estado=estado.lower()
                                CreaAviones(ID, modelo, AñoConstruccion, aerolinea, pasajeros, estado)
                            elif decision==2:
                                MuestraAviones()
                            elif decision==3:
                                ID=int(input("ingrese el ID del avión que desea modificar: "))
                                ModificaAviones (ID)
                            elif decision==4:
                                ID=int(input("ingrese el ID del avión que desea eliminar: "))
                                EliminaAviones (ID)
                        elif opcion==3:
                            print ("1-Agregar Tripulantes","\n","2-Ver Tripulación","\n","3-Modificar la Tripulación","\n","4-Eliminar Tripulación")
                            decision=int(input ("Ingrese la opción que desea realizar: "))
                            if decision==1:
                                ID=int (input ("Ingrese el ID del tripulante"))
                                nombre=input("Ingrese el nombre del tripulante: ")
                                nacimiento=input ("Ingrese la fecha de nacimiento del tripulante: ")
                                aerolinea=input ("Ingrese la aerolínea para la cual trabaja: ")
                                rol=input ("Ingrese el rol del tripulante (piloto o servicio al cliente): ")
                                estado=input ("Ingrese el estado del tripulante (disponible o en servicio): ")
                                CreaTripulacion (ID, nombre, nacimiento, aerolinea, rol, estado)
                            elif decision==2:
                                MuestraTripulacion()
                            elif decision==3:
                                ID=int (input ("Ingrese el ID del tripulante que desea modificar: "))
                                ModificaTripulacion(ID)
                            elif decision==4:
                                ID=int (input ("Ingrese el ID del tripulante que desea eliminar: "))
                                EliminaTripulacion(ID)
                        elif opcion==4:
                            print ("1-Agregar Vuelos","\n","2-Ver Vuelos","\n","3-Modificar Vuelos","\n","4-Eliminar Vuelos")
                            decision=int(input ("Ingrese la opción que desea realizar: "))
                            if decision==1:
                                codigo=input("Ingrese el código que reprsentará al vuelo: ")
                                aerolinea=input("Ingrese la aerolinea a la que pertenece: ")
                                print ("Ingrese la fecha con el siguiente formato (dd/mm/yy) \n ejemplo: 22/04/19")
                                FechaSalida=input ("Ingrese la Fecha de Salida: ")
                                HoraSalida=input ("Ingrese la Hora de Salida: ")
                                HoraLlegada=input ("Ingrese la Hora de llegada: ")
                                AropuertoSalida=input ("Ingrese el aeropuerto de Salida: ")
                                Aropuertollegada=input ("Ingrese el aeropuerto de llegada: ")
                                CreaVuelos (codigo, aerolinea, FechaSalida, HoraSalida, HoraLlegada, AropuertoSalida, Aropuertollegada)
                            elif decision==2:
                                MuestraVuelos()
                            elif decision==3:
                                codigo=input("Inserte el código del vuelo que desea modificar")
                                ModificaVuelos (codigo)
                            elif decision==4:
                                codigo=input("Inserte el código del vuelo que desea eliminar")
                                EliminaVuelos(codigo)
                    elif comando==4:
                        print ("1-Ver la lista de vuelos en un rango de fechas")
                        print ("2-Ver la lista de vuelos en una puerta de embarque de un aeropuerto de salida")
                        print ("3-Ver el ranking de aeropuertos con más vuelos registrados")
                        print ("4-Ver el ranking de miembros de la tripulación con más vuelos realizados")
                        opcion=int(input ("Ingrese el número de la opción que desea realizar: "))
                        if opcion==1:
                            print ("Favor dar las fechas con el siguiente formato dd/mm/yy")
                            print ("Ejemplo: 22/04/19")
                            FechaInicial=input("Ingrese la fecha inicial: ")
                            FechaFinal=input("Ingrese la fina final: ")
                            ReporteVueloPorFechas(FechaInicial, FechaFinal)
                        elif opcion==2:
                            puerta=int(input("Ingrese el número de la puerta de abordaje: "))
                            aeropuerto=input("Ingrese el aeropuerto de la puerta de abordaje: ")
                            ReportePuertas(puerta, aeropuerto)
                        elif opcion==3:
                            ReporteAeropuertos()
                        elif opcion==4:
                            ReporteTripulacion()
                    elif comando==5:
                        MostrarUsuarios()
                    elif comando==6:
                        ID=int(input("Ingrese el ID del usuario que desea modificar"))
                        if ValidaExistenciaUsuario(ID)==True:
                            ModificaUsuarios(ID)
                        else:
                            print ("El ID indicado no existe")
                    elif comando==7:
                        RecorrerArchiVuelo ()
                        print ("El archivo de vuelos ha sido refrescado")
                    elif comando==8:
                        valor=False
                        print("Sesión cerrada")
                #except:
                    #print ("Error en datos")
        elif tipo==2:
            valor=True
            while comando!=-1 and valor==True:
                try:
                    CambiaEstadoEmpiezaVuelo()
                    CambiaEstadoTerminaVuelo()
                    print ("\n","\t","Menú de opciones")
                    print ("1-Aeropuertos (Aeropuertos, Puertas de Abordaje, Pistas)")
                    print ("2-Aerolineas (Aerolíneas, Aviones, Tripulación, Vuelos)")
                    print ("3-Cerrar sesión")
                    comando=int(input ("Ingrese la opción que desea realizar: "))

                    if comando==1:
                        print ("Seleccione el número que desea ver")
                        print ("1-Aeropuertos", "\n","2-Pistas", "\n","3-Puertas de Abordaje")
                        opcion=int(input ("Ingrese la opción que desea realizar: "))
                        if opcion==1:
                            MuestraAeropuertos()
                        elif opcion==2:
                            MuestraPistas ()
                        elif opcion==3:
                            MuestraPuertas()
                    if comando==2:
                        print ("1-Aerolíneas", "\n", "2-Aviones","\n", "3-Tripulación", "\n", "4-Vuelos")
                        opcion=int(input ("Ingrese la opción que desea realizar: "))
                        if opcion==1:
                            MuestraAerolineas()
                        elif opcion==2:
                            MuestraAviones()    
                        elif opcion==3:
                            MuestraTripulacion()
                        elif opcion==4:
                            MuestraVuelos()
                    elif comando==3:
                        valor=False
                        print("Sesión cerrada")
                except:
                    print ("Error en datos")
        elif tipo ==3:
            valor=True
            while comando!=-1 and valor==True:
                #try:
                    CambiaEstadoEmpiezaVuelo()
                    CambiaEstadoTerminaVuelo()
                    print ("\n","\t","Menú de opciones")
                    print ("1-Busqueda de Vuelos (solo ida - ida y vuelta, Por precio - Por duración)")
                    print ("2-Busqueda de Vuelos inteligente (Más baratos, Matriz de precios y fechas)")
                    print ("3-Perfil (Ver historial de vuelos, modificar información)")
                    print ("4-Refrescar datos (Historial y vuelos)")
                    print ("5-Cerrar Sesión")
                    comando=int(input ("Ingrese la opción que desea realizar: "))

                    if comando == 1:
                        print ("\n\t\tBúsqueda de vuelos")
                        print ("1-Seleccionar Vuelo de Ida")
                        print ("2-Seleccionar Vuelo de Ida y Vuelta")
                        print ("3-Mostra Vuelos por Precios (de menor a mayor)")
                        print ("4-Mostra Vuelos por Tiempo de Llegada (del más rápido al más lento)")
                        opcion=int(input ("Ingrese la opción que desea realizar: "))
                        if opcion == 1:
                            cont=1
                            for i in ListaAeropuertos: #print the list of airports with a counter and so the user enters the number of the airport you want to select
                                print(cont,end="- ") 
                                print (i.get__nombre())
                                cont+=1
                            num1=int(input("\nSeleccione el Aeorpuerto de origen: "))
                            num2=int(input("Seleccione el Aeorpuerto de destino: "))
                            AeroOrigen=ListaAeropuertos[num1-1].get__nombre()
                            AeroDestino=ListaAeropuertos[num2-1].get__nombre()
                            FechaSalida=input ("Ingrese la inicial (dd/mm/yy): ")
                            FechaLlegada=input ("Ingrese la fecha final (dd/mm/yy): ")
                            viajes=CreaEscalas (AeroOrigen, AeroDestino, FechaSalida, FechaLlegada)
                            if MostrarEscalas(viajes)==True: #shows all the possible trips that the user can choose, in case of not having one, False returns and does not ask him to select trips
                                v=int(input("Seleccione el número de viaje: "))
                                SeleccionarViaje(IDPasajero,viajes,v) #Look for the passenger number and when you find the trip, call the function to add it to the flight history
                            else:
                                print ("Lo sentimos, no hay un viaje existente con tales aeropuertos en el rango de fechas establecidas, inténtalo de nuevo!")
                        elif opcion==2:
                            cont=1
                            for i in ListaAeropuertos:
                                print(cont,end="- ")
                                print (i.get__nombre())
                                cont+=1
                            num1=int(input("\nSeleccione el Aeorpuerto de origen: "))
                            num2=int(input("Seleccione el Aeorpuerto de destino: "))
                            AeroOrigen=ListaAeropuertos[num1-1].get__nombre()
                            AeroDestino=ListaAeropuertos[num2-1].get__nombre()
                            FechaSalida=input ("Ingrese la inicial (dd/mm/yy): ")
                            FechaLlegada=input ("Ingrese la fecha final (dd/mm/yy): ")
                            viajes1=CreaEscalas (AeroOrigen, AeroDestino, FechaSalida, FechaLlegada)
                            if MostrarEscalas(viajes1)==True:
                                v=int(input("Seleccione el número de viaje de ida: "))
                                SeleccionarViaje(IDPasajero,viajes1,v)
                                viajes2=CreaEscalas (AeroDestino, AeroOrigen, FechaSalida, FechaLlegada)
                                if MostrarEscalas(viajes2)==True: #shows the possible return flights in the time frame that was entered
                                    v2=int(input("Seleccione el número de viaje de venida: "))
                                    SeleccionarViaje(IDPasajero,viajes2,v2) 
                                else:
                                    print ("Lo sentimos, no hay un viaje existente con tales aeropuertos en el rango de fechas establecidas, inténtalo de nuevo!")
                            else:
                                print ("Lo sentimos, no hay un viaje existente con tales aeropuertos en el rango de fechas establecidas, inténtalo de nuevo!")
                        elif opcion == 3:
                                MuestraVuelosPrecio() #shows the flights of the minor at the highest price
                        elif opcion==4:
                            MuestraVuelosFecha() #shows the minor's flights for the longest duration
                    elif comando == 2:
                        print ("\t\tBúsqueda de vuelos inteligente")
                        print ("1-Mostrar 5 viajes más rápidos")
                        print ("2-Ver 5 viajes más baratos en el rango de fecas indicado")
                        print ("3-ver una matriz con toda la oferta de precios que existen para su viaje")
                        opcion=int(input("Ingrese la opción que desea  realizar: "))
                        if opcion==1:
                            cont=1
                            for i in ListaAeropuertos:
                                print(cont,end="- ")
                                print (i.get__nombre())
                                cont+=1
                            num1=int(input("\nSeleccione el Aeorpuerto de origen: "))
                            num2=int(input("Seleccione el Aeorpuerto de destino: "))
                            AeroOrigen=ListaAeropuertos[num1-1].get__nombre()
                            AeroDestino=ListaAeropuertos[num2-1].get__nombre()
                            FechaSalida=input("Ingrese la fecha de salida (dd/mm/yy): ")
                            FechaLlegada=input("Ingrese la fecha de llegada (dd/mm/yy): ")
                            RangoFechas=int(input("Ingrese el rango de días en los que desea viajar (un solo número): "))
                            BusquedaInteligenteTiempo(AeroOrigen,AeroDestino,FechaSalida,FechaLlegada)
                        elif opcion==2:
                            cont=1
                            for i in ListaAeropuertos:
                                print(cont,end="- ")
                                print (i.get__nombre())
                                cont+=1
                            num1=int(input("\nSeleccione el Aeorpuerto de origen: "))
                            num2=int(input("Seleccione el Aeorpuerto de destino: "))
                            AeroOrigen=ListaAeropuertos[num1-1].get__nombre()
                            AeroDestino=ListaAeropuertos[num2-1].get__nombre()
                            FechaSalida=input("Ingrese la fecha inicial: ")
                            FechaLlegada=input("Ingrese la fecha final: ")
                            RangoFechas=int(input("Ingrese el rango de días en los que desea viajar (un solo número): "))
                            BusquedaInteligentePrecio (AeroOrigen,AeroDestino,FechaSalida,FechaLlegada)
                        elif opcion==3:
                            cont=1
                            for i in ListaAeropuertos:
                                print(cont,end="- ")
                                print (i.get__nombre())
                                cont+=1
                            num1=int(input("\nSeleccione el Aeorpuerto de origen: "))
                            num2=int(input("Seleccione el Aeorpuerto de destino: "))
                            AeroOrigen=ListaAeropuertos[num1-1].get__nombre()
                            AeroDestino=ListaAeropuertos[num2-1].get__nombre()
                            FechaSalida=input("Ingrese la fecha inicial: ")
                            FechaLlegada=input("Ingrese la fecha final: ")
                            RangoFechas=int(input("Ingrese el rango de días en los que desea viajar (un solo número): "))
                            MuestraMatriz(AeroOrigen, AeroDestino, FechaSalida, FechaLlegada)
                    elif comando==3:
                        print ("\n\t\tMi perfil")
                        print ("1-Ver mi historial de viajes")
                        print ("2-Ver mi información personal")
                        print ("3-Modificar mi información")
                        opcion=int(input("Ingrese la opción que desea  realizar: "))
                        if opcion==1:
                            IDPasajero=objeto.get__ID()
                            MostrarHistorialPasajero(IDPasajero)
                        elif opcion==2:
                            MostrarInformacionPasajero(IDPasajero)
                        elif opcion==3:
                            ModificaPasajeros(IDPasajero)
                    elif comando==4:
                        RecorrerArchiVuelo ()
                        #RecorrerArchiHistorial()
                        print ("El archivo de vuelos ha sido refrescado")
                    elif comando==5:
                        valor=False
                        print("Sesión cerrada")
                #except:
                    #print ("Error en datos")

#primero se creará lo que el programa traerá por defecto

CreaUsuarios ()
CreaAeropuertoArchi ()
CreaPistasArchi ()
CreaPuertasArchi ()
CreaAerolineasArchi ()
CreaAvionesArchi ()
CreaTripulacionArchi ()
CreaVuelosArchi()

Menu () #finally the interactive part is done














