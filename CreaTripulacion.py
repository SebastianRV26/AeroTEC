ListaTripulacion=[]
class Tripulacion (): #An object is created for the crew, which will contain attributes such as an identification, the name of the crew, the date of birth, the airline to which it belongs, its role and the state
    def __init__(self):
        self.ID=""
        self.NombreTripulante=""
        self.FechaNacimiento=""
        self.AerolineaPatrona=""
        self.RolDelTripulante="" #pilot or customer service
        self.Estado="" #available, not available
        self.contador=0
    def set__info (self,ES,ID,NT,FN,AP,AT):
        self.Estado=ES
        self.ID=ID
        self.NombreTripulante=NT
        self.FechaNacimiento=FN
        self.AerolineaPatrona=AP
        self.RolDelTripulante=AT
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
def CreaArchivo():
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
        t.set__info(tripu[0], tripu[1], tripu[2], tripu[3], tripu[4], tripu[5])
        ListaTripulacion.append (t)   
    archi.close()

CreaArchivo()
CreaTripulacion (107890345, "Juan", "11/01/1991", "Volaris", "piloto", "disponible") #ID, name, birth, airline, role and status
CreaTripulacion (305470839, "Javier","28/06/1985", "Volaris", "piloto", "disponible")
CreaTripulacion (607770357, "Brayan","09/12/1994", "Volaris", "piloto", "disponible")
CreaTripulacion (502810273, "Felipe","04/10/1980", "Volaris", "piloto", "disponible")
CreaTripulacion (401920482, "Jeremy","27/11/1986", "Volaris", "piloto", "disponible")
CreaTripulacion (401390926, "Sandra","16/09/1990", "Volaris", "piloto", "disponible")
CreaTripulacion (107290928, "Juana","12/03/1991", "Volaris", "servicio al cliente", "disponible")
CreaTripulacion (702670282, "Adriana","10/07/1983", "Volaris", "servicio al cliente", "disponible")
CreaTripulacion (209170273, "Santiago","25/02/1993", "Volaris", "servicio al cliente", "disponible")
CreaTripulacion (202460802, "María","23/04/1987", "Volaris", "servicio al cliente", "disponible")
CreaTripulacion (904530631, "Emilia","20/07/1991", "Volaris", "servicio al cliente", "disponible")
CreaTripulacion (702890529, "Jose","03/11/1994", "Volaris", "servicio al cliente", "disponible")
CreaTripulacion (803940637, "Oscar","10/04/1999", "Volaris", "servicio al cliente", "disponible")
CreaTripulacion (906270819, "Michael","24/05/1986", "Volaris", "servicio al cliente", "disponible")
CreaTripulacion (500270631, "Tatiana","03/11/1994", "Volaris", "servicio al cliente", "disponible")
CreaTripulacion (301350791, "Pablo", "02/03/1990","Avianca", "piloto", "disponible")
CreaTripulacion (508630247, "Fernanda", "10/09/1985", "Avianca", "piloto", "disponible")
CreaTripulacion (206930139, "Bleer", "11/06/1988", "Avianca", "piloto", "disponible")
CreaTripulacion (308200368, "Lauren", "17/08/1989", "Avianca", "piloto", "disponible")
CreaTripulacion (607030372, "Yerlin", "15/10/1987", "Avianca", "piloto", "disponible")
CreaTripulacion (403215037, "Mariana", "24/03/1983", "Avianca", "piloto", "disponible")
CreaTripulacion (401230456, "Luis", "27/09/1993","Avianca", "servicio al cliente", "disponible")
CreaTripulacion (908630382, "Fernando", "11/01/1989", "Avianca", "servicio al cliente", "disponible")
CreaTripulacion (508630489, "Angela", "27/03/1996", "Avianca", "servicio al cliente", "disponible")
CreaTripulacion (602430977, "Yuri", "28/08/1979", "Avianca", "servicio al cliente", "disponible")
CreaTripulacion (500270632, "Jennifer","03/11/1994", "Avianca", "servicio al cliente", "disponible")
CreaTripulacion (702890173, "Jairo","19/07/1980", "Avianca", "servicio al cliente", "disponible")
CreaTripulacion (235820132, "Wagner","30/01/1985", "Avianca", "servicio al cliente", "disponible")
CreaTripulacion (258723059, "Andrey","12/10/1994", "Avianca", "servicio al cliente", "disponible")
CreaTripulacion (693906094, "Nelson","03/01/1987", "Avianca", "servicio al cliente", "disponible")
CreaTripulacion (509750541, "Juli", "30/11/1995", "Interjet", "piloto", "disponible")
CreaTripulacion (802461018, "Daniela", "18/05/1993", "Interjet", "piloto", "disponible")
CreaTripulacion (409270133, "Diego", "02/06/1990", "Interjet", "piloto", "disponible")
CreaTripulacion (502840173, "Daniel", "03/09/1996", "Interjet", "piloto", "disponible")
CreaTripulacion (324097342, "Jimena", "18/09/1983", "Interjet", "piloto", "disponible")
CreaTripulacion (983250913, "Gilberto", "09/09/1983", "Interjet", "piloto", "disponible")
CreaTripulacion (603210876, "Nick", "20/07/1989", "Interjet", "servicio al cliente", "disponible")
CreaTripulacion (306940729, "Juan", "31/09/1990", "Interjet", "servicio al cliente", "disponible")
CreaTripulacion (901530642, "Freddy", "19/12/1982", "Interjet", "servicio al cliente", "disponible")
CreaTripulacion (403820384, "Jhonny", "10/03/1984", "Interjet", "servicio al cliente", "disponible")
CreaTripulacion (709280192, "Mónica", "05/10/1995", "Interjet", "servicio al cliente", "disponible")
CreaTripulacion (105730253, "Andrea", "23/09/1999", "Interjet", "servicio al cliente", "disponible")
CreaTripulacion (489217132, "Adriana", "27/11/1985", "Interjet", "servicio al cliente", "disponible")
CreaTripulacion (894377275, "Raquel", "18/01/1994", "Interjet", "servicio al cliente", "disponible")
CreaTripulacion (739208759, "Agustín", "02/07/1987", "Interjet", "servicio al cliente", "disponible")
CreaTripulacion (602630725, "Jose", "02/06/1990", "Wingo", "piloto", "disponible")
CreaTripulacion (207530124, "María", "17/02/1987", "Wingo", "piloto", "disponible")
CreaTripulacion (109480073, "Mauricio", "25/08/1984", "Wingo", "piloto", "disponible")
CreaTripulacion (203910258, "Jeannette", "18/05/1981", "Wingo", "piloto", "disponible")
CreaTripulacion (987543729, "Allan", "02/07/1989", "Wingo", "piloto", "disponible")
CreaTripulacion (109844387, "Lorena", "19/01/1985", "Wingo", "piloto", "disponible")
CreaTripulacion (602810548, "Danny", "14/29/1993", "Wingo", "servicio al cliente", "disponible")
CreaTripulacion (502840282, "Adriana", "02/06/1990", "Wingo", "servicio al cliente", "disponible")
CreaTripulacion (701830278, "Isabel", "23/08/1982", "Wingo", "servicio al cliente", "disponible")
CreaTripulacion (321928390, "Hugo", "29/01/19980", "Wingo", "servicio al cliente", "disponible")
CreaTripulacion (427391732, "Nuria", "15/07/1979", "Wingo", "servicio al cliente", "disponible")
CreaTripulacion (828018392, "Manuel", "03/12/1994", "Wingo", "servicio al cliente", "disponible")
CreaTripulacion (468923104, "Dilan", "03/12/1994", "Wingo", "servicio al cliente", "disponible")
CreaTripulacion (109427853, "Sofía", "03/12/1994", "Wingo", "servicio al cliente", "disponible")
CreaTripulacion (902135032, "Alejandro", "03/12/1994", "Wingo", "servicio al cliente", "disponible")
CreaTripulacion (109480073, "Yosiney", "25/08/1984", "SANSA", "piloto", "disponible")
CreaTripulacion (325192802, "Olivier", "30/10/1987", "SANSA", "piloto", "disponible")
CreaTripulacion (712492021, "Elison", "29/02/1985", "SANSA", "piloto", "disponible")
CreaTripulacion (125309843, "Ian", "17/04/1980", "SANSA", "piloto", "disponible")
CreaTripulacion (382919874, "Enoc", "29/09/1982", "SANSA", "piloto", "disponible")
CreaTripulacion (274127372, "Leandro", "22/11/1991", "SANSA", "piloto", "disponible")
CreaTripulacion (418291829, "Alejandra", "04/11/1992", "SANSA", "servicio al cliente", "disponible")
CreaTripulacion (718290382, "Jordan", "23/07/1995", "SANSA", "servicio al cliente", "disponible")
CreaTripulacion (203810934, "Omar", "05/02/1993", "SANSA", "servicio al cliente", "disponible")
CreaTripulacion (518292712, "Jorge", "19/06/1995", "SANSA", "servicio al cliente", "disponible")
CreaTripulacion (801830822, "Anthony", "20/04/1992", "SANSA", "servicio al cliente", "disponible")
CreaTripulacion (602810479, "Andres", "13/10/1991", "SANSA", "servicio al cliente", "disponible")
CreaTripulacion (381794721, "Pedro", "12/03/1990", "SANSA", "servicio al cliente", "disponible")
CreaTripulacion (128471742, "Jose", "01/06/1982", "SANSA", "servicio al cliente", "disponible")
CreaTripulacion (612839683, "Carlos", "10/04/1992", "SANSA", "servicio al cliente", "disponible")

