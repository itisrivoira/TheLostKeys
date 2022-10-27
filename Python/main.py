import pandas as pd
import pygame, os, sys, random

#Importo i vari file e classi necessarie
import giocatore, menu, camera, debug, collisioni
from components import Bar, Button, Dialoghi, Delay, Dialoghi_Interattivi, Risultato, Timer, GUI, MiniMap, Code, Pc
from pygame import mixer
from pyvidplayer import Video
from animazione import Transizione
from mostro import Keeper
import stanze

# Importo le variabili Globali
import global_var as GLOB

def get_font(size):
    return pygame.font.Font("font/font.ttf", size)


def SetPlayer_speed():
    GLOB.setCharacter()
    GLOB.setMonster()

def SetPlayer_sprite():
    global Folder_walkO, Folder_walkVD, Folder_walkVU
    
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
    
    
def ChangeDeltaTime(f):
    
    if f:
        GLOB.Delta_Time = 1
        GLOB.FPS = 30 * GLOB.Delta_Time
        timer.Pause()
    else:
        GLOB.Delta_Time = GLOB.Default_DeltaTime
        GLOB.FPS = 30 * GLOB.Delta_Time
        timer.DePause()
        
    SetPlayer_sprite()
    SetPlayer_speed()

#funzione di default
def inizializza():
    global console, player, cam, timer, clock, collisions, animazione, messaggio_a_schermo, Gui

    GLOB.isGameRunning = True
    GLOB.isPaused = False

    stanze.inizializza()
    GLOB.setResources()
    GLOB.LoadGame(GLOB.CaricaPartita)
    
    SetPlayer_speed()
    SetPlayer_sprite()

    # Inizializzazione Tupla di animazioni
    character_image = (GLOB.PlayerWalkingVD,GLOB.PlayerWalkingVU,GLOB.PlayerWalkingO)
    
    GLOB.Default_Character = 'Characters'+GLOB.scelta_rep+'/WalkVerticalD/Walk0.png'

    # Ottengo la larghezza e l'altezza che ha il giocatore nell'immagine ( questo per evitare di allungarla in modo sbagliato e non proporzionale )
    Player_width = pygame.image.load(os.path.join(Folder_walkVD,character_image[0][0])).convert().get_width() * GLOB.MULT / GLOB.Player_proportion
    Player_height = pygame.image.load(os.path.join(Folder_walkVD,character_image[0][0])).convert().get_height() * GLOB.MULT / GLOB.Player_proportion

    # Settaggio del Clock
    clock = pygame.time.Clock()

    # Fa Spawnare il giocatore e al centro dello schermo e con che velocità
    player = giocatore.Player(GLOB.PlayerXSpawn, GLOB.PlayerYSpawn, GLOB.scelta_rep, Player_width, Player_height, character_image)

    # Faccio nascere l'oggetto "cam"
    cam = camera.Cam(GLOB.CamXSpawn, GLOB.CamYSpawn)

    Gui = GUI()

    # Messaggio visualizzabile a schermo
    messaggio_a_schermo = Risultato(text = "Esempio", color = "White", size = 12, delay_scomparsa = 1)
    messaggio_a_schermo.Stop()

    timer = Timer(minutes = GLOB.TimerMin, seconds = GLOB.TimerSec, molt_sec = 1, event = game_over)
    animazione = Transizione(vel = 0.01)

    collisions = collisioni.Map(risoluzione = 24, path = GLOB.Default_path+"/"+ GLOB.Piano +"/")

    console = debug.Debug()



    if GLOB.MonsterCanSpawn:
        global mostro
        mostro = Keeper((GLOB.MonsterXSpawn, GLOB.MonsterYSpawn), (20 * GLOB.MULT, 0.45 * GLOB.MULT))


def load_collisions(path):

    def CaricaLista(file):
        csv = pd.read_csv(GLOB.Default_path+"/"+ GLOB.Piano +"/"+ GLOB.Stanza +"/csv/"+file, header = None)
        csv = list(csv.values)

        lista_valori = []

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

    for i in GLOB.Mappa[1]:
        if i >= 0 and i < 56:
            CanCollide = True
        elif i >= 56 and i < 125:
            CanCollide = False
        collisions.render(lista = GLOB.Mappa[0], var = i, hitbox = CanCollide)


