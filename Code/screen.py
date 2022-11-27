from __modules__ import *

TITLE = "The Lost Keys"

# Valori di proporzione

MoltTime = 2 # MoltTime (Congliabile 1/2)
Default_MoltTime = MoltTime

Player_proportion = 1 # Divisore della grandezza del giocatore

#FPS
FPS = 30

# rapporto di proporzione allo schermo NON INFERIORE AD 1
MULT = 2

# Dimensione Schermo

Num_resolutions = 4


py.init()
DF_width = py.display.Info().current_w // Num_resolutions
DF_height = py.display.Info().current_h // Num_resolutions

DEF = GameManager (
   
               window_resolution = (DF_width, DF_height),
               fps = FPS,
               screen_molt = MULT,
               time_molt = MoltTime

               )


Background_Color = "#0c0c51"

logo = py.image.load("../Assets/Logo/Logo.png").convert_alpha()
py.display.set_caption(TITLE)
py.display.set_icon(logo)


# rapporto offset telecamera dello schermo MAX 40
Moff = 30