# import pygame, os, sys
import main
import global_var as GLOB
from button import MiniMap

def testa():

# ---- GESTIONE EVENTI ----

    # if main.player.evento == "porta" or main.player.evento == "porta-1" or main.player.evento == "porta-2" or main.player.evento == "porta-3":
    #     print(GLOB.Default_Map, GLOB.Stanza)
    #     main.animazione.iFinished = False

    if main.player.evento == "enigma":
        condizione = False

        for value in GLOB.enigmi_da_risolvere:
    
            if value != GLOB.Stanza:

                GLOB.Enigma = False
                main.player.evento = None
            
            else:
                condizione = True
                

        if condizione:
            # print("Risolto: "+str(GLOB.enigmi_risolti))
            # print("Da risolvere: "+str(GLOB.enigmi_da_risolvere))
            GLOB.Enigma = True
        else:
            GLOB.Enigma = False

    if main.player.evento == "mappa":
        mappa = MiniMap()
        mappa.update()

    if main.player.evento == "piano-0":
        GLOB.Piano = "0-PianoSegreto"
        main.player.evento = None
        main.stanze.setToDefault()

    elif main.player.evento == "piano-1":
        GLOB.Piano = "1-PianoTerra"
        main.player.evento = None
        main.stanze.setToDefault()
        main.stanze.flag_Corridoio = True

        print(GLOB.Default_Map, GLOB.Stanza)
        print(main.stanze.flag_Corridoio, main.stanze.flag_Corridoio1)
        main.animazione.iFinished = False
        main.stanze.setPosition((192, 72), (146, 62))

    elif main.player.evento == "piano-2":
        last_floor = GLOB.Piano
        GLOB.Piano = "2-PrimoPiano"
        main.player.evento = None
        main.stanze.setToDefault()
        main.stanze.flag_Corridoio1 = True

        print(GLOB.Default_Map, GLOB.Stanza)
        main.animazione.iFinished = False
        print(last_floor)

        if last_floor == "1-PianoTerra":
            main.stanze.setPosition((274, 110), (-312, -148))
        elif last_floor == "3-SecondoPiano":
            main.stanze.setPosition((244, 110), (-312, -148))
        else:
            main.stanze.setPosition((260, 110), (-312, -148))

    elif main.player.evento == "piano-3":
        GLOB.Piano = "3-SecondoPiano"
        main.player.evento = None
        main.stanze.setToDefault()
        main.stanze.flag_Corridoio2 = True

        print(GLOB.Default_Map, GLOB.Stanza)
        main.animazione.iFinished = False
        main.stanze.setPosition((270, 110), (-326, -148))

    elif main.player.evento == "piano-4":
        GLOB.Piano = "4-Esterno"
        main.player.evento = None
        main.stanze.setToDefault()


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

    if main.player.evento == "porta-7":
        main.player.evento = None
        main.stanze.setToDefault()

        if GLOB.Piano == "2-PrimoPiano":
            
            if GLOB.Stanza == "Corridoio":
                main.stanze.flag_Classe1A = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

            if GLOB.Stanza == "1A":
                main.stanze.flag_Corridoio1 = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

        print(GLOB.Default_Map, GLOB.Stanza)
        main.animazione.iFinished = False

    if main.player.evento == "porta-8":
        main.player.evento = None
        main.stanze.setToDefault()


        if GLOB.Piano == "1-PianoTerra":
        
            if GLOB.Stanza == "Corridoio":
                main.stanze.flag_Archivio = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

            if GLOB.Stanza == "Archivio":
                main.stanze.flag_Corridoio = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)


        if GLOB.Piano == "2-PrimoPiano":
            
            if GLOB.Stanza == "Corridoio":
                main.stanze.flag_AulaMagna = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

            if GLOB.Stanza == "AulaMagna":
                main.stanze.flag_Corridoio1 = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

        

        print(GLOB.Default_Map, GLOB.Stanza)
        main.animazione.iFinished = False


    if main.player.evento == "porta-9":
        main.player.evento = None
        main.stanze.setToDefault()

        
        if GLOB.Piano == "3-SecondoPiano":
            
            if GLOB.Stanza == "Corridoio":
                main.stanze.flag_Classe4A = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

            if GLOB.Stanza == "4A":
                main.stanze.flag_Corridoio2 = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)
        

        print(GLOB.Default_Map, GLOB.Stanza)
        main.animazione.iFinished = False


    if main.player.evento == "porta-10":
        main.player.evento = None
        main.stanze.setToDefault()


        if GLOB.Piano == "2-PrimoPiano":
            
            if GLOB.Stanza == "Corridoio":
                main.stanze.flag_WCfemmine = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

            if GLOB.Stanza == "WC-Femmine":
                main.stanze.flag_Corridoio1 = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)        
        

        print(GLOB.Default_Map, GLOB.Stanza)
        main.animazione.iFinished = False

    if main.player.evento == "porta-11":
        main.player.evento = None
        main.stanze.setToDefault()


        if GLOB.Piano == "2-PrimoPiano":
            
            if GLOB.Stanza == "Corridoio":
                main.stanze.flag_AulaProfessori = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

            if GLOB.Stanza == "AulaProfessori":
                main.stanze.flag_Corridoio1 = True
                print(main.stanze.pos_portaP, main.stanze.pos_portaC)

        

        print(GLOB.Default_Map, GLOB.Stanza)
        main.animazione.iFinished = False