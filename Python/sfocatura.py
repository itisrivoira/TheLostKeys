import pygame, sys
import global_var as GLOB

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



class Sfoca():
    def __init__(self, vel):
        self.flag_changeBg = True 
        self.__vel = vel
        self.__delay = Delay(sec = self.__vel, event = self.sgrana)
        self.superficie = pygame.surface.Surface((GLOB.screen_width, GLOB.screen_height))
        self.superficie.fill((255,255,255))
        
        self.val_scurisci = 0

        self.flag_reverse = False
        self.iFinished = False

    def Start(self):
        self.__delay.Infinite()

    def sgrana(self):

        if not self.iFinished:

            val_incremento = 5
            val_max = 310
            val_min = 50

            if not self.flag_reverse:
                self.val_scurisci += val_incremento
            else:
                self.val_scurisci -= val_incremento

            if self.val_scurisci >= val_max:
                self.val_scurisci = val_max
                self.flag_reverse = True
            elif self.val_scurisci <= val_min and self.flag_reverse:
                self.val_scurisci = val_min
                self.flag_reverse = False
                self.iFinished = True

            self.superficie.set_alpha(self.val_scurisci)


    def disegna(self):
    
        self.Start()
        GLOB.screen.blit(self.superficie, (0, 0))




def inizializza():
    global clock, animazione
    pygame.display.set_caption("Effetto")
    clock = pygame.time.Clock()
    animazione = Sfoca(vel = 0.05)


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