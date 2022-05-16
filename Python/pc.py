import random
import pygame, sys, os
import global_var as GLOB
from components import Pc

pygame.init()

FPS = 30
clock = pygame.time.Clock()

def get_font(size):
    return pygame.font.Font("font/retro.ttf", size)


chiavette = list(GLOB.chiavette.values())

# c = 10
# for elemento in chiavette:
#     b = "chiavetta-"+str(c + 1)
#     GLOB.inventario[b] = (GLOB.chiavette[GLOB.enigmi_da_risolvere[c]][2], False, "- Ciaooo -")
    
#     c -= 1

c = "chiavetta-1"
GLOB.inventario[c] = (GLOB.chiavette[GLOB.enigmi_da_risolvere[0]][2], False, "- Ciaooo -")

c = "chiavetta-2"
GLOB.inventario[c] = (GLOB.chiavette[GLOB.enigmi_da_risolvere[1]][2], False, "- Ciaooo -")

c = "chiavetta-8"
GLOB.inventario[c] = (GLOB.chiavette[GLOB.enigmi_da_risolvere[7]][2], False, "- Ciaooo -")

c = "chiavetta-7"
GLOB.inventario[c] = (GLOB.chiavette[GLOB.enigmi_da_risolvere[6]][2], False, "- Ciaooo -")

pc = Pc()
pc.show()
