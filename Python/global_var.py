import pygame, os, sys, random, ast

TITLE = "The Lost Keys"

# Valori di proporzione

Delta_Time = 2 # Delta_Time (Congliabile 1/2)
Default_DeltaTime = Delta_Time

Player_proportion = 1 # Divisore della grandezza del giocatore

#FPS
FPS = 30 * Delta_Time

# rapporto di proporzione allo schermo NON INFERIORE AD 1
MULT = 2
DF_MULT = MULT

# rapporto offset telecamera dello schermo MAX 40
Moff = 30

# rapporto audio del gioco
AU = 5

# rapporto musica del gioco
MU = 2

CaricaPartita = True

Scelta = 0
Cam_visible = False

OptionDebug = True
Debug = False
ShowGrid = False
ShowFps = True
ShowDropFrames = False
ShowScore = True
ShowRecord = True
LoadCollisions = True

Mappa = []

isGameRunning = False
isPaused = False
ShowInventory = False

KeyPressed = ""
PlayerHasPressedButton = False

Dialogo = False
Enigma = False
ImInEnigmaMode = False

PlayerHasChangedRoom = False
MonsterHasChangedRoom = False

Performance = False

if Delta_Time <= 1:
    Performance = False
else:
    Performance = True

Drop_Frames = False

Accurate_Velocity = False
Player_speed = 2 * MULT / Delta_Time
PlayerRun_speed = 3
PlayerReset = False

PlayerContRoom = 0
MonsterContRoom = 0

# -- MOSTRO
MonsterCanSpawn = True
ShowMonsterRange = False
MonsterCanAttack = True


SecondDiffPos = 10
CounterChecker = 0
FlagSecRand = True
Val_sec = 59

Player_default_speed = Player_speed

ShowComand = False

# Inizializzazione lista di animazione camminata
PlayerWalkingO = []
PlayerWalkingVD = []
PlayerWalkingVU = []
PlayerIdle = []

MonsterWO = []
MonsterWVD = []
MonsterWVU = []
MonsterAngry = []
MonsterIdle = []

# STATISTICHE
#  Chimica - Storia - Inglese - Fisica - Matematica - Informatica - Italiano - Sistemi - TPSIT
Senex_Evaluations = [  8,  6,  7,  3,  6,  6,  5,  4, 10 ]
Seima_Evaluations = [  8, 10,  8,  9, 10, 10,  8, 10, 10 ]
Aleks_Evaluations = [ 10, 10,  6,  2,  7,  8, 10,  7,  2 ]
Beppe_Evaluations = [  2,  8,  4,  2,  6,  6,  5,  9,  7 ]
Dark_Evaluations  = [  8,  7,  9, 10,  8,  6,  7,  6,  2 ]

# Vel
Senex_Stat = [ 6 ] + Senex_Evaluations
Seima_Stat = [ 2 ] + Seima_Evaluations
Aleks_Stat = [ 5 ] + Aleks_Evaluations
Beppe_Stat = [ 7 ] + Beppe_Evaluations
Dark_Stat  = [ 3 ] + Dark_Evaluations

if Accurate_Velocity:
    Max = 13
    Senex_Stat = [ int(Max - (sum(Senex_Evaluations))/len(Senex_Evaluations)) ] + Senex_Evaluations
    Seima_Stat = [ int(Max - (sum(Seima_Evaluations))/len(Seima_Evaluations)) ] + Seima_Evaluations
    Aleks_Stat = [ int(Max - (sum(Aleks_Evaluations))/len(Aleks_Evaluations)) ] + Aleks_Evaluations
    Beppe_Stat = [ int(Max - (sum(Beppe_Evaluations))/len(Beppe_Evaluations)) ] + Beppe_Evaluations
    Dark_Stat =  [ int(Max - (sum(Dark_Evaluations))/len(Dark_Evaluations))   ] + Dark_Evaluations

Stats = ( Senex_Stat, Seima_Stat, Aleks_Stat, Beppe_Stat, Dark_Stat )

#Background_Color = (12, 24, 36)
Background_Color = (0, 0, 0)

# Dimensione Schermo
pygame.init()
Fullscreen = False

