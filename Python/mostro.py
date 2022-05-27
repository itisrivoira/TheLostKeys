import pygame, random, os, re
from components import Delay
import global_var as GLOB
import main
from pygame import mixer

"""

    --- DA OTTIMIZZARE ---
       ( quasi finito )
     
     
"""

sceltaG = "Keeper"

Folder_walkO = 'Characters/'+sceltaG+'/WalkOrizontal'
Folder_walkVD = 'Characters/'+sceltaG+'/WalkVerticalD'
Folder_walkVU = 'Characters/'+sceltaG+'/WalkVerticalU'
Folder_angry = 'Characters/'+sceltaG+'/Angry'


def riempi(percorso):
    FileNames = os.listdir(percorso)

    # Ordino i file e gli appendo ad una lista, in modo che le animazioni siano lineari e ordinate
    FileNames.sort(key=lambda f: int(re.sub('\D', '', f)))
    sorted(FileNames)

    for filename in FileNames:
        if percorso == Folder_walkO:
            #print("Trovato Percorso WO")
            GLOB.MonsterWO.append(filename)
        if percorso == Folder_walkVD:
            #print("Trovato Percorso WVD")
            GLOB.MonsterWVD.append(filename)
        if percorso == Folder_walkVU:
            #print("Trovato Percorso WVU")
            GLOB.MonsterWVU.append(filename)
            
        if percorso == Folder_angry:
            GLOB.MonsterAngry.append(filename)

riempi(Folder_walkO)
riempi(Folder_walkVD)
riempi(Folder_walkVU)
riempi(Folder_angry)


