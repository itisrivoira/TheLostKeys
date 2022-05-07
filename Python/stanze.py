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
    global flag_Classe1A, flag_AulaMagna
    flag_Chimica = False
    flag_Fisica = False
    flag_Archivio = False
    flag_Classe1A = False
    flag_AulaMagna = False
    flag_Corridoio = False
    flag_Corridoio1 = False
    flag_Corridoio2 = False

def Chimica():
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Chimica"
    main.load_collisions("ProvaChimica_CollisioniStefano.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaChimica.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaChimicaOggetti.png"
    
    # PORTA ORIGINE STANZA
    setPosition((270, 114), (-372, -96))


def Fisica():
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Fisica"
    main.load_collisions("ProvaFisica_CollisioniStefano.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaFisica.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaFisicaOggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((228, 122), (-372, -110))


def Archivio():
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Archivio"
    main.load_collisions("ProvaArchivio_CollisioniStefano.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaArchivio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaArchivioOggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((264, 120), (-160, -118))


def Classe1A():
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "1A"
    main.load_collisions("Classe1A_CollisioniStefano.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Classe1A.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Classe1AOggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((272, 120), (-314, -118))


def AulaMagna():
    global pos_portaP, pos_portaC

    # PIANO - STANZA - COLLISIONI
    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "AulaMagna"
    main.load_collisions("ProvaAulaMagna_CollsioniStefano.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaMagna.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/AulaMagnaOggetti.png"

    # PORTA ORIGINE STANZA
    setPosition((238, 118), (-372, -142))

def Corridoio():

        # PORTA ORIGINE STANZA

    if GLOB.Stanza == "Chimica":
        # Chimica
        setPosition((270, 74), (-244, 56))

    elif GLOB.Stanza == "Fisica":
        # Fisica
        setPosition((200, 74), (0, 54))

    elif GLOB.Stanza == "Archivio":
        # Fisica
        setPosition((152, 108), (146, -58))


    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Corridoio"
    main.load_collisions("Corridoio_Collisioni.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Corridoio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/CorridoioOggetti.png"

def Corridoio1():

        # PORTA ORIGINE STANZA

    if GLOB.Stanza == "AulaMagna":
        # Chimica
        setPosition((250, 116), (-262, -144))

    elif GLOB.Stanza == "AulaProfessori":
        # Fisica
        setPosition((200, 74), (0, 54))

    elif GLOB.Stanza == "LabInfo":
        # Fisica
        setPosition((152, 108), (146, -58))

    elif GLOB.Stanza == "1A":
        # Fisica
        setPosition((160, 112), (-208, -148))


    GLOB.Piano = "2-PrimoPiano"
    GLOB.Stanza = "Corridoio"
    main.load_collisions("CorridoioPrimoPiano_Collisioni.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/CorridoioPrimoPiano.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/CorridoioPrimoPianoOggetti.png"

def Corridoio2():
    pass

inizializza()
def caricaStanza():
    global flag_Chimica, flag_Fisica, flag_Archivio, flag_Corridoio, flag_Corridoio1, flag_Corridoio2
    # posX = main.player.getPositionX()-main.cam.getPositionX()
    # posY = main.player.getPositionY()-main.cam.getPositionY()

    if not main.animazione.iFinished:
        main.collisions.load_map(GLOB.Default_Map)

        if GLOB.Default_object != None:
            main.collisions.load_objects(GLOB.Default_object)
        #print(660 * GLOB.MULT, 210 * GLOB.MULT)


    #print("Chimica: %s | Fisica: %s | Archivio: %s | Corridoio: %s" % (flag_Chimica, flag_Fisica, flag_Archivio, flag_Corridoio))

    if GLOB.Piano == "1-PianoTerra":

        if flag_Corridoio1:
            Corridoio1()

        if flag_Corridoio:
            Corridoio()

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

        if flag_Classe1A:
            Classe1A()

        if flag_AulaMagna:
            AulaMagna()


    if GLOB.Piano == "3-SecondoPiano":
        
        if flag_Corridoio2:
            Corridoio2()
        #print("Sono Uscito")