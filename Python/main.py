import pandas as pd
import pygame, os, sys

#Importo i vari file e classi necessarie
import giocatore, menu, camera, debug, collisioni
from button import Bar, Button, Dialoghi, Dialoghi_Interattivi, Risultato, Timer, GUI
from pygame import mixer
from animazione import Transizione
import stanze

# Importo le variabili Globali
import global_var as GLOB

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font/font.ttf", size)


def SetPlayer_speed():
    """

             --- Cambio il personaggio in base alla scelta del giocatore ---
        

    """

    GLOB.setCharacter()


def SetPlayer_sprite():
    global Folder_walkO, Folder_walkVD, Folder_walkVU
    
    """
 
            ---   Setto il percorso degli sprite ---


    """
    
    #(0 => "/Senex" - 1 => "/Seima" - 2 => "/Alexandra" - 3 => "/XPeppoz" - 4 => "/Giulio" - Default => "/Senex")
    Folder_walkO = 'Characters'+GLOB.scelta_rep+'/WalkOrizontal'
    Folder_walkVD = 'Characters'+GLOB.scelta_rep+'/WalkVerticalD'
    Folder_walkVU = 'Characters'+GLOB.scelta_rep+'/WalkVerticalU'

    # estrapolo tutti i file (sprite/immagini) dalla cartella selezionata
    def riempi(percorso):
        FileNames = os.listdir(percorso)

        # Ordino i file e gli appendo ad una lista, in modo che le animazioni siano lineari e ordinate
        FileNames.sort()
        sorted(FileNames)

        for filename in FileNames:
            if percorso == Folder_walkO:
                # print("Trovato Percorso WO")
                GLOB.PlayerWalkingO.append(filename)
            if percorso == Folder_walkVD:
                # print("Trovato Percorso WVD")
                GLOB.PlayerWalkingVD.append(filename)
            if percorso == Folder_walkVU:
                # print("Trovato Percorso WVU")
                GLOB.PlayerWalkingVU.append(filename)

            # print("File name:"+filename+"\n\n")

    riempi(Folder_walkO)
    riempi(Folder_walkVD)
    riempi(Folder_walkVU)

#funzione di default
def inizializza():
    global player, cam, timer, clock, collisions, animazione, messaggio_a_schermo, Gui

    GLOB.isGameRunning = True
    GLOB.isPaused = False

    stanze.inizializza()
    SetPlayer_speed()

    SetPlayer_sprite()
    GLOB.setResources()

    # Inizializzazione Tupla di animazioni
    character_image = (GLOB.PlayerWalkingVD,GLOB.PlayerWalkingVU,GLOB.PlayerWalkingO)
    
    GLOB.Default_Character = 'Characters'+GLOB.scelta_rep+'/WalkVerticalD/Walk0.png'

    # Ottengo la larghezza e l'altezza che ha il giocatore nell'immagine ( questo per evitare di allungarla in modo sbagliato e non proporzionale )
    Player_width = pygame.image.load(os.path.join(Folder_walkVD,character_image[0][0])).convert().get_width() * GLOB.MULT / GLOB.Player_proportion
    Player_height = pygame.image.load(os.path.join(Folder_walkVD,character_image[0][0])).convert().get_height() * GLOB.MULT / GLOB.Player_proportion

    # Settaggio del Clock
    clock = pygame.time.Clock()

    # Fa Spawnare il giocatore e al centro dello schermo e con che velocità
    player = giocatore.Player(152 * GLOB.MULT, 122 * GLOB.MULT, GLOB.scelta_rep, Player_width, Player_height, character_image)

    # Faccio nascere l'oggetto "cam"
    cam = camera.Cam(130 * GLOB.MULT, -118 * GLOB.MULT)

    Gui = GUI()

    # Messaggio visualizzabile a schermo
    messaggio_a_schermo = Risultato(text = "Esempio", color = "White", size = 12, delay_scomparsa = 4)
    messaggio_a_schermo.Stop()

    timer = Timer(minutes = GLOB.Timer, molt_sec = 1, event = game_over)
    animazione = Transizione(vel = 0.01)

    collisions = collisioni.Map(risoluzione = 24, path = "../MappaGioco/Tileset/Stanze/"+ GLOB.Piano +"/")