class Keeper():
    def __init__(self, pos, wh):
        self.x = pos[0]
        self.y = pos[1]
        self.width = wh[0]
        self.height = wh[1]
        self.default_height = self.height
        self.x, self.y = GLOB.screen.get_rect().center
        self.line_vector = pygame.math.Vector2(1, 0)
        self.angle = 90

        self.monster_ai_vel = 0.5
        self.default_monster_ai_vel = self.monster_ai_vel
        self.monster_ai_brain = 0
        self.delay_monster = Delay(self.monster_ai_vel, self.__setBrain)
        self.Last_keyPressed = "Null"

        self.distanza = 90

        self.color_triangle = (255, 0, 0)

        self.altezza_rect = 20 * GLOB.MULT

        self.aggr = False

        self.direzione = ""

        self.flag_CanStartAttack = False

        self.valore_distanza = 200 * GLOB.MULT
        self.setHitbox()

        self.__left_pressed = False
        self.__right_pressed = False
        self.__up_pressed = False
        self.__down_pressed = False

        self.superfice = pygame.Surface((GLOB.screen_width, GLOB.screen_height))        
        
        self.start_valueAnimation = 0.7
        self.current_spriteWO = self.start_valueAnimation
        self.current_spriteWVU = self.start_valueAnimation
        self.current_spriteWVD = self.start_valueAnimation
        self.current_spriteAngry = self.start_valueAnimation
        
        self.Name_animationWVD = Folder_walkVD
        self.Name_animationWVU = Folder_walkVU
        self.Name_animationWO = Folder_walkO
        self.Name_animationAngry = Folder_angry
        
        self.velocita_sprite = 0.1
        self.character_update(3)
        
        self.char_w, self.char_h = self.image.get_width() * GLOB.MULT / GLOB.Player_proportion, self.image.get_height() * GLOB.MULT / GLOB.Player_proportion

        self.luce_image = pygame.image.load("assets/luce.png").convert_alpha()
        self.luce_image = pygame.transform.scale(self.luce_image, (self.char_w, self.char_h))

        self.value_surface = 45 * GLOB.MULT
        self.transparenza = 40
        
        
        self.ICollide = False

        self.collision_state = {
            
            "top": False,
            "bottom": False,
            "left": False,
            "right": False,
            
        }
        
        self.Sound_Angry = mixer.Sound("suoni/AngryMonster.wav")


        self.__setMovement()
        
        self.delay_movement = Delay(0.8, self.__setMovement)
        
        mult = 1.2
        self.ombra = pygame.image.load("assets/ombra.png").convert_alpha()
        self.ombra = pygame.transform.scale(self.ombra, (self.ombra.get_width()*GLOB.MULT/GLOB.Player_proportion * mult,self.ombra.get_height()*GLOB.MULT/GLOB.Player_proportion * mult))


    def __setMovement(self):
        
        self.flag_movement = {
            
            "up": True,
            "down": True,
            "left": True,
            "right": True,
        }
        
        

    def setHitbox(self):
        self.hitbox = (self.x + 20 * GLOB.MULT /GLOB.Player_proportion + main.cam.getPositionX(),  self.y + 35 * GLOB.MULT /GLOB.Player_proportion + main.cam.getPositionY(), 15 * GLOB.MULT, 10 * GLOB.MULT)
        self.mesh = pygame.Rect(self.hitbox)

    def __setBrain(self):
        lista_valori = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
        self.monster_ai_brain = random.choice(lista_valori)
        
    def character_update(self, c):
        
        if not GLOB.isPaused:
            self.current_spriteWO += self.velocita_sprite / GLOB.Delta_Time
            self.current_spriteWVD += self.velocita_sprite / GLOB.Delta_Time
            self.current_spriteWVU += self.velocita_sprite / GLOB.Delta_Time

        if c == 1:
            if self.current_spriteWO >= len(GLOB.PlayerWalkingO):
                self.current_spriteWO = self.start_valueAnimation
            
            immagine = GLOB.PlayerWalkingO[int(self.current_spriteWO)]
            self.image = pygame.image.load(Folder_walkO + "/" + immagine).convert_alpha()
    
        if c == 2:
            if self.current_spriteWO >= len(GLOB.PlayerWalkingO):
                self.current_spriteWO = self.start_valueAnimation
            
            immagine = pygame.image.load(Folder_walkO + "/" + GLOB.PlayerWalkingO[int(self.current_spriteWO)]).convert_alpha()
            immagine_flip = pygame.transform.flip(immagine, True, False)
            self.image = immagine_flip
            
        if c == 3 or c == 0:
            if self.current_spriteWVD >= len(GLOB.PlayerWalkingVD):
                self.current_spriteWVD = self.start_valueAnimation
            
            immagine = GLOB.PlayerWalkingVD[int(self.current_spriteWVD)]
            self.image = pygame.image.load(Folder_walkVD + "/" + immagine).convert_alpha()
            
        if c == 4:
            if self.current_spriteWVU >= len(GLOB.PlayerWalkingVU):
                self.current_spriteWVU = self.start_valueAnimation
            
            immagine = GLOB.PlayerWalkingVU[int(self.current_spriteWVU)]
            self.image = pygame.image.load(Folder_walkVU + "/" + immagine).convert_alpha()
            
        if c == 5 and not self.flag_CanStartAttack:
            
            self.monster_ai_brain = -1

            if not GLOB.isPaused:
                self.current_spriteAngry += 0.2 / GLOB.Delta_Time
            
            if self.current_spriteAngry >= len(GLOB.MonsterAngry) or self.monster_ai_brain != -1:
                self.flag_CanStartAttack = True
                self.current_spriteAngry = self.start_valueAnimation
                self.Sound_Angry.stop()
                
            if self.current_spriteAngry >= 4 and self.current_spriteAngry < 4.2:
                self.Sound_Angry.set_volume(0.4 * GLOB.AU)
                self.Sound_Angry.play()
                
            if self.current_spriteAngry >= 7:
                main.cam.screen_shake()
            
            immagine = GLOB.MonsterAngry[int(self.current_spriteAngry)]
            self.image = pygame.image.load(Folder_angry + "/" + immagine).convert_alpha()
            
        if self.current_spriteAngry > self.start_valueAnimation and self.monster_ai_brain != -1:
            self.current_spriteAngry = self.start_valueAnimation
            
            
    def finish(self):
        self.current_spriteAngry = self.start_valueAnimation
        self.current_spriteWO = self.start_valueAnimation
        self.current_spriteWVU = self.start_valueAnimation
        self.current_spriteWVD = self.start_valueAnimation
        
        if self.monster_ai_brain != -1:
            self.character_update(0)
        self.image = pygame.transform.scale(self.image, (self.char_w, self.char_h))

    def load_monsterSurface(self):
        self.surface = pygame.Surface((self.char_w, self.value_surface), pygame.SRCALPHA)

        self.surface.blit(self.image, (0, 0))
        GLOB.screen.blit(self.surface, (self.x + main.cam.getPositionX(), self.y + main.cam.getPositionY()))

        if self.aggr:
            GLOB.screen.blit(self.luce_image, (self.x + main.cam.getPositionX(), self.y + main.cam.getPositionY()))

        if GLOB.Debug:
            pygame.draw.rect(GLOB.screen, "Green", self.mesh, GLOB.MULT)
            # pygame.draw.rect(GLOB.screen, "Red", pygame.Rect((self.x + main.cam.getPositionX(), self.y + main.cam.getPositionY(), self.image.get_width(), self.image.get_height())), GLOB.MULT)



    def update(self):
        radius = 360
        
        if GLOB.PlayerIsHidden:
            self.aggr = False
            self.flag_CanStartAttack = False
        
        self.velocitaTilesM = round(((24 * GLOB.MULT) / GLOB.Monster_speed) / GLOB.FPS, 2)
        self.velocitaTilesG = round(((24 * GLOB.MULT) / GLOB.Player_speed) / GLOB.FPS, 2)
        
        # self.diff = round(((self.x + main.cam.getPositionX() + self.y + main.cam.getPositionY()) * self.velocitaTilesM - ((main.player.x + main.player.y) * self.velocitaTilesG)) / GLOB.FPS, 2)
        
        self.line = pygame.draw.line(self.superfice, "Red", (self.mesh.centerx, self.mesh.centery), (main.player.mesh.centerx, main.player.mesh.centery), GLOB.MULT)
        self.lung = round(((self.line.bottomright[0] / GLOB.MULT + self.line.bottomright[1] / GLOB.MULT)/2 - (self.line.bottomleft[0] / GLOB.MULT + self.line.bottomleft[1] / GLOB.MULT)/2), 6)
        self.diff = round((self.lung / GLOB.FPS) + 2 / GLOB.Delta_Time, 2)
        
        if not main.animazione.flag_room:
            GLOB.SecondDiffPos = self.diff
        
        if GLOB.Debug:
            print(self.flag_movement)

        self.setHitbox()
        self.delay_movement.Start()

            
        if self.monster_ai_brain:
            if self.monster_ai_brain == int(self.monster_ai_brain):
                self.character_update(self.monster_ai_brain)
            
            elif self.monster_ai_brain == 1.5 or self.monster_ai_brain == 2.5:
                self.character_update(3)
                
            elif self.monster_ai_brain == 3.5 or self.monster_ai_brain == 4.5:
                self.character_update(4)
        else:
            self.finish()

        if not GLOB.MonsterCanAttack:
            self.aggr = False

        self.line_vector = pygame.math.Vector2(self.height, 0)
        
        rot_vector = self.line_vector.rotate(self.angle) * radius
        rot_vector1 = self.line_vector.rotate(self.angle + self.distanza) * radius

        distanza = (17 * GLOB.MULT, 22 * GLOB.MULT)

        start_line = round(self.x + self.width/2 + distanza[0] + main.cam.getPositionX()), round(self.y + main.cam.getPositionY() + distanza[1])
        end_line = round(self.x + self.width/2 + distanza[0] - rot_vector.x + main.cam.getPositionX()), round(self.y - rot_vector.y + main.cam.getPositionY() + distanza[1])


        end_line1 = round(self.x + self.width/2 + distanza[0] - rot_vector1.x + main.cam.getPositionX()), round(self.y - rot_vector1.y + main.cam.getPositionY() + distanza[1])


        self.superfice.fill(pygame.SRCALPHA)

        self.triangle = pygame.draw.polygon(surface=self.superfice, color=self.color_triangle, points=[end_line, end_line1, start_line], width=0)

        self.superfice.set_alpha(self.transparenza)


        # pygame.draw.line(GLOB.screen, (5,80,255), start_line, end_line, 8)
        # pygame.draw.line(GLOB.screen, (255,80,5), start_line, end_line1, 8)

        if (self.triangle.colliderect(main.player.hitbox) or self.aggr) and GLOB.MonsterCanAttack and not GLOB.PlayerIsHidden:
            
            self.character_update(5)
            
            if self.flag_CanStartAttack and GLOB.MonsterCanAttack:
                self.raggio_ai_brain = 0
                self.monster_ai_brain = 0
                self.height = 0
                self.circle = pygame.draw.circle(self.superfice, "Red", (self.x + self.image.get_width()/2 + main.cam.getPositionX() + distanza[0], self.y + self.image.get_height()/2 + main.cam.getPositionY() + distanza[1]), self.valore_distanza, 0)
                self.color_triangle = (255, 0, 0)
                self.aggr = True

        else:
            self.height = self.default_height

            if not GLOB.isPaused:
                self.delay_monster.Infinite()
            else:
                self.monster_ai_brain = 0
            
            self.color_triangle = (255, 0, 0)

        self.image = pygame.transform.scale(self.image, (self.char_w, self.char_h))
        
        GLOB.screen.blit(self.ombra, (self.x - distanza[0] + 11.2 * GLOB.MULT + main.cam.getPositionX(), self.y-10*GLOB.MULT/GLOB.Player_proportion + main.cam.getPositionY()))
        GLOB.screen.blit(self.image, (self.x + main.cam.getPositionX(), self.y + main.cam.getPositionY()))

        if GLOB.ShowMonsterRange or GLOB.Debug:
            GLOB.screen.blit(self.superfice, (0, 0))

            # pygame.draw.line(GLOB.screen, (5,80,255), start_line, end_line, 8)
            # pygame.draw.line(GLOB.screen, (255,80,5), start_line, end_line1, 8)

        if self.mesh.colliderect(main.player.hitbox) and GLOB.MonsterCanAttack and not GLOB.PlayerIsHidden:
            main.game_over()

        if not self.aggr:

            if self.monster_ai_brain == 1.5:
                self.direzione = "destra-basso"
                self.angle = 180
                self.Last_keyPressed = "Null"

            if self.monster_ai_brain == 2.5:
                self.direzione = "sinistra-basso"
                self.angle = 270
                self.Last_keyPressed = "Null"

            if self.monster_ai_brain == 3.5:
                self.direzione = "sinistra-alto"
                self.angle = 0
                self.Last_keyPressed = "Null"

            if self.monster_ai_brain == 4.5:
                self.direzione = "destra-alto"
                self.angle = 90
                self.Last_keyPressed = "Null"

            
            if self.monster_ai_brain == 0:
                self.direzione = "fermo"
                self.Last_keyPressed = "Null"
            
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
                self.Last_keyPressed = "Up"
                self.angle = 45

            # print(self.monster_ai_brain, self.direzione)


            # -- DESTRA --
            if ((self.monster_ai_brain == 1 or self.monster_ai_brain == 1.5 or self.monster_ai_brain == 4.5) and self.monster_ai_brain):
                self.x += GLOB.Monster_speed
                self.setRightPress(True)
            else:
                self.setRightPress(False)

            # -- SINISTRA --
            if ((self.monster_ai_brain == 2 or self.monster_ai_brain == 2.5 or self.monster_ai_brain == 3.5)):
                self.x -= GLOB.Monster_speed
                self.setLeftPress(True)
            else:
                self.setLeftPress(False)
            
            # -- BASSO --
            if ((self.monster_ai_brain == 3 or self.monster_ai_brain == 1.5 or self.monster_ai_brain == 2.5)):
                self.y += GLOB.Monster_speed
                self.setDownPress(True)
            else:
                self.setDownPress(False)

            # -- ALTO --
            if ((self.monster_ai_brain == 4 or self.monster_ai_brain == 4.5 or self.monster_ai_brain == 3.5)):
                self.y -= GLOB.Monster_speed
                self.setUpPress(True)
            else:
                self.setUpPress(False)

        
        if self.aggr and self.circle.colliderect(main.player.hitbox) and not GLOB.isPaused:
            
            GLOB.Monster_speed = GLOB.Monster_default_speed * GLOB.MonsterRun_speed
            
            self.velocita_sprite = 0.25
        
            if self.mesh.right > main.player.mesh.right - 2 * GLOB.MULT and self.flag_movement["right"]:
                self.x -= GLOB.Monster_speed
                self.direzione = "sinistra"
                self.monster_ai_brain = 2


            if self.mesh.left < main.player.mesh.left + 2 * GLOB.MULT and self.flag_movement["left"]:
                self.x += GLOB.Monster_speed
                self.direzione = "destra"
                self.monster_ai_brain = 1


            if self.mesh.bottom > main.player.mesh.bottom + 2 * GLOB.MULT and self.flag_movement["up"]:
                self.y -= GLOB.Monster_speed
                self.direzione = "alto"
                self.monster_ai_brain = 4


            if self.mesh.top < main.player.mesh.top - 2 * GLOB.MULT and self.flag_movement["down"]:
                self.y += GLOB.Monster_speed
                self.direzione = "basso"
                self.monster_ai_brain = 3
                
            
            self.Last_keyPressed = "Null"

        else:
            
            GLOB.setMonster()
            self.velocita_sprite = 0.1
            self.flag_CanStartAttack = False
            self.aggr = False
            # self.monster_ai_brain = -1


        # GLOB.screen.blit(self.image, (self.x + cam.getPositionX(), self.y + cam.getPositionY()))

        # pygame.draw.rect(GLOB.screen, "Purple", self.mesh, 2 * GLOB.MULT)



        if self.angle >= 360:
            self.angle = 0

        if self.angle <= -1:
            self.angle = 359

    def ruota_destra(self):
        self.angle += 1

    def ruota_sinistra(self):
        self.angle -= 0.25 * GLOB.MULT

    def aumenta_distanza(self):
        self.distanza += 0.25 * GLOB.MULT

    def diminuisci_distanza(self):
        self.distanza -= 0.25 * GLOB.MULT

    def aumenta_lunghezza(self):
        self.default_height += 0.025 * GLOB.MULT

    def diminuisci_lunghezza(self):
        self.default_height -= 0.025 * GLOB.MULT

    def attacca(self, v):
        GLOB.MonsterCanAttack = v

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

                if self.mesh.right >= object.right:
                    self.x += GLOB.Monster_speed + GLOB.MULT
                    self.collision_state["right"] = True
                    self.flag_movement["left"] = False

                    
                elif self.mesh.left <= object.left:
                    self.x -= GLOB.Monster_speed + GLOB.MULT
                    self.collision_state["left"] = True
                    self.flag_movement["right"] = False



            if value=="y":

                if self.mesh.bottom >= object.bottom:
                    self.y += GLOB.Monster_speed + GLOB.MULT
                    self.collision_state["bottom"] = True
                    self.flag_movement["up"] = False
                    
                elif self.mesh.top <= object.top:
                    self.y -= GLOB.Monster_speed + GLOB.MULT
                    self.collision_state["top"] = True
                    self.flag_movement["down"] = False

            

        if self.mesh.colliderect(object):

            self.finish()
            
            self.delay_movement.ReStart()
            
            self.ICollide = True
            
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
                    self.Last_keyPressed = "Null"

                    
                if (c1 or d1) and (not a1 and not b1):

                    Confronta("y")
                    self.Last_keyPressed = "Null"
                    

                if (self.getRightPress() or self.getLeftPress() or a or d) and (not w and not s):
                    Confronta("x")
                
                if (self.getUpPress() or self.getDownPress() or w or s) and (not d and not a):
                    Confronta("y")
            else:
                Confronta("y")
                Confronta("x")
            #self.setAllkeys(None)
            
        else:
            
            self.ICollide = False
            
            self.collision_state = {
                
                "top": False,
                "bottom": False,
                "left": False,
                "right": False,
                
            }
            
            self.monster_ai_vel = self.default_monster_ai_vel