MAX_width = pygame.display.Info().current_w
MAX_height = pygame.display.Info().current_h

DF_width = MAX_width // 4
DF_height = MAX_height // 4


MULT_INCREMENT = (1920 / MAX_width + 1080 / MAX_height)/2

MULT *= MULT_INCREMENT
print(MULT)
RESOLUTION = DF_MULT

screen_width = DF_width * RESOLUTION
screen_height = DF_height * RESOLUTION

# Configurazione Schermo

def Quit():
    pygame.quit()
    sys.exit()

def setScreenSize(wh, flag = None):
    global screen, Fullscreen
    
    pos_x = MAX_width / 2 - screen_width / 2
    pos_y = MAX_height / 2 - screen_height / 2
    
    if MULT == 4 or Fullscreen:
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (0,0)
    else:
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (pos_x,pos_y)
    
    if flag != None:
        screen = pygame.display.set_mode(wh, flag)
    else:
        screen = pygame.display.set_mode(wh)

setScreenSize((screen_width, screen_height))

logo = pygame.image.load("assets/Logo.png").convert_alpha()
pygame.display.set_caption(TITLE)
pygame.display.set_icon(logo)

playbutton = False


if not os.path.exists("dati.txt"):
    AlertSalva = False
else:
    AlertSalva = True
    
Default_path = 'Stanze'

def setFPS():
    global Delta_Time, Default_DeltaTime, FPS, Performance
    
    if Performance:
        Delta_Time = 2
    else:
        Delta_Time = 1
        
    FPS = 30 * Delta_Time
    Default_DeltaTime = Delta_Time

def setCharacter():
    global Player_speed, Player_default_speed, PlayerRun_speed, scelta_char, scelta_rep
    Player_speed = 2 * MULT / Delta_Time / Player_proportion
    Player_default_speed = Player_speed

    if Scelta==1:
        scelta_char = "Seima"
        PlayerRun_speed = 1 + Seima_Stat[0]/10
    elif Scelta==2:
        scelta_char="Aleks"
        PlayerRun_speed = 1 + Aleks_Stat[0]/10
    elif Scelta==3:
        scelta_char="Beppe"
        PlayerRun_speed = 1 + Beppe_Stat[0]/10
    elif Scelta==4:
        scelta_char="Dark Angel"
        PlayerRun_speed = 1 + Dark_Stat[0]/10
    else:
        # SceltaG è il percorso dove si trovano i sprite per le animazioni
        scelta_char="Senex"

        # In base alla statistica della velolità del giocatore vado ad impostrare la velocità corrente che deve avere il player nel gioco
        PlayerRun_speed = 1 + Senex_Stat[0]/10

    scelta_rep = "/" + scelta_char


def setMonster():
    global Monster_speed, MonsterRun_speed, Monster_default_speed
    # -- MOSTRO
    Monster_speed = Player_default_speed - 0.75 * MULT / Delta_Time
    Monster_default_speed = Monster_speed
    MonsterRun_speed = PlayerRun_speed

setFPS()
setCharacter()
setMonster()