def load_collisions(path):

    def CaricaLista(file):
        csv = pd.read_csv("../MappaGioco/Tileset/Stanze/"+ GLOB.Piano +"/"+ GLOB.Stanza +"/csv/"+file, header = None)
        csv = list(csv.values)

        lista_valori = []


        #print("csv",csv)
        #print(GLOB.Drop_Frames)
        # collisions.render_object(event = csv)
        #print(clock.get_fps())
        for value in range(len(csv)):
            for val in csv[value]:
                if val not in lista_valori and val != -1:
                    lista_valori.append(val)
        
        lista_valori.sort()

        tupla = (csv, lista_valori)
        return tupla

    if GLOB.LoadCollisions:
        GLOB.Mappa = CaricaLista(path)
        GLOB.LoadCollisions = False
    # l2 = CaricaLista("ChimicaProva_Basamento.csv")

    #print("\nLista valori",lista_valori)

    for i in GLOB.Mappa[1]:
        if i >= 0 and i < 56:
            CanCollide = True
        elif i >= 56 and i < 125:
            CanCollide = False
        collisions.render_gamemapCollision(lista = GLOB.Mappa[0], object = None, var = i, collisione = CanCollide)

    # for i in l2[1]:
    #     collisions.render_gamemapCollision(lista = l2[0], object= True, var = i, collisione = None)

def disegna():

    if animazione.flag_changeBg:
        animazione.ImpostaSfondo()

    if animazione.iFinished:
        GLOB.PlayerCanMove = True
        #timer.DePause()
    else:
        #timer.Pause()
        GLOB.PlayerIsRunning = False
        GLOB.PlayerCanMove = False
        player.setAllkeys(False)
        player.finish()
        SetPlayer_speed()

    timer.Start()

    if GLOB.score_seconds:
        timer.AddSeconds(GLOB.score_seconds)
        
    GLOB.screen.fill(GLOB.Background_Color)

    cam.update()
    
    collisions.render_map((0,0))

    player.update() # richiama la funzione di aggiornamento del giocatore

    collisions.render_objects((0,0))

    stanze.caricaStanza()

    player.load_playerSurface()

    timer.Show()

    animazione.disegna()

    if GLOB.Enigma:
        messaggio_a_schermo.ReStart()

    try:

        if Enigma.risultato != None:

            if Enigma.isFinished:
                if Enigma.risultato:
                    messaggio_a_schermo.ChangeParamatrer(text = "CORRETTO!", color = "#70c73e", size = 12)
                    condizione = False
                    var = 0

                    for value in range(len(GLOB.enigmi_da_risolvere)):

                        if GLOB.enigmi_da_risolvere[value] == GLOB.Stanza:
                            GLOB.enigmi_risolti.append(GLOB.enigmi_da_risolvere[value])
                            condizione = True
                            var = value

                    if condizione:
                        GLOB.enigmi_da_risolvere.pop(var)

                else:
                    messaggio_a_schermo.ChangeParamatrer(text = "SBAGLIATO!", color = "#e83838", size = 12)

                if messaggio_a_schermo.isFinished:
                    Enigma.risultato = None

            messaggio_a_schermo.Start()
    
    except NameError:
        pass

    # MOSTRO LA GUI A SCHERMO
    Gui.show()

    if player.evento == "porta-99":
        print("Porta chiusa")
        c = Dialoghi(GLOB.scelta_char, "La porta sembra chiusa", 3)
        c.stampa()
        player.evento = None

    if not GLOB.PlayerCanRun:
        SetPlayer_speed()


