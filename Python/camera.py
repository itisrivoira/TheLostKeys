import pygame, random
import main
import global_var as GLOB

class Cam():
    def __init__(self, x, y):

        self.setPositionX(x) 
        self.setPositionY(y)
        self.Player_hitbox = [ 20 * GLOB.MULT /GLOB.Player_proportion, 35 * GLOB.MULT /GLOB.Player_proportion, 15 * GLOB.MULT /GLOB.Player_proportion, 10 * GLOB.MULT /GLOB.Player_proportion]
        self.offset_cam = (0, 0, 0, 0)

    def setPositionX(self, x):
        self.x = x

    def setPositionY(self, y):
        self.y = y

    def getPositionX(self):
        return self.x

    def getPositionY(self):
        return self.y

    def screen_shake(self):

        if not GLOB.isPaused:
            intervallo = 1 * int(GLOB.MULT)
            random_value = random.randint(-intervallo, intervallo)
            self.y += random_value
            main.player.y += random_value

        
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
            
        GLOB.CamPosX = self.x
        GLOB.CamPosY = self.y


    def ShowCam(self):
        self.offset = (5 * GLOB.Moff * GLOB.MULT, 2.25 * GLOB.Moff * GLOB.MULT)
        self.offset_cam = self.offset[0] + self.Player_hitbox[0], self.offset[1] + self.Player_hitbox[1], GLOB.screen_width - self.offset[0]*2 - self.Player_hitbox[0]*2, GLOB.screen_height - self.offset[1]*2 - self.Player_hitbox[1]*2
        Offset_rect = pygame.Rect(self.offset_cam)
        pygame.draw.rect(GLOB.screen, (255,0,255), Offset_rect, int(GLOB.MULT))
        
        
class Corrente():
    def __init__(self):
        self.x, self.y = 0, 0
        self.flag_update = True
        
        self.brightness = 90
        self.__default_value = GLOB.Torcia
        self.__load_resources()
        
        self.__Start = not GLOB.PlayerHasPressedButton
        
        self.__sound = main.mixer.Sound("suoni/"+str(not GLOB.corrente)+"corrente.wav")
        self.__sound.set_volume(0.5 * GLOB.AU)
        self.__sound.fadeout(900)
        
        self.__delay_attivazione = main.Delay(1, self.__CanStart)
        self.__delay_sound = main.Delay(0.5, self.__sound.play)
        
        self.__flag_dialogo = True
        
        self.__num_min_enigmi = 1
        
        if GLOB.MonsterCanSpawn:
            self.__monster_surface = pygame.Surface((GLOB.screen_width, GLOB.screen_height), pygame.SRCALPHA).convert_alpha()
            
            if GLOB.MonsterSpawning:
                self.__update_triagle()
        
    def __update_triagle(self):
        if GLOB.Stanza == GLOB.MonsterActualRoom and main.animazione.iFinished:
            self.__monster_view_polygon = main.mostro.view_polygon
            
            color = "#ff3e3e25"
            
            self.__monster_surface.fill(pygame.SRCALPHA)
            
            pygame.draw.polygon(self.__monster_surface, color, self.__monster_view_polygon)
            
            GLOB.screen.blit(self.__monster_surface, (0, 0))
        
    def __load_resources(self):
        self.__sound = main.mixer.Sound("suoni/"+str(GLOB.corrente)+"corrente.wav")
        self.__sound.set_volume(0.5 * GLOB.AU)
        self.__sound.fadeout(900)
        
        
        div = 2
        self.__image = pygame.image.load("assets/"+str(GLOB.Torcia)+"Torcia.png").convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (
            self.__image.get_width() * GLOB.MULT / div, self.__image.get_height() * GLOB.MULT / div))
        
        if GLOB.corrente: self.__image.set_alpha(self.brightness)
        self.size = self.__image.get_size()
        
    def __CanStart(self):
        self.__Start = True
        
        self.__load_resources()
        
        if self.__flag_dialogo and not GLOB.PlayerHasPressedButton:
            frase = "Oh no! La corrente è saltata!|Per fortuna che mi sono portato una torcia nel mio zaino."
            
            for testo in frase.split("|"):
                dialogue = main.Dialoghi(GLOB.scelta_char, testo, 4)
                dialogue.stampa()
                
            self.__flag_dialogo = False
            
            
    def disegna(self):
        GLOB.MonsterCanSeePlayer = GLOB.corrente or len(GLOB.enigmi_risolti) > self.__num_min_enigmi
        
        if GLOB.corrente:
            self.__Start = False
            self.__delay_attivazione.ReStart()
        
        if not GLOB.corrente and self.__Start:
            if len(GLOB.enigmi_risolti) > self.__num_min_enigmi and GLOB.MonsterCanSpawn and GLOB.MonsterSpawning:
                self.__update_triagle()
                GLOB.MonsterCanSeePlayer = True
                
        if self.__default_value != GLOB.Torcia:
            self.flag_update = True
            self.__default_value = GLOB.Torcia
        
        if self.flag_update:
            self.__load_resources()
            self.flag_update = False
                
        space = 7 * GLOB.MULT, 7 * GLOB.MULT
        GLOB.screen.blit(self.__image, (main.player.hitbox[0] + space[0] - self.size[0]/2, main.player.hitbox[1] + space[1] - self.size[1]/2))
        
        if not self.__Start and not GLOB.corrente:
            self.__delay_attivazione.Start()
            self.__delay_sound.Start()