def setResources():
    global score, score_seconds, tentativo, Record
    global inventario, Inventory_support

    global codice, codice_archivio, ShowCodice

    global enigmi_da_risolvere, enigmi_risolti
    global chiavette, chiavetta_start, chiavetta_end
    global RandomKey, RandomRoom
    global oggetti, oggetti_start, oggetti_end

    global MonsterActualFloor, MonsterActualRoom, MonsterSpawning, MonsterIntro, MonsterCanChangeRoom
    global MonsterHasSeenPlayer, MonsterAggr, MonsterIsAttacking
    
    global Default_Character, PlayerCanInteract, PlayerInteract, PlayerTextInteract, PlayerCanMove, PlayerCanRun, PlayerCanHide, PlayerIsHidden, PlayerIsMoving, PLayerMovement, PlayerIsWalking, PlayerIsRunning, PlayerCanCollect
    global Piano, Stanza, Default_path, Default_Map, Default_object, Default_walls, Default_collisions
    
    global stanze_da_visitare, stanze_visitate
    
    global TimerMin, TimerSec
    global PlayerXSpawn, PlayerYSpawn
    global CamXSpawn, CamYSpawn, CamPosX, CamPosY
    global MonsterXSpawn, MonsterYSpawn
    
    global Mappa_Immagine, Muri_Immagine, Oggetti_Immagine
    
    global ShowIntro

    # -- CODICI ---
    
    codice_archivio = False
    
    value_cod_max = 9999
    codice = str(random.randint(0, value_cod_max))
    
    l = "0"
    z = len(str(value_cod_max)) - len(codice)


    for i in range(z):
        codice = l + str(codice)
        
        
        
    ShowCodice = False

    # --- SCORE ---

    score = 0
    score_seconds = 0

    # Apri il file in modalita lettura
    if not os.path.exists("score.txt"):
        with open('score.txt', 'w') as f:
            f.write("Record:\n0")
        f.close()
        
    with open('score.txt', 'r') as f:
        f_contest = f.readlines()
        Record = f_contest[1]
    f.close()

    # --- ENIGMI ---

    tentativo = {}
    enigmi_da_risolvere = ["Fisica", "1A", "WC-Femmine", "AulaMagna", "AulaProfessori", "LabInfo", "4A", "AulaVideo", "LabInformatica", "Ripostiglio", "1D", "Corridoio3", "Chimica", "Archivio"]
    enigmi_risolti = []

    # --- INVENTARIO ---


    # CHIAVETTE

    chiavette = {}
    chiavetta_start = 140
    molt_chiavetta = 2


    lista_chiavette = [4, 2, 5, 7, 8, 9, 11, 12]
    RandomKey = "chiavetta-" + str(random.choice(lista_chiavette))
    # print("Chiavetta Random:",RandomKey)


    for i in enigmi_da_risolvere:
        tentativo[i] = 0
        
        if enigmi_da_risolvere.index(i)+1 <= 12:
            immagine = pygame.image.load("Collectibles/chiavetta-" + str(enigmi_da_risolvere.index(i) + 1)+".png").convert_alpha()
            immagine = pygame.transform.scale(immagine, (immagine.get_width() * MULT * molt_chiavetta, immagine.get_height() * MULT * molt_chiavetta))
            chiavette[i] = (chiavetta_start, True, immagine, (enigmi_da_risolvere.index(i) + 1))
            chiavetta_start += 1
            chiavetta_end = chiavetta_start
            
            if "chiavetta-" + str(enigmi_da_risolvere.index(i) + 1) == RandomKey:
                RandomRoom = i
                
            # print( "| " + str(i)+": "  + str(chiavette[i][0])+" - " + str(chiavette[i][1])+ "| - chiavetta-" + str(enigmi_da_risolvere.index(i) + 1))

    chiavetta_start = 140

    #  -- STANZE --
    
    stanze_da_visitare = ["Chimica", "Fisica", "Archivio", "1A", "1D", "AulaMagna", "AulaProfessori", "LabInfo", "WC-Femmine", "WC-Maschi", "4A", "AulaVideo", "LabInformatica", "Ripostiglio"]
    stanze_visitate = []



    # OGGETTI

    oggetti = {}
    oggetti_start = 154
    molt_oggetto = 2
    oggetti_end = 4

    for i in range(oggetti_end):
        immagine = pygame.image.load("Collectibles/oggetto-" + str(i)+".png").convert_alpha()
        immagine = pygame.transform.scale(immagine, (immagine.get_width() * MULT * molt_oggetto, immagine.get_height() * MULT * molt_oggetto))
        oggetti[i] = (oggetti_start, True, immagine)
        oggetti_start += 1
        # print( "| " + str(i)+": "  + str(oggetti[i][0])+" - " + str(oggetti[i][1])+ "| ")

    oggetti_start = 154
    oggetti_end = oggetti_start + oggetti_end

    PlayerCanCollect = False


    inventario = {}
    Inventory_support = {}
        
    Default_Character = 'Characters/Senex/WalkOrizontal/Walk0.png'

    Piano = "1-PianoTerra"
    Stanza = "Corridoio1"
    Default_Map = Default_path + '/1-PianoTerra/Corridoio1/png/Corridoio.png'
    Default_object = None
    Default_walls = Default_path + '/1-PianoTerra/Corridoio1/png/CorridoioMuri.png'
    Default_collisions = 'Corridoio_Collisioni.csv'

    PlayerCanMove = True
    PlayerCanRun = True
    PlayerCanHide = True
    PlayerIsHidden = False
    PlayerInteract = False
    PlayerCanInteract = False
    PlayerTextInteract = "Interagisci"

    PlayerIsWalking = True
    PlayerIsRunning = False
    PlayerIsMoving = False

    PLayerMovement = {
            
    "up": False, 
    "down": False, 
    "left": False, 
    "right": False, 
            
    }
    
    ShowIntro = True
    
    MonsterActualFloor = "1-PianoTerra"
    MonsterActualRoom = "Corridoio1"
    MonsterSpawning = False
    MonsterIntro = True
    MonsterCanChangeRoom = False
    
    MonsterHasSeenPlayer = False
    MonsterAggr = False
    MonsterIsAttacking = False
    
    TimerMin, TimerSec = 15, 0
    PlayerXSpawn, PlayerYSpawn = 200 * MULT, 100 * MULT
    CamXSpawn, CamYSpawn = 130 * MULT, -167 * MULT
    MonsterXSpawn, MonsterYSpawn = 160 * MULT, 120 * MULT
    
    CamPosX = 0
    CamPosY = 0

    Mappa_Immagine = None
    Oggetti_Immagine = None
    Muri_Immagine = None

