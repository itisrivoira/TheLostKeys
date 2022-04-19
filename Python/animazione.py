import pygame, sys
import global_var as GLOB
import main

class Delay():
    def __init__(self, sec, event):
        self.__min = 0
        self.__max = sec * GLOB.FPS
        self.__increment = 1
        self.__function = event
        self.__flag = True
        self.__times = 0

    # | Avvia il delay -> Poi si interromperà |
    def Start(self):
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) >= self.__max:
                self.__function()
                self.__flag = False

    # | Restarta il delay |
    def ReStart(self):
        if not self.__flag:
            self.__min = 0
            self.__flag = True

    # | Imposta il delay a infinito |
    def Infinite(self):
        self.ReStart()
        self.Start()

    def TotTimes(self, val):
        if self.__times <= val:
            self.ReStart()
            self.Start()
            self.__times += 1

    # | Stampa lo stato attuale del delay |
    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/GLOB.FPS, self.__max/GLOB.FPS, self.__function))



class Transizione():
    def __init__(self, vel):
        self.flag_changeBg = True 
        self.ImpostaSfondo()
        self.__character = GLOB.Default_Character

        self.__vel = vel
        self.__delay = Delay(sec = self.__vel, event = self.sgrana)
        self.superficie = pygame.surface.Surface((GLOB.screen_width, GLOB.screen_height))
        self.superficie.fill((0,0,0))        
        
        self.schermo = pygame.surface.Surface((GLOB.screen_width, GLOB.screen_height))
        self.schermo.fill((0,0,0))
        
        self.val_scurisci = 300
        self.val_sgrana = 1
        self.val_caricamento = 0

        self.flag_reverse = False
        self.flag_sgrana = False
        self.iFinished = False

        self.flag_caricamento = True
        self.__loadImagesANDconvert()

    def Start(self):
        self.__delay.Infinite()

    def ImpostaSfondo(self):
        var = 2
        self.___mappa = GLOB.Default_Map
        self.mappa = pygame.image.load(self.___mappa).convert()
        self.mappa = pygame.transform.scale(self.mappa, (self.mappa.get_width() * GLOB.MULT / var, self.mappa.get_height() * GLOB.MULT / var))
        
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
        
    def __loadImages(self):
        self.ombra = pygame.image.load("assets/ombra.png").convert_alpha()
        self.immagine = pygame.image.load(self.__character).convert_alpha()
        self.mappa = pygame.image.load(self.___mappa).convert()

    def __loadImagesANDconvert(self):
        var = 2
        self.__loadImages()
        self.ombra = pygame.transform.scale(self.ombra, (self.ombra.get_width()*GLOB.MULT / GLOB.Player_proportion,self.ombra.get_height()*GLOB.MULT / GLOB.Player_proportion))
        self.immagine = pygame.transform.scale(self.immagine, ( self.immagine.get_width() * GLOB.MULT / GLOB.Player_proportion, self.immagine.get_height() * GLOB.MULT / GLOB.Player_proportion))
        self.mappa = pygame.transform.scale(self.mappa, (self.mappa.get_width() * GLOB.MULT / var, self.mappa.get_height() * GLOB.MULT / var))

    def __caricamento(self):
        molt = 10

        LOAD_TEXT = main.get_font(12*int(GLOB.MULT)).render("Caricamento", True, "white")
        LOAD_RECT = LOAD_TEXT.get_rect(center=(GLOB.screen_width/2, GLOB.screen_height/2 - LOAD_TEXT.get_height()/2 - 10*GLOB.MULT))

        VALUE_TEXT = main.get_font(6*int(GLOB.MULT)).render(str(int(self.val_caricamento*10))+"%", True, "Gray")
        VALUE_RECT = LOAD_TEXT.get_rect(center=(GLOB.screen_width/2 + 6 * GLOB.MULT * molt, GLOB.screen_height/2 - LOAD_TEXT.get_height()/2 + 14 * GLOB.MULT))

        GLOB.screen.fill((0,0,0))
        GLOB.screen.blit(LOAD_TEXT, LOAD_RECT)
        pygame.draw.rect(GLOB.screen, "White", pygame.Rect(GLOB.screen_width/2 - (5 * GLOB.MULT * molt), GLOB.screen_height/2, 10 * GLOB.MULT * molt, 10 * GLOB.MULT))
        pygame.draw.rect(GLOB.screen, "Gray", pygame.Rect(GLOB.screen_width/2 - (5 * GLOB.MULT * molt), GLOB.screen_height/2, 10 * GLOB.MULT * molt, 10 * GLOB.MULT), 1 * GLOB.MULT)
        pygame.draw.rect(GLOB.screen, "Green", pygame.Rect(GLOB.screen_width/2 - (5 * GLOB.MULT * molt) + GLOB.MULT, GLOB.screen_height/2 + GLOB.MULT, self.val_caricamento * GLOB.MULT * molt, 8 * GLOB.MULT))
        GLOB.screen.blit(VALUE_TEXT, VALUE_RECT)

    def disegna(self):
        if self.flag_caricamento:
            self.Start()
            if self.iFinished:
                self.flag_caricamento = False
            else:
                self.__caricamento()

        if not self.iFinished and not self.flag_caricamento:

            self.schermo.fill((0,0,0))

            self.Start()
            self.schermo.blit(self.mappa, (-self.val_sgrana * GLOB.MULT + main.cam.getPositionX() + GLOB.MULT, -self.val_sgrana * GLOB.MULT + main.cam.getPositionY() + GLOB.MULT))

            self.schermo.blit(self.ombra, (main.player.getPositionX() -self.val_sgrana * GLOB.MULT + GLOB.MULT, main.player.getPositionY()-2.5*GLOB.MULT/GLOB.Player_proportion -self.val_sgrana * GLOB.MULT + GLOB.MULT))
            self.schermo.blit(self.immagine, (main.player.getPositionX() -self.val_sgrana * GLOB.MULT + GLOB.MULT, main.player.getPositionY() -self.val_sgrana * GLOB.MULT + GLOB.MULT))

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