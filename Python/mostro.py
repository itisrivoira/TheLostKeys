import pygame, sys, math
import global_var as GLOB
# import main




class Mostro():
    def __init__(self, pos, vel, wh):
        self.x = pos[0]
        self.y = pos[1]
        self.width = wh[0]
        self.height = wh[1]
        self.vel = vel
        self.x, self.y = GLOB.screen.get_rect().center
        self.line_vector = pygame.math.Vector2(1, 0)
        self.angle = 90

        self.distanza = 20

        self.color_triangle = (255,255,255)
        self.color_rect = (255, 0, 0)

        self.altezza_nascondiglio = 1 * GLOB.MULT

        self.altezza_rect = 20 * GLOB.MULT

    def aggiorna(self):
        radius = 360

        self.line_vector = pygame.math.Vector2(self.height, 0)
        
        rot_vector = self.line_vector.rotate(self.angle) * radius
        rot_vector1 = self.line_vector.rotate(self.angle + self.distanza) * radius

        start_line = round(self.x + self.width/2), round(self.y)
        end_line = round(self.x + self.width/2 - rot_vector.x), round(self.y - rot_vector.y)


        end_line1 = round(self.x + self.width/2 - rot_vector1.x), round(self.y - rot_vector1.y)
        

        self.triangle = pygame.draw.polygon(surface=GLOB.screen, color=self.color_triangle, points=[end_line, end_line1, start_line])

        # pygame.draw.ellipse(GLOB.screen, self.color_triangle, pygame.Rect(end_line[0]/2 + end_line1[0]/2, end_line[1]/2 + end_line1[1]/2, (self.distanza - self.height), (self.distanza + self.height)), width=0)


        pygame.draw.line(GLOB.screen, (5,80,255), start_line, end_line, 8)
        pygame.draw.line(GLOB.screen, (255,80,5), start_line, end_line1, 8)

        self.rect = pygame.Rect((40 * GLOB.MULT, 40 * GLOB.MULT, 20 * GLOB.MULT, self.altezza_rect))

        self.nascondiglio = pygame.Rect((60 * GLOB.MULT, 40 * GLOB.MULT, 20 * GLOB.MULT, self.altezza_nascondiglio))

        pygame.draw.rect(GLOB.screen, self.color_rect, self.rect)
        pygame.draw.rect(GLOB.screen, (0, 0, 255), self.nascondiglio)

        if self.triangle.colliderect(self.rect) and self.altezza_nascondiglio < self.altezza_rect:
            pygame.draw.rect(GLOB.screen, (0, 255, 0), self.rect, 6)
            pygame.draw.polygon(surface=GLOB.screen, color=(0, 255, 0), points=[end_line, end_line1, start_line], width= 6)
            self.color_rect = (255, 0, 255)
            self.color_triangle = (255, 0, 0)

        else:      
            self.color_triangle = (255,255,255)
            self.color_rect = (255, 0, 0)




        if self.angle >= 360:
            self.angle = 0

        if self.angle <= -1:
            self.angle = 359
            

        # GLOB.screen.blit(immagine, (GLOB.screen_width/2 - int(immagine.get_width()/2)  - rot_vector.x/2, GLOB.screen_height/2 - int(immagine.get_height()/2) - rot_vector.y/2))

        # rect = pygame.Rect(MENU_MOUSE_POS[0], MENU_MOUSE_POS[1], 1, 1) 
        # print(rect)
        # if not pygame.sprite.collide_mask(mask, rect):
        #     print("Sto collidendo")

    def aumenta_altezza(self):
        self.altezza_nascondiglio += 1 * GLOB.MULT

    def diminuisci_altezza(self):
        self.altezza_nascondiglio -= 1 * GLOB.MULT

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
        self.height += 0.025 * GLOB.MULT

    def diminuisci_lunghezza(self):
        self.height -= 0.025 * GLOB.MULT




def inizializza():
    global clock, animazione, mostro
    pygame.display.set_caption("Effetto")
    clock = pygame.time.Clock()
    mostro = Mostro((500,500), 20, (10 * GLOB.MULT, 0.2 * GLOB.MULT))

def disegna():
    GLOB.screen.fill((12,24,36))
    mostro.aggiorna()
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


        if pygame.mouse.get_pressed()[0] or keys_pressed[pygame.K_d]:
            mostro.ruota_destra()

        if pygame.mouse.get_pressed()[2] or keys_pressed[pygame.K_a]:
            mostro.ruota_sinistra()

        if keys_pressed[pygame.K_UP]:
            mostro.aumenta_lunghezza()

        if keys_pressed[pygame.K_DOWN]:
            mostro.diminuisci_lunghezza()

        if keys_pressed[pygame.K_RIGHT]:
            mostro.aumenta_distanza()

        if keys_pressed[pygame.K_LEFT]:
            mostro.diminuisci_distanza()

        if keys_pressed[pygame.K_o]:
            mostro.diminuisci_altezza()

        if keys_pressed[pygame.K_p]:
            mostro.aumenta_altezza()

        disegna()

        clock.tick(GLOB.FPS)
        pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    testa()