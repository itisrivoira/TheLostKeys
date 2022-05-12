import pygame, os
import global_var as GLOB


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
        
        # setta a video l'immagine del giocatore
        self.character = pygame.image.load(
        os.path.join(self.Name_animationWVD,char_image[0][0])).convert_alpha()

        self.value_surface = 45 * GLOB.MULT

        self.surface = pygame.Surface((self.width, self.value_surface), pygame.SRCALPHA)

        # animazione di walking
        self.animationWO = char_image[2]
        self.current_spriteWOL = 0 # indica il corrente sprite generato e ciclato
        self.current_spriteWOR = 0 # indica il corrente sprite generato e ciclato

        self.animationWVD = char_image[0]
        self.current_spriteWVD = 0

        self.animationWVU = char_image[0]
        self.current_spriteWVU = 0
        
        # setta l'immagine di animazione attuale di walking
        self.image = self.animationWVD[0]

        # Evento Interazione Oggetti
        self.evento = None

# ---------- self.set() ----------

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
        # Controlla se l'animazione è attiva
        if self.getIsWalking():

            u = self.getUpPress() or self.Last_keyPressed == "Up"
            d = self.getDownPress() or self.Last_keyPressed == "Down"
            l = self.getLeftPress() or self.Last_keyPressed == "Left"
            r = self.getRightPress() or self.Last_keyPressed == "Right"

            # LEFT_KEY

            if l and not r:
                #è un float perchè quando arriverà ad un int l'animazione cambiera quindi è come se fosse un delay
                self.current_spriteWOL += self.getAnimationSpeed() / GLOB.Delta_Time
 
                # Controllo di non uscire dal range dei frames possibili
                if self.current_spriteWOL >= len(self.animationWO) or self.getRightPress():
                    self.current_spriteWOL = 0

                # setta l'immagine di animazione attuale di walking
                self.image = self.animationWO[int(self.current_spriteWOL)]


            # RIGHT_KEY

            elif r and not l:
                self.current_spriteWOR += self.getAnimationSpeed() / GLOB.Delta_Time

                if self.current_spriteWOR >= len(self.animationWO)or self.getLeftPress():
                    self.current_spriteWOR = 0
                    
                self.image = self.animationWO[int(self.current_spriteWOR)]


            # DOWN_KEY

            elif d and not u:
                self.current_spriteWVD += self.getAnimationSpeed() / GLOB.Delta_Time

                if self.current_spriteWVD >= len(self.animationWVD):
                    self.current_spriteWVD = 0
            
                self.image = self.animationWVD[int(self.current_spriteWVD)]


            # UP_KEY

            elif u and not d:
                self.current_spriteWVU += self.getAnimationSpeed() / GLOB.Delta_Time

                if self.current_spriteWVU >= len(self.animationWVU):
                    self.current_spriteWVU = 0
                
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
                os.path.join(self.Name_animationWO,self.image)).convert_alpha() # carica l'immagine presa dalla cartella Walk

            if var==3:
                immagine = pygame.image.load(
                os.path.join(self.Name_animationWO,self.image)).convert_alpha()
                self.character = pygame.transform.flip(immagine, True, False) # specchia l'immagine dalle assi x
            
            #print("Sprite WO corrente: "+str(self.current_spriteWO)+" | Sprite WVD corrente: "+str(self.current_spriteWVD)+" | Sprite WVU corrente: "+str(int(self.current_spriteWVU)))

    def HasCollision(self, object):

        def Confronta(value):   # Creo una funziona dato che la utilizzo piu' volte e se gli passo "x" fa una cosa mentre se gli passo "y" ne fa un'altra

            if value=="x":  # confronto il valore passato

                if self.mesh.right >= object.right:  # confronto se la posizione del player delle x è maggiore o uguale della posizione delle x dell'oggetto di cui ho collisione
                    self.x += GLOB.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setLeftPress(False)    # ogni volta che collido dal lato sinistro non posso riandare a ricliccare il pulsante destro
                    self.collision_state["right"] = True
                elif self.mesh.left <= object.left:
                    self.x -= GLOB.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setRightPress(False)    # ogni volta che collido dal lato destro non posso riandare a ricliccare il pulsante sinistro
                    self.collision_state["left"] = True

            if value=="y":  # confronto il valore passato

                if self.mesh.bottom >= object.bottom:  # confronto se la posizione del player delle y è maggiore o uguale della posizione delle y dell'oggetto di cui ho collisione
                    self.y += GLOB.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setUpPress(False)    # ogni volta che collido dal lato basso non posso riandare a ricliccare il pulsante alto
                    self.collision_state["bottom"] = True
                elif self.mesh.top <= object.top:
                    self.y -= GLOB.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setDownPress(False)    # ogni volta che collido dal lato alto non posso riandare a ricliccare il pulsante basso
                    self.collision_state["top"] = True
            

        if self.mesh.colliderect(object):   # Metodo di pygame che confronta se due rettangoli collidono

            self.finish()    # ogni volta che collido stoppo l'animazione del player
            self.character = pygame.transform.scale(self.character, (self.width, self.height))

            # Setto diverse variabili per non ripeterli nei confronti
            w = (self.Last_keyPressed == "Up")
            a = (self.Last_keyPressed == "Left")
            
            s = (self.Last_keyPressed == "Down")
            d = (self.Last_keyPressed == "Right")

            
            a1 = (self.getRightPress() and w or self.getLeftPress() and w)
            b1 =  (self.getLeftPress() and s or self.getRightPress() and s)

            c1 =  (self.getUpPress() and a or self.getDownPress() and a)
            d1 =  (self.getUpPress() and d or self.getDownPress() and d)


            if self.Last_keyPressed != "Null":  # Confronto se il giocatore è fermo o si sta muovendo

                if (a1 or b1) and (not c1 and not d1):  # se è stato premuto il pulsante destro/sinistro e NON quello alto o basso mentre si ha una collisione allora:

                    Confronta("x")  # richiamo la funzione
                    self.Last_keyPressed = "Null"   # Variabile usata per non dare errori dato che l'ultimo pulsante cliccato sono l'insieme di due in contemporanea

                    
                if (c1 or d1) and (not a1 and not b1):  # se è stato premuto il pulsante alto/basso e NON con quello sinistro o destro mentre si ha una collisione allora:

                    Confronta("y")  # richiamo la funzione
                    self.Last_keyPressed = "Null"   # Variabile usata per non dare errori dato che l'ultimo pulsante cliccato sono l'insieme di due in contemporanea
                    

                if (self.getRightPress() or self.getLeftPress() or a or d) and (not w and not s):   # Qua altri confronti con unicamente con un pulante a volta cliccato sinistra/destra
                    Confronta("x")
                
                if (self.getUpPress() or self.getDownPress() or w or s) and (not d and not a):   # Qua altri confronti con unicamente con un pulante a volta cliccato alto/basso
                    Confronta("y")
            else:
                Confronta("y")
                Confronta("x")

        else:
            if (self.current_spriteWOL or self.current_spriteWOR or self.current_spriteWVD or self.current_spriteWVU) > 0:
                self.collision_state["top"] = False
                self.collision_state["bottom"] = False
                self.collision_state["left"] = False
                self.collision_state["right"] = False
            #self.setAllkeys(None)

    def HasInteraction(self, chunk_render, object, var):
        keys_pressed = pygame.key.get_pressed()

        if chunk_render.colliderect(object):

            
            # -- PIANO --

            if var == 127:
                self.evento = "piano-0"

            elif var == 128:
                self.evento = "piano-1"

            elif var == 129:
                self.evento = "piano-2"

            elif var == 130:
                self.evento = "piano-3"

            elif var == 131:
                self.evento = "piano-4"

            # -- CHIAVETTE --

            elif var == GLOB.chiavetta_start:
                self.evento = "chiavetta-1"

            elif var == GLOB.chiavetta_start + 1:
                self.evento = "chiavetta-2"

            elif var == GLOB.chiavetta_start + 2:
                self.evento = "chiavetta-3"

            elif var == GLOB.chiavetta_start + 3:
                self.evento = "chiavetta-4"

            elif var == GLOB.chiavetta_start + 4:
                self.evento = "chiavetta-5"

            elif var == GLOB.chiavetta_start + 5:
                self.evento = "chiavetta-6"

            elif var == GLOB.chiavetta_start + 6:
                self.evento = "chiavetta-7"

            elif var == GLOB.chiavetta_start + 7:
                self.evento = "chiavetta-8"

            elif var == GLOB.chiavetta_start + 8:
                self.evento = "chiavetta-9"

            elif var == GLOB.chiavetta_start + 9:
                self.evento = "chiavetta-10"

            elif var == GLOB.chiavetta_start + 10:
                self.evento = "chiavetta-11"

            elif var == GLOB.chiavetta_start + 11:
                self.evento = "chiavetta-12"


            else:
                self.evento = None
                

            if keys_pressed[pygame.K_e] and GLOB.PlayerCanMove:

                # -- PORTE --

                if var == 112:
                    self.evento = "porta-0"

                elif var == 113:
                    self.evento = "porta-1"

                elif var == 114:
                    self.evento = "porta-2"

                elif var == 115:
                    self.evento = "porta-3"

                elif var == 116:
                    self.evento = "porta-4"

                elif var == 117:
                    self.evento = "porta-5"

                elif var == 118:
                    self.evento = "porta-6"

                elif var == 119:
                    self.evento = "porta-7"

                elif var == 120:
                    self.evento = "porta-8"

                elif var == 121:
                    self.evento = "porta-9"

                elif var == 122:
                    self.evento = "porta-10"

                elif var == 123:
                    self.evento = "porta-11"

                elif var == 124:
                    self.evento = "porta-12"

                elif var == 125:
                    self.evento = "porta-13"

                

                # -- EVENTO --

                elif var >= 56 and var <= 111:
                    self.evento = "enigma"


                # -- PLANIMETRIA --

                elif var == 126:
                    self.evento = "mappa"

                else:
                    self.evento = None

                print(var, self.evento)

    # Funzione che serve ad aggiornare la velocità attuale del giocatore la velocità da' un'impressione Smooth
    def update(self):
        self.setVelocitaX(0)
        self.setVelocitaY(0)

        #print(self.collision_state)

        getUp = self.getUpPress()
        getDown = self.getDownPress()
        getLeft = self.getLeftPress()
        getRight = self.getRightPress()

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
        else:
            slow = 0.15
            normal = 0.4

        if condition_1:
            self.setVelocitaY(-GLOB.Player_speed)
            self.setVelocitaX(GLOB.Player_speed)           
            self.setIsWalking(True)
            self.character_update(1) # richiamo la funzione di aggiorna l'animazione

        if condition_2:
            self.setVelocitaY(GLOB.Player_speed)
            self.setVelocitaX(GLOB.Player_speed)           
            self.setIsWalking(True)
            self.character_update(0) # richiamo la funzione di aggiorna l'animazione

        if condition_3:
            self.setVelocitaY(-GLOB.Player_speed)
            self.setVelocitaX(-GLOB.Player_speed)           
            self.setIsWalking(True)
            self.character_update(1) # richiamo la funzione di aggiorna l'animazione

        if condition_4:
            self.setVelocitaY(GLOB.Player_speed)
            self.setVelocitaX(-GLOB.Player_speed)           
            self.setIsWalking(True)
            self.character_update(1) # richiamo la funzione di aggiorna l'animazione

        if condition_1 or condition_2 or condition_3 or condition_4:
            self.setAnimationSpeed(slow)
        else:
            self.setAnimationSpeed(normal)

        if (getLeft and not getRight):
            self.setVelocitaX(-GLOB.Player_speed)
            self.setIsWalking(True)
            self.character_update(3) # richiamo la funzione di aggiorna l'animazione
        
        if (getRight and not getLeft):
            self.setVelocitaX(GLOB.Player_speed)
            self.setIsWalking(True)
            self.character_update(2) # richiamo la funzione di aggiorna l'animazione

        if (getUp and not getDown):
            self.setVelocitaY(-GLOB.Player_speed)
            self.setIsWalking(True)
            self.character_update(1) # richiamo la funzione di aggiorna l'animazione

        if (getDown and not getUp):
            self.setVelocitaY(GLOB.Player_speed)
            self.setIsWalking(True)
            self.character_update(0) # richiamo la funzione di aggiorna l'animazione

        if (getLeft and getRight) or (getUp and getDown):
            self.finish()

        self.x += self.getVelocitaX()
        self.y += self.getVelocitaY()

        self.mesh = pygame.Rect(self.hitbox) # indico la hitbox (mesh) del Player

        self.character = pygame.transform.scale(self.character, (self.width, self.height)) # ingrandisco (scalo) l'immagine presa dalle cartelle

        GLOB.screen.blit(self.ombra, (self.x , self.y-2.5*GLOB.MULT/GLOB.Player_proportion)) # indica che lo schermo fa nascere il giocatore
        GLOB.screen.blit(self.character, (self.x , self.y)) # indica che lo schermo fa nascere il giocatore
        # self.hitbox = (self.x-60, self.y-55, 200, 180)
        self.setHitbox()

        #print("| Condizione 1: "+str(condition_1)+" | Condizione 2: "+str(condition_2)+" | Condizione 3: "+str(condition_3)+" | Condizione 4: "+str(condition_4))
        #print(self.animation_speed)


    def setHitbox(self):
        self.hitbox = (self.x + 20 * GLOB.MULT /GLOB.Player_proportion, self.y + 35 * GLOB.MULT /GLOB.Player_proportion, 15 * GLOB.MULT /GLOB.Player_proportion, 10 * GLOB.MULT /GLOB.Player_proportion)

    # setta l'animazione della camminata a vera
    def animate(self):
        self.setIsWalking(True)

    # setta l'animazione della camminata a falso e rimette le variabili a default
    def finish(self):
        self.setIsWalking(False)
        self.current_spriteWOL = 0
        self.current_spriteWOR = 0
        self.current_spriteWVD = 0
        self.current_spriteWVU = 0

        # imposta un'animazione di default dopo aver eseguito l'ultima
        self.character = pygame.image.load(
            os.path.join(self.Name_animationWVD,'Walk0.png')).convert_alpha()

    def load_playerSurface(self):
        self.surface = pygame.Surface((self.width, self.value_surface), pygame.SRCALPHA)

        self.surface.blit(self.character, (0, 0))

        GLOB.screen.blit(self.surface, (self.getPositionX(), self.getPositionY()))