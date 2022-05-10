import pygame, sys, random
from button import Delay
import global_var as GLOB
# import main



#Player Class
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

        #indicazione grandezza (statica)
        self.width = 16 * GLOB.MULT / GLOB.Player_proportion
        self.height = 16 * GLOB.MULT / GLOB.Player_proportion

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = "Blue"

        self.vel = 3 * GLOB.MULT

        #indicazione velocità (dinamica)
        self.setVelocitaX(0)
        self.setVelocitaY(0)

        #pulsanti cliccati si/no
        self.setLeftPress(False)
        self.setRightPress(False)
        self.setUpPress(False)
        self.setDownPress(False)
        self.speed = self.vel

        self.Last_keyPressed = "Null"

        #hitbox del player
        self.setHitbox()
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self):
        #indicazione velocità (dinamica)
        self.setVelocitaX(0)
        self.setVelocitaY(0)
        if self.getLeftPress() and not self.getRightPress():
            self.setVelocitaX(-self.vel)
        if self.getRightPress() and not self.getLeftPress():
            self.setVelocitaX(self.vel)
        if self.getUpPress() and not self.getDownPress():
            self.setVelocitaY(-self.vel)
        if self.getDownPress() and not self.getUpPress():
            self.setVelocitaY(self.vel)
        
        self.setPositionX(self.getPositionX()+self.getVelocitaX())
        self.setPositionY(self.getPositionY()+self.getVelocitaY())

        self.rect = pygame.Rect(int(self.x), int(self.y), self.width, self.height)

        self.setHitbox()
        self.rect = pygame.Rect(self.hitbox) # indico la hitbox (mesh) del Player

    def HasCollision(self, object):
    
        def Confronta(value):   # Creo una funziona dato che la utilizzo piu' volte e se gli passo "x" fa una cosa mentre se gli passo "y" ne fa un'altra
            
            #self.finish()    # ogni volta che collido stoppo l'animazione del player

            if value=="x":  # confronto il valore passato

                if self.x >= object.x:  # confronto se la posizione del player delle x è maggiore o uguale della posizione delle x dell'oggetto di cui ho collisione
                    self.x += self.vel    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setLeftPress(False)    # ogni volta che collido dal lato sinistro non posso riandare a ricliccare il pulsante destro
                    return True # ritorno un valore perchè dopo lo vado ad utilizzare
                elif self.x <= object.x:
                    self.x -= self.vel    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setRightPress(False)    # ogni volta che collido dal lato destro non posso riandare a ricliccare il pulsante sinistro
                    return False # ritorno un valore perchè dopo lo vado ad utilizzare

            if value=="y":  # confronto il valore passato

                if self.y >= object.y:  # confronto se la posizione del player delle y è maggiore o uguale della posizione delle y dell'oggetto di cui ho collisione
                    self.y += self.vel    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setUpPress(False)    # ogni volta che collido dal lato basso non posso riandare a ricliccare il pulsante alto
                    return True # ritorno un valore perchè dopo lo vado ad utilizzare
                elif self.y <= object.y:
                    self.y -= self.vel    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setDownPress(False)    # ogni volta che collido dal lato alto non posso riandare a ricliccare il pulsante basso
                    return False # ritorno un valore perchè dopo lo vado ad utilizzare
            

        if self.rect.colliderect(object):   # Metodo di pygame che confronta se due rettangoli collidono

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

# ---------- self.set() ----------

    def setPositionX(self, x):
        self.x = x

    def setPositionY(self, y):
        self.y = y

    def setVelocitaX(self, x):
        self.__velX = x

    def setVelocitaY(self, y):
        self.__velY = y

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

    def setHitbox(self):
        #self.hitbox = (self.x + 15 * GLOB.MULT /GLOB.Player_proportion, self.y + 17 * GLOB.MULT /GLOB.Player_proportion, 24* GLOB.MULT /GLOB.Player_proportion, 43 * GLOB.MULT /GLOB.Player_proportion)
        self.hitbox = (self.rect)

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


