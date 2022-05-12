import pygame, os, sys
import global_var as GLOB
import main

percorso = "../MappaGioco/Tileset/Stanze/"

def setPosition(posP, posC):
    global pos_portaP, pos_portaC
    pos_portaP = posP
    pos_portaC = posC

def inizializza():
    global flag_Corridoio

    setToDefault()
    flag_Corridoio = True


    setPosition((152, 122), (130, -118))

def setToDefault():
    global  flag_Corridoio, flag_Corridoio1, flag_Corridoio2
    global flag_Chimica, flag_Fisica, flag_Archivio
    global flag_Classe1A, flag_AulaMagna, flag_AulaProfessori, flag_LabInfo, flag_WCfemmine, flag_WCmaschi
    global flag_Classe4A, flag_LabInformatica, flag_Ripostiglio
    flag_Chimica = False
    flag_Fisica = False
    flag_Archivio = False
    flag_Classe1A = False
    flag_AulaMagna = False
    flag_AulaProfessori = False
    flag_LabInfo = False
    flag_WCfemmine = False
    flag_WCmaschi = False
    flag_Classe4A = False
    flag_LabInformatica = False
    flag_Ripostiglio = False
    flag_Corridoio = False
    flag_Corridoio1 = False
    flag_Corridoio2 = False

def Chimica():
    global flag_Chimica
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Chimica"
    GLOB.Default_collisions = "ProvaChimica_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaChimica.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaChimicaOggetti.png"
    
    # PORTA ORIGINE STANZA
    setPosition((270, 114), (-372, -96))

    flag_Chimica = False


def Fisica():
    global flag_Fisica
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Fisica"
    GLOB.Default_collisions = "ProvaFisica_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaFisica.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaFisicaOggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((228, 122), (-372, -110))

    flag_Fisica = False


def Archivio():
    global flag_Archivio
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Archivio"
    GLOB.Default_collisions = "ProvaArchivio_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaArchivio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaArchivioOggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((264, 120), (-160, -118))

    flag_Archivio = False


def Classe1A():
    global flag_Classe1A
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "1A"
    GLOB.Default_collisions = "Classe1A_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Classe1A.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Classe1AOggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((272, 120), (-314, -118))

    flag_Classe1A = False


def AulaMagna():
    global flag_AulaMagna
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "AulaMagna"
    GLOB.Default_collisions = "ProvaAulaMagna_CollsioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaMagna.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaMagnaOggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((238, 118), (-372, -142))

    flag_AulaMagna = False

def AulaProfessori():
    global flag_AulaProfessori
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "AulaProfessori"
    GLOB.Default_collisions = "AulaProfessori.room.gmx_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaProfessori.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaProfessoriOggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((274, 100), (-386, -63))

    flag_AulaProfessori = False
    

def LabInfo():
    global flag_LabInfo
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "LabInfo"
    GLOB.Default_collisions = "ProvaLabInfo_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/LabInfo.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/LabInfoOggetto.png"

    # PORTA ORIGINE STANZA
    setPosition((270, 104), (-290, -62))

    flag_LabInfo = False

def WCfemmine():
    global flag_WCfemmine
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "WC-Femmine"
    GLOB.Default_collisions = "WCfemmine_CollisioniPY.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/WCfemmine.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/WCfemmineOggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((214, 70), (-146, -22))

    flag_WCfemmine = False


def WCmaschi():
    global flag_WCmaschi
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "WC-Maschi"
    GLOB.Default_collisions = "ProvaBagniMaschili_CollisioniStefano.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/BagniMaschili.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/BagniMaschiliOggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((272, 120), (-264, -120))

    flag_WCmaschi = False

def Classe4A():
    global flag_Classe4A
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "3-SecondoPiano"
    GLOB.Stanza = "4A"
    GLOB.Default_collisions = "4A_Collisioni_Python.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/4A.png"
    # GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/WCfemmineOggetti.png"
    GLOB.Default_object = None

    # PORTA ORIGINE STANZA
    setPosition((268, 69), (-318, 30))

    flag_Classe4A = False