#Funzione GAME OVER
def game_over():
    sfondo = pygame.image.load("assets/gameover.png").convert()
    sfondo = pygame.transform.scale(sfondo, (sfondo.get_width() * GLOB.MULT, sfondo.get_height() * GLOB.MULT))

    restarta = False

    pygame.mouse.set_visible(True)

    while not restarta:

        # Ottengo la posizione corrente del cursore del mouse
        MENU_MOUSE_POS = pygame.mouse.get_pos()


        distanza_riga = 30
        posy = 180


        PLAY_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, posy * GLOB.MULT), 
            text_input="RESTART", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)
        
        QUIT_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, (posy + distanza_riga) * GLOB.MULT), 
                            text_input="BACK TO MENU", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)

        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_ESCAPE] or (event.type == pygame.MOUSEBUTTONDOWN and QUIT_BUTTON.checkForInput(MENU_MOUSE_POS)):
                GLOB.isGameRunning = False
                menu.main_menu()

            if keys_pressed[pygame.K_RETURN] or (event.type == pygame.MOUSEBUTTONDOWN and PLAY_BUTTON.checkForInput(MENU_MOUSE_POS)):
                pygame.mouse.set_visible(False)
                restarta = True
                inizializza()

        GLOB.screen.blit(sfondo, (0, 0))


        altezza = 6 * GLOB.MULT
        size = 20

        distanza = 40 * GLOB.MULT
        distanza_riga = 20 * GLOB.MULT

    
        GAME_TEXT = get_font(size*int(GLOB.MULT)).render("GAME", True, "Yellow")
        GAME_POS = (GLOB.screen_width/2 - GAME_TEXT.get_width()/2, GLOB.screen_height/3 - GAME_TEXT.get_height()/2 + distanza)

        CGAME_TEXT = get_font(size*int(GLOB.MULT)).render("GAME", True, "Black")
        CGAME_POS = (GLOB.screen_width/2 - CGAME_TEXT.get_width()/2, GLOB.screen_height/3 - CGAME_TEXT.get_height()/2 + distanza + altezza)

        OVER_TEXT = get_font(size*int(GLOB.MULT)).render("OVER", True, "Red")
        OVER_POS = (GLOB.screen_width/2 - OVER_TEXT.get_width()/2, GLOB.screen_height/3 - OVER_TEXT.get_height()/2 + distanza + distanza_riga)

        COVER_TEXT = get_font(size*int(GLOB.MULT)).render("OVER", True, "Black")
        COVER_POS = (GLOB.screen_width/2 - COVER_TEXT.get_width()/2, GLOB.screen_height/3 - COVER_TEXT.get_height()/2 + distanza + distanza_riga + altezza)

        GLOB.screen.blit(CGAME_TEXT, CGAME_POS)
        GLOB.screen.blit(COVER_TEXT, COVER_POS)

        GLOB.screen.blit(GAME_TEXT, GAME_POS)
        GLOB.screen.blit(OVER_TEXT, OVER_POS)

		
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(GLOB.screen)


        clock.tick(GLOB.FPS)
        pygame.display.flip()