def controllo_condizioni():
    
    if GLOB.Stanza in GLOB.stanze_da_visitare and not GLOB.Stanza in GLOB.stanze_visitate:
        GLOB.stanze_da_visitare.remove(GLOB.Stanza)
        GLOB.stanze_visitate.append(GLOB.Stanza)
    
    
    if GLOB.MonsterCanSpawn and GLOB.Stanza != GLOB.MonsterActualRoom:
        if GLOB.FlagSecRand:    
            GLOB.Val_sec = random.randint(0, abs(int((timer.getSeconds() - GLOB.SecondDiffPos + 1))))
            GLOB.FlagSecRand = False
        
        if int(timer.getSeconds()) == GLOB.Val_sec and not mostro.IseePlayer and not mostro.aggr:
            valuex, valuey = 220, 68
            flag_stanza = False
            
            prec_piano = GLOB.MonsterActualFloor
            
            if GLOB.MonsterActualFloor == "1-PianoTerra":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    flag_stanza = True
                    GLOB.MonsterActualRoom = random.choice(["Fisica", "Archivio", "Chimica", "Corridoio2"])
                    
                if GLOB.MonsterActualRoom == "Fisica":
                    valuex, valuey = 322, 20
                    mostro.monster_ai_brain = 3
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 574, 232
                    
                if GLOB.MonsterActualRoom == "Archivio":
                    valuex, valuey = 8, 166
                    mostro.monster_ai_brain = 1
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 408, 238
                    
                if GLOB.MonsterActualRoom == "Chimica":
                    valuex, valuey = 610, 20
                    mostro.monster_ai_brain = 1
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 620, 210
                        
                if GLOB.MonsterActualRoom == "Corridoio2":
                    GLOB.MonsterActualFloor = "2-PrimoPiano"
                    valuex, valuey = 428, 170
                    mostro.monster_ai_brain = 0
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 228, 86
                        mostro.monster_ai_brain = 4
                
            if GLOB.MonsterActualFloor == "2-PrimoPiano":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    flag_stanza = True
                    GLOB.MonsterActualRoom = random.choice(["AulaProfessori", "AulaMagna", "1D", "WC-Maschi", "LabInfo", "Corridoio3", "Corridoio1"])
                
                if GLOB.MonsterActualRoom == "AulaProfessori":
                    valuex, valuey = 516, 70
                    mostro.monster_ai_brain = 2
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 164, 162
                    
                if GLOB.MonsterActualRoom == "WC-Femmine":
                    valuex, valuey = 516, 142
                    mostro.monster_ai_brain = 2
                    
                if GLOB.MonsterActualRoom == "AulaMagna":
                    valuex, valuey = 360, 168
                    mostro.monster_ai_brain = 4
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 598, 260
                    
                if GLOB.MonsterActualRoom == "1A":
                    valuex, valuey = 250, 168
                    mostro.monster_ai_brain = 4
                       
                if GLOB.MonsterActualRoom == "1D":
                    valuex, valuey = 180, 168
                    mostro.monster_ai_brain = 4
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 528, 164
                    
                if GLOB.MonsterActualRoom == "WC-Maschi":
                    valuex, valuey = 32, 168
                    mostro.monster_ai_brain = 4
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 526, 240
                    
                if GLOB.MonsterActualRoom == "LabInfo":
                    valuex, valuey = 10, 90
                    mostro.monster_ai_brain = 1
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 288, 216
                        
                if GLOB.MonsterActualRoom == "Corridoio1":
                    GLOB.MonsterActualFloor = "1-PianoTerra"
                    valuex, valuey = 46, 10
                    mostro.monster_ai_brain = 1
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 200, 96
                        mostro.monster_ai_brain = 3
                        
                if GLOB.MonsterActualRoom == "Corridoio3":
                    GLOB.MonsterActualFloor = "3-SecondoPiano"
                    valuex, valuey = 454, 98
                    mostro.monster_ai_brain = 3
                    mostro.monster_ai_brain = 0
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 454, 154
                        mostro.monster_ai_brain = 4
                    
            if GLOB.MonsterActualFloor == "3-SecondoPiano":
                
                if "Corridoio" in GLOB.MonsterActualRoom:
                    flag_stanza = True
                    GLOB.MonsterActualRoom = random.choice(["AulaVideo", "4A", "LabInformatica", "Corridoio2"])
                
                if GLOB.MonsterActualRoom == "AulaVideo":
                    valuex, valuey = 506, 46
                    mostro.monster_ai_brain = 2
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 18, 262
                    
                if GLOB.MonsterActualRoom == "4A":
                    valuex, valuey = 176, 148
                    mostro.monster_ai_brain = 4
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 584, 54
                    
                if GLOB.MonsterActualRoom == "LabInformatica":
                    valuex, valuey = 52, 148
                    mostro.monster_ai_brain = 4
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 408, 234
                    
                if GLOB.MonsterActualRoom == "Ripostiglio":
                    valuex, valuey = 56, 18
                    mostro.monster_ai_brain = 1
                    
                if GLOB.MonsterActualRoom == "Corridoio2":
                    GLOB.MonsterActualFloor = "2-PrimoPiano"
                    valuex, valuey = 100, 90
                    mostro.monster_ai_brain = 0
                    
                    if GLOB.MonsterActualRoom == GLOB.Stanza:
                        valuex, valuey = 428, 174
                        mostro.monster_ai_brain = 4
                    
            GLOB.MonsterHasChangedRoom = True
            
            if not flag_stanza:
                GLOB.MonsterActualRoom = "Corridoio" + str(GLOB.MonsterActualFloor[0])
            
            mostro.x = valuex * GLOB.MULT
            mostro.y = valuey * GLOB.MULT
            mostro.IseePlayer = False
            mostro.aggr = False
            mostro.IAttacking = False
            mostro.contatore_collisioni = 0
            mostro.delayInteract.ReStart()
            mostro.character_update(0)
            mostro.flag_interact = False
            GLOB.FlagSecRand = True
            
            if GLOB.Stanza == GLOB.MonsterActualRoom and prec_piano == GLOB.MonsterActualFloor:
                Gui.door_sound.play()
    
    if not GLOB.PlayerHasPressedButton:
        player.setAllkeys(False)
        player.finish()
    
    if len(GLOB.enigmi_risolti) > 0 and GLOB.MonsterIntro and animazione.iFinished and not animazione.flag_caricamento:
        
        if messaggio_a_schermo.isFinished:
            mostro.Sound_Angry.fadeout(2200)
            testo = "Che cos'era quello strano suono?|Proveniva dall'ingresso principale!"
            
            testo = testo.split("|")
            
            for t in testo:
                dialogo = Dialoghi(GLOB.scelta_char, t, 4)
                dialogo.stampa()
                
            GLOB.MonsterIntro = False
        else:
            
            if not GLOB.MonsterSpawning:
                mostro.Sound_Angry.play()    
                GLOB.MonsterSpawning = True
                SetPlayer_speed()

    if GLOB.Stanza == GLOB.MonsterActualRoom and GLOB.Piano == GLOB.MonsterActualFloor:
        GLOB.MonsterCanChangeRoom = True
                
    if (GLOB.ShowComand or GLOB.ShowIntro) and not animazione.flag_caricamento:
        testo1 = "Ciao! Io sono la prof. Dalbesio e saro' la tua guida di questo viaggio!|"
        testo2 = "Per muoverti clicca le freccie direzionali o WASD|Per correre tieni premuto SHIFT|"
        testo3 = "Per aprire l'inventario premi TAB|Per interagire con gli oggetti premere E|"
        testo4 = "Nei vari enigmi che troverai pensa con calma, e trova tutti gli indizi|"
        testo5 = "Se durante gli enigmi avrai bisogno di un aiuto premi 'I'"
        testo6 = "|Detto questo, hai un compito, trova la via di fuga contenuta in una chiavetta, cerca le pagine e vinci! Buona fortuna!"
        
        if GLOB.ShowIntro:
            testo = testo1 + testo2 + testo3 + testo4 + testo5 + testo6
        else:
            testo = testo2 + testo3 + testo5


        testo = testo.split("|")

        for frase in testo:
            d = Dialoghi("Dalbesio", frase, 4)
            d.stampa()

        GLOB.ShowIntro = False
        GLOB.ShowComand = False


    if GLOB.PlayerReset:
        SetPlayer_sprite()
        player.setAllkeys(False)
        player.finish()
        SetPlayer_speed()
        GLOB.PlayerReset = False

    if animazione.flag_changeBg:
        animazione.ImpostaSfondo()

    if animazione.iFinished:
        GLOB.PlayerCanMove = True
    else:
        GLOB.PlayerIsRunning = False
        GLOB.PlayerCanMove = False
        player.setAllkeys(False)
        player.finish()
        SetPlayer_speed()


