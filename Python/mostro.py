import pygame, random, os, re
from components import Delay
import global_var as GLOB
import main
from pygame import mixer

sceltaG = "Keeper"

Folder_walkO = 'Characters/'+sceltaG+'/WalkOrizontal'
Folder_walkVD = 'Characters/'+sceltaG+'/WalkVerticalD'
Folder_walkVU = 'Characters/'+sceltaG+'/WalkVerticalU'
Folder_angry = 'Characters/'+sceltaG+'/Angry'
Folder_idle = 'Characters/'+sceltaG+'/Idle'


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
            
        if percorso == Folder_idle:
            GLOB.MonsterIdle.append(filename)

riempi(Folder_walkO)
riempi(Folder_walkVD)
riempi(Folder_walkVU)
riempi(Folder_angry)
riempi(Folder_idle)


class Keeper():
    def __init__(self, pos, wh):
        self.x = pos[0]
        self.y = pos[1]
        self.width = wh[0]
        self.height = wh[1]
        self.default_height = self.height
        self.line_vector = pygame.math.Vector2(1, 0)
        self.angle = 90

        self.monster_ai_vel = 0.5
        self.default_monster_ai_vel = self.monster_ai_vel
        self.monster_ai_brain = 0
        self.delay_monster = Delay(self.monster_ai_vel, self.__setBrain)
        self.Last_keyPressed = "Null"

        self.distanza = 90

        self.altezza_rect = 20 * GLOB.MULT

        self.aggr = GLOB.MonsterAggr
        self.IseePlayer = GLOB.MonsterHasSeenPlayer
        self.IAttacking = GLOB.MonsterIsAttacking

        self.direzione = ""

        self.flag_CanStartAttack = False

        self.valore_distanza = 300 * GLOB.MULT
        self.setHitbox()

        self.__left_pressed = False
        self.__right_pressed = False
        self.__up_pressed = False
        self.__down_pressed = False

        self.superfice = pygame.Surface((GLOB.screen_width, GLOB.screen_height))        
        
        self.start_valueAnimation = 0.7
        self.current_spriteI = self.start_valueAnimation
        self.current_spriteWO = self.start_valueAnimation
        self.current_spriteWVU = self.start_valueAnimation
        self.current_spriteWVD = self.start_valueAnimation
        self.current_spriteAngry = self.start_valueAnimation
        
        self.Name_animationIdle= Folder_idle
        self.Name_animationWVD = Folder_walkVD
        self.Name_animationWVU = Folder_walkVU
        self.Name_animationWO = Folder_walkO
        self.Name_animationAngry = Folder_angry
        
        self.respiro = mixer.Sound("suoni/Respiro.wav")
        self.chain = mixer.Sound("suoni/chain.wav")
        
        self.velocita_sprite = 0.15 * GLOB.Monster_default_speed / 2
        self.default_vel_sprite = self.velocita_sprite
        
        self.flag_coll = False
        
        self.image = pygame.image.load(Folder_idle + "/" + GLOB.MonsterIdle[0]).convert_alpha()
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
        
        self.delay_movement = Delay(0.2, self.__setMovement)
        
        mult = 1.2
        self.ombra = pygame.image.load("assets/ombra.png").convert_alpha()
        self.ombra = pygame.transform.scale(self.ombra, (self.ombra.get_width()*GLOB.MULT/GLOB.Player_proportion * mult,self.ombra.get_height()*GLOB.MULT/GLOB.Player_proportion * mult))
        
        self.delay_aggr = Delay(0.2, self.__setTraslazione)
        
        self.contatore_collisioni = 0
        self.max_val_cont = 10

        self.diff = 1
        self.evento = None
        self.flag_interact = False
        
        self.delayInteract = Delay(3, self.__setInteraction)
        
        self.__setBrain()
        self.monster_ai_brain = 0


    def __setInteraction(self):
        if not self.flag_interact:
            self.flag_interact = True


    def __setTraslazione(self):
        if self.flag_coll:
            self.flag_coll = False

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
        
        self.monster_ai_vel = random.randint(0, 50)/10
        
        if not self.flag_coll:
            lista_valori = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
        else:
            lista_valori = [1, 2, 3, 4]
            self.monster_ai_vel = random.randint(7, 10)/10
            
        
        self.delay_aggr = Delay(self.monster_ai_vel, self.__setTraslazione)
        self.delay_monster = Delay(self.monster_ai_vel, self.__setBrain)
            
        self.monster_ai_brain = random.choice(lista_valori)
        
    def character_update(self, c):
        
        if not GLOB.isPaused:
            flag = False
            
            if c == 0:
                
                if self.current_spriteI == self.start_valueAnimation + 0.05 and not self.flag_coll:
                    self.respiro.set_volume(0.005 * GLOB.AU)
                    
                    if not GLOB.isPaused:
                        self.respiro.play()
                
                self.current_spriteI += 0.05 / GLOB.Delta_Time
                
                if self.current_spriteI >= len(GLOB.MonsterIdle):
                    self.current_spriteI = self.start_valueAnimation
                    self.respiro.fadeout(1000)
                
                immagine = GLOB.MonsterIdle[int(self.current_spriteI)]
                self.image = pygame.image.load(Folder_idle + "/" + immagine).convert_alpha()
                
            else:
                self.current_spriteI = self.start_valueAnimation
                self.respiro.fadeout(1000)
            

            if c == 1:
                self.current_spriteWO += self.velocita_sprite
                
                if self.current_spriteWO >= len(GLOB.MonsterWO):
                    self.current_spriteWO = self.start_valueAnimation
                    flag = True
                
                immagine = GLOB.MonsterWO[int(self.current_spriteWO)]
                self.image = pygame.image.load(Folder_walkO + "/" + immagine).convert_alpha()
        
            if c == 2:
                self.current_spriteWO += self.velocita_sprite
                
                if self.current_spriteWO >= len(GLOB.MonsterWO):
                    self.current_spriteWO = self.start_valueAnimation
                    flag = True
                
                immagine = pygame.image.load(Folder_walkO + "/" + GLOB.MonsterWO[int(self.current_spriteWO)]).convert_alpha()
                immagine_flip = pygame.transform.flip(immagine, True, False)
                self.image = immagine_flip
                
            if c == 3:
                self.current_spriteWVD += self.velocita_sprite
                
                if self.current_spriteWVD >= len(GLOB.MonsterWVD):
                    self.current_spriteWVD = self.start_valueAnimation
                    flag = True
                
                immagine = GLOB.MonsterWVD[int(self.current_spriteWVD)]
                self.image = pygame.image.load(Folder_walkVD + "/" + immagine).convert_alpha()
                
            if c == 4:
                self.current_spriteWVU += self.velocita_sprite
                
                if self.current_spriteWVU >= len(GLOB.MonsterWVU):
                    self.current_spriteWVU = self.start_valueAnimation
                    flag = True
                
                immagine = GLOB.MonsterWVU[int(self.current_spriteWVU)]
                self.image = pygame.image.load(Folder_walkVU + "/" + immagine).convert_alpha()
                
            if flag:
                self.chain.set_volume(0.005 * GLOB.AU)
                if not GLOB.isPaused:
                    self.chain.play()
            else:
                self.chain.fadeout(3000)
                
            if c == 5 and not self.flag_CanStartAttack:
                
                self.monster_ai_brain = -1

                if not GLOB.isPaused:
                    self.current_spriteAngry += 0.2 / GLOB.Delta_Time
                    self.Sound_Angry.fadeout(2900)
                
                if self.current_spriteAngry >= len(GLOB.MonsterAngry) or self.monster_ai_brain != -1:
                    self.flag_CanStartAttack = True
                    self.current_spriteAngry = self.start_valueAnimation
                    self.contatore_collisioni = 0
                    
                if self.current_spriteAngry >= len(GLOB.MonsterAngry) - 2:
                    self.Sound_Angry.fadeout(2900)
                    
                if self.current_spriteAngry >= 4 and self.current_spriteAngry < 4.2:
                    self.Sound_Angry.set_volume(0.2 * GLOB.AU)
                    if not GLOB.isPaused:
                        self.Sound_Angry.play()
                    
                if self.current_spriteAngry >= 7:
                    main.cam.screen_shake()
                
                immagine = GLOB.MonsterAngry[int(self.current_spriteAngry)]
                self.image = pygame.image.load(Folder_angry + "/" + immagine).convert_alpha()
                
            if self.current_spriteAngry > self.start_valueAnimation and self.monster_ai_brain != -1:
                self.current_spriteAngry = self.start_valueAnimation
            
                        
    def finish(self):
        GLOB.setMonster()
        self.character_update(0)
        self.image = pygame.transform.scale(self.image, (self.char_w, self.char_h))


    def trackMovement(self):
        GLOB.Monster_speed = GLOB.Monster_default_speed * GLOB.MonsterRun_speed
                
        self.velocita_sprite = self.default_vel_sprite + 0.05 / GLOB.Delta_Time
        
        val = 0
            
        if self.mesh.right > main.player.mesh.right - 2 * GLOB.MULT:
            self.x -= GLOB.Monster_speed
            self.direzione = "sinistra"              
            val = 2


        elif self.mesh.left < main.player.mesh.left + 2 * GLOB.MULT:
            self.x += GLOB.Monster_speed
            self.direzione = "destra"
            val = 1


        if self.mesh.bottom > main.player.mesh.bottom + 2 * GLOB.MULT:
            self.y -= GLOB.Monster_speed
            self.direzione = "alto"
            val = 4


        elif self.mesh.top < main.player.mesh.top - 2 * GLOB.MULT:
            self.y += GLOB.Monster_speed
            self.direzione = "basso"
            val = 3
            
            
        if self.ICollide and not GLOB.PlayerIsMoving:
            val = 0
            
            
        self.monster_ai_brain = val
        
        
        self.Last_keyPressed = "Null"


    def randomMovement(self):
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
        
        if self.monster_ai_brain == 3 or self.monster_ai_brain == 0:
            self.direzione = "basso"
            self.Last_keyPressed = "Down"
            self.angle = 225
        
        if self.monster_ai_brain == 4:
            self.direzione = "alto"
            self.Last_keyPressed = "Up"
            self.angle = 45


        # -- DESTRA --
        if ((self.monster_ai_brain == 1 or self.monster_ai_brain == 1.5 or self.monster_ai_brain == 4.5)):
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
            
    def load_monsterSurface(self):
        self.surface = pygame.Surface((self.char_w, self.value_surface), pygame.SRCALPHA)

        self.surface.blit(self.image, (0, 0))
        GLOB.screen.blit(self.surface, (self.x + main.cam.getPositionX(), self.y + main.cam.getPositionY()))

        if self.aggr:
            GLOB.screen.blit(self.luce_image, (self.x + main.cam.getPositionX(), self.y + main.cam.getPositionY()))

        if GLOB.Debug:
            pygame.draw.rect(GLOB.screen, "Green", self.mesh, GLOB.MULT)


    def update(self):
        radius = 360
        
        # CALCOLO VISUALE PERFIFERICA MOSTRO
        self.line_vector = pygame.math.Vector2(self.height, 0)
        
        rot_vector = self.line_vector.rotate(self.angle) * radius
        rot_vector1 = self.line_vector.rotate(self.angle + self.distanza) * radius

        distanza = (17 * GLOB.MULT, 18 * GLOB.MULT)

        start_line = round(self.x + self.width/2 + distanza[0] + main.cam.getPositionX()), round(self.y + main.cam.getPositionY() + distanza[1])
        end_line = round(self.x + self.width/2 + distanza[0] - rot_vector.x + main.cam.getPositionX()), round(self.y - rot_vector.y + main.cam.getPositionY() + distanza[1])


        end_line1 = round(self.x + self.width/2 + distanza[0] - rot_vector1.x + main.cam.getPositionX()), round(self.y - rot_vector1.y + main.cam.getPositionY() + distanza[1])
        
        
        if not GLOB.isPaused:
        
            # GIOCATORE NASCOSTO
            
            if GLOB.PlayerIsHidden and not self.IseePlayer:
                self.aggr = False
                self.flag_CanStartAttack = False
                self.IAttacking = False
                
                
            if not self.IseePlayer:
                self.delayInteract.Infinite()
                
                
            self.superfice.fill(pygame.SRCALPHA)
            
            # CALCOLO VELOCITA TILES DI GIOCATORE - KEEPER
            self.velocitaTilesM = round(((24 * GLOB.MULT) / GLOB.Monster_speed) / GLOB.FPS, 2)
            self.velocitaTilesG = round(((24 * GLOB.MULT) / GLOB.Player_speed) / GLOB.FPS, 2)
            
            # CALCOLO DISTANZA GIOCATORE <--> KEEPER
            self.lung = round((abs(main.player.mesh.centerx - self.mesh.centerx) + abs(main.player.mesh.centery - self.mesh.centery))/2, 6)
            self.diff = round(((self.lung / GLOB.MULT / GLOB.Monster_speed) / (7 / GLOB.MULT)), 2)
            
            self.inspector_area = pygame.draw.circle(self.superfice, "Orange", (self.x + self.image.get_width()/2 + main.cam.getPositionX(), self.y + self.image.get_height()/2 + main.cam.getPositionY()), self.valore_distanza/2, 0)    
            self.proximity_area = pygame.draw.circle(self.superfice, "Yellow", (self.x + self.image.get_width()/2 + main.cam.getPositionX(), self.y + self.image.get_height()/2 + main.cam.getPositionY()), self.valore_distanza/5, 0)    
            
            
            if self.inspector_area.colliderect(main.player.mesh) and GLOB.PlayerIsRunning and GLOB.PlayerIsMoving and GLOB.PlayerCanRun and not self.IseePlayer and not GLOB.PlayerIsHidden and GLOB.MonsterCanAttack:
                self.IseePlayer = True
                
            if self.proximity_area.colliderect(main.player.mesh) and not self.IseePlayer and not self.IseePlayer and not GLOB.PlayerIsHidden and GLOB.MonsterCanAttack:
                self.IseePlayer = True
                self.aggr = True
                self.IAttacking = True
            

            # SE IL FLAG DELL'ANIMAZIONE E' FALSE ALLORA AGGIORNA LA DIFFERENZA DI SECONDI
            if main.animazione.iFinished:
                GLOB.SecondDiffPos = self.diff
                

            # IMPOSTA HITBOX E STARTA IL DELAY DELLE COLLISIONI
            self.setHitbox()
            self.delay_movement.Start()

            
            if int(self.monster_ai_brain):
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

            # STAMPA VISUALE PERIFERICA
            self.triangle = pygame.draw.polygon(surface=self.superfice, color=(255, 0, 0), points=[end_line, end_line1, start_line], width=0)
            
            if self.IseePlayer and GLOB.MonsterCanAttack:
                self.circle = pygame.draw.circle(self.superfice, "Red", (self.x + self.image.get_width()/2 + main.cam.getPositionX() + distanza[0], self.y + self.image.get_height()/2 + main.cam.getPositionY() + distanza[1]), self.valore_distanza, 0)    
            
            # STAMPA DISTANZA GIOCATORE <--> MOSTRO
            self.line = pygame.draw.line(self.superfice, "#2a9df4", (self.mesh.centerx, self.mesh.centery), (main.player.mesh.centerx, main.player.mesh.centery), GLOB.MULT)

            self.superfice.set_alpha(self.transparenza)
            
            if self.IseePlayer and GLOB.MonsterCanAttack and not self.IAttacking:
                self.character_update(5)
                
            if self.flag_CanStartAttack and GLOB.MonsterCanAttack:
                self.monster_ai_brain = 0
                self.height = 0
                self.aggr = True
                self.IAttacking = True
                self.flag_CanStartAttack = False

            if (self.triangle.colliderect(main.player.hitbox)) and GLOB.MonsterCanAttack and not GLOB.PlayerIsHidden or (self.IseePlayer and not self.IAttacking):
                self.IseePlayer = True

            else:
                self.height = self.default_height

                self.delay_monster.Infinite()
                self.delay_aggr.Infinite()


            if GLOB.ShowMonsterRange or GLOB.Debug:
                GLOB.screen.blit(self.superfice, (0, 0))
                

            if self.mesh.colliderect(main.player.hitbox) and GLOB.MonsterCanAttack and not GLOB.PlayerIsHidden:
                main.game_over()

            if not self.aggr:
                self.randomMovement()
                self.velocita_sprite = self.default_vel_sprite

            # MODALITA' TRACKING
            
            if self.IAttacking:
                if not self.circle.colliderect(main.player.hitbox):
                    self.IseePlayer = False
                    self.IAttacking = False
                    self.flag_CanStartAttack = False
                    self.aggr = False
                    self.finish()



            if self.contatore_collisioni >= self.max_val_cont:
                self.flag_coll = True
                self.__setBrain()
                self.contatore_collisioni = 0
            
            
            if self.aggr and self.circle.colliderect(main.player.hitbox):
                
                self.IAttacking = True
                
                if self.flag_coll:
                    self.randomMovement()
                else:
                    self.trackMovement()

            else:
                GLOB.setMonster()
                
                
        else:
            self.finish()



        if self.angle >= 360:
            self.angle = 0

        if self.angle <= -1:
            self.angle = 359
            
    
        self.image = pygame.transform.scale(self.image, (self.char_w, self.char_h))
        
        GLOB.screen.blit(self.ombra, (self.x - distanza[0] + 11.2 * GLOB.MULT + main.cam.getPositionX(), self.y-10*GLOB.MULT/GLOB.Player_proportion + main.cam.getPositionY()))
        GLOB.screen.blit(self.image, (self.x + main.cam.getPositionX(), self.y + main.cam.getPositionY()))

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
            
            val = 1
    
            if value=="x":

                if self.mesh.right >= object.right:
                    self.x += GLOB.Monster_speed + val * GLOB.MULT
                    self.collision_state["right"] = True
                    self.flag_movement["left"] = False

                    
                elif self.mesh.left <= object.left:
                    self.x -= GLOB.Monster_speed + val * GLOB.MULT
                    self.collision_state["left"] = True
                    self.flag_movement["right"] = False



            if value=="y":

                if self.mesh.bottom >= object.bottom:
                    self.y += GLOB.Monster_speed + val * GLOB.MULT
                    self.collision_state["bottom"] = True
                    self.flag_movement["up"] = False
                    
                elif self.mesh.top <= object.top:
                    self.y -= GLOB.Monster_speed + val * GLOB.MULT
                    self.collision_state["top"] = True
                    self.flag_movement["down"] = False

            

        if self.mesh.colliderect(object):

            if self.monster_ai_brain != -1:
                
                self.delay_movement.ReStart()
                
                self.ICollide = True
            
            
                if self.aggr:
                    self.contatore_collisioni += 1
                    self.flag_coll = False

                else:
                    self.finish()
                    self.flag_coll = False
                    self.__setBrain()
            
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
            

    def HasInteraction(self, chunk_render, object, var):
        self.evento = None

        if chunk_render.colliderect(object) and self.flag_interact and not self.IAttacking:
            
            # -- PIANO --
            start_id = 127
            var_max = 4
            
            for i in range(var_max):
                if var == (start_id + i):
                    self.evento = "piano-"+str(i)
                

            # -- PORTE --

            start_id = 112
            var_max = 14

            for i in range(var_max):
                if var == (start_id + i):
                    self.evento = "porta-"+str(i)   


            # -- NASCONDIGLIO --

            if var == 132:
                self.evento = "nascondiglio"
                
                
            if GLOB.Debug:
                print(var, self.evento, GLOB.Stanza, GLOB.Piano)

            for i in range(4):
                if self.evento == f"piano-{i}":
                    GLOB.MonsterActualRoom = f"Corridoio{i}"
                    self.evento = None
                    
                if GLOB.MonsterActualRoom == "Corridoio1":
                    GLOB.MonsterActualFloor = "1-PianoTerra"
                elif GLOB.MonsterActualRoom == "Corridoio2":
                    GLOB.MonsterActualFloor = "2-PrimoPiano"
                elif GLOB.MonsterActualRoom == "Corridoio3":
                    GLOB.MonsterActualFloor = "3-TerzoPiano"
                elif GLOB.MonsterActualRoom == "Corridoio0":
                    GLOB.MonsterActualFloor = "0-PianoSegreto"
                    GLOB.MonsterActualRoom = "StanzaSegreta"
                
            self.flag_interact = False