def LabInformatica():
    global flag_LabInformatica
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "3-SecondoPiano"
    GLOB.Stanza = "LabInformatica"
    GLOB.Default_collisions = "LabInfo2_CollisioniPY.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/LabInfo2.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/LabInfo2Oggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((154, 120), (-264, -114))

    flag_LabInformatica = False


def Ripostiglio():
    global flag_Ripostiglio
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "3-SecondoPiano"
    GLOB.Stanza = "Ripostiglio"
    GLOB.Default_collisions = "ripostiglio_CollisioniPY.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ripostiglio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ripostiglioOggetto.png"

    # PORTA ORIGINE STANZA
    setPosition((272, 118), (-100, -72))

    flag_Ripostiglio = False

def Corridoio():
    global flag_Corridoio

    # PORTA ORIGINE STANZA - CORRIDOIO

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

    flag_Corridoio = False


def Corridoio1():
    global flag_Corridoio1

    # PORTA ORIGINE STANZA - CORRIDOIO

    if GLOB.Stanza == "AulaMagna":
        setPosition((250, 116), (-262, -144))

    elif GLOB.Stanza == "AulaProfessori":
        setPosition((268, 96), (-386, -114))

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

    flag_Corridoio1 = False

def Corridoio2():
    global flag_Corridoio2

    # PORTA ORIGINE STANZA - CORRIDOIO

    if GLOB.Stanza == "4A":
        setPosition((162, 110), (-114, -148))

    if GLOB.Stanza == "LabInformatica":
        setPosition((162, 110), (-16, -148))

    if GLOB.Stanza == "Ripostiglio":
        setPosition((152,72), (72, 6))

    GLOB.Piano = "3-SecondoPiano"
    GLOB.Stanza = "Corridoio"
    GLOB.Default_collisions = "SecondoPiano_Collisioni.csv"
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Corridoio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/CorridoioOggetti.png"

    flag_Corridoio2 = False

inizializza()
def caricaStanza():
    global flag_Chimica, flag_Fisica, flag_Archivio, flag_Corridoio, flag_Corridoio1, flag_Corridoio2
    # posX = main.player.getPositionX()-main.cam.getPositionX()
    # posY = main.player.getPositionY()-main.cam.getPositionY()

    if not main.animazione.iFinished:
        main.collisions.load_map(GLOB.Default_Map)
        GLOB.LoadCollisions = True
        

        if GLOB.Default_object != None:
            main.collisions.load_objects(GLOB.Default_object)

    if GLOB.Default_collisions != None:
        main.load_collisions(GLOB.Default_collisions)

        #print(660 * GLOB.MULT, 210 * GLOB.MULT)


    #print("Chimica: %s | Fisica: %s | Archivio: %s | Corridoio: %s" % (flag_Chimica, flag_Fisica, flag_Archivio, flag_Corridoio))

    if GLOB.Piano == "1-PianoTerra":

        if flag_Corridoio1:
            Corridoio1()

        if flag_Corridoio:
            Corridoio()

        if flag_Corridoio2:
            Corridoio2()

        if flag_Chimica:
            Chimica()
        
        if flag_Fisica:
            Fisica()
        
        if flag_Archivio:
            Archivio()
        #print("Sono Uscito")

    if GLOB.Piano == "2-PrimoPiano":
    
        if flag_Corridoio1:
            Corridoio1()

        if flag_Corridoio:
            Corridoio()

        if flag_Corridoio2:
            Corridoio2()

        if flag_Classe1A:
            Classe1A()

        if flag_AulaMagna:
            AulaMagna()

        if flag_AulaProfessori:
            AulaProfessori()

        if flag_LabInfo:
            LabInfo()

        if flag_WCfemmine:
            WCfemmine()

        if flag_WCmaschi:
            WCmaschi()


    if GLOB.Piano == "3-SecondoPiano":

        if flag_Corridoio1:
            Corridoio1()
        
        if flag_Corridoio2:
            Corridoio2()

        if flag_Classe4A:
            Classe4A()

        if flag_LabInformatica:
            LabInformatica()

        if flag_Ripostiglio:
            Ripostiglio()
        #print("Sono Uscito")