def Stampa_messaggio():
    Stanza = GLOB.Stanza
    if GLOB.Enigma:
        messaggio_a_schermo.ReStart()

    try:

        if Enigma.risultato != None:

            if Enigma.isFinished:
                if Enigma.risultato:
                    messaggio_a_schermo.ChangeParamatrer(text = "ENIGMA RISOLTO!", color = "#70c73e", size = 12)
                    condizione = False
                    var = 0

                    for value in range(len(GLOB.enigmi_da_risolvere)):

                        if GLOB.enigmi_da_risolvere[value] == Stanza:
                            GLOB.enigmi_risolti.append(GLOB.enigmi_da_risolvere[value])
                            condizione = True
                            var = value

                    if condizione:
                        GLOB.enigmi_da_risolvere.pop(var)
                        player.evento = "enigma-risolto"
                        collisioni.eventi.testa()

                else:
                    messaggio_a_schermo.ChangeParamatrer(text = "RIPROVA", color = "#e83838", size = 12)

                if messaggio_a_schermo.isFinished:
                    Enigma.risultato = None

            messaggio_a_schermo.Start()
    
    except NameError:
        pass

    if timer.getMinutes() == 0 and timer.getSeconds() <= 30:
        cam.screen_shake()
        timer.ChangeColor("Red")

