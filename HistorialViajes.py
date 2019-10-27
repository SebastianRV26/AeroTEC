def CreaArchivoHistorial():
    archi=open('Historial.txt','w') 
    archi.close()

def CreaHistorial(IDPasajero, ObjetoViaje):
    archi=open('Historial.txt','a') #se abre el archivo en modo adjunción
    archi.write(str(ID)+", "+str(nombre)+", "+str(nacimiento)+", "+str(aerolinea)+", "+str(rol)+", "+str(estado)+", ")
    archi.write('\n') #cuando cambia de elemento va a hacer la identacion
    archi.close()

def CreaHistorialArchi():
    archi=open('Historial.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        tripu=[]
        tripu=li.split(', ')
        t=Tripulacion()
        t.set__info(tripu[0], tripu[1], tripu[2], tripu[3], tripu[4], tripu[5])
        ListaTripulacion.append (t)   
    archi.close()

CreaArchivoHistorial ()
