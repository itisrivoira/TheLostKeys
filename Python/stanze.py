import global_var as GLOB
import main

percorso = "../MappaGioco/Tileset/Stanze/"

def setPosition(posP, posC):
    global pos_portaP, pos_portaC
    pos_portaP = posP
    pos_portaC = posC

def inizializza():
    global dizionario_flag

    setToDefault()
    dizionario_flag["Corridoio"] = True


    setPosition((152, 122), (130, -118))

def setToDefault():
    global dizionario_flag

    dizionario_flag = {
        
        "Chimica" : False,
        "Fisica" : False,
        "Archivio" : False,
        "Classe1A" : False,
        "AulaMagna" : False,
        "AulaProfessori" : False,
        "LabInfo" : False,
        "WCfemmine" : False,
        "WCmaschi" : False,
        "Classe4A" : False,
        "AulaVideo" : False,
        "LabInformatica" : False,
        "Ripostiglio" : False,
        "Corridoio" : False,
        "Corridoio1" : False,
        "Corridoio2" : False,
    
     }

def Chimica():
    global dizionario_flag

    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Chimica"
    GLOB.Default_collisions = "ProvaChimica_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaChimica.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaChimicaOggetti.png"
    
    setPosition((270, 114), (-372, -96))
    dizionario_flag["Chimica"] = False


def Fisica():
    global dizionario_flag

    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Fisica"
    GLOB.Default_collisions = "ProvaFisica_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaFisica.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaFisicaOggetti.png"

    setPosition((228, 122), (-372, -110))
    dizionario_flag["Fisica"] = False


def Archivio():
    global dizionario_flag

    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Archivio"
    GLOB.Default_collisions = "ProvaArchivio_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaArchivio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaArchivioOggetti.png"

    setPosition((264, 120), (-160, -118))
    dizionario_flag["Archivio"] = False


def Classe1A():
    global dizionario_flag

    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "1A"
    GLOB.Default_collisions = "Classe1A_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Classe1A.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Classe1AOggetti.png"

    setPosition((272, 120), (-314, -118))
    dizionario_flag["Classe1A"] = False


def AulaMagna():
    global dizionario_flag

    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "AulaMagna"
    GLOB.Default_collisions = "ProvaAulaMagna_CollsioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaMagna.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaMagnaOggetti.png"

    setPosition((238, 118), (-372, -142))
    dizionario_flag["AulaMagna"] = False

def AulaProfessori():
    global dizionario_flag

    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "AulaProfessori"
    GLOB.Default_collisions = "AulaProfessori.room.gmx_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaProfessori.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaProfessoriOggetti.png"

    setPosition((154, 100), (4, -62))
    dizionario_flag["AulaProfessori"] = False
    

def LabInfo():
    global dizionario_flag

    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "LabInfo"
    GLOB.Default_collisions = "ProvaLabInfo_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/LabInfo.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/LabInfoOggetto.png"

    setPosition((270, 104), (-290, -62))
    dizionario_flag["LabInfo"] = False

def WCfemmine():
    global dizionario_flag

    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "WC-Femmine"
    GLOB.Default_collisions = "WCfemmine_CollisioniPY.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/WCfemmine.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/WCfemmineOggetti.png"

    setPosition((214, 70), (-146, -22))
    dizionario_flag["WCfemmine"] = False


def WCmaschi():
    global dizionario_flag

    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "WC-Maschi"
    GLOB.Default_collisions = "ProvaBagniMaschili_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/BagniMaschili.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/BagniMaschiliOggetti.png"

    setPosition((272, 120), (-264, -120))
    dizionario_flag["WCmaschi"] = False

def Classe4A():
    global dizionario_flag

    GLOB.Piano = "3-SecondoPiano"
    GLOB.Stanza = "4A"
    GLOB.Default_collisions = "4A_Collisioni_Python.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/4A.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/4AOggetti.png"

    setPosition((268, 70), (-318, 30))
    dizionario_flag["Classe4A"] = False

def AulaVideo():
    global dizionario_flag

    GLOB.Piano = "3-SecondoPiano"
    GLOB.Stanza = "AulaVideo"
    GLOB.Default_collisions = "salavideo_Collisioni_Python.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaVideo.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaVideoOggetti.png"

    setPosition((156, 118), (50, -144))
    dizionario_flag["AulaVideo"] = False

def LabInformatica():
    global dizionario_flag

    GLOB.Piano = "3-SecondoPiano"
    GLOB.Stanza = "LabInformatica"
    GLOB.Default_collisions = "LabInfo2_CollisioniPY.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/LabInfo2.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/LabInfo2Oggetti.png"

    setPosition((154, 120), (-264, -114))
    dizionario_flag["LabInformatica"] = False


