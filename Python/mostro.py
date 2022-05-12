import pygame, sys, random
from components import Delay
import global_var as GLOB
import main


class Keeper():
    def __init__(self, pos, vel, wh):
        self.x = pos[0]
        self.y = pos[1]
        self.width = wh[0]
        self.height = wh[1]
        self.default_height = self.height
        self.vel = vel * GLOB.MULT / GLOB.Delta_Time
        self.run = self.vel * 1.4
        self.x, self.y = GLOB.screen.get_rect().center
        self.line_vector = pygame.math.Vector2(1, 0)
        self.angle = 90

        self.default_speed = self.vel

        self.monster_ai_vel = 0.5
        self.default_monster_ai_vel = self.monster_ai_vel
        self.monster_ai_brain = 0
        self.delay_monster = Delay(self.monster_ai_vel, self.__setBrain)
        self.Last_keyPressed = "Null"

        self.distanza = 90

        self.color_triangle = (255, 0, 0)

        self.altezza_rect = 20 * GLOB.MULT

        self.__setMonster(False)

        self.aggr = False

        self.direzione = ""

        self.valore_distanza = 180 * GLOB.MULT
        self.setHitbox()

        self.__left_pressed = False
        self.__right_pressed = False
        self.__up_pressed = False
        self.__down_pressed = False

        
        self.superfice = pygame.Surface((GLOB.screen_width, GLOB.screen_height))

        self.line_vector = pygame.math.Vector2(self.height, 0)

        self.transparency = 20

        self.lista_movimento = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]

        self.value_surface = 45 * GLOB.MULT
        self.surface = pygame.Surface((self.width, self.value_surface), pygame.SRCALPHA)


    def load_monsterSurface(self):
        self.surface = pygame.Surface((self.width, self.value_surface), pygame.SRCALPHA)

        self.surface.blit(self.image, (0, 0))

        GLOB.screen.blit(self.surface, (self.x + main.cam.getPositionX(), self.y + main.cam.getPositionY()))


    def setHitbox(self):
        self.hitbox = (self.x + 20 * GLOB.MULT + main.cam.getPositionX(),  self.y + 35 * GLOB.MULT + main.cam.getPositionY(), 16 * GLOB.MULT, 16 * GLOB.MULT)
        self.mesh = pygame.Rect(self.hitbox)

    def __setBrain(self):

        self.monster_ai_brain = random.choice(self.lista_movimento)

    def __setMonster(self, v):

        if not v:
            self.image = pygame.image.load("assets/mostro.png").convert_alpha()
        else:
            self.image = pygame.image.load("assets/angry-mostro.png").convert_alpha()

        self.image = pygame.transform.scale(self.image, (self.image.get_width() * GLOB.MULT / GLOB.Player_proportion, self.image.get_height() * GLOB.MULT / GLOB.Player_proportion))

    def update(self):
        radius = 360

        self.setHitbox()

        if GLOB.isPaused:

            self.monster_ai_brain = 0

        else:

            if not GLOB.MonsterCanAttack:
                self.aggr = False

            if self.angle >= 360:
                self.angle = 0

            if self.angle <= -1:
                self.angle = 359
            
            rot_vector = self.line_vector.rotate(self.angle) * radius
            rot_vector1 = self.line_vector.rotate(self.angle + self.distanza) * radius

            distanza = (17 * GLOB.MULT, 22 * GLOB.MULT)

            start_line = round(self.x + self.width/2 + distanza[0] + main.cam.getPositionX()), round(self.y + main.cam.getPositionY() + distanza[1])
            end_line = round(self.x + self.width/2 + distanza[0] - rot_vector.x + main.cam.getPositionX()), round(self.y - rot_vector.y + main.cam.getPositionY() + distanza[1])


            end_line1 = round(self.x + self.width/2 + distanza[0] - rot_vector1.x + main.cam.getPositionX()), round(self.y - rot_vector1.y + main.cam.getPositionY() + distanza[1])

            if GLOB.ShowMonsterRange:
                self.superfice.fill(pygame.SRCALPHA)
                self.superfice.set_alpha(self.transparency)
            else:
                self.superfice.fill((0, 0, 0))
                self.triangle = pygame.draw.polygon(surface=self.superfice, color=self.color_triangle, points=[end_line, end_line1, start_line])


            if (self.triangle.colliderect(main.player.mesh) or self.aggr) and GLOB.MonsterCanAttack:
                self.raggio_ai_brain = 0
                self.monster_ai_brain = 0
                self.height = 0
                self.circle = pygame.draw.circle(self.superfice, "Red", (self.x + self.image.get_width()/2 + main.cam.getPositionX(), self.y + main.cam.getPositionY() + distanza[1]), self.valore_distanza, 0)
                self.__setMonster(True)
                self.aggr = True

            else:
                self.height = self.default_height
                self.delay_monster.Infinite()
                self.__setMonster(False)


            if self.mesh.colliderect(main.player.hitbox) and GLOB.MonsterCanAttack:
                main.game_over()

            if not self.aggr:

                self.vel = self.default_speed

                if self.monster_ai_brain == 1.5:
                    self.direzione = "destra-basso"
                    self.angle = 180

                if self.monster_ai_brain == 2.5:
                    self.direzione = "sinistra-basso"
                    self.angle = 270

                if self.monster_ai_brain == 3.5:
                    self.direzione = "sinistra-alto"
                    self.angle = 0

                if self.monster_ai_brain == 4.5:
                    self.direzione = "destra-alto"
                    self.angle = 90

                
                if self.monster_ai_brain == 0:
                    self.direzione = "fermo"
                
                if self.monster_ai_brain == 1:
                    self.direzione = "destra"
                    self.Last_keyPressed = "Right"
                    self.angle = 135
                
                if self.monster_ai_brain == 2:
                    self.direzione = "sinistra"
                    self.Last_keyPressed = "Left"
                    self.angle = 315
                
                if self.monster_ai_brain == 3:
                    self.direzione = "basso"
                    self.Last_keyPressed = "Down"
                    self.angle = 225
                
                if self.monster_ai_brain == 4:
                    self.direzione = "alto"
                    self.Last_keyPressed = "Top"
                    self.angle = 45

                # -- DESTRA --
                if ((self.monster_ai_brain == 1 or self.monster_ai_brain == 1.5 or self.monster_ai_brain == 4.5) and self.monster_ai_brain):
                    self.x += self.vel
                    self.setRightPress(True)
                else:
                    self.setRightPress(False)

                # -- SINISTRA --
                if ((self.monster_ai_brain == 2 or self.monster_ai_brain == 2.5 or self.monster_ai_brain == 3.5)):
                    self.x -= self.vel
                    self.setLeftPress(True)
                else:
                    self.setLeftPress(False)
                
                # -- BASSO --
                if ((self.monster_ai_brain == 3 or self.monster_ai_brain == 1.5 or self.monster_ai_brain == 2.5)):
                    self.y += self.vel
                    self.setDownPress(True)
                else:
                    self.setDownPress(False)

                # -- ALTO --
                if ((self.monster_ai_brain == 4 or self.monster_ai_brain == 4.5 or self.monster_ai_brain == 3.5)):
                    self.y -= self.vel
                    self.setUpPress(True)
                else:
                    self.setUpPress(False)

            
            if self.aggr and self.circle.colliderect(main.player.mesh):

                self.vel = self.run

                if (main.player.Last_keyPressed == "Left" and main.player.Last_keyPressed != "Right") or self.hitbox[0] > main.player.hitbox[0]:
                    self.x -= self.vel
                    self.direzione = "sinistra"

                if (main.player.Last_keyPressed == "Right" and main.player.Last_keyPressed != "Left") or self.hitbox[0] + self.hitbox[2]/2 < main.player.hitbox[0] + main.player.hitbox[2]/2:
                    self.x += self.vel
                    self.direzione = "destra"

                if (main.player.Last_keyPressed == "Up" and main.player.Last_keyPressed != "Down") or self.hitbox[1] > main.player.hitbox[1]:
                    self.y -= self.vel
                    self.direzione = "alto"

                if (main.player.Last_keyPressed == "Down" and main.player.Last_keyPressed != "Up") or self.hitbox[1] + self.hitbox[3]/2 < main.player.hitbox[1] + main.player.hitbox[3]/2:
                    self.y += self.vel
                    self.direzione = "basso"

            else:

                self.aggr = False


        GLOB.screen.blit(self.image, (self.x + main.cam.getPositionX(), self.y + main.cam.getPositionY()))
        
        if GLOB.ShowMonsterRange:
            GLOB.screen.blit(self.superfice, (0, 0))



    def aumenta_distanza(self):
        self.distanza += 0.25 * GLOB.MULT

    def diminuisci_distanza(self):
        self.distanza -= 0.25 * GLOB.MULT

    def aumenta_lunghezza(self):
        self.default_height += 0.025 * GLOB.MULT

    def diminuisci_lunghezza(self):
        self.default_height -= 0.025 * GLOB.MULT

    def setRightPress(self, r):
        self.__right_pressed = r

    def setLeftPress(self, l):
        self.__left_pressed = l

    def setUpPress(self, u):
        self.__up_pressed = u

    def setDownPress(self, d):
        self.__down_pressed = d

    def getRightPress(self):
        return self.__right_pressed

    def getLeftPress(self):
        return self.__left_pressed

    def getUpPress(self):
        return self.__up_pressed

    def getDownPress(self):
        return self.__down_pressed

    def HasCollision(self, object):
        
        def Confronta(value):

            if value=="x":

                if self.hitbox[0] >= object.x:
                    self.x += self.vel
                    return True
                elif self.hitbox[2] <= object.x:
                    self.x -= self.vel
                    return False

            if value=="y":

                if self.hitbox[1] >= object.y:
                    self.y += self.vel
                    return True
                elif self.hitbox[3] <= object.y:
                    self.y -= self.vel
                    return False
            

        if self.mesh.colliderect(object):

            self.monster_ai_vel = 0.25

            pygame.draw.rect(GLOB.screen, "Green", self.mesh, 1)

            w = (self.Last_keyPressed == "Up")
            a = (self.Last_keyPressed == "Left")
            
            s = (self.Last_keyPressed == "Down")
            d = (self.Last_keyPressed == "Right")

            
            a1 = (self.getRightPress() and w or self.getLeftPress() and w)
            b1 =  (self.getLeftPress() and s or self.getRightPress() and s)

            c1 =  (self.getUpPress() and a or self.getDownPress() and a)
            d1 =  (self.getUpPress() and d or self.getDownPress() and d)

            
            if self.Last_keyPressed != "Null":

                if (a1 or b1) and (not c1 and not d1):

                    Confronta("x")

                    if Confronta("x"):
                        self.setLeftPress(False)
                    else:
                        self.setRightPress(False)

                    self.Last_keyPressed = "Null"

                    
                if (c1 or d1) and (not a1 and not b1):

                    Confronta("y")

                    if Confronta("y"):
                        self.setUpPress(False)
                    else:
                        self.setDownPress(False)

                    self.Last_keyPressed = "Null"
                    

                if (self.getRightPress() or self.getLeftPress() or a or d) and (not w and not s):
                    Confronta("x")
                
                if (self.getUpPress() or self.getDownPress() or w or s) and (not d and not a):
                    Confronta("y")
            else:
                Confronta("y")
                Confronta("x")
        else:
            self.monster_ai_vel = self.default_monster_ai_vel