#Funzione Volume e Audio del gioco
def options_audio():
    # Setto visibile il cursore del mouse
    pygame.mouse.set_visible(True)

    indietro = False

    BG_Seimi = pygame.image.load("assets/BG_semitransparent.png").convert_alpha()
    BG_Seimi = pygame.transform.scale(BG_Seimi, (GLOB.screen_width, GLOB.screen_height))

    while not indietro:

        disegna()


        GLOB.screen.blit(BG_Seimi, (0, 0))

        # Ottengo la posizione corrente del cursore del mouse
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE_TEXT = menu.get_font(12*int(GLOB.MULT)).render("AUDIO SETTINGS", True, "#e9eef7")
        PAUSE_RECT = PAUSE_TEXT.get_rect(center=(GLOB.screen_width/2, 50*GLOB.MULT))

        AUDIO_TEXT = menu.get_font(10*int(GLOB.MULT)).render("EFFETTI SONORI: ", True, "#e9eef7")
        AUDIO_RECT = AUDIO_TEXT.get_rect(center=(GLOB.screen_width/2, 90*GLOB.MULT))

        MUSICA_TEXT = menu.get_font(10*int(GLOB.MULT)).render("MUSICA: ", True, "#e9eef7")
        MUSICA_RECT = MUSICA_TEXT.get_rect(center=(GLOB.screen_width/2, 130*GLOB.MULT))

        #BARRA AUDIO
        AUDIO = Bar((GLOB.screen_width/2, 100*GLOB.MULT), "#4287f5", GLOB.AU, 1)
        AUDIO.update(GLOB.screen)


        #BARRA MUSICA
        MUSICA = Bar((GLOB.screen_width/2, 140*GLOB.MULT), "#4287f5", GLOB.MU, 1)
        MUSICA.update(GLOB.screen)


        AUDIOPLUS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2+20*GLOB.MULT, 110*GLOB.MULT), 
                            text_input="+", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        AUDIOLESS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2-20*GLOB.MULT, 110*GLOB.MULT), 
                            text_input="-", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        MUSICPLUS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2+20*GLOB.MULT, 150*GLOB.MULT), 
                            text_input="+", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        MUSICLESS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2-20*GLOB.MULT, 150*GLOB.MULT), 
                            text_input="-", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        QUIT_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 190*GLOB.MULT), 
                            text_input="BACK", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)
		
        for button in [AUDIOPLUS_BUTTON, AUDIOLESS_BUTTON, MUSICPLUS_BUTTON, MUSICLESS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(GLOB.screen)

        for event_pausa in pygame.event.get():

            button_sound = mixer.Sound("suoni/option-sound.wav")
            keys_pressed = pygame.key.get_pressed()

            if event_pausa.type == pygame.MOUSEBUTTONDOWN and AUDIOPLUS_BUTTON.checkForInput(MENU_MOUSE_POS):
                GLOB.AU += 1

                if GLOB.AU > 10:
                    GLOB.AU = 10

                button_sound.set_volume(0.16*GLOB.AU)
                button_sound.play()

            if event_pausa.type == pygame.MOUSEBUTTONDOWN and AUDIOLESS_BUTTON.checkForInput(MENU_MOUSE_POS):
                GLOB.AU -= 1

                if GLOB.AU < 0:
                    GLOB.AU = 0
                
                button_sound.set_volume(0.16*GLOB.AU)
                button_sound.play()

            if event_pausa.type == pygame.MOUSEBUTTONDOWN and MUSICPLUS_BUTTON.checkForInput(MENU_MOUSE_POS):
                GLOB.MU += 1

                if GLOB.MU > 10:
                    GLOB.MU = 10

                button_sound.set_volume(0.16*GLOB.MU)
                button_sound.play()

            if event_pausa.type == pygame.MOUSEBUTTONDOWN and MUSICLESS_BUTTON.checkForInput(MENU_MOUSE_POS):
                GLOB.MU -= 1

                if GLOB.MU < 0:
                    GLOB.MU = 0
                
                button_sound.set_volume(0.16*GLOB.MU)
                button_sound.play()

            if event_pausa.type == pygame.QUIT:
                pygame.quit()
                sys.exit()	# mi riapplica le variabili di default quindi è come se riavviassi il gioco

            
            if event_pausa.type == pygame.MOUSEBUTTONDOWN:

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    indietro = True
                    pausa()

        GLOB.screen.blit(PAUSE_TEXT, PAUSE_RECT)
        GLOB.screen.blit(AUDIO_TEXT, AUDIO_RECT)
        GLOB.screen.blit(MUSICA_TEXT, MUSICA_RECT)
        

        pygame.display.flip()
        clock.tick(GLOB.FPS) # setto i FramesPerSecond

# Funzione Gioco in Pausa
def pausa():
    mixer.music.stop()
    timer.Pause()
    # Setto visibile il cursore del mouse
    pygame.mouse.set_visible(True)

    ricominciamo = False

    BG_Seimi = pygame.image.load("assets/BG_semitransparent.png").convert_alpha()
    BG_Seimi = pygame.transform.scale(BG_Seimi, (GLOB.screen_width, GLOB.screen_height))

    GLOB.PlayerCanMove = False

    GLOB.isPaused = True
	
    while not ricominciamo:

        player.setAllkeys(False)
    
        disegna()


        GLOB.screen.blit(BG_Seimi, (0, 0))

        # Ottengo la posizione corrente del cursore del mouse
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE_TEXT = menu.get_font(10*int(GLOB.MULT)).render("MENU DI PAUSA", True, "#e9eef7")
        PAUSE_RECT = PAUSE_TEXT.get_rect(center=(GLOB.screen_width/2, 50*GLOB.MULT))


        PLAY_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 110*GLOB.MULT), 
                            text_input="PLAY", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)
        
        OPTIONS_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 150*GLOB.MULT), 
                            text_input="AUDIO SETTINGS", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)
        
        QUIT_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, 190*GLOB.MULT), 
                            text_input="BACK TO MENU", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)
		
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(GLOB.screen)

        for event_pausa in pygame.event.get():
			
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_ESCAPE] or event_pausa.type == pygame.MOUSEBUTTONDOWN and PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                ricominciamo = True
                GLOB.isPaused = False
                player.finish()
                timer.DePause()
                main()

            if event_pausa.type == pygame.QUIT:
                pygame.quit()
                sys.exit()	# mi riapplica le variabili di default quindi è come se riavviassi il gioco

            if event_pausa.type == pygame.MOUSEBUTTONDOWN:

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                     options_audio()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu.main_menu()

        GLOB.screen.blit(PAUSE_TEXT, PAUSE_RECT)

        pygame.display.flip()
        clock.tick(GLOB.FPS) # setto i FramesPerSecond


