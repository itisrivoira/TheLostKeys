# import pygame, os, sys
import main
import global_var as GLOB

def testa():

# ---- GESTIONE EVENTI ----
    
    if main.player.evento == "porta":
        main.player.evento = None
        main.stanze.setToDefault()
        
        if GLOB.Stanza == "Corridoio":
            main.stanze.flag_Fisica = True
            print(main.stanze.pos_portaP, main.stanze.pos_portaC)

        if GLOB.Stanza == "Chimica":
            main.stanze.flag_Corridoio = True

            # USCITA STANZA
            main.stanze.setPosition((270, 74), (-244, 56))

            print(main.stanze.pos_portaP, main.stanze.pos_portaC)

        if GLOB.Stanza == "Fisica":
            main.stanze.flag_Corridoio = True
            print(main.stanze.pos_portaP, main.stanze.pos_portaC)

        if GLOB.Stanza == "Archivio":
            main.stanze.flag_Corridoio = True
            print(main.stanze.pos_portaP, main.stanze.pos_portaC)

        print(GLOB.Default_Map, GLOB.Stanza)

        main.animazione.iFinished = False