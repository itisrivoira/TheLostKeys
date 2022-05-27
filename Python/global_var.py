import pygame, os, random
from pygame.locals import *

TITLE = "The Lost Keys"

# Valori di proporzione

Delta_Time = 2 # Delta_Time (Congliabile 1/2)
Default_DeltaTime = Delta_Time

Player_proportion = 1 # Divisore della grandezza del giocatore

#FPS
FPS = 30 * Delta_Time

# rapporto di proporzione allo schermo NON INFERIORE AD 1
MULT = 4

# rapporto offset telecamera dello schermo MAX 40
Moff = 30

# rapporto audio del gioco
AU = 5

# rapporto musica del gioco
MU = 1

# Timer del gioco
Timer = 15

Scelta = 0
Cam_visible = False

OptionDebug = True
Debug = False
ShowGrid = False
ShowFps = True
ShowDropFrames = True
ShowScore = True
ShowRecord = True
LoadCollisions = True

Mappa = []

isGameRunning = False
isPaused = False
ShowInventory = False

KeyPressed = ""

Dialogo = False
Enigma = False

PlayerHasChangedRoom = False
MonsterHasChangedRoom = False

Fullscreen = True
Drop_Frames = False

Player_speed = 2 * MULT / Delta_Time
PlayerRun_speed = 3
PlayerReset = False

PlayerCanHide = True
PlayerIsHidden = False

# -- MOSTRO
MonsterCanSpawn = True
ShowMonsterRange = False
MonsterCanAttack = False


SecondDiffPos = 5

Player_default_speed = Player_speed

ShowComand = True

# Inizializzazione lista di animazione camminata
PlayerWalkingO = []
PlayerWalkingVD = []
PlayerWalkingVU = []

MonsterWO = []
MonsterWVD = []
MonsterWVU= []
MonsterAngry = []

# STATISTICHE
#  Chimica - Storia - Inglese - Fisica - Matematica - Informatica - Italiano - Sistemi - TPSIT

Senex_Evaluations = [ 8, 6, 7, 3, 6, 6, 5, 4, 10 ]
Seima_Evaluations = [ 8, 10, 8, 9, 10, 10, 8, 10, 10 ]
Aleks_Evaluations = [ 10, 10, 6, 2, 7, 8, 10, 7, 2 ]
Beppe_Evaluations = [ 2, 8, 4, 2, 6, 6, 5, 9, 7 ]
Dark_Evaluations = [ 8, 7, 9, 10, 8, 6, 7, 6, 2 ]

# Max = 13
# Senex_Stat = [ int(Max - (sum(Senex_Evaluations))/len(Senex_Evaluations)) ] + Senex_Evaluations
# Seima_Stat = [ int(Max - (sum(Seima_Evaluations))/len(Seima_Evaluations)) ] + Seima_Evaluations
# Aleks_Stat = [ int(Max - (sum(Aleks_Evaluations))/len(Aleks_Evaluations)) ] + Aleks_Evaluations
# Beppe_Stat = [ int(Max - (sum(Beppe_Evaluations))/len(Beppe_Evaluations)) ] + Beppe_Evaluations
# Dark_Stat = [ int(Max - (sum(Dark_Evaluations))/len(Dark_Evaluations)) ] + Dark_Evaluations

# Vel
Senex_Stat = [ 5 ] + Senex_Evaluations
Seima_Stat = [ 2 ] + Seima_Evaluations
Aleks_Stat = [ 5 ] + Aleks_Evaluations
Beppe_Stat = [ 6 ] + Beppe_Evaluations
Dark_Stat  = [ 3 ] + Dark_Evaluations

Stats = ( Senex_Stat, Seima_Stat, Aleks_Stat, Beppe_Stat, Dark_Stat )

#Background_Color = (12, 24, 36)
Background_Color = (0, 0, 0)

# Dimensione Schermo
DF_width = 480
DF_height = 270

screen_width = DF_width * MULT
screen_height = DF_height * MULT

flags = FULLSCREEN | DOUBLEBUF

# Configurazione Schermo
if Fullscreen:
    screen = pygame.display.set_mode((screen_width,screen_height), flags, 8)
else:
    screen = pygame.display.set_mode((screen_width,screen_height))


