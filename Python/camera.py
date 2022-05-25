import pygame, random
import main
import global_var as GLOB


"""

    ---  Classe che controlla la posizione attuale del giocatore dello schermo e aggiorna i contenuti dello schermo spostandoli 

                In questo modo ferma anche il giocatore e da' l'illusione che tutto si sta muovendo

"""

class Cam():
    def __init__(self, x, y):

        self.setPositionX(x) 
        self.setPositionY(y)
        self.Player_hitbox = [ 20 * GLOB.MULT /GLOB.Player_proportion, 35 * GLOB.MULT /GLOB.Player_proportion, 15 * GLOB.MULT /GLOB.Player_proportion, 10 * GLOB.MULT /GLOB.Player_proportion]


    def setPositionX(self, x):
        self.x = x

    def setPositionY(self, y):
        self.y = y

    def getPositionX(self):
        return self.x

    def getPositionY(self):
        return self.y

    def screen_shake(self):
        intervallo = 5
        self.y = self.y + random.randint(-intervallo, intervallo)

        
    def update(self):
        self.offset = (5 * GLOB.Moff * GLOB.MULT, 2.25 * GLOB.Moff * GLOB.MULT)

        a = main.player.getPositionX() >= GLOB.screen_width - self.offset[0] - main.player.width
        b = main.player.getPositionX() <= self.offset[0]

        c = main.player.getPositionY() >= GLOB.screen_height - self.offset[1] - main.player.height
        d = main.player.getPositionY() <= self.offset[1]

        a1 = main.player.getRightPress()
        b1 = main.player.getLeftPress()

        c1 = main.player.getDownPress()
        d1 = main.player.getUpPress()

        ln = main.player.Last_keyPressed == "Null"

        if a and ln and not (main.player.getLeftPress() or main.player.getRightPress()):
            main.player.x -= GLOB.Player_speed

        if b and ln and not (main.player.getLeftPress() or main.player.getRightPress()):
            main.player.x += GLOB.Player_speed

        if c and ln and not (main.player.getUpPress() or main.player.getDownPress()):
            main.player.y -= GLOB.Player_speed

        if d and ln and not (main.player.getUpPress() or main.player.getDownPress()):
            main.player.y += GLOB.Player_speed

        if a and a1 or ln and a:
            main.player.setPositionX(main.player.getPositionX()-main.player.getVelocitaX())
            self.x -= main.player.getVelocitaX()
    

        if b and b1 or ln and b:
            main.player.setPositionX(main.player.getPositionX()-main.player.getVelocitaX())
            self.x += -main.player.getVelocitaX()


        if c and c1 or ln and c:
            main.player.setPositionY(main.player.getPositionY()-main.player.getVelocitaY())
            self.y -= main.player.getVelocitaY()
    

        if d and d1 or ln and d:
            main.player.setPositionY(main.player.getPositionY()-main.player.getVelocitaY())
            self.y += -main.player.getVelocitaY()


    def ShowCam(self):
        self.offset = (5 * GLOB.Moff * GLOB.MULT, 2.25 * GLOB.Moff * GLOB.MULT)
        Offset_rect = pygame.Rect(self.offset[0] + self.Player_hitbox[0], self.offset[1] + self.Player_hitbox[1], GLOB.screen_width - self.offset[0]*2 - self.Player_hitbox[0]*2, GLOB.screen_height - self.offset[1]*2 - self.Player_hitbox[1]*2)
        pygame.draw.rect(GLOB.screen, (255,0,255), Offset_rect, int(GLOB.MULT))