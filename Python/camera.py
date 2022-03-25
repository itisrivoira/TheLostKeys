import pygame
import main
import global_var as GLOB


"""

    ---  Classe che controlla la posizione attuale del giocatore dello schermo e aggiorna i contenuti dello schermo spostandoli 

                In questo modo ferma anche il giocatore e da' l'illusione che tutto si sta muovendo

"""

class Cam():
    def __init__(self):

        #indico il giocatore impostato
        self.setPositionX(0) 
        self.setPositionY(0)

        self.image = pygame.image.load("assets/BackgroundCam.png").convert()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.image = pygame.transform.scale(self.image,((self.width*GLOB.MULT*2), (self.height*GLOB.MULT*2)))

        self.Player_hitbox = [ 15 * GLOB.MULT /GLOB.Player_proportion, 17 * GLOB.MULT /GLOB.Player_proportion, 24 * GLOB.MULT /GLOB.Player_proportion, 43 * GLOB.MULT /GLOB.Player_proportion]


    def setPositionX(self, x):
        self.x = x

    def setPositionY(self, y):
        self.y = y

    def getPositionX(self):
        return self.x

    def getPositionY(self):
        return self.y

        
    def update(self, visibility):

        self.offset = (4 * GLOB.Moff * GLOB.MULT, 2.25 * GLOB.Moff * GLOB.MULT)

        a =  main.player.getPositionX() >= GLOB.screen_width - self.offset[0] - main.player.width
        b =  main.player.getPositionX() <= self.offset[0]

        c =  main.player.getPositionY() >= GLOB.screen_height - self.offset[1] - main.player.height
        d =  main.player.getPositionY() <= self.offset[1]

        a1 = main.player.getRightPress()
        b1 = main.player.getLeftPress()

        c1 = main.player.getDownPress()
        d1 = main.player.getUpPress()

        ln = main.player.Last_keyPressed=="Null"

        if a and ln and not (main.player.getLeftPress() or main.player.getRightPress()):
            main.player.x -= GLOB.Player_default_speed

        if b and ln and not (main.player.getLeftPress() or main.player.getRightPress()):
            main.player.x += GLOB.Player_default_speed

        if c and ln and not (main.player.getUpPress() or main.player.getDownPress()):
            main.player.y -= GLOB.Player_default_speed

        if d and ln and not (main.player.getUpPress() or main.player.getDownPress()):
            main.player.y += GLOB.Player_default_speed

        if a and a1 or ln and a:
            main.player.setPositionX(main.player.getPositionX()-main.player.getVelocitaX())
            self.x -= main.player.getVelocitaX()
            # print("A vero")
    

        if b and b1 or ln and b:
            main.player.setPositionX(main.player.getPositionX()-main.player.getVelocitaX())
            self.x += -main.player.getVelocitaX()
            # print("B vero")


        if c and c1 or ln and c:
            main.player.setPositionY(main.player.getPositionY()-main.player.getVelocitaY())
            self.y -= main.player.getVelocitaY()
            # print("C vero")
    

        if d and d1 or ln and d:
            main.player.setPositionY(main.player.getPositionY()-main.player.getVelocitaY())
            self.y += -main.player.getVelocitaY()
            # print("D vero")
        
        if visibility:        
            self.ShowCam()

        
        #print("Posizione x: "+str(main.player.getPositionX())+" | Posizione y: "+str(main.player.getPositionY())+" | VelocitàX: "+str(main.player.getVelocitaX()))

    def ShowCam(self):
        Offset_rect = pygame.Rect(self.offset[0] + self.Player_hitbox[0], self.offset[1] + self.Player_hitbox[1], GLOB.screen_width - self.offset[0]*2 - self.Player_hitbox[0]*2, GLOB.screen_height - self.offset[1]*2 - self.Player_hitbox[1]*2)
        pygame.draw.rect(GLOB.screen, (255,255,255), Offset_rect, int(GLOB.MULT))


    def ShowBackground(self):
        GLOB.screen.blit(self.image, (self.x, self.y))