def Ripostiglio():
    global dizionario_flag

    GLOB.Piano = "3-SecondoPiano"
    GLOB.Stanza = "Ripostiglio"
    GLOB.Default_collisions = "ripostiglio_CollisioniPY.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ripostiglio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ripostiglioOggetto.png"

    setPosition((272, 118), (-100, -72))
    dizionario_flag["Ripostiglio"] = False

def Corridoio():
    global dizionario_flag

    if GLOB.Stanza == "Chimica":
        setPosition((270, 74), (-244, 56))

    elif GLOB.Stanza == "Fisica":
        setPosition((200, 74), (0, 54))

    elif GLOB.Stanza == "Archivio":
        setPosition((152, 108), (146, -58))

    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Corridoio"
    GLOB.Default_collisions = "Corridoio_Collisioni.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Corridoio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/CorridoioOggetti.png"

    dizionario_flag["Corridoio"] = False


def Corridoio1():
    global dizionario_flag

    if GLOB.Stanza == "AulaMagna":
        setPosition((250, 116), (-262, -144))

    elif GLOB.Stanza == "AulaProfessori":
        setPosition((274, 96), (-386, -70))

    elif GLOB.Stanza == "LabInfo":
        setPosition((152, 70), (144, -118))

    elif GLOB.Stanza == "1A":
        setPosition((160, 112), (-208, -148))

    elif GLOB.Stanza == "WC-Femmine": 
        setPosition((270, 110), (-388, -148))

    elif GLOB.Stanza == "WC-Maschi": 
        setPosition((152, 122), (120, -144))

    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "Corridoio"
    GLOB.Default_collisions = "CorridoioPrimoPiano_Collisioni.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Corridoio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/CorridoioOggetti.png"

    dizionario_flag["Corridoio1"] = False

def Corridoio2():
    global dizionario_flag

    if GLOB.Stanza == "4A":
        setPosition((162, 110), (-114, -148))

    elif GLOB.Stanza == "AulaVideo":
        setPosition((270, 94), (-386, -72))

    elif GLOB.Stanza == "LabInformatica":
        setPosition((162, 110), (-16, -148))

    elif GLOB.Stanza == "Ripostiglio":
        setPosition((152,72), (72, 6))

    GLOB.Piano = "3-SecondoPiano"
    GLOB.Stanza = "Corridoio"
    GLOB.Default_collisions = "SecondoPiano_Collisioni.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Corridoio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/CorridoioOggetti.png"

    dizionario_flag["Corridoio2"] = False

inizializza()

def caricaStanza():
    global dizionario_flag

    if not main.animazione.iFinished:
        main.collisions.load_map(GLOB.Default_Map)
        GLOB.LoadCollisions = True

        if GLOB.Default_object != None:
            main.collisions.load_objects(GLOB.Default_object)

    if GLOB.Default_collisions != None:
        main.load_collisions(GLOB.Default_collisions)


    if GLOB.Piano == "1-PianoTerra":

        if dizionario_flag["Corridoio1"]:
            Corridoio1()

        if dizionario_flag["Corridoio"]:
            Corridoio()

        if dizionario_flag["Corridoio2"]:
            Corridoio2()

        if dizionario_flag["Chimica"]:
            Chimica()
        
        if dizionario_flag["Fisica"]:
            Fisica()
        
        if dizionario_flag["Archivio"]:
            Archivio()

    elif GLOB.Piano == "2-PrimoPiano":
    
        if dizionario_flag["Corridoio1"]:
            Corridoio1()

        if dizionario_flag["Corridoio"]:
            Corridoio()

        if dizionario_flag["Corridoio2"]:
            Corridoio2()

        if dizionario_flag["Classe1A"]:
            Classe1A()

        if dizionario_flag["AulaMagna"]:
            AulaMagna()

        if dizionario_flag["AulaProfessori"]:
            AulaProfessori()

        if dizionario_flag["LabInfo"]:
            LabInfo()

        if dizionario_flag["WCfemmine"]:
            WCfemmine()

        if dizionario_flag["WCmaschi"]:
            WCmaschi()


    elif GLOB.Piano == "3-SecondoPiano":

        if dizionario_flag["Corridoio1"]:
            Corridoio1()
        
        if dizionario_flag["Corridoio2"]:
            Corridoio2()

        if dizionario_flag["Classe4A"]:
            Classe4A()

        if dizionario_flag["AulaVideo"]:
            AulaVideo()

        if dizionario_flag["LabInformatica"]:
            LabInformatica()

        if dizionario_flag["Ripostiglio"]:
            Ripostiglio()