class Mostro():
    def __init__(self, pos, vel, wh):
        self.x = pos[0]
        self.y = pos[1]
        self.width = wh[0]
        self.height = wh[1]
        self.default_height = self.height
        self.vel = vel
        self.x, self.y = GLOB.screen.get_rect().center
        self.line_vector = pygame.math.Vector2(1, 0)
        self.angle = 90

        self.default_speed = 1.1 * GLOB.MULT

        self.speed = self.default_speed

        self.monster_ai_vel = 0.5
        self.monster_ai_brain = 0
        self.delay_monster = Delay(self.monster_ai_vel, self.__setBrain)

        self.distanza = 90

        self.color_triangle = (255,255,255)

        self.altezza_rect = 20 * GLOB.MULT

        self.__setMonster(False)

        self.aggr = False

        self.direzione = ""
        self.setHitbox()


    def setHitbox(self):
        self.hitbox = (self.x - self.image.get_width()/2,  self.y - self.image.get_height()/2, self.image.get_width(), self.image.get_height())

    def __setBrain(self):
        self.monster_ai_brain = round(random.uniform(-1, 4), 1)

    def __setMonster(self, v):

        if not v:
            self.image = pygame.image.load("krita/mostro.png").convert_alpha()
        else:
            self.image = pygame.image.load("krita/angry-mostro.png").convert_alpha()

        self.image = pygame.transform.scale(self.image, (self.image.get_width() * GLOB.MULT / GLOB.Player_proportion, self.image.get_height() * GLOB.MULT / GLOB.Player_proportion))

    def aggiorna(self):
        radius = 360

        self.setHitbox()

        self.mesh = pygame.Rect(self.hitbox)

        self.line_vector = pygame.math.Vector2(self.height, 0)
        
        rot_vector = self.line_vector.rotate(self.angle) * radius
        rot_vector1 = self.line_vector.rotate(self.angle + self.distanza) * radius

        start_line = round(self.x + self.width/2), round(self.y)
        end_line = round(self.x + self.width/2 - rot_vector.x), round(self.y - rot_vector.y)


        end_line1 = round(self.x + self.width/2 - rot_vector1.x), round(self.y - rot_vector1.y)

        self.triangle = pygame.draw.polygon(surface=GLOB.screen, color=self.color_triangle, points=[end_line, end_line1, start_line])

        valore_distanza = 250 * GLOB.MULT

        if self.triangle.colliderect(player.hitbox) or self.aggr:
            self.raggio_ai_brain = 0
            self.monster_ai_brain = 0
            self.height = 0
            self.circle = pygame.draw.circle(GLOB.screen, "Red", (self.x, self.y), valore_distanza, 0)
            self.color_rect = (255, 0, 255)
            self.color_triangle = (255, 0, 0)
            self.__setMonster(True)
            self.aggr = True
            player.color = "White"

        else:
            self.height = self.default_height
            self.delay_monster.Infinite()
            self.__setMonster(False)
            self.color_triangle = (255,255,255)
            self.color_rect = (255, 0, 0)
            player.color = "Blue"

            # pygame.draw.ellipse(GLOB.screen, self.color_triangle, pygame.Rect(end_line[0]/2 + end_line1[0]/2, end_line[1]/2 + end_line1[1]/2, (self.distanza - self.height), (self.distanza + self.height)), width=0)

            pygame.draw.line(GLOB.screen, (5,80,255), start_line, end_line, 8)
            pygame.draw.line(GLOB.screen, (255,80,5), start_line, end_line1, 8)

        val = 20

        if self.mesh.colliderect(player.hitbox):
            pygame.draw.rect(GLOB.screen, (0, 255, 0), self.mesh, GLOB.MULT)
            print("GAME OVER")
            inizializza()

        if not self.aggr:

            self.speed = self.default_speed

            if self.monster_ai_brain < 0:
                self.monster_ai_brain = 4 - self.monster_ai_brain

            if self.monster_ai_brain > 1 and self.monster_ai_brain < 2:
                self.monster_ai_brain = 1.5
                self.direzione = "destra-basso"
                self.angle = 90

            if self.monster_ai_brain > 2 and self.monster_ai_brain < 3:
                self.monster_ai_brain = 2.5
                self.direzione = "sinistra-basso"
                self.angle = 270

            if self.monster_ai_brain > 3 and self.monster_ai_brain < 4:
                self.monster_ai_brain = 3.5
                self.direzione = "sinistra-alto"
                self.angle = 0

            if self.monster_ai_brain > 4:
                self.monster_ai_brain = 4.5
                self.direzione = "destra-alto"
                self.angle = 180

            
            if self.monster_ai_brain == 0:
                self.direzione = "fermo"
            
            if self.monster_ai_brain == 1:
                self.direzione = "destra"
                self.angle = 0
            
            if self.monster_ai_brain == 2:
                self.direzione = "sinistra"
                self.angle = 270
            
            if self.monster_ai_brain == 3:
                self.direzione = "basso"
                self.angle = 180
            
            if self.monster_ai_brain == 4:
                self.direzione = "alto"
                self.angle = 90

            # print(self.monster_ai_brain, self.direzione)

            # -- DESTRA --
            if (self.monster_ai_brain == 1 or self.monster_ai_brain == 1.5 or self.monster_ai_brain == 4.5) and self.monster_ai_brain:
                if self.x > val and self.x < GLOB.screen_width:
                    self.x += self.speed
            
            # -- SINISTRA --
            if (self.monster_ai_brain == 2 or self.monster_ai_brain == 2.5 or self.monster_ai_brain == 3.5):
                if self.x > val and self.x < GLOB.screen_width:
                    self.x -= self.speed
            
            # -- BASSO --
            if (self.monster_ai_brain == 3 or self.monster_ai_brain == 1.5 or self.monster_ai_brain == 2.5):
                # if self.y > val and self.y < GLOB.screen_height:
                    self.y += self.speed

            # -- ALTO --
            if (self.monster_ai_brain == 4 or self.monster_ai_brain == 4.5 or self.monster_ai_brain == 3.5):
                if self.y > val and self.y < GLOB.screen_height:
                    self.y -= self.speed

        
        if self.aggr and self.circle.colliderect(player.hitbox):

            self.speed *= 1.002

            if player.Last_keyPressed == "Left" or self.x > player.x:
                self.x -= self.speed

            if player.Last_keyPressed == "Right" or self.x < player.x:
                self.x += self.speed

            if player.Last_keyPressed == "Up" or self.y > player.y:
                self.y -= self.speed

            if player.Last_keyPressed == "Down" or self.y < player.y:
                self.y += self.speed

        else:

            self.aggr = False





        GLOB.screen.blit(self.image, (self.x - self.image.get_width()/2,  self.y - self.image.get_height()/2))



        if self.angle >= 360:
            self.angle = 0

        if self.angle <= -1:
            self.angle = 359
            

        # GLOB.screen.blit(immagine, (GLOB.screen_width/2 - int(immagine.get_width()/2)  - rot_vector.x/2, GLOB.screen_height/2 - int(immagine.get_height()/2) - rot_vector.y/2))

        # rect = pygame.Rect(MENU_MOUSE_POS[0], MENU_MOUSE_POS[1], 1, 1) 
        # print(rect)
        # if not pygame.sprite.collide_mask(mask, rect):
        #     print("Sto collidendo")

    def ruota_destra(self):
        self.angle += 1
        print(self.angle)

    def ruota_sinistra(self):
        self.angle -= 0.25 * GLOB.MULT
        print(self.angle)

    def aumenta_distanza(self):
        self.distanza += 0.25 * GLOB.MULT

    def diminuisci_distanza(self):
        self.distanza -= 0.25 * GLOB.MULT

    def aumenta_lunghezza(self):
        self.default_height += 0.025 * GLOB.MULT

    def diminuisci_lunghezza(self):
        self.default_height -= 0.025 * GLOB.MULT




