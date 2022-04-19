import pygame, os, sys
import global_var as GLOB
import main

percorso = "../MappaGioco/Tileset/Stanze/"

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
#    print(GLOB.Default_Map)


def caricaStanza():
    posX = main.player.getPositionX()-main.cam.getPositionX()
    posY = main.player.getPositionY()-main.cam.getPositionY()
    if not main.animazione.iFinished:
        main.collisions.load_map(GLOB.Default_Map)
        main.collisions.load_objects(GLOB.Default_object)
        #print(660 * GLOB.MULT, 210 * GLOB.MULT)

    if (posX >= 0 and posY >= 0):
        Chimica()
        #print("Sono Uscito")