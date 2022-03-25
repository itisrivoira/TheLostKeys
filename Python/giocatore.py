import pygame, os
import global_var as GLOB


"""

    ---  Classe che genera il giocatore e ne controlla i pulsanti cliccati, gli sprite e le collisioni  ---

"""


# Creazione della classe Player ed è figlia di sprite +ottimizzata e veloce
class Player(pygame.sprite.Sprite):
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

        self.collision_state = {'top': False, 'bottom': False, 'right': False, 'left': False}

        #hitbox del player
        self.setHitbox()
        
        # setta a video l'immagine del giocatore
        self.character = pygame.image.load(
        os.path.join(self.Name_animationWVD,char_image[0][0])).convert_alpha()

        # animazione di walking
        self.animationWO = char_image[2]
        self.current_spriteWO = 0 # indica il corrente sprite generato e ciclato

        self.animationWVD = char_image[0]
        self.current_spriteWVD = 0

        self.animationWVU = char_image[0]
        self.current_spriteWVU = 0
        
        # setta l'immagine di animazione attuale di walking
        self.image = self.animationWVD[0]

        self.animation_speed = 0.4

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
        self.animation_speed = s

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

    def getAllkeys(self):
        keys = {'Key_Up': self.getUpPress(),'Key_Down': self.getDownPress(),'Key_Left': self.getLeftPress(),'Key_Right': self.getRightPress()}
        return keys

    # aggiorna a schermo l'immagine attuale del Player
    def character_update(self,var):

        # Controlla se l'animazione è attiva
        if self.getIsWalking():

            self.current_spriteWO += self.animation_speed / GLOB.Delta_Time # è un float perchè quando arriverà ad un int l'animazione cambiera quindi è come se fosse un delay
            self.current_spriteWVD += self.animation_speed / GLOB.Delta_Time
            self.current_spriteWVU += self.animation_speed / GLOB.Delta_Time

            # Controllo di non uscire dal range dei frames possibili
            if self.current_spriteWO >= len(self.animationWO):
                self.current_spriteWO = 0

            # setta l'immagine di animazione attuale di walking
            if self.getLeftPress():
                self.image = self.animationWO[int(self.current_spriteWO)]

            if self.current_spriteWVD >= len(self.animationWVD):
                self.current_spriteWVD = 0
            
            self.image = self.animationWVD[int(self.current_spriteWVD)]

            if self.current_spriteWVU >= len(self.animationWVU):
                self.current_spriteWVU = 0
            
            self.image = self.animationWVU[int(self.current_spriteWVU)]

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
            
            self.finish()    # ogni volta che collido stoppo l'animazione del player

            if value=="x":  # confronto il valore passato

                if self.hitbox[0] >= object.x:  # confronto se la posizione del player delle x è maggiore o uguale della posizione delle x dell'oggetto di cui ho collisione
                    self.x += GLOB.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setLeftPress(False)    # ogni volta che collido dal lato sinistro non posso riandare a ricliccare il pulsante destro
                    return True # ritorno un valore perchè dopo lo vado ad utilizzare
                elif self.hitbox[2] <= object.x:
                    self.x -= GLOB.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setRightPress(False)    # ogni volta che collido dal lato destro non posso riandare a ricliccare il pulsante sinistro
                    return False # ritorno un valore perchè dopo lo vado ad utilizzare

            if value=="y":  # confronto il valore passato

                if self.hitbox[1] >= object.y:  # confronto se la posizione del player delle y è maggiore o uguale della posizione delle y dell'oggetto di cui ho collisione
                    self.y += GLOB.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setUpPress(False)    # ogni volta che collido dal lato basso non posso riandare a ricliccare il pulsante alto
                    return True # ritorno un valore perchè dopo lo vado ad utilizzare
                elif self.hitbox[3] <= object.y:
                    self.y -= GLOB.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setDownPress(False)    # ogni volta che collido dal lato alto non posso riandare a ricliccare il pulsante basso
                    return False # ritorno un valore perchè dopo lo vado ad utilizzare
            

        if self.mesh.colliderect(object):   # Metodo di pygame che confronta se due rettangoli collidono

            # Setto diverse variabili per non ripeterli nei confronti
            w = (self.Last_keyPressed == "Up")
            a = (self.Last_keyPressed == "Left")
            
            s = (self.Last_keyPressed == "Down")
            d = (self.Last_keyPressed == "Right")

            
            a1 = (self.getRightPress() and w or self.getLeftPress() and w)
            b1 =  (self.getLeftPress() and s or self.getRightPress() and s)

            c1 =  (self.getUpPress() and a or self.getDownPress() and a)
            d1 =  (self.getUpPress() and d or self.getDownPress() and d)

            # print("\n\nSinistro o Destro and Sù: ",str(a1))
            # print("Sinistro o Destro and Giù: ",str(b1))
            # print("Alto o Basso and Sinistra: ",str(c1))
            # print("Alto o Basso and Destra: ",str(d1))

            # print("\nup: "+str(self.getUpPress())+" |down: "+str(self.getDownPress())+" |left: "+str(self.getLeftPress())+" |right: "+str(self.getRightPress())+"\n")
            
            if self.Last_keyPressed != "Null":  # Confronto se il giocatore è fermo o si sta muovendo

                if (a1 or b1) and (not c1 and not d1):  # se è stato premuto il pulsante destro/sinistro e NON quello alto o basso mentre si ha una collisione allora:

                    Confronta("x")  # richiamo la funzione

                    if Confronta("x"):  # se la funzione mi ritorna True allora:
                        self.setLeftPress(False)
                    else:  # se la funzione mi ritorna False allora:
                        self.setRightPress(False)

                    self.Last_keyPressed = "Null"   # Variabile usata per non dare errori dato che l'ultimo pulsante cliccato sono l'insieme di due in contemporanea

                    
                if (c1 or d1) and (not a1 and not b1):  # se è stato premuto il pulsante alto/basso e NON con quello sinistro o destro mentre si ha una collisione allora:

                    Confronta("y")  # richiamo la funzione

                    if Confronta("y"):  # se la funzione mi ritorna True allora:
                        self.setUpPress(False)
                    else:  # se la funzione mi ritorna False allora:
                        self.setDownPress(False)

                    self.Last_keyPressed = "Null"   # Variabile usata per non dare errori dato che l'ultimo pulsante cliccato sono l'insieme di due in contemporanea
                    

                if (self.getRightPress() or self.getLeftPress() or a or d) and (not w and not s):   # Qua altri confronti con unicamente con un pulante a volta cliccato sinistra/destra
                    Confronta("x")
                
                if (self.getUpPress() or self.getDownPress() or w or s) and (not d and not a):   # Qua altri confronti con unicamente con un pulante a volta cliccato alto/basso
                    Confronta("y")
            else:
                Confronta("y")
                Confronta("x")
                #self.setAllkeys(None)

    # Funzione che serve ad aggiornare la velocità attuale del giocatore la velocità da' un'impressione Smooth
    def update(self):
        self.setVelocitaX(0)
        self.setVelocitaY(0)

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
        self.hitbox = (self.x + 15 * GLOB.MULT /GLOB.Player_proportion, self.y + 17 * GLOB.MULT /GLOB.Player_proportion, 24 * GLOB.MULT /GLOB.Player_proportion, 43 * GLOB.MULT /GLOB.Player_proportion)

    # setta l'animazione della camminata a vera
    def animate(self):
        self.setIsWalking(True)

    # setta l'animazione della camminata a falso e rimette le variabili a default
    def finish(self):
        self.setIsWalking(False)
        self.current_spriteWO = 0
        self.current_spriteWVD = 0
        self.current_spriteWVU = 0

        # imposta un'animazione di default dopo aver eseguito l'ultima
        self.image = self.animationWO[int(self.current_spriteWO)]
        self.character = pygame.image.load(
            os.path.join(self.Name_animationWVD,'Walk0.png')).convert_alpha()