def disegna():

    timer.Start()

    if GLOB.score_seconds:
        timer.AddSeconds(GLOB.score_seconds)
        
    GLOB.screen.fill(GLOB.Background_Color)

    cam.update()
    
    collisions.render_map((0,0))

    if not GLOB.PlayerIsHidden:
        player.update()

    if animazione.iFinished and GLOB.MonsterCanSpawn and animazione.iFinished and GLOB.MonsterSpawning and GLOB.Stanza == GLOB.MonsterActualRoom and GLOB.Piano == GLOB.MonsterActualFloor:
        mostro.update()

    collisions.render_objects((0,0))

    stanze.caricaStanza()

    if not GLOB.PlayerIsHidden:
        player.load_playerSurface()

    if animazione.iFinished and GLOB.MonsterCanSpawn and animazione.iFinished and GLOB.MonsterSpawning and GLOB.Stanza == GLOB.MonsterActualRoom and GLOB.Piano == GLOB.MonsterActualFloor:
        mostro.load_monsterSurface()
        
    collisions.render_walls((0,0))
    

    animazione.disegna()

    Stampa_messaggio()

    # MOSTRO LA GUI A SCHERMO
    Gui.show()

    # MOSTRO IL TIMER
    if not GLOB.Debug:
        timer.Show()

    if not GLOB.PlayerCanRun:
        SetPlayer_speed()