def inizializza():
    global clock, animazione, player, mostro
    pygame.display.set_caption("Effetto")
    clock = pygame.time.Clock()
    player = Player(10, 10)
    mostro = Mostro((500,500), 20, (10 * GLOB.MULT, 0.5 * GLOB.MULT))

def disegna():
    GLOB.screen.fill((12,24,36))
    mostro.aggiorna()

    player.draw(GLOB.screen)
    player.update()
    #rettangolo = pygame.Rect(GLOB.screen_width/2 - immagine.get_width()/2, GLOB.screen_height/2 - immagine.get_height()/2, immagine.get_width(), immagine.get_height())
    #pygame.draw.rect(GLOB.screen, (255, 0, 0), rettangolo, 1)

def testa():
    inizializza()
    global MENU_MOUSE_POS

    while True:

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.setLeftPress(True)
                    player.Last_keyPressed = "Left"
                if event.key == pygame.K_d:
                    player.setRightPress(True)
                    player.Last_keyPressed = "Right"
                if event.key == pygame.K_w:
                    player.setUpPress(True)
                    player.Last_keyPressed = "Up"
                if event.key == pygame.K_s:
                    player.setDownPress(True)
                    player.Last_keyPressed = "Down"
                    
            if event.type == pygame.KEYUP:
                player.Last_keyPressed = "Null"
                if event.key == pygame.K_a:
                    player.setLeftPress(False)
                if event.key == pygame.K_d:
                    player.setRightPress(False)
                if event.key == pygame.K_w:
                    player.setUpPress(False)
                if event.key == pygame.K_s:
                    player.setDownPress(False)


        if pygame.mouse.get_pressed()[0] or keys_pressed[pygame.K_e]:
            mostro.ruota_destra()

        if pygame.mouse.get_pressed()[2] or keys_pressed[pygame.K_q]:
            mostro.ruota_sinistra()

        if keys_pressed[pygame.K_UP]:
            mostro.aumenta_lunghezza()

        if keys_pressed[pygame.K_DOWN]:
            mostro.diminuisci_lunghezza()

        if keys_pressed[pygame.K_RIGHT]:
            mostro.aumenta_distanza()

        if keys_pressed[pygame.K_LEFT]:
            mostro.diminuisci_distanza()

        disegna()

        clock.tick(GLOB.FPS)
        pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    testa()