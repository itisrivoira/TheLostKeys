import random
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


    if main.player.evento == "enigma-risolto":
        print("Entrato")
        testo = "Default"
        if GLOB.Stanza == "Chimica":
            testo = "Ho trovato un appunto del quale dice che ci sia una chiavetta nascosta all'interno dell'armadio...|Mmmm... mi potrebbe essere utile."

            testo = testo.split("|")

            for t in testo:
                d = main.Dialoghi(GLOB.scelta_char, t, 3)
                d.stampa()


    if main.player.evento == "mappa":
        mappa = MiniMap()
        mappa.update()
        main.player.setAllkeys(False)
        main.SetPlayer_speed()

    if main.player.evento == "piano-0":
        GLOB.Piano = "0-PianoSegreto"
        main.player.evento = None
        main.stanze.setToDefault()
        main.stanze.dizionario_flag["StanzaSegreta"] = True

        main.animazione.iFinished = False
        main.stanze.setPosition((192, 72), (146, 62))

    elif main.player.evento == "piano-1":
        last_floor = GLOB.Piano
        GLOB.Piano = "1-PianoTerra"
        main.player.evento = None
        main.stanze.setToDefault()

        main.animazione.iFinished = False

        if last_floor == "0-PianoSegreto":
            GLOB.Piano = "0-PianoSegreto"
            main.stanze.dizionario_flag["Archivio1"] = True
        else:
            main.stanze.setPosition((192, 72), (146, 62))
            main.stanze.dizionario_flag["Corridoio"] = True

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
    
    elif main.player.evento == "porta-1":
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


    elif main.player.evento == "porta-2":
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


    elif main.player.evento == "porta-7":
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

    elif main.player.evento == "porta-8":
        main.player.evento = None
        main.stanze.setToDefault()


        if GLOB.Piano == "1-PianoTerra":
        
            if GLOB.Stanza == "Corridoio":
                if not GLOB.codice_archivio:
                    main.stanze.dizionario_flag["Archivio0"] = True
                else:
                    main.stanze.dizionario_flag["Archivio1"] = True

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


    elif main.player.evento == "porta-9":
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


    elif main.player.evento == "porta-10":
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

    elif main.player.evento == "porta-11":
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


    elif main.player.evento == "porta-12":
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

    if main.player.evento == "porta-3" or main.player.evento == "porta-4" or main.player.evento == "porta-5" or main.player.evento == "porta-6" or main.player.evento == "porta-13" or main.player.evento == "porta-14":
        main.player.evento = "porta-99"
        return


    # print(GLOB.PlayerCanCollect)
    if GLOB.PlayerCanCollect:

        if main.player.evento == "chiavetta-1":
            var = "Fisica"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-1"] = (GLOB.chiavette[var][2], False, "Proprietario: Tommaso Dalbesio - Files: stringhe.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-2":
            var = "1A"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-2"] = (GLOB.chiavette[var][2], False, "Proprietario: Stefano Senestro - Files: stringhe.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-3":
            var = "WC-Femmine"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-3"] = (GLOB.chiavette[var][2], False, "Proprietario: Aleksandra Venezia - Files: stringhe.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-4":
            var = "AulaMagna"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-4"] = (GLOB.chiavette[var][2], False, "Proprietario: Matteo Seimandi - Files: stringhe.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-5":
            var = "AulaProfessori"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-5"] = (GLOB.chiavette[var][2], False, "Proprietario: Giuseppe Di Biase - Files: stringhe.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-6":
            var = "LabInfo"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-6"] = (GLOB.chiavette[var][2], False, "Proprietario: Giulio Dajani - Files: stringhe.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-7":
            var = "4A"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-7"] = (GLOB.chiavette[var][2], False, "Proprietario: Marco Giachero - Files: stringhe.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-8":
            var = "AulaVideo"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-8"] = (GLOB.chiavette[var][2], False, "Proprietario: Chiara Bossolasco - Files: stringhe.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-9":
            var = "LabInformatica"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-9"] = (GLOB.chiavette[var][2], False, "Proprietario: Mattia Barbero - Files: stringhe.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-10":
            var = "Ripostiglio"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-10"] = (GLOB.chiavette[var][2], False, "Proprietario: Lorenzo Ferrato - Files: stringhe.c")
            main.player.evento = None



    def Cerca(o):
        try:
            GLOB.inventario[o]
            return False

        except KeyError:
            return True


    def NonTrovato():
        risposte = ["Non ho trovato nulla", "Sembrerebbe che non ci sia nulla", "Niente.", "Qua non c'è nulla."]
        
        d = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 3)
        d.stampa()
        GLOB.PlayerReset = True
        main.player.evento = None


    if main.player.evento == "cerca-T":
        oggetto = "Default"
        descrizione = "Default"

        if GLOB.Stanza == "AulaProfessori":
            oggetto = "Libro Karl Marx"
            descrizione = "All'interno c'è uno strano post-it con su scritto: \"1917\""

        if Cerca(oggetto):
            GLOB.inventario[oggetto] = (GLOB.oggetti[1][2], True, descrizione)
        else:
            NonTrovato()
            return

        risposte = ["Trovato "+str(oggetto), "Ho trovato "+str(oggetto)]
        d = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 3)
        d.stampa()
        GLOB.PlayerReset = True
        main.player.evento = None


    if main.player.evento == "cerca-F":
        NonTrovato()


    if main.player.evento == "codice":
        if GLOB.Stanza == "Archivio" and not GLOB.codice_archivio:
            codice = main.Code(4096)
            codice.Show()

            GLOB.codice_archivio = codice.risolto

            if codice.risolto:
                main.stanze.setToDefault()
                main.stanze.dizionario_flag["Archivio1"] = True
                main.stanze.caricaStanza()
                main.stanze.CaricaElementi()