CreaTripulacion (201854145, "Francisco","22/03/1990","Aeroméxico","piloto","disponible")
CreaTripulacion (201880128, "Guadalupe","31/12/1992","Aeroméxico", "piloto","disponible")
CreaTripulacion (201894928, "Gustavo", "14/02/1973","Aeroméxico","piloto","disponible")
CreaTripulacion (201892023, "Juana", "27/10/1996","Aeroméxico","piloto","disponible")
CreaTripulacion (201810966, "Francisco", "09/07/1998","Aeroméxico","piloto","disponible")
CreaTripulacion (201826854, "Adriana", "09/01/1985","Aeroméxico","piloto","disponible")
CreaTripulacion (201821120, "Pedro", "27/10/1988","Aeroméxico", "servicio al cliente", "disponible")
CreaTripulacion (201836232, "Margarita", "30/1/1986","Aeroméxico","servicio al cliente", "disponible")
CreaTripulacion (201854268, "Alejandro", "06/11/1976","Aeroméxico","servicio al cliente", "disponible")
CreaTripulacion (201871122, "Maria del Carmen", "8/12/1987", "Aeroméxico","servicio al cliente", "disponible")
CreaTripulacion (201889243, "Roberto", "09/08/12/1996","Aeroméxico","servicio al cliente", "disponible")
CreaTripulacion (201821427, "Josefina", "23/06/1998", "Aeroméxico","servicio al cliente", "disponible")
CreaTripulacion (201867370, "Agustín", "11/05/1997", "Aeroméxico","servicio al cliente", "disponible")
CreaTripulacion (201848824, "Lucía", "20/04/1992", "Aeroméxico","servicio al cliente", "disponible")
CreaTripulacion (201891545, "Diego", "23/08/1981", "Aeroméxico","servicio al cliente", "disponible")
CreaTripulacion (503040186, "Adrien","22/10/1992","Air France","piloto","disponible")
CreaTripulacion (505820120, "Alizee","13/11/1981","Air France", "piloto","disponible")
CreaTripulacion (502410183, "Albert","16/03/1981","Air France", "piloto","disponible")
CreaTripulacion (504860161, "Annette", "06/01/1998","Air France","piloto","disponible")
CreaTripulacion (509280110, "Alexandre", "22/06/1976","Air France","piloto","disponible")
CreaTripulacion (507430138, "Sandrine", "18/10/1983","Air France","piloto","disponible")
CreaTripulacion (507310154, "Antoine", "18/10/1979","Air France", "servicio al cliente", "disponible")
CreaTripulacion (501770159, "Brigitte", "22/01/1990","Air France","servicio al cliente", "disponible")
CreaTripulacion (503220102, "Belmont", "30/08/1989","Air France","servicio al cliente", "disponible")
CreaTripulacion (506390144, "Camile", "28/01/1972", "Air France","servicio al cliente", "disponible")
CreaTripulacion (502660188, "Chandler", "18/02/1988","Air France","servicio al cliente", "disponible")
CreaTripulacion (501900118, "Eliette", "14/06/1985", "Air France","servicio al cliente", "disponible")
CreaTripulacion (502430133, "Alphonse", "27/04/1978", "Air France","servicio al cliente", "disponible")
CreaTripulacion (501100171, "Violette", "09/01/1972", "Air France","servicio al cliente", "disponible")
CreaTripulacion (509510131, "Christophe", "01/11/1974", "Air France","servicio al cliente", "disponible")
CreaTripulacion (711319277, "Sora","04/11/1978","Zennikku","piloto","disponible")
CreaTripulacion (715950777, "Saya","30/05/1984","Zennikku", "piloto","disponible")
CreaTripulacion (715070477, "Takeru","28/07/1985","Zennikku", "piloto","disponible")
CreaTripulacion (711943677, "Haruka", "14/5/1997","Zennikku","piloto","disponible")
CreaTripulacion (714684077, "Akemi", "28/09/1974","Zennikku","piloto","disponible")
CreaTripulacion (719046377, "Ayumi", "15/09/1996","Zennikku","piloto","disponible")
CreaTripulacion (714078877, "Tomoya", "29/04/1985","Zennikku", "servicio al cliente", "disponible")
CreaTripulacion (718265477, "Nagisa", "30/10/1980","Zennikku","servicio al cliente", "disponible")
CreaTripulacion (718327377, "Eiji", "13/12/1972","Zennikku","servicio al cliente", "disponible")
CreaTripulacion (714017677, "Natsuki", "01/08/1978", "Zennikku","servicio al cliente", "disponible")
CreaTripulacion (719238677, "Jiro", "15/03/1980","Zennikku","servicio al cliente", "disponible")
CreaTripulacion (717761377, "Akane", "16/01/1972", "Zennikku","servicio al cliente", "disponible")
CreaTripulacion (711716077, "Akiyama", "07/07/1994", "Zennikku","servicio al cliente", "disponible")
CreaTripulacion (715918477, "Chika", "31/01/1980", "Zennikku","servicio al cliente", "disponible")
CreaTripulacion (711342777, "Keiji", "24/02/1998", "Zennikku","servicio al cliente", "disponible")
CreaTripulacion (107970277, "Oscar","30/07/1976","Ticos Air","piloto","disponible")
CreaTripulacion (102280224, "Jimena","30/03/1983","Ticos Air", "piloto","disponible")
CreaTripulacion (109740293, "Sebastián","17/03/1993","Ticos Air", "piloto","disponible")
CreaTripulacion (107130257, "Sofía", "25/01/1980","Ticos Air","piloto","disponible")
CreaTripulacion (104340272, "Cleto", "15/05/1981","Ticos Air","piloto","disponible")
CreaTripulacion (105910159, "Mariángel", "16/06/1972","Ticos Air","piloto","disponible")
CreaTripulacion (109350271, "Ricardo", "02/12/1992","Ticos Air", "servicio al cliente", "disponible")
CreaTripulacion (109400289, "Valeria", "17/03/1976","Ticos Air","servicio al cliente", "disponible")
CreaTripulacion (105180214, "Rafael", "08/08/1992","Ticos Air","servicio al cliente", "disponible")
CreaTripulacion (101470213, "Mariana", "14/09/1986", "Ticos Air","servicio al cliente", "disponible")
CreaTripulacion (107980280, "Rodrigo", "11/09/1995","Ticos Air","servicio al cliente", "disponible")
CreaTripulacion (102280290, "Valentina", "28/04/1994", "Ticos Air","servicio al cliente", "disponible")
CreaTripulacion (106860256, "Santiago", "02/11/1986", "Ticos Air","servicio al cliente", "disponible")
CreaTripulacion (106120231, "María Paula", "19/02/1970", "Ticos Air","servicio al cliente", "disponible")
CreaTripulacion (102280244, "Gabriel", "21/02/1994", "Ticos Air","servicio al cliente", "disponible")
CreaTripulacion (272649968, "Jayden","02/04/1979","Silver Airways","piloto","disponible")
CreaTripulacion (271729911, "Emily","27/08/1980","Silver Airways", "piloto","disponible")
CreaTripulacion (277679914, "Simone","04/04/1987","Silver Airways", "piloto","disponible")
CreaTripulacion (277009986, "Janeth", "14/11/1991","Silver Airways","piloto","disponible")
CreaTripulacion (278459967, "Mylan", "12/01/1983","Silver Airways","piloto","disponible")
CreaTripulacion (271669958, "Astrid", "21/06/1992","Silver Airways","piloto","disponible")
CreaTripulacion (278759919, "Maverick", "25/01/1981","Silver Airways", "servicio al cliente", "disponible")
CreaTripulacion (278909993, "Nicki", "06/04/1973","Silver Airways","servicio al cliente", "disponible")
CreaTripulacion (273179977, "Pharell", "01/11/1973","Silver Airways","servicio al cliente", "disponible")
CreaTripulacion (277169978, "Raylee", "31/01/1981", "Silver Airways","servicio al cliente", "disponible")
CreaTripulacion (274359934, "Tiger", "06/10/1996","Silver Airways","servicio al cliente", "disponible")
CreaTripulacion (277919937, "Keira", "24/11/1991", "Silver Airways","servicio al cliente", "disponible")
CreaTripulacion (276899935, "Brooks", "23/02/1995", "Silver Airways","servicio al cliente", "disponible")
CreaTripulacion (272109994, "Astrid", "18/11/1998", "Silver Airways","servicio al cliente", "disponible")
CreaTripulacion (274169988, "Cain", "29/03/1982", "Silver Airways","servicio al cliente", "disponible")
CreaTripulacionArchi()








