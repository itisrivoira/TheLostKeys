import random
import pygame, os
import global_var as GLOB
from pygame import mixer
from components import Delay


class Player():
    def __init__(self):

        #stato attuale dell'animazione
        self.__normal_speed = 0.3
        self.__run_speed = 0.45
        
        self.setIsWalking(False)
        self.setIsRunning(False)

        self.ombra = pygame.image.load("assets/ombra.png").convert_alpha()
        self.ombra = pygame.transform.scale(self.ombra, (self.ombra.get_width()*GLOB.MULT/GLOB.Player_proportion,self.ombra.get_height()*GLOB.MULT/GLOB.Player_proportion))

        #indicazione posizione (dinamica)
        self.setPositionX(GLOB.PlayerXSpawn)
        self.setPositionY(GLOB.PlayerYSpawn)

        #indicazione velocità (dinamica)
        self.setVelocitaX(0)
        self.setVelocitaY(0)

        #pulsanti cliccati si/no
        self.setLeftPress(False)
        self.setRightPress(False)
        self.setUpPress(False)
        self.setDownPress(False)

        self.Last_keyPressed = "Null"

        self.collision_state = {'top': False, 'bottom': False, 'left': False, 'right': False}
        self.movement_state = {'up': False, 'down': False, 'left': False, 'right': False,}

        #hitbox del player
        self.setHitbox()

        # mesh del giocatore
        self.mesh = pygame.Rect(self.hitbox)

        self.value_surface = 46 * GLOB.MULT

        # animazione di walking
        path = GLOB.Default_characters_path + GLOB.scelta_char
        self.animationWOR = GLOB.load_images(path + "/WalkOrizontal")
        self.current_spriteWOR = 0.9
        
        self.animationWOL = [pygame.transform.flip(image, True, False) for image in self.animationWOR]
        self.current_spriteWOL = 0.9

        self.animationWVD = GLOB.load_images(path+ "/WalkVerticalD")
        self.current_spriteWVD = 0.9

        self.animationWVU = GLOB.load_images(path + "/WalkVerticalU")
        self.current_spriteWVU = 0.9
        
        self.animationIdle = GLOB.load_images(path + "/Idle")
        self.current_spriteIdle = 0
        
        # setta l'immagine di animazione attuale di walking
        self.image = self.animationIdle[0]

        # setta a video l'immagine del giocatore
        self.character = self.image
        self.width, self.height = self.character.get_size()

        # Evento Interazione Oggetti
        self.evento = None
        
        self.soundsFootsteps = [mixer.Sound("suoni/footstep1.wav"),  mixer.Sound("suoni/footstep2.wav")]
        
        self.flag_delay = True
        self.setDelay(0.3)
        
        self.__animation_speed = self.__normal_speed
        

# ---------- self.set() ----------

    def setDelay(self, v):
        if self.flag_delay:
            self.delay_sound = Delay(v, self.__playSounds)
            self.flag_delay = False
        
        
    def __playSounds(self):
        passo = random.choice(self.soundsFootsteps)
        passo.set_volume(0.02*GLOB.AU)
        
        if not GLOB.isPaused:
            passo.play()


    def setPositionX(self, x):
        self.x = x

    def setPositionY(self, y):
        self.y = y

    def setVelocitaX(self, x):
        self.__velX = x

    def setVelocitaY(self, y):
        self.__velY = y

    def setIsWalking(self, val):
        self.__is_walking = val

    def setIsRunning(self, val):
        if val and GLOB.PlayerCanRun:
            self.setAnimationSpeed(self.__run_speed)
        else:
            self.setAnimationSpeed(self.__normal_speed)
            
        self.__is_running = val and GLOB.PlayerCanRun

    def setRightPress(self, r):
        self.__right_pressed = r

    def setLeftPress(self, l):
        self.__left_pressed = l

    def setUpPress(self, u):
        self.__up_pressed = u

    def setDownPress(self, d):
        self.__down_pressed = d

    def setAllkeys(self, v):
        
        if (v != True and v != False):
            return

        self.setUpPress(v)
        self.setDownPress(v)
        self.setLeftPress(v)
        self.setRightPress(v)

    def setAnimationSpeed(self, s):
        self.__animation_speed = s


