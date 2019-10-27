ListaUsuarios=[]
class Usuario: #An object is created for the users, it will contain the attributes such as name, ID, age, password, email and its type (administrator or guest)
    def __init__(self):
        self.NombreCompleto=""
        self.ID=0
        self.edad=0
        self.CorreoElectronico=""
        self.contraseña=""
        self.tipo=""
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
        print (self.nombre,self.ID, self.edad,self.CorreoElectronico,self.contraseña,self.tipo)
    def get__ID (self):
        return self.ID
    def get__contraseña(self):
        return self.contraseña
    def get__tipo(self):
        return self.tipo
    
def CreaArchivoUsuario():
    archi=open('Usuarios.txt','w') 
    archi.close()
def leertxt():
    #función que crea una lista de las lineas y la recorre
    archi=open('Usuarios.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        print (li )
    archi.close()

def CreaUsuario(nombre, ID, edad, correo, contra, tipo):
    archi=open('Usuarios.txt','a') #se abre el archivo en modo adjunción
    archi.write(str(nombre)+", "+str(ID)+", "+str(edad)+", "+str(correo)+", "+str(contra)+", "+str(tipo)+", ")
    archi.write('\n') #cuando cambia de elemento va a hacer la identacion
    archi.close()

def CreaUsuarios():
    archi=open('Usuarios.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        usuario=[]
        usuario=li.split(', ')
        u=Usuario()
        u.set__info(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5])
        ListaUsuarios.append (u)   
    archi.close()
def MuestraUsuarios():
    for i in ListaUsuarios:
        i.get__info()
CreaArchivoUsuario()
#CreaUsuarios()
CreaUsuario ("Vera Gamboa", 1, 30, "vgamboa@gmail.com","1", 1)
CreaUsuario ("Sebastián Rojas Vargas", 2, 17, "sebasrv26@gmail.com","2", 1) # name, ID, age, mail, password, type
CreaUsuario ("Cesar Enrique Acuña Perez", 111111111, 19, "cesar@gmail.com", "contraseña", 2)
CreaUsuario ("Juan", 3, 20, "juansoto@gmail.com", "3", 3)
CreaUsuario ("Kevin Quesada Mora", 208930391, 20, "kqm@gmail.com", "12345678", 3)
CreaUsuario ("Pablo", 301290412, 25, "pablitoclavounclavito@gmail.com", "12345678", 3)
CreaUsuario ("Daniel", 472987129, 22, "noobmaster69@gmail.com", "12345678", 3)
CreaUsuario ("Thor", 837953275, 48, "eldiosdeasgard@gmail.com", "12345678", 3)
CreaUsuario ("Tony", 982492841, 35, "yosoytonystark@gmail.com", "12345678", 3)
CreaUsuario ("Steve", 587975817, 50, "capitanamerica@gmail.com", "12345678", 3)
CreaUsuario ("Natasha", 463891634, 30, "laviudanegra@gmail.com", "12345678", 3)
CreaUsuario ("Sam", 728917354, 27, "falcon@gmail.com", "12345678", 3)
CreaUsuario ("Peter", 207420743, 15, "elhombrearaña@gmail.com", "12345678", 3)
CreaUsuario ("Goku", 831813728, 36, "holasoygoku@gmail.com", "12345678", 3)
CreaUsuario ("Naruto", 901219192, 30, "meencantaelramenichiraku@gmail.com", "12345678", 3)
CreaUsuario ("Rick", 641264328, 53, "rickdeluniversoe108@gmail.com", "12345678", 3)
CreaUsuario ("Morty", 461282912, 15, "megustanlasempanadas@gmail.com", "12345678", 3)
CreaUsuario ("Felipe", 7418348738, 18, "feli777@gmail.com", "12345678", 3)
CreaUsuario ("Santiago", 302710674, 25, "santyelcrack@gmail.com", "12345678", 3)
CreaUsuario ("German Garmendia", 437812746, 28, "holasoygerman@gmail.com", "12345678", 3)
CreaUsuario ("Rubén Doblas", 509340214, 28, "elrubiusomg@gmail.com", "12345678", 3)
CreaUsuario ("Raúl Álvarez", 317943193, 25, "auronplay@gmail.com", "12345678", 3)
CreaUsuario ("Luis Villar", 618356816, 27, "pablitoclavounclavito@gmail.com", "12345678", 3)
CreaUsuario ("Luis Flores", 872474892, 22, "elcanaldefernanfloo@gmail.com", "12345678", 3)
CreaUsuario ("Ángel David", 124374339, 25, "eldiariodedross@gmail.com", "12345678", 3)
CreaUsuario ("Roberto Darkar", 437753473, 25, "vetealaversh@gmail.com", "12345678", 3)
CreaUsuario ("Mauricio Montero", 873264872, 25, "elchunchemontero@gmail.com", "12345678", 3)
CreaUsuario ("Keylor Navas", 982665474, 25, "knavas13@gmail.com", "12345678", 3)
CreaUsuario ("Macho Gonzales", 458742389, 25, "asteniarapsodia@gmail.com", "12345678", 3)
CreaUsuarios()
