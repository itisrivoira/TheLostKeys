import pygame, os, sys
import global_var as GLOB
import main

percorso = "../MappaGioco/Tileset/Stanze/"

def inizializza():
    global flag_Chimica, flag_Fisica, flag_Archivio, flag_Corridoio, pos_portaP, pos_portaC
    flag_Chimica = True
    flag_Fisica = False
    flag_Archivio = False
    flag_Corridoio = False
    pos_portaP = (660, 210)
    pos_portaC = (660, 210)

def setToDefault():
    global flag_Chimica, flag_Fisica, flag_Archivio, flag_Corridoio
    flag_Chimica = False
    flag_Fisica = False
    flag_Archivio = False
    flag_Corridoio = False

def Chimica():
    global pos_portaP, pos_portaC
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Chimica"
    main.load_collisions("ProvaChimica_CollisioniStefano.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaChimica.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaChimicaOggetti.png"
    pos_portaP = (224, 122)
    pos_portaC = (-372, -111)
    # pos_portaP = (270, 114)
    # pos_portaC = (-372, -96)


def Fisica():
    global pos_portaP, pos_portaC
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Fisica"
    main.load_collisions("ProvaFisica_CollisioniStefano.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaFisica.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaFisicaOggetti.png"
    pos_portaP = (270, 114)
    pos_portaC = (-372, -96)
    # pos_portaP = (228, 122)
    # pos_portaC = (-372, -111)
#    print(GLOB.Default_Map)


def Archivio():
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Archivio"
    main.load_collisions("ProvaArchivio._CollisioniStefano.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaArchivio.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaArchivioOggetti.png"

def Corridoio():
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Corridoio"
    main.load_collisions("Corridoio_Collisioni.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/Corridoio.png"
    GLOB.Default_object = None
#    print(GLOB.Default_Map)

inizializza()
def caricaStanza():
    global flag_Chimica, flag_Fisica, flag_Archivio, flag_Corridoio
    posX = main.player.getPositionX()-main.cam.getPositionX()
    posY = main.player.getPositionY()-main.cam.getPositionY()
    if not main.animazione.iFinished:
        main.collisions.load_map(GLOB.Default_Map)
        main.collisions.load_objects(GLOB.Default_object)
        #print(660 * GLOB.MULT, 210 * GLOB.MULT)


    #print("Chimica: %s | Fisica: %s | Archivio: %s | Corridoio: %s" % (flag_Chimica, flag_Fisica, flag_Archivio, flag_Corridoio))

    if flag_Chimica:
        Chimica()
    
    if flag_Fisica:
        Fisica()
    
    if flag_Archivio:
        Archivio()
    
    if flag_Corridoio:
        Corridoio()
        #print("Sono Uscito")