import random
import pygame, os
import global_var as GLOB
from pygame import mixer
from components import Delay


"""

    ---  Classe che genera il giocatore e ne controlla i pulsanti cliccati, gli sprite e le collisioni  ---

"""


class Player():
    def __init__(self, x, y, selected, width, height, char_image):

        #stato attuale dell'animazione
        self.setIsWalking(False)

        self.setIsRunning(False)

        #indico il giocatore impostato
        self.Player_selected = selected

        #indico i nomi dei movimenti
        self.Name_animationWO = 'Characters'+self.Player_selected+"/WalkOrizontal"
        self.Name_animationWVD = 'Characters'+self.Player_selected+"/WalkVerticalD"
        self.Name_animationWVU = 'Characters'+self.Player_selected+"/WalkVerticalU"

        self.ombra = pygame.image.load("assets/ombra.png").convert_alpha()
        self.ombra = pygame.transform.scale(self.ombra, (self.ombra.get_width()*GLOB.MULT/GLOB.Player_proportion,self.ombra.get_height()*GLOB.MULT/GLOB.Player_proportion))

        #indicazione posizione (dinamica)
        self.setPositionX(int(x))
        self.setPositionY(int(y))

        #indicazione grandezza (statica)
        self.width = width
        self.height = height

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

        #hitbox del player
        self.setHitbox()

        # mesh del giocatore
        self.mesh = pygame.Rect(self.hitbox)
        
        # setta a video l'immagine del giocatore
        self.character = pygame.image.load(
        os.path.join(self.Name_animationWVD,char_image[0][0])).convert_alpha()

        self.value_surface = 45 * GLOB.MULT

        self.surface = pygame.Surface((self.width, self.value_surface), pygame.SRCALPHA)

        # animazione di walking
        self.animationWO = char_image[2]
        self.current_spriteWOL = 0.9 # indica il corrente sprite generato e ciclato
        self.current_spriteWOR = 0.9 # indica il corrente sprite generato e ciclato

        self.animationWVD = char_image[0]
        self.current_spriteWVD = 0.9

        self.animationWVU = char_image[0]
        self.current_spriteWVU = 0.9
        
        # setta l'immagine di animazione attuale di walking
        self.image = self.animationWVD[0]

        # Evento Interazione Oggetti
        self.evento = None
        
        self.soundsFootsteps = [mixer.Sound("suoni/footstep1.wav"),  mixer.Sound("suoni/footstep2.wav")]
        
        self.flag_delay = True
        self.setDelay(0.3)