setResources()


def SaveGame():
    global AlertSalva
    
    # Apri il file in modalita lettura
    if not os.path.exists("dati.txt"):
        with open('dati.txt', 'w') as f:
            AlertSalva = True
            f.write("")
    
    with open('dati.txt', 'w') as f:
        f.write("""
            
--- DATI SALVATI ---
    - Giocatore:
        Giocatore Piano = |""" + str(Piano) + """|
        Giocatore Stanza = |""" + str(Stanza) + """|
        Default_Map = |""" + str(Default_Map) + """|
        Default_object = |""" + str(Default_object) + """|
        Default_walls = |""" + str(Default_walls) + """|
        Default_collisions = |""" + str(Default_collisions) + """|
        Enigmi da risolvere = |""" + str(enigmi_da_risolvere) + """|
        Enigmi risolti = |""" + str(enigmi_risolti) + """|
        Stanze da visitare = |""" + str(stanze_da_visitare) + """|
        Stanze visitate = |""" + str(stanze_visitate) + """|
        Inventario = |""" + str(Inventory_support) + """|
        Scelta = |""" + str(Scelta) + """|
        Giocatore X = |""" + str(PlayerXSpawn) + """|
        Giocatore Y = |""" + str(PlayerYSpawn) + """|
    
    - Camera:
        Camera X = |""" + str(CamXSpawn) + """|
        Camera Y = |""" + str(CamYSpawn) + """|
    
    - Mostro:
        Mostro Piano = |""" + str(MonsterActualFloor) + """|
        Mostro Stanza = |""" + str(MonsterActualRoom) + """|
        Mostro isSpawned = |""" + str(MonsterSpawning) + """|
        Mostro HasSeenPlayer = |""" + str(MonsterHasSeenPlayer) + """|
        Mostro Aggr = |""" + str(MonsterAggr) + """|
        Mostro IsAttacking = |""" + str(MonsterIsAttacking) + """|
        Mostro X = |""" + str(MonsterXSpawn) + """|
        Mostro Y = |""" + str(MonsterYSpawn) + """|
        
        
    - Timer:
        Minuti = |""" + str(TimerMin) + """|
        Secondi = |""" + str(TimerSec if TimerSec <= 59 else 59) + """|
        
    - Score:
        ActualScore = |""" + str(score) + """|
        ShowCodice = |""" + str(ShowCodice) + """|
        
    - Comands:
        ShowIntro = |""" + str(ShowIntro) + """|
        MonsterIntro = |""" + str(MonsterIntro) + """|
        
    - USB Keys:
       RandomKey = |""" + str(RandomKey) + """|
                    
            """)
        
        f.close()
    
