import main
import global_var as GLOB
from components import MiniMap

def testa():

# ---- GESTIONE EVENTI ----

    if main.player.evento == "enigma":
        condizione = False

        for value in GLOB.enigmi_da_risolvere:
    
            if value != GLOB.Stanza:

                GLOB.Enigma = False
                main.player.evento = None
            
            else:
                condizione = True
                

        if condizione:
            GLOB.Enigma = True
        else:
            GLOB.Enigma = False

    if main.player.evento == "mappa":
        mappa = MiniMap()
        mappa.update()
        main.player.setAllkeys(False)
        main.SetPlayer_speed()

    if main.player.evento == "piano-0":
        GLOB.Piano = "0-PianoSegreto"
        main.player.evento = None
        main.stanze.setToDefault()

    elif main.player.evento == "piano-1":
        GLOB.Piano = "1-PianoTerra"
        main.player.evento = None
        main.stanze.setToDefault()
        main.stanze.dizionario_flag["Corridoio"] = True

        main.animazione.iFinished = False
        main.stanze.setPosition((192, 72), (146, 62))

    elif main.player.evento == "piano-2":
        last_floor = GLOB.Piano
        GLOB.Piano = "2-PrimoPiano"
        main.player.evento = None
        main.stanze.setToDefault()
        main.stanze.dizionario_flag["Corridoio1"] = True

        main.animazione.iFinished = False

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
        main.stanze.dizionario_flag["Corridoio2"] = True

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
                main.stanze.dizionario_flag["Fisica"] = True

            if GLOB.Stanza == "Fisica":
                main.stanze.dizionario_flag["Corridoio"] = True

        elif GLOB.Piano == "2-PrimoPiano":
                    
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["LabInfo"] = True

            if GLOB.Stanza == "LabInfo":
                main.stanze.dizionario_flag["Corridoio1"] = True

        else:
            main.player.evento = "porta-99"
            return

        main.animazione.iFinished = False
    
    if main.player.evento == "porta-1":
        main.player.evento = None
        main.stanze.setToDefault()


        if GLOB.Piano == "2-PrimoPiano":
            
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["WCmaschi"] = True

            if GLOB.Stanza == "WC-Maschi":
                main.stanze.dizionario_flag["Corridoio1"] = True

        else:
            main.player.evento = "porta-99"
            return
        

        main.animazione.iFinished = False


    if main.player.evento == "porta-2":
        main.player.evento = None
        main.stanze.setToDefault()


        if GLOB.Piano == "1-PianoTerra":
        
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["Chimica"] = True

            if GLOB.Stanza == "Chimica":
                main.stanze.dizionario_flag["Corridoio"] = True

        else:
            main.player.evento = "porta-99"
            return

        main.animazione.iFinished = False

    if main.player.evento == "porta-3":
        main.player.evento = None
        main.stanze.setToDefault()

        main.player.evento = "porta-99"
        return        

        main.animazione.iFinished = False

    if main.player.evento == "porta-4":
        main.player.evento = None
        main.stanze.setToDefault()

        main.player.evento = "porta-99"
        return        

        main.animazione.iFinished = False

    if main.player.evento == "porta-5":
        main.player.evento = None
        main.stanze.setToDefault()

        main.player.evento = "porta-99"
        return        

        main.animazione.iFinished = False

    if main.player.evento == "porta-6":
        main.player.evento = None
        main.stanze.setToDefault()

        main.player.evento = "porta-99"
        return        

        main.animazione.iFinished = False

    if main.player.evento == "porta-7":
        main.player.evento = None
        main.stanze.setToDefault()

        if GLOB.Piano == "2-PrimoPiano":
            
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["Classe1A"] = True

            if GLOB.Stanza == "1A":
                main.stanze.dizionario_flag["Corridoio1"] = True

        elif GLOB.Piano == "3-SecondoPiano":
                    
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["AulaVideo"] = True

            if GLOB.Stanza == "AulaVideo":
                main.stanze.dizionario_flag["Corridoio2"] = True

        else:
            main.player.evento = "porta-99"
            return

        main.animazione.iFinished = False

    if main.player.evento == "porta-8":
        main.player.evento = None
        main.stanze.setToDefault()


        if GLOB.Piano == "1-PianoTerra":
        
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["Archivio"] = True

            if GLOB.Stanza == "Archivio":
                main.stanze.dizionario_flag["Corridoio"] = True


        elif GLOB.Piano == "2-PrimoPiano":
            
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["AulaMagna"] = True

            if GLOB.Stanza == "AulaMagna":
                main.stanze.dizionario_flag["Corridoio1"] = True

        else:
            main.player.evento = "porta-99"
            return

        

        main.animazione.iFinished = False


    if main.player.evento == "porta-9":
        main.player.evento = None
        main.stanze.setToDefault()

        
        if GLOB.Piano == "3-SecondoPiano":
            
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["Classe4A"] = True

            if GLOB.Stanza == "4A":
                main.stanze.dizionario_flag["Corridoio2"] = True

        else:
            main.player.evento = "porta-99"
            return
        

        main.animazione.iFinished = False


    if main.player.evento == "porta-10":
        main.player.evento = None
        main.stanze.setToDefault()


        if GLOB.Piano == "2-PrimoPiano":
            
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["WCfemmine"] = True

            if GLOB.Stanza == "WC-Femmine":
                main.stanze.dizionario_flag["Corridoio1"] = True


        else:
            main.player.evento = "porta-99"
            return  
        

        main.animazione.iFinished = False

    if main.player.evento == "porta-11":
        main.player.evento = None
        main.stanze.setToDefault()


        if GLOB.Piano == "2-PrimoPiano":
            
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["AulaProfessori"] = True

            if GLOB.Stanza == "AulaProfessori":
                main.stanze.dizionario_flag["Corridoio1"] = True


        elif GLOB.Piano == "3-SecondoPiano":
                
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["LabInformatica"] = True

            if GLOB.Stanza == "LabInformatica":
                main.stanze.dizionario_flag["Corridoio2"] = True

        else:
            main.player.evento = "porta-99"
            return

        main.animazione.iFinished = False


    if main.player.evento == "porta-12":
        main.player.evento = None
        main.stanze.setToDefault()


        if GLOB.Piano == "3-SecondoPiano":
                
            if GLOB.Stanza == "Corridoio":
                main.stanze.dizionario_flag["Ripostiglio"] = True

            if GLOB.Stanza == "Ripostiglio":
                main.stanze.dizionario_flag["Corridoio2"] = True

        else:
            main.player.evento = "porta-99"
            return

        main.animazione.iFinished = False

    if main.player.evento == "porta-13":
        main.player.evento = None
        main.stanze.setToDefault()

        main.player.evento = "porta-99"
        return

        main.animazione.iFinished = False


    if main.player.evento == "chiavetta-1":
        var = "Fisica"
        print(GLOB.chiavette[var][1])
        GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
        GLOB.inventario["chiavetta-1"] = (False, "Proprietario: Tommaso Dalbesio - Files: stringhe.c")
        print(GLOB.inventario)
        main.player.evento = None


    if main.player.evento == "chiavetta-2":
        var = "1A"
        print(GLOB.chiavette[var][1])
        GLOB.chiavette[var] = (GLOB.chiavette[var][1], False, GLOB.chiavette[var][2])
        GLOB.inventario["chiavetta-2"] = (False, "Proprietario: Stefano Senestro - Files: stringhe.c")
        print(GLOB.inventario)
        main.player.evento = None


    if main.player.evento == "chiavetta-3":
        var = "WC-Femmine"
        print(GLOB.chiavette[var][1])
        GLOB.chiavette[var] = (GLOB.chiavette[var][2], False, GLOB.chiavette[var][2])
        GLOB.inventario["chiavetta-3"] = (False, "Proprietario: Aleksandra Venezia - Files: stringhe.c")
        print(GLOB.inventario)
        main.player.evento = None


    if main.player.evento == "chiavetta-4":
        var = "AulaMagna"
        print(GLOB.chiavette[var][1])
        GLOB.chiavette[var] = (GLOB.chiavette[var][3], False, GLOB.chiavette[var][2])
        GLOB.inventario["chiavetta-4"] = (False, "Proprietario: Matteo Seimandi - Files: stringhe.c")
        print(GLOB.inventario)
        main.player.evento = None


    if main.player.evento == "chiavetta-5":
        var = "AulaProfessori"
        print(GLOB.chiavette[var][1])
        GLOB.chiavette[var] = (GLOB.chiavette[var][4], False, GLOB.chiavette[var][2])
        GLOB.inventario["chiavetta-5"] = (False, "Proprietario: Giuseppe Di Biase - Files: stringhe.c")
        print(GLOB.inventario)
        main.player.evento = None


    if main.player.evento == "chiavetta-6":
        var = "LabInfo"
        print(GLOB.chiavette[var][1])
        GLOB.chiavette[var] = (GLOB.chiavette[var][5], False, GLOB.chiavette[var][2])
        GLOB.inventario["chiavetta-6"] = (False, "Proprietario: Giulio Dajani - Files: stringhe.c")
        print(GLOB.inventario)
        main.player.evento = None


    if main.player.evento == "chiavetta-7":
        var = "4A"
        print(GLOB.chiavette[var][1])
        GLOB.chiavette[var] = (GLOB.chiavette[var][6], False, GLOB.chiavette[var][2])
        GLOB.inventario["chiavetta-7"] = (False, "Proprietario: Marco Giachero - Files: stringhe.c")
        print(GLOB.inventario)
        main.player.evento = None


    if main.player.evento == "chiavetta-8":
        var = "AulaVideo"
        print(GLOB.chiavette[var][1])
        GLOB.chiavette[var] = (GLOB.chiavette[var][7], False, GLOB.chiavette[var][2])
        GLOB.inventario["chiavetta-8"] = (False, "Proprietario: Chiara Bossolasco - Files: stringhe.c")
        print(GLOB.inventario)
        main.player.evento = None


    if main.player.evento == "chiavetta-9":
        var = "LabInformatica"
        print(GLOB.chiavette[var][1])
        GLOB.chiavette[var] = (GLOB.chiavette[var][8], False, GLOB.chiavette[var][2])
        GLOB.inventario["chiavetta-9"] = (False, "Proprietario: Mattia Barbero - Files: stringhe.c")
        print(GLOB.inventario)
        main.player.evento = None


    if main.player.evento == "chiavetta-10":
        var = "Ripostiglio"
        print(GLOB.chiavette[var][1])
        GLOB.chiavette[var] = (GLOB.chiavette[var][9], False, GLOB.chiavette[var][2])
        GLOB.inventario["chiavetta-10"] = (False, "Proprietario: Lorenzo Ferrato - Files: stringhe.c")
        print(GLOB.inventario)
        main.player.evento = None
        