def enigma():
    global enigma_file

    print('../MappaGioco/Tileset/Stanze/'+GLOB.Piano+'/'+GLOB.Stanza+'/enigmi/Enigmi'+GLOB.Stanza+'.csv')

    try:
        
        print("- Stanza trovata! -")
        enigma_file = pd.read_csv('../MappaGioco/Tileset/Stanze/'+GLOB.Piano+'/'+GLOB.Stanza+'/enigmi/Enigmi'+GLOB.Stanza+'.csv')

    except FileNotFoundError:

        print("Stanza non trovata!")
        enigma_file = pd.read_csv('../MappaGioco/Tileset/Stanze/1-PianoTerra/Fisica/enigmi/EnigmiFisica.csv')

    SetPlayer_speed()


#funzione principale
def main():

    mixer.music.load("suoni/mix.wav")
    mixer.music.set_volume(0.02*GLOB.MU)
    mixer.music.play(-1)	# La setto a -1 che indica un loop quindi a infinito

    # Setto il messaggio a schermo a false
    messaggio_a_schermo.Stop()

    # Setto il cursore del mouse a non visibile
    pygame.mouse.set_visible(False)
   
    run = True # funzione mainloop() principale

    SetPlayer_speed()

    
    # Funzione che controlla se il tasto è stato premuto
    def key_pressed(event, IsPressed):
        UP = event.key == pygame.K_w or event.key == pygame.K_UP
        DOWN = event.key == pygame.K_s or event.key == pygame.K_DOWN
        LEFT = event.key == pygame.K_a or event.key == pygame.K_LEFT
        RIGHT = event.key == pygame.K_d or event.key == pygame.K_RIGHT

        getUp = player.getUpPress()
        getDown = player.getDownPress()
        getLeft = player.getLeftPress()
        getRight = player.getRightPress()

        condition_1 = getLeft and UP and not(getRight and getDown)
        condition_2 = getLeft and getDown and not(getRight and getUp)
        condition_3 = getRight and UP and not(getLeft and getDown)
        condition_4 = getRight and getDown and not(getLeft and getUp)

        if LEFT and not RIGHT and not(condition_1 and condition_2):
            player.setLeftPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Left"
            else:
                player.finish()
            
        elif RIGHT and not LEFT and not(condition_3 and condition_4):    
            player.setRightPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Right"
            else:
                player.finish()

        elif UP and not DOWN and not(condition_1 and condition_3):
            player.setUpPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Up"
            else:
                player.finish()
            
        elif DOWN and not UP and not(condition_2 and condition_4):
            player.setDownPress(IsPressed)

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Down"
            else:
                player.finish()

        elif event.key == pygame.K_LSHIFT:
            if IsPressed and GLOB.PlayerCanRun:

                GLOB.PlayerIsWalking = False
                GLOB.PlayerIsRunning = True

                player.setIsRunning(GLOB.PlayerCanRun)
                GLOB.Player_speed = GLOB.Player_speed * GLOB.PlayerRun_speed
            else:

                GLOB.PlayerIsWalking = True
                GLOB.PlayerIsRunning = False

                player.setIsRunning(GLOB.PlayerCanRun)
                GLOB.Player_speed = GLOB.Player_default_speed
                
        elif not UP and player.getUpPress() or not DOWN and player.getDownPress():
            player.setAllkeys(False)    # Evita che ci siano input zombie
            player.finish()

    """
    
        ---- Indico la classe dialoghi ----
    
    """

    # personaggi Senex/Seima/Aleks/Beppe/Dark Angel | Limite testo 192 caratteri | velocità minima/massima 1/5

    df = pd.read_csv('Dialoghi/dialogo.csv')

    enigma()

    # print(df[df['Personaggi']])

    while run:
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get(): # per ogni evento che viene eseguito in pygame.event.get()
            keys_pressed = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                GLOB.KeyPressed = pygame.key.name(event.key)
            elif event.type == pygame.KEYUP:
                GLOB.KeyPressed = ""


            if event.type == pygame.QUIT:
                run = False

            if keys_pressed[pygame.K_ESCAPE]:
                pausa()


            
            # FLIP FLOP - SHOW GRID
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_z and GLOB.Debug:
                                
                    if not GLOB.ShowGrid:
                        GLOB.ShowGrid = True
                    elif GLOB.ShowGrid:
                        GLOB.ShowGrid = False

            # FLIP FLOP - DEBUG
            if keys_pressed[pygame.K_F3]:
            
                if not GLOB.Debug:
                    GLOB.Debug = True
                    GLOB.Cam_visible = True
                elif GLOB.Debug:
                    GLOB.Debug = False
                    GLOB.Cam_visible = False

            if GLOB.Debug:

                if keys_pressed[pygame.K_l]:
                    animazione.iFinished = False

                if keys_pressed[pygame.K_k]:
                        
                    if not GLOB.Dialogo:
                        GLOB.Dialogo = True

                if keys_pressed[pygame.K_n]:

                    if not GLOB.Enigma:
                        GLOB.Enigma = True

            if GLOB.PlayerCanMove:

                if event.type == pygame.KEYDOWN:
                    key_pressed(event,True)
                    # print("Ultima key: ",player.Last_keyPressed)
                    
                if event.type == pygame.KEYUP:
                    key_pressed(event,False)
                    player.Last_keyPressed = "Null"

            # if int(clock.get_fps())<110:
            #     print("| fps: "+str(int(clock.get_fps()))) # Per mostrare gli GLOB.FPS

        disegna()


        if GLOB.Dialogo:
            #print(len(df.values))
            for row in range(len(df.values)):
                Racconto = Dialoghi(
                    personaggio = df.values[row][0], 
                    descrizione = df.values[row][1], 
                    text_speed = 3
                )
                
                player.setAllkeys(False)
                player.finish()
                Racconto.stampa()
            GLOB.Dialogo = False


        if GLOB.Enigma:
            global enigma_file, Enigma

            enigma()

            #print(len(df.values))
            row = 0
            Enigma = Dialoghi_Interattivi(
                
                tipo_enigma = str(enigma_file.values[row][0]), 
                personaggio = str(enigma_file.values[row][1]), 
                oggetto = "Documento", 
                descrizione =  str(enigma_file.values[row][2]), 
                suggerimento =  str(enigma_file.values[row][3]), 
                risposte = (str(enigma_file.values[row][4]), str(enigma_file.values[row][5]), str(enigma_file.values[row][6]), str(enigma_file.values[row][7])), 
                soluzione = int(enigma_file.values[row][8]), 
                difficolta = str(enigma_file.values[row][9]), 
                malus = (int(enigma_file.values[row][10]), int(enigma_file.values[row][11]), int(enigma_file.values[row][12]), int(enigma_file.values[row][13]), int(enigma_file.values[row][14])), 
                text_speed = 3
                                          
            )
            player.setAllkeys(False)
            player.finish()
            Enigma.stampa()
            GLOB.Enigma = False
            player.evento = None
        
        # Debugging
        console = debug.Debug()
        
        console.log()

        
        pygame.display.flip() # ti permette di aggiornare una area dello schermo per evitare lag e fornire piu' ottimizzazione
        pygame.display.update()

        clock.tick(GLOB.FPS) # setto i FramesPerSecond
    
    pygame.quit() # per stoppare pygame in modo appropriato
    sys.exit()


# se volessi importare il file non verrebbe autoeseguito automaticamente
if __name__ == "__main__":
    pygame.init()
    main()