def LoadGame(flag):
    global score, score_seconds, tentativo, Record
    global inventario, Inventory_support

    global codice, codice_archivio, ShowCodice

    global enigmi_da_risolvere, enigmi_risolti
    global chiavette, chiavetta_start, chiavetta_end
    global RandomKey, RandomRoom
    global oggetti, oggetti_start, oggetti_end

    global MonsterActualFloor, MonsterActualRoom, MonsterSpawning, MonsterIntro, MonsterCanChangeRoom
    global MonsterHasSeenPlayer, MonsterAggr, MonsterIsAttacking
    
    global Default_Character, PlayerCanInteract, PlayerInteract, PlayerTextInteract, PlayerCanMove, PlayerCanRun, PlayerCanHide, PlayerIsHidden, PlayerIsMoving, PLayerMovement, PlayerIsWalking, PlayerIsRunning, PlayerCanCollect
    global Piano, Stanza, Default_Map, Default_object, Default_walls, Default_collisions
    
    global stanze_da_visitare, stanze_visitate
    
    global TimerMin, TimerSec
    global PlayerXSpawn, PlayerYSpawn
    global CamXSpawn, CamYSpawn
    global MonsterXSpawn, MonsterYSpawn
    
    global Scelta, ShowIntro
    
    if flag and os.path.exists("dati.txt"):
        
        
        with open('dati.txt', 'r') as f:
            f_contest = f.readlines()
            
            
            def cont(v):
                g = f_contest[v].split("=")[1]
                g = "".join(g)
                return g.split("|")[1]
            
            
            Piano, Stanza = cont(4), cont(5)
            Default_Map, Default_object, Default_walls, Default_collisions = cont(6), cont(7), cont(8), cont(9)
            enigmi_da_risolvere, enigmi_risolti = ast.literal_eval(cont(10)), ast.literal_eval(cont(11))
            stanze_da_visitare = ast.literal_eval(cont(12))
            stanze_visitate = ast.literal_eval(cont(13))
            
            Inventory_support = ast.literal_eval(cont(14))
            
            j = 0
            for i in range(len(Inventory_support)):
                
                if "chiavetta" in Inventory_support[i][0]:
                    molt_oggetto = 2
                    immagine = pygame.image.load("./Collectibles/"+ str(Inventory_support[i][0]) + ".png").convert_alpha()
                    immagine = pygame.transform.scale(immagine, (immagine.get_width() * MULT * molt_oggetto, immagine.get_height() * MULT * molt_oggetto))
                    inventario[Inventory_support[i][0]] = (immagine, Inventory_support[i][1], Inventory_support[i][2])
                
                else:
                    tipo = 0
                    if "Ghiaccio" in Inventory_support[i][0]:
                        tipo = 0
                    elif "Libro" in Inventory_support[i][0]:
                        tipo = 1
                    elif "Chiave" in Inventory_support[i][0]:
                        tipo = 3
                    
                    inventario[Inventory_support[i][0]] = (oggetti[tipo][2], Inventory_support[i][1], Inventory_support[i][2])

            
            
            Scelta = int(cont(15))
            PlayerXSpawn, PlayerYSpawn = float(cont(16)) * MULT, float(cont(17)) * MULT
            
            CamXSpawn, CamYSpawn = float(cont(20)) * MULT, float(cont(21)) * MULT
            
            MonsterActualFloor, MonsterActualRoom = cont(24), cont(25)
            MonsterSpawning, MonsterHasSeenPlayer, MonsterAggr, MonsterIsAttacking = ast.literal_eval(cont(26)), ast.literal_eval(cont(27)), ast.literal_eval(cont(28)), ast.literal_eval(cont(29))
            MonsterXSpawn, MonsterYSpawn = float(cont(30)) * MULT, float(cont(31)) * MULT
            
            TimerMin, TimerSec = int(cont(35)), float(cont(36)) if float(cont(36)) <= 59 else 59
            
            score = int(cont(39))
            ShowCodice = ast.literal_eval(cont(40))
            
            ShowIntro = ast.literal_eval(cont(43))
            MonsterIntro = ast.literal_eval(cont(44))
            
            RandomKey = cont(47)
            
        f.close()