logo = pygame.image.load("assets/Logo.png").convert_alpha()
pygame.display.set_caption(TITLE)
pygame.display.set_icon(logo)

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
    Monster_speed = Player_default_speed - 0.8 * MULT / Delta_Time
    Monster_default_speed = Monster_speed
    MonsterRun_speed = PlayerRun_speed / 1.05

setCharacter()
setMonster()



def setResources():
    global score, score_seconds, tentativo, Record
    global inventario

    global codice, codice_archivio, ShowCodice

    global enigmi_da_risolvere, enigmi_risolti
    global chiavette, chiavetta_start, chiavetta_end
    global RandomKey, RandomRoom
    global oggetti, oggetti_start, oggetti_end

    global MonsterActualFloor, MonsterActualRoom
    
    global Default_Character, PlayerCanMove, PlayerCanRun, PLayerMovement, PlayerIsWalking, PlayerIsRunning, PlayerCanCollect
    global Piano, Stanza, Default_Map, Default_object, Default_collisions

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
        
        os.system("attrib +h score.txt")
        
    with open('score.txt', 'r') as f:
        f_contest = f.readlines()
        Record = f_contest[1]
    f.close()

    # --- ENIGMI ---

    tentativo = {}
    enigmi_da_risolvere = ["Fisica", "1A", "WC-Femmine", "AulaMagna", "AulaProfessori", "LabInfo", "4A", "AulaVideo", "LabInformatica", "Ripostiglio", "1D", "Corridoio", "Chimica", "Archivio"]
    enigmi_risolti = []

    # --- INVENTARIO ---


        # CHIAVETTE

    chiavette = {}
    chiavetta_start = 140
    molt_chiavetta = 2


    lista_chiavette = [4, 2, 5, 7, 8, 9, 11, 12]
    RandomKey = "chiavetta-"+str(random.choice(lista_chiavette))
    print("Chiavetta Random:",RandomKey)


    for i in enigmi_da_risolvere:
        tentativo[i] = 0
        
        if enigmi_da_risolvere.index(i)+1 <= 12:
            immagine = pygame.image.load("Collectibles/chiavetta-"+str(enigmi_da_risolvere.index(i) + 1)+".png").convert_alpha()
            immagine = pygame.transform.scale(immagine, (immagine.get_width() * MULT * molt_chiavetta, immagine.get_height() * MULT * molt_chiavetta))
            chiavette[i] = (chiavetta_start, True, immagine)
            chiavetta_start += 1
            chiavetta_end = chiavetta_start
            
            if "chiavetta-"+str(enigmi_da_risolvere.index(i) + 1) == RandomKey:
                RandomRoom = i
                
            # print( "| "+str(i)+": " +str(chiavette[i][0])+" - "+str(chiavette[i][1])+ "| - chiavetta-"+str(enigmi_da_risolvere.index(i) + 1))

    chiavetta_start = 140

    



        # OGGETTI

    oggetti = {}
    oggetti_start = 154
    molt_oggetto = 2
    oggetti_end = 3

    for i in range(oggetti_end):
        immagine = pygame.image.load("Collectibles/oggetto-"+str(i)+".png").convert_alpha()
        immagine = pygame.transform.scale(immagine, (immagine.get_width() * MULT * molt_oggetto, immagine.get_height() * MULT * molt_oggetto))
        oggetti[i] = (oggetti_start, True, immagine)
        oggetti_start += 1
        # print( "| "+str(i)+": " +str(oggetti[i][0])+" - "+str(oggetti[i][1])+ "| ")

    oggetti_start = 154
    oggetti_end = oggetti_start + oggetti_end

    PlayerCanCollect = False


    inventario = {}
    Default_Character = 'Characters/Senex/WalkOrizontal/Walk0.png'

    Piano = "1-PianoTerra"
    Stanza = "Corridoio"
    Default_Map = '../MappaGioco/Tileset/Stanze/1-PianoTerra/Corridoio/png/Corridoio.png'
    Default_object = '../MappaGioco/Tileset/Stanze/1-PianoTerra/Corridoio/png/CorridoioOggetti.png'
    Default_collisions = 'Corridoio_Collisioni.csv'

    PlayerCanMove = True
    PlayerCanRun = True

    PlayerIsWalking = True
    PlayerIsRunning = False

    PLayerMovement = {
            
    "up": False, 
    "down": False, 
    "left": False, 
    "right": False, 
            
    }
    
    MonsterActualRoom = Stanza
    MonsterActualFloor = Piano

setResources()