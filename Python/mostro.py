import pygame, sys, math
import global_var as GLOB




class Mostro(pygame.sprite.Sprite):
    def __init__(self, pos, vel, wh):
        self.x = pos[0]
        self.y = pos[1]
        self.width = wh[0]
        self.height = wh[1]
        self.vel = vel
        self.x, self.y = GLOB.screen.get_rect().center
        self.line_vector = pygame.math.Vector2(1, 0)
        self.angle = 90
        self.angle_triangle = 0

    def aggiorna(self):
        radius = 360
        rot_vector = self.line_vector.rotate(self.angle) * radius
        start = round(self.x), round(self.y)
        end = round(self.x - rot_vector.x), round(self.y - rot_vector.y)

        start_line = round(self.x + self.width/2), round(self.y)
        end_line = round(self.x + self.width/2 - rot_vector.x), round(self.y - rot_vector.y)
        self.line = pygame.draw.line(GLOB.screen, (5,80,255), start_line, end_line, 8)

        larg = 10
        lunghezza1 = self.x +self.width/2 + larg
        lunghezza2 = self.x +self.width/2 - larg


        if self.angle == 360 or self.angle == -360:
            self.angle = 0
            
        fine = round(self.y - rot_vector.y)

        self.triangle = pygame.draw.polygon(surface=GLOB.screen, color=(255, 0, 0),points=[start_line, (lunghezza1, fine), (lunghezza2, fine)])

        lunghezza, altezza = 200, 150

        self.surface = pygame.Surface((lunghezza, altezza))
        self.surface.fill((0,0,255))

        self.triangle = pygame.draw.polygon(self.surface, (255,0,0), [(0, 0), (lunghezza, 0), (lunghezza-100, altezza)])

        self.surface = pygame.transform.rotate(self.surface, self.angle_triangle)

        val = 2

        immagine = pygame.image.load("Characters_Image/luce.png").convert_alpha()
        immagine = pygame.transform.scale(immagine, (immagine.get_width() * GLOB.MULT * val, immagine.get_height() * GLOB.MULT * val))

        immagine = pygame.transform.flip(immagine, False, False)
        immagine = pygame.transform.rotate(immagine, self.angle_triangle)


        GLOB.screen.blit(self.surface, (0,0))

        # GLOB.screen.blit(immagine, (GLOB.screen_width/2 - int(immagine.get_width()/2)  - rot_vector.x/2, GLOB.screen_height/2 - int(immagine.get_height()/2) - rot_vector.y/2))

        print(" Punto X: ",start,  " Punto Y: ", end)

        # rect = pygame.Rect(MENU_MOUSE_POS[0], MENU_MOUSE_POS[1], 1, 1) 
        # print(rect)
        # if not pygame.sprite.collide_mask(mask, rect):
        #     print("Sto collidendo")

    def ruota_destra(self):
        self.angle += 1
        self.angle_triangle -= 1

        print(self.angle)

    def ruota_sinistra(self):
        self.angle -= 1
        self.angle_triangle += 1

        print(self.angle)




def inizializza():
    global clock, animazione, mostro
    pygame.display.set_caption("Effetto")
    clock = pygame.time.Clock()
    mostro = Mostro((500,500), 20, (10 * GLOB.MULT, 80 * GLOB.MULT))

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        if pygame.mouse.get_pressed()[0]:
            mostro.ruota_destra()

        if pygame.mouse.get_pressed()[2]:
            mostro.ruota_sinistra()

        disegna()

        clock.tick(GLOB.FPS)
        pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    testa()