# ---------- self.set() ----------

    def setDelay(self, v):
        if self.flag_delay:
            self.delay_sound = Delay(v, self.__playSounds)
            self.flag_delay = False
        
        
    def __playSounds(self):
        passo = random.choice(self.soundsFootsteps)
        passo.set_volume(0.2*GLOB.AU)
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
        self.__is_running = val

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
    def character_update(self,var):
        if self.getIsWalking():

            u = self.getUpPress() or self.Last_keyPressed == "Up"
            d = self.getDownPress() or self.Last_keyPressed == "Down"
            l = self.getLeftPress() or self.Last_keyPressed == "Left"
            r = self.getRightPress() or self.Last_keyPressed == "Right"

            if l and not r:
                self.current_spriteWOL += self.getAnimationSpeed() / GLOB.Delta_Time
 
                if self.current_spriteWOL >= len(self.animationWO) or self.getRightPress():
                    self.current_spriteWOL = 0.9

                self.image = self.animationWO[int(self.current_spriteWOL)]
        
            elif r and not l:
                self.current_spriteWOR += self.getAnimationSpeed() / GLOB.Delta_Time

                if self.current_spriteWOR >= len(self.animationWO) or self.getLeftPress():
                    self.current_spriteWOR = 0.9
                    
                self.image = self.animationWO[int(self.current_spriteWOR)]

            elif d and not u:
                self.current_spriteWVD += self.getAnimationSpeed() / GLOB.Delta_Time

                if self.current_spriteWVD >= len(self.animationWVD):
                    self.current_spriteWVD = 0.9
            
                self.image = self.animationWVD[int(self.current_spriteWVD)]

            elif u and not d:
                self.current_spriteWVU += self.getAnimationSpeed() / GLOB.Delta_Time

                if self.current_spriteWVU >= len(self.animationWVU):
                    self.current_spriteWVU = 0.9
                
                self.image = self.animationWVU[int(self.current_spriteWVU)]

            else:
                self.finish()


            if var==0:
                self.character = pygame.image.load(
                os.path.join(self.Name_animationWVD,self.image)).convert_alpha()

            if var==1:
                self.character = pygame.image.load(
                os.path.join(self.Name_animationWVU,self.image)).convert_alpha()

            if var==2:
                self.character = pygame.image.load(
                os.path.join(self.Name_animationWO,self.image)).convert_alpha()

            if var==3:
                immagine = pygame.image.load(
                os.path.join(self.Name_animationWO,self.image)).convert_alpha()
                self.character = pygame.transform.flip(immagine, True, False)

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
            self.character = pygame.transform.scale(self.character, (self.width, self.height))
            
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
        keys_pressed = pygame.key.get_pressed()
        self.evento = None

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


        if chunk_render.colliderect(object):
            
            if keys_pressed[pygame.K_e] and GLOB.PlayerCanMove:


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


                # -- MACCHINETTA --

                if var == 132:
                    self.evento = "macchinetta"


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

                if GLOB.Debug:
                    print(var, self.evento, GLOB.Stanza, GLOB.Piano)             

    def update(self):
        
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

        condition_1 = getLeft and getUp and not(getRight and getDown)
        condition_2 = getLeft and getDown and not(getRight and getUp)
        condition_3 = getRight and getUp and not(getLeft and getDown)
        condition_4 = getRight and getDown and not(getLeft and getUp)

        slow = 0.15
        normal = 0.4
        run = 1.35

        if self.getIsRunning():
            slow *= run
            normal *= run
            self.setDelay(normal / (run * 2))
        else:
            slow = 0.15
            normal = 0.4
            self.setDelay(normal-0.1)

        if condition_1:
            self.setVelocitaY(-GLOB.Player_speed)
            self.setVelocitaX(GLOB.Player_speed)           
            self.setIsWalking(True)
            self.character_update(1)

        if condition_2:
            self.setVelocitaY(GLOB.Player_speed)
            self.setVelocitaX(GLOB.Player_speed)           
            self.setIsWalking(True)
            self.character_update(0)

        if condition_3:
            self.setVelocitaY(-GLOB.Player_speed)
            self.setVelocitaX(-GLOB.Player_speed)           
            self.setIsWalking(True)
            self.character_update(1)

        if condition_4:
            self.setVelocitaY(GLOB.Player_speed)
            self.setVelocitaX(-GLOB.Player_speed)           
            self.setIsWalking(True)
            self.character_update(1)

        if condition_1 or condition_2 or condition_3 or condition_4:
            self.setAnimationSpeed(slow)
        else:
            self.setAnimationSpeed(normal)

        if (getLeft and not getRight):
            self.setVelocitaX(-GLOB.Player_speed)
            self.setIsWalking(True)
            self.character_update(3)
        
        if (getRight and not getLeft):
            self.setVelocitaX(GLOB.Player_speed)
            self.setIsWalking(True)
            self.character_update(2)

        if (getUp and not getDown):
            self.setVelocitaY(-GLOB.Player_speed)
            self.setIsWalking(True)
            self.character_update(1)

        if (getDown and not getUp):
            self.setVelocitaY(GLOB.Player_speed)
            self.setIsWalking(True)
            self.character_update(0)

        if (getLeft and getRight) or (getUp and getDown):
            self.finish()
            
        if self.getIsWalking() or self.getIsRunning():
            self.delay_sound.Infinite()
        else:
            self.delay_sound.Stop()

        self.x += self.getVelocitaX()
        self.y += self.getVelocitaY()

        self.mesh = pygame.Rect(self.hitbox)

        self.character = pygame.transform.scale(self.character, (self.width, self.height))

        GLOB.screen.blit(self.ombra, (self.x , self.y-2.5*GLOB.MULT/GLOB.Player_proportion))
        GLOB.screen.blit(self.character, (self.x , self.y))
        self.setHitbox()

    def setHitbox(self):
        self.hitbox = (self.x + 20 * GLOB.MULT /GLOB.Player_proportion, self.y + 35 * GLOB.MULT /GLOB.Player_proportion, 15 * GLOB.MULT /GLOB.Player_proportion, 10 * GLOB.MULT /GLOB.Player_proportion)

    def animate(self):
        self.setIsWalking(True)

    def finish(self):
        self.setIsWalking(False)
        self.current_spriteWOL = 0.9
        self.current_spriteWOR = 0.9
        self.current_spriteWVD = 0.9
        self.current_spriteWVU = 0.9

        self.character = pygame.image.load(
            os.path.join(self.Name_animationWVD,'Walk0.png')).convert_alpha()

    def load_playerSurface(self):
        self.surface = pygame.Surface((self.width, self.value_surface), pygame.SRCALPHA)

        self.surface.blit(self.character, (0, 0))

        GLOB.screen.blit(self.surface, (self.getPositionX(), self.getPositionY()))