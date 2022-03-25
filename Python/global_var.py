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
Moff = 40

# rapporto audio del gioco
AU = 5

# rapporto musica del gioco
MU = 5

Scelta = 0
Cam_visible = False

Debug = False

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

Background_Color = (12, 24, 36)

# Dimensione Schermo
DF_width = 480
DF_height = 270

screen_width = DF_width * MULT
screen_height = DF_height * MULT

# Configurazione Schermo
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(TITLE)