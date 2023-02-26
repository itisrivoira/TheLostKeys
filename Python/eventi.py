import random
import main
import global_var as GLOB

def testa():

# ---- GESTIONE EVENTI ----

    def AggiungiChiavetta():
        
        button_sound = main.mixer.Sound("suoni/PickUp.wav")
        button_sound.set_volume(0.4 * GLOB.AU)
        button_sound.play()
        
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
            var = "Corridoio3"
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
        risposte = ["la porta sembra chiusa", "non si apre", "è bloccata!", "purtroppo non si apre", "Niente... non riesco ad aprirla"]
        
        if "Corridoio1" in GLOB.Stanza and main.player.evento == "piano-4":
            risposte = ["Amico... Stai giocando ad un gioco, giocalo!", "Non posso scappare ora!!", "Devo completare il mio compito... Non me ne posso andare ora", "Anche se ho paura devo comunque riuscire a farcela", "Bene a sto punto \"Utente\" facevi prima a non giocare ad un gioco horror", "Ehhh! Sarebbe facile la vita.", "Non sono un codardo", "Non sono un codardo. Te invece a quanto pare si'"]

        if "Corridoio2" in GLOB.Stanza:
            risposte = ["Sembra chiusa a chiave", "La porta sembra chiusa a chiave", "Il bagno a quanto pare non accetta piu' personale", "Sembra il bagno maschile... Ma purtroppo è chiuso. Adesso come faccio?!?!", "Sembra il bagno maschile... Ma purtroppo è chiuso. Eh nulla mi tocca tenermela"]
            if GLOB.scelta_char == "Aleks":
                risposte = ["Sembra chiusa a chiave", "La porta sembra chiusa a chiave", "Il bagno a quanto pare non accetta piu' personale", "Magari da qualche parte c'è una chiave!?!", "E' il bagno maschile. Per ora grazie ma non mi scappa! E poi c'è anche il bagno femminile che direi sia meglio."]

        if "Segreteria" in GLOB.Stanza:
            risposte = ["Sembra chiusa a chiave", "Chissa' dove posso trovare la chiave!", "Ah per poco! Il generatore e' proprio li'... Peccato che sia chiusa"]
        
        main.player.evento = "porta-99"
        
        main.player.finish()
        main.player.setAllkeys(False)
        GLOB.PlayerIsRunning = False
        c = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 4)
        c.stampa()
        GLOB.PlayerReset = True


    def Controlla(o):
        return o in GLOB.inventario
    
    def ControllaContenuto(o):
        if not Controlla(o):
            return False
        return GLOB.inventario[o][1]



    def CheckEnigma(v = False):
        var = v if v else GLOB.Stanza

        c = False
        for value in GLOB.enigmi_risolti:
            if var == value:
                c = True
        return c



    def piano():
        
        if main.mostro.evento == "piano-0":
            GLOB.MonsterActualFloor = "0-PianoSegreto"
            GLOB.MonsterActualRoom = "StanzaSegreta"
            
        elif main.mostro.evento == "piano-1":
            GLOB.MonsterActualFloor = "1-PianoTerra"
            GLOB.MonsterActualRoom = "Corridoio1"
            
        elif main.mostro.evento == "piano-2":
            GLOB.MonsterActualFloor = "2-PrimoPiano"
            GLOB.MonsterActualRoom = "Corridoio2"
            
        elif main.mostro.evento == "piano-3":
            GLOB.MonsterActualFloor = "3-SecondoPiano"
            GLOB.MonsterActualRoom = "Corridoio3"
            
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
                main.stanze.dizionario_flag["Archivio"] = True
            else:
                main.stanze.setPosition((192, 72), (146, 62))
                main.stanze.dizionario_flag["Corridoio1"] = True

        elif main.player.evento == "piano-2":
            last_floor = GLOB.Piano
            GLOB.Piano = "2-PrimoPiano"
            main.player.evento = None
            main.stanze.setToDefault()
            main.stanze.dizionario_flag["Corridoio2"] = True

            main.animazione.iFinished = False

            if last_floor == "1-PianoTerra":
                main.stanze.setPosition((210, 90), (-264, -74))
            elif last_floor == "3-SecondoPiano":
                main.stanze.setPosition((214, 90), (-214, -74))
            else:
                main.stanze.setPosition((210, 90), (-264, -74))

        elif main.player.evento == "piano-3":
            GLOB.Piano = "3-SecondoPiano"
            main.player.evento = None
            main.stanze.setToDefault()
            main.stanze.dizionario_flag["Corridoio3"] = True

            main.animazione.iFinished = False
            main.stanze.setPosition((218, 94), (-236, -48))

        elif main.player.evento == "piano-4":
            Blocca()
            return False

    def porte():
        
        if main.mostro.evento != None:
            if "porta" in main.mostro.evento:
                main.Gui.door_sound.play()

        
        if not "Corridoio" in GLOB.MonsterActualRoom and not "Segreteria" in GLOB.MonsterActualRoom:
            
            valuex, valuey = 0, 0
            
            if GLOB.MonsterActualFloor == "1-PianoTerra":
                valuex, valuey =  150, 92
                
            if GLOB.MonsterActualFloor == "2-PrimoPiano" or GLOB.MonsterActualFloor == "3-SecondoPiano":
                valuex, valuey = 222, 72
            
            if main.mostro.evento != None:
                
                if "porta" in main.mostro.evento:
                    
                    main.mostro.evento = None
                    GLOB.MonsterHasChangedRoom = True
                    GLOB.MonsterActualRoom = "Corridoio" + str(GLOB.MonsterActualFloor[0])
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom
                    
                    main.mostro.x = valuex * GLOB.MULT
                    main.mostro.y = valuey * GLOB.MULT
                        
                    GLOB.SecondDiffPos = 0
                    
        if main.mostro.evento != None:
            if "porta" in main.mostro.evento:
                GLOB.FlagSecRand = True
            
            
        if main.mostro.evento == "porta-0":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "1-PianoTerra":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "Fisica"
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom
                    
                    main.mostro.x = 344 * GLOB.MULT
                    main.mostro.y = 188 * GLOB.MULT
                    
            elif GLOB.MonsterActualFloor == "3-SecondoPiano":
                
                if "Generatore" in GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "Segreteria"
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom
                    
                    main.mostro.x = 226 * GLOB.MULT
                    main.mostro.y = 174 * GLOB.MULT
                    
                elif "Segreteria" in GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "Generatore"
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom

                    main.mostro.x = 152 * GLOB.MULT
                    main.mostro.y = 190 * GLOB.MULT
                    main.mostro.monster_ai_brain = 0
                    
                if GLOB.Stanza == "Segreteria":
                        main.stanze.setToDefault()
                        main.stanze.dizionario_flag["Segreteria"] = True
                        main.stanze.caricaStanza()
                        main.stanze.CaricaElementi()
                
            else:
                main.Gui.door_sound_locked.play()
            
            
        if main.mostro.evento == "porta-2":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "1-PianoTerra":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "Chimica"
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom
                    
                    main.mostro.x = 508 * GLOB.MULT
                    main.mostro.y = 137 * GLOB.MULT
                    
                    main.mostro.monster_ai_brain = 2
                    
            else:
                main.Gui.door_sound_locked.play()
                
                
        if main.mostro.evento == "porta-3":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "3-SecondoPiano":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "Segreteria"
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom
                    
                    main.mostro.x = 56 * GLOB.MULT
                    main.mostro.y = 62 * GLOB.MULT
                    
                    main.mostro.monster_ai_brain = 2
                    
            else:
                main.Gui.door_sound_locked.play()
            
            
        if main.mostro.evento == "porta-5":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "2-PrimoPiano":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "1D"
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom
                    
                    main.mostro.x = 376 * GLOB.MULT
                    main.mostro.y = 202 * GLOB.MULT
                    
            else:
                main.Gui.door_sound_locked.play()
            
        if main.mostro.evento == "porta-7":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "3-SecondoPiano":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "AulaVideo"
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom
                    
                    main.mostro.x = 180 * GLOB.MULT
                    main.mostro.y = 32 * GLOB.MULT
                    
            else:
                main.Gui.door_sound_locked.play()
            
        
        if main.mostro.evento == "porta-8":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "1-PianoTerra":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "Archivio"
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom
                    
                    main.mostro.x = 392 * GLOB.MULT
                    main.mostro.y = 236 * GLOB.MULT
                    
            else:
                main.Gui.door_sound_locked.play()
            
            
            
        if main.mostro.evento == "porta-9":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "3-SecondoPiano":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "4A"
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom
                    
                    main.mostro.x = 460 * GLOB.MULT
                    main.mostro.y = 160 * GLOB.MULT
                    
            else:
                main.Gui.door_sound_locked.play()
            
            
        if main.mostro.evento == "porta-12":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "3-SecondoPiano":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "Ripostiglio"
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom
                    
                    main.mostro.x = 271 * GLOB.MULT
                    main.mostro.y = 176 * GLOB.MULT
                    
                    main.mostro.monster_ai_brain = 2
                    
            else:
                main.Gui.door_sound_locked.play()
                    
                    
        if main.mostro.evento == "porta-11":
            main.mostro.evento = None
            GLOB.MonsterHasChangedRoom = True
            
            if GLOB.MonsterActualFloor == "2-PrimoPiano":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    GLOB.MonsterActualRoom = "AulaProfessori"
                    GLOB.MonsterPreviousRoom = GLOB.MonsterActualRoom
                    
                    main.mostro.x = 338 * GLOB.MULT
                    main.mostro.y = 152 * GLOB.MULT
                    
            else:
                main.Gui.door_sound_locked.play()
        
    
        if main.player.evento == "porta-0":
            main.player.evento = None
            main.stanze.setToDefault()

            if GLOB.Piano == "1-PianoTerra":
            
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["Fisica"] = True

                if GLOB.Stanza == "Fisica":
                    main.stanze.dizionario_flag["Corridoio1"] = True

            elif GLOB.Piano == "2-PrimoPiano":
                        
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["LabInfo"] = True

                if GLOB.Stanza == "LabInfo":
                    main.stanze.dizionario_flag["Corridoio2"] = True
                    
            elif GLOB.Piano == "3-SecondoPiano" and Controlla("Chiave Segreteria"):
                
                if GLOB.Stanza == "Segreteria":
                    main.stanze.dizionario_flag["Generatore"] = True
                    
                if GLOB.Stanza == "Generatore":
                    main.stanze.dizionario_flag["Segreteria"] = True

            else:
                Blocca()
                return False
            
            main.Gui.door_sound.play()
            main.animazione.iFinished = False
        
        elif main.player.evento == "porta-1":
            main.player.evento = None
            main.stanze.setToDefault()

            if GLOB.Piano == "2-PrimoPiano" and Controlla("Chiave WC"):
                
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["WCmaschi"] = True

                if GLOB.Stanza == "WC-Maschi":
                    main.stanze.dizionario_flag["Corridoio2"] = True

            else:
                Blocca()
                return False
            

            main.Gui.door_sound.play()
            main.animazione.iFinished = False


        elif main.player.evento == "porta-2":
            main.player.evento = None
            main.stanze.setToDefault()


            if GLOB.Piano == "1-PianoTerra":
            
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["Chimica"] = True

                if GLOB.Stanza == "Chimica":
                    main.stanze.dizionario_flag["Corridoio1"] = True

            else:
                Blocca()
                return False

            main.Gui.door_sound.play()
            main.animazione.iFinished = False
            
            
        elif main.player.evento == "porta-3":
            main.player.evento = None
            main.stanze.setToDefault()
                    
            if GLOB.Piano == "3-SecondoPiano":
                
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["Segreteria"] = True

                if GLOB.Stanza == "Segreteria":
                    main.stanze.dizionario_flag["Corridoio3"] = True

            else:
                Blocca()
                return False

            main.Gui.door_sound.play()
            main.animazione.iFinished = False
            
            
        elif main.player.evento == "porta-5":
            main.player.evento = None
            main.stanze.setToDefault()
            
            if GLOB.Piano == "2-PrimoPiano":
                    
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["Classe1D"] = True

                if GLOB.Stanza == "1D":
                    main.stanze.dizionario_flag["Corridoio2"] = True
                    
            else:
                Blocca()
                return False

            main.Gui.door_sound.play()            
            main.animazione.iFinished = False
            
            
        elif main.player.evento == "porta-6":
            main.player.evento = None
            main.stanze.setToDefault()

            Blocca()
            return False


        elif main.player.evento == "porta-7":
            main.player.evento = None
            main.stanze.setToDefault()

            if GLOB.Piano == "2-PrimoPiano":
                
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["Classe1A"] = True

                if GLOB.Stanza == "1A":
                    main.stanze.dizionario_flag["Corridoio2"] = True

            elif GLOB.Piano == "3-SecondoPiano":
                        
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["AulaVideo"] = True
                    
                    try:
                        if not main.mostro.aggr and GLOB.enigmi_risolti[0] != "AulaVideo":
                                            
                            GLOB.MonsterActualFloor = "3-SecondoPiano"
                            GLOB.MonsterActualRoom = "Corridoio"
                            main.mostro.evento = "porta-7"
                            porte()
                    except IndexError:
                        pass

                if GLOB.Stanza == "AulaVideo":
                    main.stanze.dizionario_flag["Corridoio3"] = True

            else:
                Blocca()
                return False

            main.Gui.door_sound.play()
            main.animazione.iFinished = False

        elif main.player.evento == "porta-8":
            main.player.evento = None
            main.stanze.setToDefault()


            if GLOB.Piano == "1-PianoTerra":
            
                if "Corridoio" in GLOB.Stanza:
                        main.stanze.dizionario_flag["Archivio"] = True

                if GLOB.Stanza == "Archivio":
                    main.stanze.dizionario_flag["Corridoio1"] = True


            elif GLOB.Piano == "2-PrimoPiano":
                
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["AulaMagna"] = True

                if GLOB.Stanza == "AulaMagna":
                    main.stanze.dizionario_flag["Corridoio2"] = True

            else:
                Blocca()
                return False
            
            main.Gui.door_sound.play()
            main.animazione.iFinished = False


        elif main.player.evento == "porta-9":
            main.player.evento = None
            main.stanze.setToDefault()

            
            if GLOB.Piano == "3-SecondoPiano":
                
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["Classe4A"] = True

                if GLOB.Stanza == "4A":
                    main.stanze.dizionario_flag["Corridoio3"] = True

            else:
                Blocca()
                return False
            
            main.Gui.door_sound.play()
            main.animazione.iFinished = False


        elif main.player.evento == "porta-10":
            main.player.evento = None
            main.stanze.setToDefault()


            if GLOB.Piano == "2-PrimoPiano":
                
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["WCfemmine"] = True

                if GLOB.Stanza == "WC-Femmine":
                    main.stanze.dizionario_flag["Corridoio2"] = True


            else:
                Blocca()
                return False
            
            main.Gui.door_sound.play()
            main.animazione.iFinished = False

        elif main.player.evento == "porta-11":
            main.player.evento = None
            main.stanze.setToDefault()


            if GLOB.Piano == "2-PrimoPiano":
                
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["AulaProfessori"] = True

                if GLOB.Stanza == "AulaProfessori":
                    main.stanze.dizionario_flag["Corridoio2"] = True


            elif GLOB.Piano == "3-SecondoPiano":
                    
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["LabInformatica"] = True

                if GLOB.Stanza == "LabInformatica":
                    main.stanze.dizionario_flag["Corridoio3"] = True

            else:
                Blocca()
                return False

            main.Gui.door_sound.play()
            main.animazione.iFinished = False


        elif main.player.evento == "porta-12":
            main.player.evento = None
            main.stanze.setToDefault()


            if GLOB.Piano == "3-SecondoPiano":
                    
                if "Corridoio" in GLOB.Stanza:
                    main.stanze.dizionario_flag["Ripostiglio"] = True

                if GLOB.Stanza == "Ripostiglio":
                    main.stanze.dizionario_flag["Corridoio3"] = True

            else:
                Blocca()
                return False

            main.Gui.door_sound.play()
            main.animazione.iFinished = False

    def NonTrovato():
        risposte = ["Non ho trovato nulla", "Sembrerebbe che non ci sia nulla", "Niente.", "Qua non c'è nulla.", "Vuoto.", "Bello! Non c'è nulla", "Ho trovato... Eh volevi!"]
        
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



    if main.player.evento == "enigma":
        condizione = False

        for value in GLOB.enigmi_da_risolvere:
    
            if value != GLOB.Stanza:

                GLOB.Enigma = False
                main.player.evento = None
            
            else:
                condizione = True

        
        if GLOB.Stanza == "WC-Femmine" and not Controlla("Ghiaccio"):
            condizione = False
            
            risposte = ["Certo! A questo punto faccio prima a non lavarmele... guarda te", "Grazie, ma non GRAZIE! Troppo sporca!", "Bleah! Che acqua putrida", "Non ne trovo l'utilita' adesso"]
        
            d = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 4)
            d.stampa()
            
            
        if ("Corridoio" in GLOB.Stanza and GLOB.Piano == "3-SecondoPiano" and not ControllaContenuto("chiavetta-10")):
            condizione = False
            
            risposte = ["Sembra un distributore di merendine", "Cosa farei per un duplo", "Strano che non sia ancora stato distrutto, sarebbero state merendine gratis...", "Non so il perche', ma ho una certa fame..."]
            
            d = main.Dialoghi(GLOB.scelta_char, random.choice(risposte), 4)
            d.stampa()
            
            
        if GLOB.Stanza == "Archivio" and not ControllaContenuto(GLOB.RandomKey):
            condizione = False
            
            testo = "Sembrano due vecchi telefoni..."
            
            d = main.Dialoghi(GLOB.scelta_char, testo, 4)
            d.stampa()
            

        GLOB.Enigma = condizione
        GLOB.PlayerReset = True


    if main.player.evento == "enigma-risolto":
        testo = "Default"
        
        if GLOB.Stanza == "Chimica":
            testo = "Ho trovato un appunto che dice che ci sia una chiavetta nascosta all'interno della cella frigorifero...|Mmmm... mi potrebbe essere utile."
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterActualRoom = "Chimica"
                GLOB.MonsterPreviousRoom = "Chimica"
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
                
                if GLOB.Stanza != GLOB.MonsterActualRoom and not main.mostro.IseePlayer:
                    GLOB.MonsterActualRoom = "WC-Femmine"
                    GLOB.MonsterPreviousRoom = "WC-Femmine"
                    GLOB.MonsterActualFloor = "2-PrimoPiano"
                    main.mostro.evento = "porta"
                    GLOB.MonsterHasChangedRoom = True

        if GLOB.Stanza == "AulaMagna":
            testo = "Mmmm.|Forse la prossima chiavetta ha qualcosa a che fare con una sedia."

            if GLOB.Stanza != GLOB.MonsterActualRoom and len(GLOB.enigmi_risolti) > 1:
                GLOB.MonsterActualRoom = "AulaMagna"
                GLOB.MonsterPreviousRoom = "Corridoio2"
                GLOB.MonsterActualFloor = "2-PrimoPiano"
                main.mostro.evento = "porta"
                GLOB.MonsterHasChangedRoom = True

        if GLOB.Stanza == "1A":
            testo = "Pensavo piu' difficile...|Ad ogni modo che cos'e' quella strana cosa tra i gessetti della lavagna?!?"

        if GLOB.Stanza == "AulaProfessori":
            testo = "Interessante.|Ho trovato una chiave dietro al foglio, con su scritto \"WC\""
            
            oggetto = "Chiave WC"
            descrizione = "Chiave del bagno Maschile"
            tipo = 3
            
            GLOB.inventario[oggetto] = (GLOB.oggetti[tipo][2], True, descrizione)

        if GLOB.Stanza == "AulaVideo":
            testo = "Pascoli...|Chissa' se nella libreria della scuola ci potrebbe essere quello che sto cercando."
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterPreviousRoom = "Chimica"
                GLOB.MonsterActualRoom = "Chimica"
                GLOB.MonsterActualFloor = "1-PianoTerra"
                main.mostro.evento = "porta"
                GLOB.MonsterHasChangedRoom = True

        if GLOB.Stanza == "LabInfo":
            testo = "Scratch... che ricordi, chissa' se tra questi pc ce ne sarà uno funzionante..."
                
        if "Corridoio" in GLOB.Stanza and GLOB.Piano == "3-SecondoPiano":
            
            if Cerca("chiavetta-10"):
                main.player.evento = "chiavetta-12"
                AggiungiChiavetta()
            
            
            testo = "Si, evvai!!| Oltretutto inserendo il codice 4096 nella macchinetta, mi ha dato un'altra chiavetta!|Andiamo ad analizzarne il contenuto!"
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterPreviousRoom = "WC-Maschi"
                GLOB.MonsterActualRoom = "Default"
                GLOB.MonsterActualFloor = "2-PrimoPiano"
                main.mostro.evento = "porta"
                GLOB.MonsterHasChangedRoom = True
                
        if GLOB.Stanza == "Archivio":
            testo = "Ce l'ho fatta!!|Oltretutto c'è pure uno strano codice dietro al foglio...|C'è scritto: '"+str(GLOB.codice)+"'"
            
            GLOB.ShowCodice = True
            
            if GLOB.Stanza != GLOB.MonsterActualRoom:
                GLOB.MonsterActualRoom = "Corridoio1"
                GLOB.MonsterActualFloor = "1-PianoTerra"
                main.mostro.evento = "porta-8"
                main.mostro.IseePlayer = True
        
        if testo != "Default":
            testo = testo.split("|")
            for t in testo:
                d = main.Dialoghi(GLOB.scelta_char, t, 4)
                d.stampa()
                
        GLOB.PlayerReset = True


    if main.player.evento == "mappa":
        main.MiniMap().update()
        main.player.setAllkeys(False)
        main.SetPlayer_speed()


    if main.player.evento != None:
        if "porta" in main.player.evento or "piano" in main.player.evento:
            GLOB.LoadCollisions = True
            GLOB.LoadImages = True


    if piano() == False or porte() == False:
        return

    if GLOB.PlayerCanCollect:
        AggiungiChiavetta()

    if main.player.evento == "cerca-T":
        main.Gui.searching_sound.set_volume(0.3*GLOB.AU)
        main.Gui.searching_sound.play()
        
        GLOB.PlayerReset = True
        oggetto = "Default"
        descrizione = "Default"
        tipo = -1

        if GLOB.Stanza == "Chimica" and CheckEnigma():
            tipo = 0
            oggetto = "Ghiaccio"
            descrizione = "All'interno si intravede uno strano elemento"

        if GLOB.Stanza == "AulaProfessori":
            tipo = 1
            oggetto = "Libro Karl Marx"
            descrizione = "All'interno c'e' uno strano post-it con su scritto: \"E' stato bello finche\' e' durato stare in questa scuola 02/02/2018\""

        if GLOB.Stanza == "WC-Maschi":
            tipo = 4
            oggetto = "Chiave Segreteria"
            descrizione = "Chiave che apre la porta della segreteria situata  al terzo piano..."

        if GLOB.Stanza == "AulaMagna" and CheckEnigma():
            oggetto = "chiavetta-4"

            if not Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return

        if GLOB.Stanza == "1A" and CheckEnigma():
            oggetto = "chiavetta-2"

            if not Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return



        if GLOB.Stanza == "Archivio" and CheckEnigma("AulaVideo"):
            oggetto = "chiavetta-8"

            if not Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return

        if GLOB.Stanza == "LabInfo" and CheckEnigma("LabInfo"):
            oggetto = "chiavetta-6"

            if not Controlla(oggetto):
                main.player.evento = oggetto
                AggiungiChiavetta()
                Trovato(oggetto)
            else:
                NonTrovato()

            return

        if Controlla(oggetto):            
            NonTrovato()
            return

        if tipo == -1:
            NonTrovato()
            return
        else:
            GLOB.inventario[oggetto] = (GLOB.oggetti[tipo][2], True, descrizione)
            
        Trovato(oggetto)


    if main.player.evento == "cerca-F":
        main.Gui.searching_sound.set_volume(0.3*GLOB.AU)
        main.Gui.searching_sound.play()
        NonTrovato()
        GLOB.PlayerReset = True


    if main.player.evento == "codice":
        if GLOB.Stanza == "Archivio" and not GLOB.codice_archivio:
            codice = main.Code(GLOB.codice)
            codice.Show()

            GLOB.codice_archivio = codice.risolto

            if codice.risolto:
                main.stanze.setToDefault()
                main.stanze.dizionario_flag["Archivio"] = True
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
            
    
    if main.player.evento == "ispeziona":
        main.player.evento = None
        
        testo = "Default"
        
        if GLOB.Piano == "1-PianoTerra":
            
            if "Corridoio" in GLOB.Stanza:
                testo = "Sembra una vecchia bacheca con gli eventi riportati di quegli anni|Nulla che mi possa servire..."
                
            if GLOB.Stanza == "Fisica":
                testo = "Ah.. che ricordi!|Non riusciro' mai a scordarmi l'omega con le chiappe del Prof. Fulchero"
                
                
        if GLOB.Piano == "2-PrimoPiano":
                
            if "Corridoio" in GLOB.Stanza:
                testo = "Sembra un distributore di merendine|Peccato che sia completamente vuoto..."
                
            if GLOB.Stanza == "AulaMagna":
                testo = "Il tempo ha proprio ridotto male questo posto..."
                
            if GLOB.Stanza == "WC-Maschi":
                testo = "Sembra un rubinetto, ma purtroppo non ne esce acqua."
                
            if GLOB.Stanza == "WC-Femmine":
                testo = "Bleah! Di certo l'igiene non era una cosa fondamentale in questa scuola"
                
        if GLOB.Piano == "3-SecondoPiano":
                
            if GLOB.Stanza == "Segreteria":
                testo = "Chissa' da quanto tempo è abbandonata...| All'interno intravedo un generatore"
                
                if not GLOB.corrente:
                    testo += "|Forse grazie a quello mi sara' possibile riattivare di nuovo la corrente!!"
                
            if GLOB.Stanza == "Generatore":
                GLOB.corrente = not GLOB.corrente
                GLOB.PlayerHasPressedButton = True

                testo = "Ho " + ("attivato" if GLOB.corrente else "disattivato") + " la corrente!"
                
                
        if testo != "Default":  
            testo = testo.split("|")
            
            for frase in testo:
                
                d = main.Dialoghi(GLOB.scelta_char, frase, 4)
                d.stampa()
                
        if GLOB.Piano == "3-SecondoPiano":
            if GLOB.Stanza == "Generatore":
                main.lum.Reload()
                sound = main.mixer.Sound("suoni/"+str(GLOB.corrente)+"corrente.wav")
                sound.set_volume(0.5 * GLOB.AU)
                sound.fadeout(900)
                sound.play()
                GLOB.PlayerHasPressedButton = False