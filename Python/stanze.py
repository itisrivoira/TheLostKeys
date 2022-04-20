import pygame, os, sys
import global_var as GLOB
import main

percorso = "../MappaGioco/Tileset/Stanze/"

flag_Chimica = True
flag_Fisica = False
flag_Archivio = False
flag_Corridoio = False

def Chimica():
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Chimica"
    main.load_collisions("ProvaChimica_CollisioniStefano.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaChimica.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaChimicaOggetti.png"


def Fisica():
    GLOB.Piano = "1-PianoTerra"
    GLOB.Stanza = "Fisica"
    main.load_collisions("ProvaFisica_CollisioniStefano.csv")
    GLOB.Default_Map = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaFisica.png"
    GLOB.Default_object = percorso + GLOB.Piano +"/"+ GLOB.Stanza +"/png/ProvaFisicaOggetti.png"
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


def caricaStanza():
    global flag_Chimica, flag_Fisica, flag_Archivio, flag_Corridoio
    posX = main.player.getPositionX()-main.cam.getPositionX()
    posY = main.player.getPositionY()-main.cam.getPositionY()
    if not main.animazione.iFinished:
        main.collisions.load_map(GLOB.Default_Map)
        main.collisions.load_objects(GLOB.Default_object)
        #print(660 * GLOB.MULT, 210 * GLOB.MULT)

    if flag_Chimica:
        Chimica()
        flag_Fisica = False
        flag_Archivio = False
        flag_Corridoio = False
    elif flag_Fisica:
        Fisica()
        flag_Chimica = False
        flag_Archivio = False
        flag_Corridoio = False
    elif flag_Archivio:
        Archivio()
        flag_Fisica = False
        flag_Chimica = False
        flag_Corridoio = False
    elif flag_Corridoio:
        Corridoio()
        flag_Fisica = False
        flag_Archivio = False
        flag_Chimica = False
        #print("Sono Uscito")