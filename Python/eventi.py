# import pygame, os, sys
import main
import global_var as GLOB

def testa():

# ---- GESTIONE EVENTI ----

    # if main.player.evento == "porta" or main.player.evento == "porta-1" or main.player.evento == "porta-2" or main.player.evento == "porta-3":
    #     print(GLOB.Default_Map, GLOB.Stanza)
    #     main.animazione.iFinished = False

    if main.player.evento == "enigma":
        GLOB.Enigma = True
    else:
        GLOB.Enigma = False


    if main.player.evento == "porta-0":
        main.player.evento = None
        main.stanze.setToDefault()

        if GLOB.Piano == "1-PianoTerra":
        
            if GLOB.Stanza == "Corridoio":
                main.stanze.flag_Fisica = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

            if GLOB.Stanza == "Fisica":
                main.stanze.flag_Corridoio = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

        print(GLOB.Default_Map, GLOB.Stanza)
        main.animazione.iFinished = False
    
    if main.player.evento == "porta-2":
        main.player.evento = None
        main.stanze.setToDefault()


        if GLOB.Piano == "1-PianoTerra":
        
            if GLOB.Stanza == "Corridoio":
                main.stanze.flag_Chimica = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

            if GLOB.Stanza == "Chimica":
                main.stanze.flag_Corridoio = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

        print(GLOB.Default_Map, GLOB.Stanza)
        main.animazione.iFinished = False