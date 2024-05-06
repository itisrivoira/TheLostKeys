import pygame, sys, os

FPS = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920,1080))

lista = []
dizionario = {}

val = 8
def riempi(percorso):
    global lista
    FileNames = os.listdir(percorso)

    print(FileNames)
    FileNames.sort()
    
    for filename in FileNames:
        if "tile" in filename and "png" in filename:
            lista.append(filename)

def caricaCollisione():
    global startx, starty, endx, endy, centerx, centery
    global lista
    molt = 12
    for value in range(len(lista)):
        cubo = pygame.image.load(path+"/"+lista[value]).convert()
        centerx, centery = screen.get_width()/2 - molt * val, screen.get_height()/2 - molt * val
        # cubo1 = cubo.set_colorkey((249, 80, 6))
        # cubo1 = cubo.get_rect(center = (screen.get_width()/2, screen.get_height()/2))

        var = pygame.PixelArray(cubo)

        x, y = 0, 0

        startx ,starty = 0, 0
        endx, endy = 0, 0

        for colorey in var:
            x = 0
            for colorex in colorey:
                if colorex == 65280:
                    startx, starty = x, y

                if colorex == 16711680:
                    endx, endy = x - startx, y - starty

                x += val

            y += val

        dizionario[value] = (centerx + starty, centery + startx, endy + val, endx + val)
        print(" | " + str(lista[value]) + " | collisione: " + str(dizionario[value]))

def caricaOggetti():
    global cubo, cubo1, cubo2
    cubo = pygame.image.load(path+"/"+lista[id_cubo]).convert()
    cubo = pygame.transform.scale(cubo, (cubo.get_width() * val, cubo.get_height() * val))

    # 17, 13
    cubo2 = pygame.Rect(centerx, centery, cubo.get_width(), cubo.get_height())
    # cubo1 = pygame.Rect(centerx + startx1 - cubo.get_width()/2 - val*2, centery + starty1 + cubo.get_height()/2 + val*2, endx1 - val*4, endy2 + val)
    cubo1 = pygame.Rect(dizionario[id_cubo])
    # print(startx, starty)
    # print(endx, endy)

def get_font(size):
    return pygame.font.Font("freesansbold.ttf", size)

path = "Collisioni"
riempi(path)
print("\n\nla lista ",lista)
caricaCollisione()

# (0, 224, 1024, 480)
#center = (screen.get_width()/2, screen.get_height()/2)
id_cubo = 0

caricaOggetti()


def testa():
    global cubo, cubo1, cubo2
    global id_cubo
    while True:
        
        ID_TEXT = get_font(24).render(lista[id_cubo], True, "WHite")
        ID_RECT = ID_TEXT.get_rect(center=(centerx + ID_TEXT.get_width()/2 + cubo.get_width()/4, centery - 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    id_cubo += 1

                    if id_cubo > len(lista) - 1:
                        id_cubo = len(lista) - 1
                    else:
                        caricaOggetti()

                if event.key == pygame.K_DOWN:
                    id_cubo -= 1

                    if id_cubo < 0:
                        id_cubo = 0
                    else:
                        caricaOggetti()

                if event.key == pygame.K_LEFT:
                    id_cubo = 0
                    caricaOggetti()

                if event.key == pygame.K_RIGHT:
                    id_cubo = len(lista) - 1
                    caricaOggetti()

        #print("Rettangolo:",startx, starty, endx, endy)
        screen.fill((12,24,36))
        screen.blit(cubo, (centerx, centery))
        screen.blit(ID_TEXT, ID_RECT)
        pygame.draw.rect(screen, (0, 0, 255), cubo2, 5)
        pygame.draw.rect(screen, (255, 255, 255), cubo1, 5)
        clock.tick(FPS)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    testa()