def enigma():
    global enigma_file
    
    try:
        enigma_file = pd.read_csv(GLOB.Default_path+'/'+GLOB.Piano+'/'+GLOB.Stanza+'/enigmi/Enigmi'+GLOB.Stanza+'.csv')
    except FileNotFoundError:
        enigma_file = pd.read_csv(GLOB.Default_path+'/1-PianoTerra/Fisica/enigmi/EnigmiFisica.csv')

    SetPlayer_speed()

def dialoghi():
    global df
    df = pd.read_csv('Dialoghi/dialogo.csv')

def Interazioni_DialoghiEnigmi():
    if GLOB.Dialogo:
        global df

        dialoghi()

        for row in range(len(df.values)):
            Racconto = Dialoghi(
                personaggio = df.values[row][0], 
                descrizione = df.values[row][1], 
                text_speed = 4
            )
            
            player.setAllkeys(False)
            player.finish()
            Racconto.stampa()
        GLOB.Dialogo = False


    if GLOB.Enigma:
        global enigma_file, Enigma

        enigma()

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
            text_speed = 4
                                        
        )
        player.setAllkeys(False)
        player.finish()
        Enigma.stampa()
        GLOB.Enigma = False
        player.evento = None


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
        global UP, DOWN, LEFT, RIGHT
        UP = event.key == pygame.K_w or event.key == pygame.K_UP
        DOWN = event.key == pygame.K_s or event.key == pygame.K_DOWN
        LEFT = event.key == pygame.K_a or event.key == pygame.K_LEFT
        RIGHT = event.key == pygame.K_d or event.key == pygame.K_RIGHT
        SHIFT = event.key == pygame.K_LSHIFT
        INTERACT = event.key == pygame.K_e

        getUp = player.getUpPress()
        getDown = player.getDownPress()
        getLeft = player.getLeftPress()
        getRight = player.getRightPress()

        condition_1 = getLeft and UP and not(getRight and getDown)
        condition_2 = getLeft and DOWN and not(getRight and getUp)
        condition_3 = getRight and UP and not(getLeft and getDown)
        condition_4 = getRight and DOWN and not(getLeft and getUp)
        
        GLOB.PlayerHasPressedButton = True

        if LEFT and not RIGHT and not(condition_1 and condition_2):
            GLOB.PlayerIsMoving = IsPressed
            
            player.setLeftPress(IsPressed)
            player.flag_delay = True

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Left"
            else:
                player.finish()
            
        elif RIGHT and not LEFT and not(condition_3 and condition_4):
            GLOB.PlayerIsMoving = IsPressed
            
            player.setRightPress(IsPressed)
            player.flag_delay = True

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Right"
            else:
                player.finish()

        elif UP and not DOWN and not(condition_1 and condition_3):
            GLOB.PlayerIsMoving = IsPressed
            
            player.setUpPress(IsPressed)
            player.flag_delay = True

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Up"
            else:
                player.finish()
            
        elif DOWN and not UP and not(condition_2 and condition_4):
            GLOB.PlayerIsMoving = IsPressed
            
            player.setDownPress(IsPressed)
            player.flag_delay = True

            if IsPressed:
                player.animate()
                player.Last_keyPressed = "Down"
            else:
                player.finish()

        elif SHIFT:
            
            if IsPressed and GLOB.PlayerCanRun:
                
                player.flag_delay = True

                GLOB.PlayerIsWalking = False
                GLOB.PlayerIsRunning = True

                player.setIsRunning(GLOB.PlayerCanRun)
                GLOB.Player_speed = GLOB.Player_speed * GLOB.PlayerRun_speed
            else:

                GLOB.PlayerIsWalking = True
                GLOB.PlayerIsRunning = False
                player.flag_delay = True

                player.setIsRunning(GLOB.PlayerCanRun)
                GLOB.Player_speed = GLOB.Player_default_speed
                
        elif INTERACT:
            GLOB.PlayerInteract = IsPressed
            
        else:
            GLOB.PlayerHasPressedButton = False
            

    # SETTO ENIGMI - DIALOGHI
    dialoghi()
    enigma()

    # print(df[df['Personaggi']])

    while run:
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                GLOB.KeyPressed = pygame.key.name(event.key)
            elif event.type == pygame.KEYUP:
                GLOB.KeyPressed = ""


            if event.type == pygame.QUIT:
                run = False

            if keys_pressed[pygame.K_ESCAPE]:
                if not animazione.flag_caricamento:
                   pausa()


            if event.type == pygame.KEYDOWN:

                if GLOB.Debug:
                    if event.key == pygame.K_z:
                        GLOB.ShowGrid = not GLOB.ShowGrid
                            
                    if event.key == pygame.K_x:
                        GLOB.PlayerIsHidden = not GLOB.PlayerIsHidden
                            
                    if event.key == pygame.K_m:
                        GLOB.MonsterSpawning = not GLOB.MonsterSpawning
                            
                            
                    if event.key == pygame.K_h:
                        MiniMap().update()
                        
                    if event.key == pygame.K_g:
                        
                        if GLOB.MonsterCanAttack:
                            GLOB.MonsterCanAttack = False
                            mostro.IAttacking = False
                            mostro.IseePlayer = False
                            mostro.aggr = False
                        else:
                            GLOB.MonsterCanAttack = True

                if event.key == pygame.K_TAB and animazione.iFinished and not animazione.flag_caricamento:
                    
                    GLOB.ShowInventory = not GLOB.ShowInventory
                    
                    if not GLOB.ShowInventory:
                        Gui.inventory_sound.play()
                        
                if event.key == pygame.K_i and animazione.iFinished and not animazione.flag_caricamento:
                    if not GLOB.ShowComand:
                        GLOB.ShowComand = True

            if keys_pressed[pygame.K_F3] and GLOB.OptionDebug:
                
                GLOB.Debug = not GLOB.Debug
                GLOB.Cam_visible = not GLOB.Cam_visible

                GLOB.ShowCodice = GLOB.Debug              
                ChangeDeltaTime(GLOB.Debug)

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
                if event.type == pygame.KEYUP:
                    key_pressed(event,False)
                    player.Last_keyPressed = "Null"


        controllo_condizioni()
        disegna()
        Interazioni_DialoghiEnigmi()

        # Debugging
        console.log()

        pygame.display.flip()
        clock.tick(GLOB.FPS)
    
    pygame.quit()
    sys.exit()

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
        
        
        if animazione.iFinished:
            cord1, cord2 = 190, 230
            
            SAVE_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, cord1*GLOB.MULT), 
                        text_input="SAVE GAME", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)
            
            SAVE_BUTTON.changeColor(MENU_MOUSE_POS)
            SAVE_BUTTON.update(GLOB.screen)
            
        else:
            cord1, cord2 = 0, 190
        
        QUIT_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, cord2*GLOB.MULT), 
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
                
            if animazione.iFinished:
                if event_pausa.type == pygame.MOUSEBUTTONDOWN and SAVE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    
                    chiavi = list(GLOB.inventario.keys())
                    
                    for i in range(len(chiavi)):
                        
                        try:
                            if not chiavi[i] in GLOB.Inventory_support[i][0]:
                                GLOB.Inventory_support[i] = ((chiavi[i], GLOB.inventario[chiavi[i]][1], GLOB.inventario[chiavi[i]][2]))
                                
                            if chiavi[i] in GLOB.Inventory_support[i][0] and GLOB.inventario[chiavi[i]][1] and not GLOB.Inventory_support[i][1]:
                                GLOB.Inventory_support[i] = ((chiavi[i], GLOB.inventario[chiavi[i]][1], GLOB.inventario[chiavi[i]][2]))
                        
                        except KeyError:
                            GLOB.Inventory_support[i] = ((chiavi[i], GLOB.inventario[chiavi[i]][1], GLOB.inventario[chiavi[i]][2]))
                        
                
                GLOB.TimerMin, GLOB.TimerSec = timer.getMinutes(), timer.getSeconds()
                GLOB.PlayerXSpawn, GLOB.PlayerYSpawn = player.x / GLOB.MULT, player.y / GLOB.MULT
                GLOB.CamXSpawn, GLOB.CamYSpawn = cam.x / GLOB.MULT, cam.y / GLOB.MULT
                GLOB.MonsterXSpawn, GLOB.MonsterYSpawn = mostro.x / GLOB.MULT, mostro.y / GLOB.MULT
                
                GLOB.MonsterHasSeenPlayer = mostro.IseePlayer
                GLOB.MonsterAggr = mostro.aggr
                GLOB.MonsterIsAttacking = mostro.IAttacking
                
                GLOB.SaveGame()

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



