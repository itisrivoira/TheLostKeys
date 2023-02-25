import pygame, sys
from pygame import mixer
import global_var as GLOB
from components import Delay
import main


class Transizione():
    def __init__(self, vel):
        self.flag_changeBg = True 
        self.UpdateBackground()
        self.__character = GLOB.Default_Character

        self.__vel = vel
        self.__delay = Delay(sec = self.__vel, event = self.sgrana)
        self.superficie = pygame.surface.Surface((GLOB.screen_width, GLOB.screen_height)).convert()
        self.superficie.fill((0,0,0))        
        
        self.schermo = pygame.surface.Surface((GLOB.screen_width, GLOB.screen_height)).convert()
        self.schermo.fill((0,0,0))
        
        self.val_scurisci = 300
        self.val_sgrana = 1
        self.val_caricamento = 0

        self.flag_reverse = False
        self.flag_sgrana = False
        self.iFinished = False

        self.flag_caricamento = True
        self.__loadImagesANDconvert()
        
        self.flag_room = False
        
        self.setDelay()
        
        GLOB.LoadCollisions = True
        
        
    def setDelay(self):
        if not self.flag_room:
            self.delay_monsterRoom = Delay(GLOB.SecondDiffPos, self.ChangeRoom)
            self.delay_monsterRoom.ReStart()
        
    def ChangeRoom(self):
        if self.flag_room:
            GLOB.PlayerHasChangedRoom = True
            self.flag_room = False
            self.delay_monsterRoom.ReStart()
        
        # -- MONSTER ROOMS MANAGER BEHAVIOUR --
        if main.mostro.IseePlayer and GLOB.MonsterCanSpawn and GLOB.MonsterSpawning and GLOB.MonsterCanChangeRoom and GLOB.Stanza != GLOB.MonsterActualRoom:
            
            if not main.mostro.aggr and main.mostro.IseePlayer:
                GLOB.SecondDiffPos = round((GLOB.SecondDiffPos + 2), 2)
                main.mostro.aggr = True
            
            if main.mostro.aggr and GLOB.PlayerHasChangedRoom and GLOB.SecondDiffPos < 12:            
                testo = "Default - Move"
                if GLOB.Piano == GLOB.MonsterActualFloor and not GLOB.Stanza[:-1] in GLOB.MonsterActualRoom:
                    testo = "Ti inseguo"
                    main.mostro.aggr = True
                    main.mostro.IAttacking = True

                    if GLOB.PlayerIsHidden or (not GLOB.Torcia and not GLOB.corrente):
                        main.mostro.character_update(0)
                        
                    if GLOB.Stanza == "Segreteria":
                        main.stanze.setToDefault()
                        main.stanze.dizionario_flag["Segreteria"] = True
                        main.stanze.caricaStanza()
                        main.stanze.CaricaElementi()
                
                if ((GLOB.MonsterActualFloor == "1-PianoTerra" and GLOB.Piano == "3-SecondoPiano") or GLOB.Piano == "1-PianoTerra" and GLOB.MonsterActualFloor == "3-SecondoPiano") or (
                    not GLOB.Stanza[:-1] in GLOB.MonsterActualRoom and GLOB.MonsterActualFloor != GLOB.Piano) or (
                    (not "Corridoio" in GLOB.MonsterActualRoom and not "Corridoio" in GLOB.Stanza) and (
                    not "Segreteria" in GLOB.MonsterActualRoom and not "Segreteria" in GLOB.Stanza) and GLOB.MonsterActualFloor == GLOB.Piano):
                    
                    testo = "Perso di vista"
                    GLOB.MonsterHasChangedRoom = True
                    main.mostro.IseePlayer = False
                    main.mostro.aggr = False
                    main.mostro.IAttacking = False
                    
                    door_sound = mixer.Sound("suoni/door.wav")
                    door_sound.set_volume(0.05 * GLOB.AU)
                    
                    if ((GLOB.MonsterActualFloor == "1-PianoTerra" and GLOB.Piano == "3-SecondoPiano") or 
                        (GLOB.Piano == "1-PianoTerra" and GLOB.MonsterActualFloor == "3-SecondoPiano")):
                        GLOB.MonsterActualFloor = "2-PrimoPiano"
                    else:
                        GLOB.MonsterActualFloor = GLOB.Piano
                        door_sound.play()
                    
                    GLOB.MonsterActualRoom = "Default"
                    main.mostro.character_update(0)
                
                elif main.mostro.IseePlayer:
                    testo = "Ho visto giocatore spawn porta"
                    
                    var1 = main.stanze.pos_portaP
                    var2 = main.stanze.pos_portaC
                    
                    if "Segreteria" in GLOB.Stanza and "Generatore" in GLOB.MonsterActualRoom:
                        var1 = (270, 78)
                        var2 = (20, 70)
                                        
                    main.mostro.x = var1[0] * GLOB.MULT - var2[0] * GLOB.MULT
                    main.mostro.y = var1[1] * GLOB.MULT - var2[1] * GLOB.MULT
                    
                    if GLOB.Piano == GLOB.MonsterActualFloor:
                        main.Gui.door_sound.play()
                    
                    GLOB.MonsterHasChangedRoom = True
                    GLOB.MonsterActualRoom = GLOB.Stanza
                    GLOB.MonsterActualFloor = GLOB.Piano
                    
                    main.mostro.contatore_collisioni = 0
                    main.mostro.delayInteract.ReStart()
                    main.mostro.flag_interact = False
                    
                    if GLOB.Stanza == "Segreteria":
                        main.stanze.setToDefault()
                        main.stanze.dizionario_flag["Segreteria"] = True
                        main.stanze.caricaStanza()
                        main.stanze.CaricaElementi()
                    
                if GLOB.PlayerIsHidden:
                    main.mostro.IseePlayer = False
                    
            else:
                testo = "Ti ho perso"
                main.mostro.IseePlayer = False
                main.mostro.IAttacking = False
                main.mostro.aggr = False
                main.mostro.finish()
            
            if GLOB.Debug:
                print(testo)
                
            GLOB.PlayerHasChangedRoom = False
            GLOB.MonsterHasChangedRoom = False

    def Start(self):
        if not GLOB.isPaused:
            self.__delay.Infinite()

    def UpdateBackground(self):
        var = 2
        self.___mappa = GLOB.Default_Map
        self.mappa = pygame.image.load(self.___mappa).convert()
        self.mappa = pygame.transform.scale(self.mappa, (self.mappa.get_width() * GLOB.MULT / var, self.mappa.get_height() * GLOB.MULT / var))

        if GLOB.Default_walls != None:
            
            try:

                self.___oggetti = GLOB.Default_walls
                self.oggetti = pygame.image.load(self.___oggetti).convert_alpha()
                
            except FileNotFoundError:
                if GLOB.Default_object != None:
                    self.___oggetti = GLOB.Default_object
                    self.oggetti = pygame.image.load(self.___oggetti).convert_alpha()
                
            self.oggetti = pygame.transform.scale(self.oggetti, (self.mappa.get_width(), self.mappa.get_height()))
        
    def sgrana(self):
        self.val_caricamento += 0.5
        
        if self.iFinished:
            self.flag_changeBg = True

        if not self.iFinished:
            
            self.flag_changeBg = False

            if not self.flag_reverse:
                self.val_sgrana += 4
                self.val_scurisci += 16
            else:
                self.val_sgrana -= 4
                self.val_scurisci -= 16

                if self.___mappa != GLOB.Default_Map:
                    self.UpdateBackground()
                    main.player.x = main.stanze.pos_portaP[0] * GLOB.MULT
                    main.player.y = main.stanze.pos_portaP[1] * GLOB.MULT

                    main.cam.x = main.stanze.pos_portaC[0] * GLOB.MULT
                    main.cam.y = main.stanze.pos_portaC[1] * GLOB.MULT
                    
                    self.setDelay()
                    self.flag_room = True
                    
                    # print(main.stanze.pos_portaP, main.stanze.pos_portaC)

            if self.val_sgrana >= 310 or self.val_scurisci >= 255:
                self.__loadImagesANDconvert()
            elif self.val_sgrana <= 1:
                self.__loadImagesANDconvert()

            if self.val_scurisci >= 310:
                self.val_scurisci = 310
                self.flag_reverse = True
            elif self.val_scurisci <= 0:
                self.val_scurisci = 0
                self.flag_reverse = False
                self.iFinished = True

            if self.val_sgrana >= 64:
                self.val_sgrana = 64
                self.flag_sgrana = True
            elif self.val_sgrana <= 1:
                self.val_sgrana = 1
                self.flag_sgrana = False

            num_alpha = 250

            self.mappa.set_alpha(self.val_sgrana+num_alpha)
            self.immagine.set_alpha(self.val_sgrana+num_alpha)
            self.superficie.set_alpha(self.val_scurisci)

            if not self.flag_reverse:
                self.__sgrana()
            else:
                self.__loadImagesANDconvert()
                self.__sgrana()

    def __sgrana(self):
        self.ombra = pygame.transform.scale(self.ombra, (self.ombra.get_width() / self.val_sgrana, self.ombra.get_height() / self.val_sgrana))
        self.ombra = pygame.transform.scale(self.ombra, (self.ombra.get_width() * self.val_sgrana + self.val_sgrana, self.ombra.get_height() * self.val_sgrana + self.val_sgrana))
            
        self.immagine = pygame.transform.scale(self.immagine, (self.immagine.get_width() / self.val_sgrana, self.immagine.get_height() / self.val_sgrana))
        self.immagine = pygame.transform.scale(self.immagine, (self.immagine.get_width() * self.val_sgrana + self.val_sgrana, self.immagine.get_height() * self.val_sgrana + self.val_sgrana))
        
        self.mappa = pygame.transform.scale(self.mappa, (self.mappa.get_width() / self.val_sgrana, self.mappa.get_height() / self.val_sgrana))                
        self.mappa = pygame.transform.scale(self.mappa, (self.mappa.get_width() * self.val_sgrana + self.val_sgrana, self.mappa.get_height() * self.val_sgrana + self.val_sgrana))

        if GLOB.Default_walls != None:

            self.oggetti = pygame.transform.scale(self.oggetti, (self.oggetti.get_width() / self.val_sgrana, self.oggetti.get_height() / self.val_sgrana))
            self.oggetti = pygame.transform.scale(self.oggetti, (self.oggetti.get_width() * self.val_sgrana + self.val_sgrana, self.oggetti.get_height() * self.val_sgrana + self.val_sgrana))
        
    def __loadImages(self):
        self.ombra = pygame.image.load("assets/ombra.png").convert_alpha()
        self.immagine = pygame.image.load(self.__character).convert_alpha()
        self.mappa = pygame.image.load(self.___mappa).convert()

        if GLOB.Default_walls != None:
            try:
                self.oggetti = pygame.image.load(self.___oggetti).convert_alpha()
            except FileNotFoundError:
                GLOB.Default_walls = None

    def __loadImagesANDconvert(self):
        var = 2
        self.__loadImages()
        self.ombra = pygame.transform.scale(self.ombra, (self.ombra.get_width()*GLOB.MULT / GLOB.Player_proportion,self.ombra.get_height()*GLOB.MULT / GLOB.Player_proportion))
        self.immagine = pygame.transform.scale(self.immagine, ( self.immagine.get_width() * GLOB.MULT / GLOB.Player_proportion, self.immagine.get_height() * GLOB.MULT / GLOB.Player_proportion))
        self.mappa = pygame.transform.scale(self.mappa, (self.mappa.get_width() * GLOB.MULT / var, self.mappa.get_height() * GLOB.MULT / var))

        if GLOB.Default_walls != None:
            self.oggetti = pygame.transform.scale(self.oggetti, (self.mappa.get_width(), self.mappa.get_height()))

    def __caricamento(self):
        molt = 10

        LOAD_TEXT = main.get_font(12*int(GLOB.MULT)).render("Caricamento", True, "white")
        LOAD_RECT = LOAD_TEXT.get_rect(center=(GLOB.screen_width/2, GLOB.screen_height/2 - LOAD_TEXT.get_height()/2 - 10*GLOB.MULT))

        rect = pygame.Rect(GLOB.screen_width/2 - (5 * GLOB.MULT * molt), GLOB.screen_height/2, 10 * GLOB.MULT * molt, 10 * GLOB.MULT)
        VALUE_TEXT = main.get_font(6*int(GLOB.MULT)).render(str(int(self.val_caricamento*10))+"%", True, "#2c2c2c")
        VALUE_RECT = (rect.x + rect.width/2 - VALUE_TEXT.get_width()/4, rect.y + rect.height/2 - VALUE_TEXT.get_height()/2)

        GLOB.screen.fill((0,0,0))
        GLOB.screen.blit(LOAD_TEXT, LOAD_RECT)
        pygame.draw.rect(GLOB.screen, "#f5f5f5", rect)
        pygame.draw.rect(GLOB.screen, "#676767", rect, int(GLOB.MULT))
        pygame.draw.rect(GLOB.screen, "#41e141", pygame.Rect(GLOB.screen_width/2 - (5 * GLOB.MULT * molt) + GLOB.MULT, GLOB.screen_height/2 + GLOB.MULT, self.val_caricamento * GLOB.MULT * molt - 2 * GLOB.MULT, 8 * GLOB.MULT))
        GLOB.screen.blit(VALUE_TEXT, VALUE_RECT)

    def disegna(self):
        if not GLOB.isPaused and not self.flag_caricamento:
            self.delay_monsterRoom.Start()
            
            if GLOB.MonsterActualRoom == "Default":
                main.mostro.evento = "porta"
        
        if not self.iFinished:
            
            if self.flag_caricamento:
                self.Start()
                if self.iFinished:
                    self.flag_caricamento = False
                else:
                    self.__caricamento()

            else:

                self.schermo.fill((0,0,0))

                self.Start()
                self.schermo.blit(self.mappa, (-self.val_sgrana * GLOB.MULT + main.cam.getPositionX() + GLOB.MULT, -self.val_sgrana * GLOB.MULT + main.cam.getPositionY() + GLOB.MULT))

                self.schermo.blit(self.ombra, (main.player.getPositionX() -self.val_sgrana * GLOB.MULT + GLOB.MULT, main.player.getPositionY()-2.5*GLOB.MULT/GLOB.Player_proportion -self.val_sgrana * GLOB.MULT + GLOB.MULT))
                self.schermo.blit(self.immagine, (main.player.getPositionX() -self.val_sgrana * GLOB.MULT + GLOB.MULT, main.player.getPositionY() -self.val_sgrana * GLOB.MULT + GLOB.MULT))

                if GLOB.Default_walls != None:
                    self.schermo.blit(self.oggetti, (-self.val_sgrana * GLOB.MULT + main.cam.getPositionX() + GLOB.MULT, -self.val_sgrana * GLOB.MULT + main.cam.getPositionY() + GLOB.MULT))

                self.schermo.blit(self.superficie, (0, 0))
                GLOB.screen.blit(self.schermo, (0, 0))




def inizializza():
    global clock, animazione
    pygame.display.set_caption("Effetto")
    clock = pygame.time.Clock()
    animazione = Transizione(vel = 0.05)


def disegna():
    GLOB.screen.fill((12,24,36))
    animazione.disegna()
    #rettangolo = pygame.Rect(GLOB.screen_width/2 - immagine.get_width()/2, GLOB.screen_height/2 - immagine.get_height()/2, immagine.get_width(), immagine.get_height())
    #pygame.draw.rect(GLOB.screen, (255, 0, 0), rettangolo, 1)

def testa():
    inizializza()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                animazione.iFinished = False

        disegna()

        clock.tick(GLOB.FPS)
        pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    testa()
