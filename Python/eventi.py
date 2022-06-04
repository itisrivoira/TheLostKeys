import random
import main
import global_var as GLOB

def testa():

# ---- GESTIONE EVENTI ----

    def AggiungiChiavetta():
        
        main.Gui.inventory_sound.play()
        
        if main.player.evento == GLOB.RandomKey:
            var = GLOB.RandomRoom
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario[GLOB.RandomKey] = (GLOB.chiavette[var][2], False, "Sono pesante, andavo di moda negli anni '80 / '90, e con me almeno una volta ci hai parlato, che cosa sono?")
            main.player.evento = None
            return
        
        
        if main.player.evento == "chiavetta-1":
            var = "Fisica"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-1"] = (GLOB.chiavette[var][2], False, "Proprietario: Tommaso Dalbesio - Files: ziopera.pkt")
            main.player.evento = None


        if main.player.evento == "chiavetta-2":
            var = "1A"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-2"] = (GLOB.chiavette[var][2], False, "Proprietario: Stefano Senestro - Files: TheLostKeys.py")
            main.player.evento = None


        if main.player.evento == "chiavetta-3":
            var = "WC-Femmine"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-3"] = (GLOB.chiavette[var][2], False, "Proprietario: Aleksandra Venezia - Files: ciauu.py")
            main.player.evento = None


        if main.player.evento == "chiavetta-4":
            var = "AulaMagna"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-4"] = (GLOB.chiavette[var][2], False, "Proprietario: Matteo Seimandi - Files: App.js")
            main.player.evento = None


        if main.player.evento == "chiavetta-5":
            var = "AulaProfessori"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-5"] = (GLOB.chiavette[var][2], False, "Proprietario: Giuseppe Di Biase - Files: stringhedibrutto.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-6":
            var = "LabInfo"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-6"] = (GLOB.chiavette[var][2], False, "Proprietario: Giulio Dajani - Files: shqipe.c")
            main.player.evento = None


        if main.player.evento == "chiavetta-7":
            var = "4A"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-7"] = (GLOB.chiavette[var][2], False, "Proprietario: Lorenzo Ferrato - Files: Ilmiocodice.sql")
            main.player.evento = None


        if main.player.evento == "chiavetta-8":
            var = "AulaVideo"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-8"] = (GLOB.chiavette[var][2], False, "Proprietario: Arvind Pal - Files: onlyCss.css index.html")
            main.player.evento = None


        if main.player.evento == "chiavetta-9":
            var = "LabInformatica"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-9"] = (GLOB.chiavette[var][2], False, "Proprietario: Alberto Boaglio - Files: ABMediaAgency")
            main.player.evento = None


        if main.player.evento == "chiavetta-10":
            var = "Ripostiglio"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-10"] = (GLOB.chiavette[var][2], False, "E' la chiavetta per le macchinette...")
            main.player.evento = None
            
            
            
        if main.player.evento == "chiavetta-11":
            var = "1D"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-11"] = (GLOB.chiavette[var][2], False, "Proprietario: Mattia Barbero - Files: Italian_Ripper.py IlBarbista.sql")
            main.player.evento = None
            
            
        if main.player.evento == "chiavetta-12":
            var = "Corridoio"
            GLOB.chiavette[var] = (GLOB.chiavette[var][0], False, GLOB.chiavette[var][2])
            GLOB.inventario["chiavetta-12"] = (GLOB.chiavette[var][2], False, "Proprietario: Marco Rolando - Files: somebodyelse.mp3")
            main.player.evento = None



    def Cerca(event):
        oggetti = (GLOB.inventario.keys())

        c = False
        for oggetto in oggetti:
            if oggetto == event:
                c = True

        return c


    def Blocca():
        main.Gui.door_sound_locked.play()
        main.player.evento = "porta-99"
        risposte = ["la porta sembra chiusa", "non si apre", "è bloccata"]
        main.player.finish()
        main.player.setAllkeys(False)
        GLOB.PlayerIsRunning = False
        c = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 4)
        c.stampa()
        GLOB.PlayerReset = True


    def Controlla(o):
        try:
            GLOB.inventario[o]
            return False

        except KeyError:
            return True
        
    
    def ControllaContenuto(o):
        try:
                        
            # print(GLOB.inventario[o][1])
            if GLOB.inventario[o][1]:
                return False
            else:
                return True
        except KeyError:
            return True


    def VerificaEnigmi():
        var = GLOB.Stanza
        # print(var)

        c = False
        for value in GLOB.enigmi_risolti:
            if var == value:
                c = True

        return c


    def CheckEnimga(v):
        var = v
        # print(var)

        c = False
        for value in GLOB.enigmi_risolti:
            if var == value:
                c = True

        return c



    if main.player.evento == "enigma":
        condizione = False

        for value in GLOB.enigmi_da_risolvere:
    
            if value != GLOB.Stanza:

                GLOB.Enigma = False
                main.player.evento = None
            
            else:
                condizione = True

        
        if GLOB.Stanza == "WC-Femmine" and Controlla("Ghiaccio"):
            condizione = False
            
            
        if GLOB.Stanza == "Corridoio" and GLOB.Piano == "3-SecondoPiano" and ControllaContenuto("chiavetta-10"):
            condizione = False
            
            risposte = ["Sembra un distributore di merendine", "Cosa farei per un duplo", "Strano che non sia ancora stato distrutto, sarebbero state merendine gratis...", "Non so il perche', ma ho una certa fame..."]
            
            d = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 4)
            d.stampa()
            
            
        if GLOB.Stanza == "Archivio" and ControllaContenuto(GLOB.RandomKey):
            condizione = False
            

        if condizione:
            GLOB.Enigma = True
        else:
            GLOB.Enigma = False
            
        GLOB.PlayerReset = True


    if main.player.evento == "enigma-risolto":
        testo = "Default"
        
        if GLOB.Stanza == "Chimica":
            testo = "Ho trovato un appunto del quale dice che ci sia una chiavetta nascosta all'interno dell'armadio...|Mmmm... mi potrebbe essere utile."
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterActualRoom = "Chimica"
                GLOB.MonsterActualFloor = "1-PianoTerra"
                main.mostro.evento = "porta"
                GLOB.MonsterHasChangedRoom = True

        if GLOB.Stanza == "WC-Femmine":
            oggetto = "Ghiaccio"

            if Cerca(oggetto):
                GLOB.inventario.pop(oggetto)
                main.player.evento = "chiavetta-3"
                AggiungiChiavetta()

                testo = "Wow!|Chi se lo sarebbe aspettato di trovare una chiavetta all'interno del ghiaccio|Magari potrei cercare un PC per vedere il suo contenuto."
                
                if GLOB.Stanza != GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "WC-Femmine"
                    GLOB.MonsterActualFloor = "2-PrimoPiano"
                    main.mostro.evento = "porta"
                    GLOB.MonsterHasChangedRoom = True

        if GLOB.Stanza == "AulaMagna":
            testo = "Mmmm.|Forse la prossima chiavetta ha qualcosa a che fare con una sedia."

        if GLOB.Stanza == "1A":
            testo = "Pensavo piu' difficile...|Ad ogni modo che cos'e' quella strana cosa tra i gessetti della lavagna?!?"

        if GLOB.Stanza == "AulaProfessori":
            testo = "Interessante.|Forse potrei provare ad aprire il libro per vedere se c'e' qualcosa di interessante al suo interno"

        if GLOB.Stanza == "AulaVideo":
            testo = "Pascoli...|Chissa' se nella libreria della scuola ci potrebbe essere quello che sto cercando."
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterActualRoom = "Chimica"
                GLOB.MonsterActualFloor = "1-PianoTerra"
                main.mostro.evento = "porta"
                GLOB.MonsterHasChangedRoom = True

        if GLOB.Stanza == "LabInfo":
            testo = "Scratch... che ricordi, chissa' se tra questi pc ce ne sarà uno funzionante..."
                
        if GLOB.Stanza == "Corridoio" and GLOB.Piano == "3-SecondoPiano":
            
            if Cerca("chiavetta-10"):
                main.player.evento = "chiavetta-12"
                AggiungiChiavetta()
            
            
            testo = "Si, evvai!!| Oltretutto inserendo il codice 4096 nella macchinetta, mi ha dato un'altra chiavetta!|Andiamo ad analizzarne il contenuto!"
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterActualRoom = "LabInfo"
                GLOB.MonsterActualFloor = "3-SecondoPiano"
                main.mostro.evento = "porta"
                GLOB.MonsterHasChangedRoom = True
                
        if GLOB.Stanza == "Archivio":
            testo = "Ce l'ho fatta!!|Oltretutto c'è pure uno strano codice dietro al foglio...|C'è scritto: '"+str(GLOB.codice)+"'"
            
            GLOB.ShowCodice = True
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterActualRoom = "Corridoio"
                GLOB.MonsterActualFloor = "1-PianoTerra"
                main.mostro.evento = "porta-8"
                main.mostro.IseePlayer = True
                main.mostro.aggr = True
                main.mostro.IAttacking = True
        
        if testo != "Default":
            testo = testo.split("|")
            for t in testo:
                d = main.Dialoghi(GLOB.scelta_char, t, 4)
                d.stampa()
                
        GLOB.PlayerReset = True


    if main.player.evento == "mappa":
        mappa = main.MiniMap()
        mappa.update()
        main.player.setAllkeys(False)
        main.SetPlayer_speed()


    def piano():
        
        if main.mostro.evento == "piano-0":
            GLOB.MonsterActualFloor = "0-PianoSegreto"
            
        elif main.mostro.evento == "piano-1":
            GLOB.MonsterActualFloor = "1-PianoTerra"
            
        elif main.mostro.evento == "piano-2":
            GLOB.MonsterActualFloor = "2-PrimoPiano"
            
        elif main.mostro.evento == "piano-3":
            GLOB.MonsterActualFloor = "3-SecondoPiano"
            
        if type(main.mostro.evento) == str:
            if "piano" in main.mostro.evento:
                GLOB.MonsterActualRoom = ""
                main.mostro.evento = "porta"
                main.mostro.IseePlayer = False
                main.mostro.aggr = False
                main.mostro.IAttacking = False
                GLOB.MonsterHasChangedRoom = True
                
                main.mostro.evento = None
        

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
            Blocca()
            return False

    def porte():
        
        if GLOB.MonsterActualRoom != "Corridoio":
            
            valuex, valuey = 0, 0
            
            if GLOB.MonsterActualFloor == "1-PianoTerra":
                valuex, valuey = 274, 114
                
            if GLOB.MonsterActualFloor == "2-PrimoPiano" or GLOB.MonsterActualFloor == "3-SecondoPiano":
                valuex, valuey = 368, 142
            
            if main.mostro.evento != None:
                
                if "porta" in main.mostro.evento:
                    
                    main.mostro.evento = None
                    GLOB.MonsterHasChangedRoom = True
                    GLOB.MonsterActualRoom = "Corridoio"
                    
                    main.mostro.x = valuex * GLOB.MULT
                    main.mostro.y = valuey * GLOB.MULT
                    
                    if GLOB.Stanza == GLOB.MonsterActualRoom:
                        main.Gui.door_sound.play()
                        
                    GLOB.SecondDiffPos = 10
                    
                if "porta-" in main.mostro.evento:
                    GLOB.FlagSecRand = True
                    
        
        if main.mostro.evento == "porta-0":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "1-PianoTerra":
                
                if GLOB.MonsterActualRoom == "Corridoio":
                    GLOB.MonsterActualRoom = "Fisica"
                    
                    main.mostro.x = 344 * GLOB.MULT
                    main.mostro.y = 188 * GLOB.MULT
                    
            main.Gui.door_sound.play()
            
            
        if main.mostro.evento == "porta-5":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "2-PrimoPiano":
                
                if GLOB.MonsterActualRoom == "Corridoio":
                    GLOB.MonsterActualRoom = "1D"
                    
                    main.mostro.x = 376 * GLOB.MULT
                    main.mostro.y = 202 * GLOB.MULT
                    
            main.Gui.door_sound.play()
            
        if main.mostro.evento == "porta-7":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "3-SecondoPiano":
                
                if GLOB.MonsterActualRoom == "Corridoio":
                    GLOB.MonsterActualRoom = "AulaVideo"
                    
                    main.mostro.x = 334 * GLOB.MULT
                    main.mostro.y = 176 * GLOB.MULT
                    
            main.Gui.door_sound.play()
            
        
        if main.mostro.evento == "porta-8":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "1-PianoTerra":
                
                if GLOB.MonsterActualRoom == "Corridoio":
                    GLOB.MonsterActualRoom = "Archivio"
                    
                    main.mostro.x = 392 * GLOB.MULT
                    main.mostro.y = 236 * GLOB.MULT
                    
            main.Gui.door_sound.play()
            
            
            
        if main.mostro.evento == "porta-9":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "3-SecondoPiano":
                
                if GLOB.MonsterActualRoom == "Corridoio":
                    GLOB.MonsterActualRoom = "4A"
                    
                    main.mostro.x = 460* GLOB.MULT
                    main.mostro.y = 160 * GLOB.MULT
                    
            main.Gui.door_sound.play()
                    
                    
        if main.mostro.evento == "porta-11":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "2-PrimoPiano":
                
                if GLOB.MonsterActualRoom == "Corridoio":
                    GLOB.MonsterActualRoom = "AulaProfessori"
                    
                    main.mostro.x = 338 * GLOB.MULT
                    main.mostro.y = 152 * GLOB.MULT
                    
            main.Gui.door_sound.play()
        
    
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
                Blocca()
                return False
            
            main.Gui.door_sound.play()
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
                Blocca()
                return False
            

            main.Gui.door_sound.play()
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
                Blocca()
                return False

            main.Gui.door_sound.play()
            main.animazione.iFinished = False
            
            
        elif main.player.evento == "porta-5":
            main.player.evento = None
            main.stanze.setToDefault()
            
            if GLOB.Piano == "2-PrimoPiano":
                    
                if GLOB.Stanza == "Corridoio":
                    main.stanze.dizionario_flag["Classe1D"] = True

                if GLOB.Stanza == "1D":
                    main.stanze.dizionario_flag["Corridoio1"] = True
                    
            else:
                Blocca()
                return False

            main.Gui.door_sound.play()            
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
                    
                    if not main.mostro.aggr:
                                        
                        GLOB.MonsterActualFloor = "3-SecondoPiano"
                        GLOB.MonsterActualRoom = "Corridoio"
                        main.mostro.evento = "porta-7"
                        porte()

                if GLOB.Stanza == "AulaVideo":
                    main.stanze.dizionario_flag["Corridoio2"] = True

            else:
                Blocca()
                return False

            main.Gui.door_sound.play()
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
                Blocca()
                return False
            
            main.Gui.door_sound.play()
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
                Blocca()
                return False
            
            main.Gui.door_sound.play()
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
                Blocca()
                return False
            
            main.Gui.door_sound.play()
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
                Blocca()
                return False

            main.Gui.door_sound.play()
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
                Blocca()
                return False

            main.Gui.door_sound.play()
            main.animazione.iFinished = False

        if main.player.evento == "porta-3" or main.player.evento == "porta-4" or main.player.evento == "porta-6" or main.player.evento == "porta-13" or main.player.evento == "porta-14":
            Blocca()
            return False
        

    if piano() == False or porte() == False:
        return

    # print(GLOB.PlayerCanCollect)
    if GLOB.PlayerCanCollect:
        AggiungiChiavetta()


    def NonTrovato():
        risposte = ["Non ho trovato nulla", "Sembrerebbe che non ci sia nulla", "Niente.", "Qua non c'è nulla."]
        
        d = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 4)
        d.stampa()
        GLOB.PlayerReset = True
        main.player.evento = None

    def Trovato(o):
        risposte = ["Trovato "+str(o), "Ho trovato "+str(o)]
        d = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 4)
        d.stampa()
        GLOB.PlayerReset = True
        main.player.evento = None


    if main.player.evento == "cerca-T":
        main.Gui.inventory_sound.play()
        GLOB.PlayerReset = True
        oggetto = "Default"
        descrizione = "Default"

        if GLOB.Stanza == "Chimica" and VerificaEnigmi():
            tipo = 0
            oggetto = "Ghiaccio"
            descrizione = "All'interno si intravede uno strano elemento"


        if GLOB.Stanza == "AulaProfessori":
            tipo = 1
            oggetto = "Libro Karl Marx"
            descrizione = "All'interno c'è uno strano post-it con su scritto: \"1917\", e ci sono anche dei rimasugli di carta igienica, ma da dove arriveranno?"

        if GLOB.Stanza == "AulaMagna" and VerificaEnigmi():
            oggetto = "chiavetta-4"

            if Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return

        if GLOB.Stanza == "1A" and VerificaEnigmi():
            oggetto = "chiavetta-2"

            if Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return



        if GLOB.Stanza == "Archivio" and CheckEnimga("AulaVideo"):
            oggetto = "chiavetta-8"

            if Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return

        if GLOB.Stanza == "LabInfo" and CheckEnimga("LabInfo"):
            oggetto = "chiavetta-6"

            if Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return

        if Controlla(oggetto):
            try:
                GLOB.inventario[oggetto] = (GLOB.oggetti[tipo][2], True, descrizione)
            except UnboundLocalError:
                NonTrovato()
                return
        else:
            NonTrovato()
            return

        Trovato(oggetto)


    if main.player.evento == "cerca-F":
        main.Gui.inventory_sound.play()
        NonTrovato()
        GLOB.PlayerReset = True


    if main.player.evento == "codice":
        if GLOB.Stanza == "Archivio" and not GLOB.codice_archivio:
            codice = main.Code(GLOB.codice)
            codice.Show()

            GLOB.codice_archivio = codice.risolto

            if codice.risolto:
                main.stanze.setToDefault()
                main.stanze.dizionario_flag["Archivio1"] = True
                main.stanze.caricaStanza()
                main.stanze.CaricaElementi()


    if main.player.evento == "vittoria":
        main.game_win()


    if main.player.evento == "pc":
        pc = main.Pc()
        pc.show()


    if main.player.evento == "nascondiglio" and GLOB.PlayerCanHide:
        main.player.evento = None
        
        if GLOB.PlayerIsHidden:
            GLOB.PlayerIsHidden = False
        else:
            GLOB.PlayerIsHidden = True
            main.Gui.door_sound.play()