# -- JUMP SCARE --
def SetVideoToFalse():
    global VideoFinito, video
    VideoFinito = True
    video.close()

def jump_scare():
    global VideoFinito, video
    
    video = Video("video/Jumpscare.mp4")
    video.set_size((GLOB.screen_width, GLOB.screen_height))
    video.set_volume(0.4 * GLOB.AU)
    delay_video = Delay(video.duration -3, SetVideoToFalse)
    
    VideoFinito = False
    while not VideoFinito:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SetVideoToFalse()
                
        delay_video.Start()
        video.draw(GLOB.screen, (0, 0))
                
        clock.tick(GLOB.FPS)
        pygame.display.flip()

#Funzione GAME OVER
def game_over():
    
    mixer.music.fadeout(1000)
    sfondo = pygame.image.load("assets/gameover.png").convert()
    sfondo = pygame.transform.scale(sfondo, (sfondo.get_width() * GLOB.MULT, sfondo.get_height() * GLOB.MULT))
    
    if not os.path.exists("dati.txt"):
        GLOB.CaricaPartita = False
    else:
        GLOB.CaricaPartita = True


    jump_scare()

    restarta = False

    pygame.mouse.set_visible(True)
    
    global i, testo1, t1, z, testo2, t2, suono
    i = -1
    z = -1
    
    testo1 = "GAME"
    t1 = ""
    
    testo2 = "OVER"
    t2 = ""
    
    suono = mixer.Sound("suoni/char-sound.wav")
    suono.set_volume(0.02 * GLOB.AU)
    
    
    def stampa():
        global i, testo1, t1, z, testo2, t2, suono
        flag = False
        
        if i < len(testo1) - 1:
            i += 1
            t1 += testo1[i]
            flag = True
            
        if i == len(testo1) - 1:
            if z < len(testo2) - 1:
                z += 1
                t2 += testo2[z]
                flag = True
        
        if flag:
            suono.play()

    delay = Delay(0.4, stampa)

    while not restarta and VideoFinito:  

        delay.Infinite()
        

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
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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

    
        GAME_TEXT = get_font(size*int(GLOB.MULT)).render(t1, True, "Yellow")
        GAME_POS = (GLOB.screen_width/2 - GAME_TEXT.get_width()/2, GLOB.screen_height/3 - GAME_TEXT.get_height()/2 + distanza)

        CGAME_TEXT = get_font(size*int(GLOB.MULT)).render(t1, True, "Black")
        CGAME_POS = (GLOB.screen_width/2 - CGAME_TEXT.get_width()/2, GLOB.screen_height/3 - CGAME_TEXT.get_height()/2 + distanza + altezza)

        OVER_TEXT = get_font(size*int(GLOB.MULT)).render(t2, True, "Red")
        OVER_POS = (GLOB.screen_width/2 - OVER_TEXT.get_width()/2, GLOB.screen_height/3 - OVER_TEXT.get_height()/2 + distanza + distanza_riga)

        COVER_TEXT = get_font(size*int(GLOB.MULT)).render(t2, True, "Black")
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