# ---------- self.get() ----------

    def getPositionX(self):
        return self.x

    def getPositionY(self):
        return self.y

    def getVelocitaX(self):
        return self.__velX

    def getVelocitaY(self):
        return self.__velY

    def getRightPress(self):
        return self.__right_pressed

    def getLeftPress(self):
        return self.__left_pressed

    def getUpPress(self):
        return self.__up_pressed

    def getDownPress(self):
        return self.__down_pressed

    def getIsWalking(self):
        return self.__is_walking

    def getIsRunning(self):
        return self.__is_running

    def getAnimationSpeed(self):
        return self.__animation_speed

    def getHitCollision(self, var):
        self.collision_state = {'top': self.flag_top, 'bottom': self.flag_bottom, 'left': self.flag_left, 'right': self.flag_right}
        return self.collision_state[var]

    # aggiorna a schermo l'immagine attuale del Player
    def character_update(self):
        if self.getIsWalking():

            u = self.getUpPress() or self.Last_keyPressed == "Up"
            d = self.getDownPress() or self.Last_keyPressed == "Down"
            l = self.getLeftPress() or self.Last_keyPressed == "Left"
            r = self.getRightPress() or self.Last_keyPressed == "Right"

            if d and not u:
                self.current_spriteWVD += self.getAnimationSpeed() / GLOB.Delta_Time

                if self.current_spriteWVD >= len(self.animationWVD):
                    self.current_spriteWVD = 0.9
            
                self.image = self.animationWVD[int(self.current_spriteWVD)]

            elif u and not d:
                self.current_spriteWVU += self.getAnimationSpeed() / GLOB.Delta_Time

                if self.current_spriteWVU >= len(self.animationWVU):
                    self.current_spriteWVU = 0.9
                
                self.image = self.animationWVU[int(self.current_spriteWVU)]
                
            elif l and not r:
                self.current_spriteWOL += self.getAnimationSpeed() / GLOB.Delta_Time
                if self.current_spriteWOL >= len(self.animationWOL) or self.getRightPress():
                    self.current_spriteWOL = 0.9

                self.image = self.animationWOL[int(self.current_spriteWOL)]
        
            elif r and not l:
                self.current_spriteWOR += self.getAnimationSpeed() / GLOB.Delta_Time

                if self.current_spriteWOR >= len(self.animationWOR) or self.getLeftPress():
                    self.current_spriteWOR = 0.9
                    
                self.image = self.animationWOR[int(self.current_spriteWOR)]

            else:
                self.finish()

    def HasCollision(self, object):

        def Confronta(value):

            if value=="x":

                if self.mesh.right >= object.right:
                    self.x += GLOB.Player_speed
                    self.setLeftPress(False)
                    self.collision_state["right"] = True
                elif self.mesh.left <= object.left:
                    self.x -= GLOB.Player_speed
                    self.setRightPress(False)
                    self.collision_state["left"] = True

            if value=="y":

                if self.mesh.bottom >= object.bottom:
                    self.y += GLOB.Player_speed
                    self.setUpPress(False)
                    self.collision_state["bottom"] = True
                elif self.mesh.top <= object.top:
                    self.y -= GLOB.Player_speed
                    self.setDownPress(False)
                    self.collision_state["top"] = True
            

        if self.mesh.colliderect(object):

            self.finish()
            
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

        else:
            if (self.current_spriteWOL or self.current_spriteWOR or self.current_spriteWVD or self.current_spriteWVU) > 0.9:
                self.collision_state["top"] = False
                self.collision_state["bottom"] = False
                self.collision_state["left"] = False
                self.collision_state["right"] = False

    def HasInteraction(self, chunk_render, object, var):
        
        self.evento = None

        if chunk_render.colliderect(object):
            
            GLOB.PlayerTextInteract = "Interagisci"
            
            # -- PIANO --
            start_id = 127
            var_max = 2

            if var == 128:
                self.evento = "piano-1"

            elif var == 129:
                self.evento = "piano-2"

            elif var == 130:
                self.evento = "piano-3"

            # -- CHIAVETTE --


            start_id = GLOB.chiavetta_start
            var_max = 11

            for i in range(var_max):
                if var == (start_id + i):
                    self.evento = "chiavetta-"+str(i+1)


            # -- VITTORIA --

            if var == 138:
                self.evento = "vittoria"
                
                
            if var == 127 or var == 131:
                GLOB.PlayerTextInteract = "Apri"
                
                
            start_id = 112
            var_max = 14

            for i in range(var_max):
                if var == (start_id + i):
                    GLOB.PlayerTextInteract = "Apri"
                    
                    
            if var >= 56 and var <= 111:
                GLOB.PlayerTextInteract = "Risolvi"
                
                if GLOB.Stanza == "Archivio":
                    GLOB.PlayerTextInteract = "Ispeziona"
                
                
            if var >= 56 and var <= 111 and (GLOB.Piano == "3-SecondoPiano" or GLOB.Piano == "2-PrimoPiano")  and "Corridoio" in GLOB.Stanza:
                GLOB.PlayerTextInteract = "Esamina"
                
                
            if var == 132:
                GLOB.PlayerTextInteract = "Nasconditi" if not GLOB.PlayerIsHidden else "Esci"
                
                
            if var == 133:
                GLOB.PlayerTextInteract = "Ispeziona"
                
                if GLOB.Stanza == "Generatore":
                    GLOB.PlayerTextInteract = "Riattiva" if not GLOB.corrente else "Disattiva"
                
            if var == 134:
                GLOB.PlayerTextInteract = "Analizza"
                
                
            if var == 136 or var == 137:
                GLOB.PlayerTextInteract = "Cerca"
                
                if "Lab" in GLOB.Stanza:
                    GLOB.PlayerTextInteract = "Esamina"
                
            if var == 126:
                GLOB.PlayerTextInteract = "Guarda"
                
                
            if (var == 134 or var == 135) or (GLOB.Stanza == "WC-Femmine" and (var == 97 or var == 88)):
                GLOB.PlayerTextInteract = "Usa"
            
            
            if GLOB.PlayerInteract and GLOB.PlayerCanMove:

                # -- PIANO SEGRETO --

                if var == 127:
                    self.evento = "piano-0"

                elif var == 131:
                    self.evento = "piano-4"

                # -- PC --

                if var == 134:
                    self.evento = "pc"

                # -- PORTE --

                start_id = 112
                var_max = 14

                for i in range(var_max):
                    if var == (start_id + i):
                        self.evento = "porta-"+str(i)                

                # -- EVENTO --

                if var >= 56 and var <= 111:
                    self.evento = "enigma"


                # -- NASCONDIGLIO --

                if var == 132:
                    self.evento = "nascondiglio"
                    
                
                # -- DIALOGHI --
                if var == 133:
                    self.evento = "ispeziona"


                # -- CODICE --
                if var == 135:
                    self.evento = "codice"


                #-- CERCA --

                if var == 136:
                    self.evento = "cerca-T"
                elif var == 137:
                    self.evento = "cerca-F"


                # -- PLANIMETRIA --

                elif var == 126:
                    self.evento = "mappa"

                GLOB.PlayerInteract = False

                if GLOB.Debug:
                    print("Player: ", var, self.evento, GLOB.Stanza, GLOB.Piano)
                    print("Keeper: ", GLOB.MonsterActualRoom, GLOB.MonsterActualFloor)

    def update(self):        

        self.movement_state = {'up': self.getUpPress(), 'down': self.getDownPress(), 'left': self.getLeftPress(), 'right': self.getRightPress()}
        
        self.setIsRunning(GLOB.PlayerIsRunning)

        self.setVelocitaX(0)
        self.setVelocitaY(0)

        getUp = self.getUpPress()
        getDown = self.getDownPress()
        getLeft = self.getLeftPress()
        getRight = self.getRightPress()

        GLOB.PLayerMovement = {
            
            "up": getUp, 
            "down": getDown, 
            "left": getLeft, 
            "right": getRight, 
            
            
        }    
        
        if list(self.movement_state.values()).count(True) > 0:
            self.setIsWalking(True)
            self.character_update()

        if (getLeft and not getRight):
            self.setVelocitaX(-GLOB.Player_speed)
        
        if (getRight and not getLeft):
            self.setVelocitaX(GLOB.Player_speed)

        if (getUp and not getDown):
            self.setVelocitaY(-GLOB.Player_speed)

        if (getDown and not getUp):
            self.setVelocitaY(GLOB.Player_speed)

        if (getLeft and getRight) or (getUp and getDown) or list(self.movement_state.values()).count(True) > 2:
            self.finish()
            
        if list(self.movement_state.values()).count(True) > 0 and (self.getIsWalking() or self.getIsRunning() and (GLOB.PLayerMovement["up"] or GLOB.PLayerMovement["down"] or GLOB.PLayerMovement["right"] or GLOB.PLayerMovement["left"])):
            self.delay_sound.Infinite()
        else:
            self.delay_sound.Stop()
            
        if not GLOB.isPaused:
            if not GLOB.PlayerIsMoving and list(self.movement_state.values()).count(True) == 0:
                self.current_spriteIdle += (self.getAnimationSpeed() / 2.4) / GLOB.Delta_Time
            
                if self.current_spriteIdle >= len(self.animationIdle):
                        self.current_spriteIdle = 0
                        
                self.image = self.animationIdle[int(self.current_spriteIdle)]
                
        self.character = self.image
        

        self.x += self.getVelocitaX()
        self.y += self.getVelocitaY()
    
        GLOB.screen.blit(self.ombra, (self.x , self.y-2.5*GLOB.MULT/GLOB.Player_proportion))
        GLOB.screen.blit(self.character, (self.x , self.y))
        self.setHitbox()
        
        self.movement_state = {'up': self.getUpPress(), 'down': self.getDownPress(), 'left': self.getLeftPress(), 'right': self.getRightPress()}
        
        GLOB.PlayerIsMoving = list(self.movement_state.values()).count(True) > 0 and (self.getVelocitaX() != 0 or self.getVelocitaY() != 0)

    def setHitbox(self):
        self.hitbox = (self.x + 20 * GLOB.MULT /GLOB.Player_proportion, self.y + 35 * GLOB.MULT /GLOB.Player_proportion, 15 * GLOB.MULT /GLOB.Player_proportion, 10 * GLOB.MULT /GLOB.Player_proportion)
        self.mesh = pygame.Rect(self.hitbox)

    def animate(self):
        self.setIsWalking(True)

    def finish(self):
        self.setIsWalking(False)
        self.setVelocitaX(0)
        self.setVelocitaY(0)
        
        GLOB.PlayerIsMoving = False
        self.current_spriteWOL = 0.9
        self.current_spriteWOR = 0.9
        self.current_spriteWVD = 0.9
        self.current_spriteWVU = 0.9
        
        self.character = self.animationIdle[0]

    def load_playerSurface(self):
        img_copy = self.character.subsurface(pygame.Rect(0, 0, self.character.get_width(), self.value_surface))
        
        GLOB.screen.blit(img_copy, (self.getPositionX(), self.getPositionY()))