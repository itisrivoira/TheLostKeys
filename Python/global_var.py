import pygame
TITLE = "The Lost Keys"

# Valori di proporzione

Delta_Time = 2 # Delta_Time (Congliabile 1/2)
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
Timer = 5

Scelta = 0
Cam_visible = False

Debug = False
ShowGrid = False
ShowFps = True
ShowDropFrames = True

isGameRunning = False
isPaused = False

KeyPressed = ""

Dialogo = False
Enigma = False

Drop_Frames = False

Player_speed = 2 * MULT
PlayerRun_speed = 3 * MULT

Player_default_speed = Player_speed

# Inizializzazione lista di animazione camminata
PlayerWalkingO = []
PlayerWalkingVD = []
PlayerWalkingVU = []

# STATISTICHE
# Vel - Chimica - Storia - Inglese - Fisica - Matematica - Informatica - Italiano - Sistemi - TPSIT
Senex_Stat = [ 5, 8, 6, 7, 3, 6, 6, 5, 4, 10 ]
Seima_Stat = [ 2, 8, 10, 8, 9, 10, 10, 8, 10, 10 ]
Aleks_Stat = [ 5, 10, 10, 6, 2, 7, 8, 10, 7, 2 ]
Beppe_Stat = [ 6, 2, 8, 4, 2, 6, 6, 5, 9, 7 ]
Dark_Stat = [ 3, 8, 7, 9, 10, 8, 6, 7, 6, 2 ]

Stats = ( Senex_Stat, Seima_Stat, Aleks_Stat, Beppe_Stat, Dark_Stat )

#Background_Color = (12, 24, 36)
Background_Color = (0, 0, 0)

# Dimensione Schermo
DF_width = 480
DF_height = 270

screen_width = DF_width * MULT
screen_height = DF_height * MULT

# Configurazione Schermo
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(TITLE)


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


setCharacter()

ShowScore = True
def setResources():
    global score, score_seconds, tentativo, enigmi_da_risolvere, enigmi_risolti, chiavette, inventario
    global Default_Character, Piano, Stanza, Default_Map, Default_object, PlayerCanMove, PlayerCanRun, PlayerIsWalking, PlayerIsRunning

    # --- SCORE ---
    score = 0
    score_seconds = 0

    # --- ENIGMI ---

    tentativo = {}
    enigmi_da_risolvere = ["WC-Femmine", "Fisica", "1A", "AulaMagna", "AulaProfessori", "4A", "LabInformatica"]
    enigmi_risolti = []

    for i in enigmi_da_risolvere:
        tentativo[i] = 0


    # --- INVENTARIO ---

    chiavette = ["Chimica", "Storia", "Inglese", "Fisica", "Matematica", "Informatica", "Italiano", "Sistemi", "TPSIT"]
    inventario = []


    Default_Character = 'Characters/Senex/WalkOrizontal/Walk0.png'

    Piano = "1-PianoTerra"
    Stanza = "Corridoio"
    Default_Map = '../MappaGioco/Tileset/Stanze/1-PianoTerra/Corridoio/png/Corridoio.png'
    Default_object = '../MappaGioco/Tileset/Stanze/1-PianoTerra/Corridoio/png/CorridoioOggetti.png'

    PlayerCanMove = True
    PlayerCanRun = True

    PlayerIsWalking = True
    PlayerIsRunning = False

setResources()