#Funzione GAME WIN
def game_win():
    mixer.music.fadeout(1500)
    
    if os.path.exists("dati.txt"):
        GLOB.CaricaPartita = False
        GLOB.AlertSalva = False
        os.remove("dati.txt")
    
    sfondo = pygame.image.load("assets/victory.png").convert()
    sfondo = pygame.transform.scale(sfondo, (sfondo.get_width() * GLOB.MULT, sfondo.get_height() * GLOB.MULT))

    restarta = False

    pygame.mouse.set_visible(True)

    d = int(((timer.getMinutes() * 60 + timer.getSeconds()) * 1.6) + 0.1)

    var_win = 300 + d
    
    GLOB.score += var_win

    if int(GLOB.Record) < int(GLOB.score):

        GLOB.Record = GLOB.score
        
        os.system("attrib -h score.txt")

        with open('score.txt', 'w') as f:
            f.write("Record:\n")
            f.write(str(GLOB.Record))
            f.close()
            
        os.system("attrib +h score.txt")
            
    while not restarta:

        # Ottengo la posizione corrente del cursore del mouse
        MENU_MOUSE_POS = pygame.mouse.get_pos()


        distanza_riga = 30
        posy = 150


        PLAY_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, posy * GLOB.MULT), 
            text_input="RESTART", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)
        
        QUIT_BUTTON = Button(image=None, pos=(GLOB.screen_width/2, (posy + distanza_riga) * GLOB.MULT), 
                            text_input="BACK TO MENU", font=menu.get_font(8*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=2)

        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if keys_pressed[pygame.K_ESCAPE] or (event.type == pygame.MOUSEBUTTONDOWN and QUIT_BUTTON.checkForInput(MENU_MOUSE_POS)):
                GLOB.isGameRunning = False
                menu.main_menu()

            if keys_pressed[pygame.K_RETURN] or (event.type == pygame.MOUSEBUTTONDOWN and PLAY_BUTTON.checkForInput(MENU_MOUSE_POS)):
                pygame.mouse.set_visible(False)
                restarta = True
                inizializza()

        GLOB.screen.blit(sfondo, (0, 0))


        altezza = 5 * GLOB.MULT
        size = 20

        distanza = 40 * GLOB.MULT
        distanza_riga = 20 * GLOB.MULT

        starty = 25 * GLOB.MULT

        SCORE_TEXT = get_font(7*int(GLOB.MULT)).render("score: "+str(GLOB.score), True, "White")
        SCORE_POS = (GLOB.screen_width/2 - SCORE_TEXT.get_width()/2, starty + 90 * GLOB.MULT)

        RECORD_TEXT = get_font(7*int(GLOB.MULT)).render("record: "+str(GLOB.Record), True, "White")
        RECORD_POS = (GLOB.screen_width/2 - RECORD_TEXT.get_width()/2, starty + 100 * GLOB.MULT)

        GLOB.screen.blit(SCORE_TEXT, SCORE_POS)
        GLOB.screen.blit(RECORD_TEXT, RECORD_POS)

    
        GAME_TEXT = get_font(size*int(GLOB.MULT)).render("HAI", True, "White")
        GAME_POS = (GLOB.screen_width/2 - GAME_TEXT.get_width()/2, starty + distanza)

        CGAME_TEXT = get_font(size*int(GLOB.MULT)).render("HAI", True, "Black")
        CGAME_POS = (GLOB.screen_width/2 - CGAME_TEXT.get_width()/2, starty + distanza + altezza)

        OVER_TEXT = get_font(size*int(GLOB.MULT)).render("VINTO", True, "Gray")
        OVER_POS = (GLOB.screen_width/2 - OVER_TEXT.get_width()/2, starty + distanza + distanza_riga)

        COVER_TEXT = get_font(size*int(GLOB.MULT)).render("VINTO", True, "Black")
        COVER_POS = (GLOB.screen_width/2 - COVER_TEXT.get_width()/2, starty + distanza + distanza_riga + altezza)

        GLOB.screen.blit(CGAME_TEXT, CGAME_POS)
        GLOB.screen.blit(COVER_TEXT, COVER_POS)

        GLOB.screen.blit(GAME_TEXT, GAME_POS)
        GLOB.screen.blit(OVER_TEXT, OVER_POS)

		
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(GLOB.screen)


        clock.tick(GLOB.FPS)
        pygame.display.flip()



# se volessi importare il file non verrebbe autoeseguito automaticamente
if __name__ == "__main__":
    pygame.init()
    main()
