import pygame, sys, os

FPS = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0,0))

lista = []
dizionario = {}

val = 8
def riempi(percorso):
    global lista
    FileNames = os.listdir(percorso)

    print(FileNames)

    # Ordino i file e gli appendo ad una lista, in modo che le animazioni siano lineari e ordinate
    FileNames.sort()

    for filename in FileNames:
        if (filename[-3] == "p" and filename[-2] == "n" and filename[-1] == "g") and (filename[0] == "t" and filename[1] == "i" and filename[2] == "l" and filename[3] == "e"):
                lista.append(filename)

def caricaCollisione():
    global startx, starty, endx, endy, centerx, centery
    global lista
    molt = 12
    for value in range(len(lista)):
        cubo = pygame.image.load(path+"/"+lista[value]).convert()
        centerx, centery = screen.get_width()/2 - molt * val, screen.get_height()/2 - molt * val

        var = pygame.PixelArray(cubo)

        x, y = 0, 0

        startx ,starty = 0, 0
        endx, endy = 0, 0

        for colorey in var:
            x = 0
            for colorex in colorey:

                # RED
                if colorex == 65280:
                    startx, starty = x, y

                # GREEN
                if colorex == 16711680:
                    endx, endy = x - startx, y - starty

                x += val

            y += val

        dizionario[value] = (centerx + starty, centery + startx, endy + val, endx + val)
        print(" | " + str(lista[value]) + " | collisione: " + str(dizionario[value]))
    print()

def caricaOggetti():
    global cubo, cubo1, cubo2
    cubo = pygame.image.load(path+"/"+lista[id_cubo]).convert()
    cubo = pygame.transform.scale(cubo, (cubo.get_width() * val, cubo.get_height() * val))

    cubo2 = pygame.Rect(centerx, centery, cubo.get_width(), cubo.get_height())
    cubo1 = pygame.Rect(dizionario[id_cubo])

def get_font(size):
    return pygame.font.Font("../Assets/font/retro.ttf", size)

path = "../Assets/Elements/Collisions"
riempi(path)
print("\n\nla lista ",lista)
caricaCollisione()

id_cubo = 0

caricaOggetti()


def testa():
    global cubo, cubo1, cubo2
    global id_cubo
    while True:
        
        ID_TEXT = get_font(24).render(lista[id_cubo], True, "White")
        ID_RECT = ID_TEXT.get_rect(center=(cubo2.centerx, centery - 20))

        SIZE_TEXT = get_font(18).render(str((dizionario[id_cubo][0] - centerx, dizionario[id_cubo][1] - centery, dizionario[id_cubo][2], dizionario[id_cubo][3])), True, "Grey")
        SIZE_RECT = SIZE_TEXT.get_rect(center=(cubo2.centerx, centery - 50))

        
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
        screen.blit(SIZE_TEXT, SIZE_RECT)
        pygame.draw.rect(screen, (0, 0, 255), cubo2, 5)
        pygame.draw.rect(screen, (255, 255, 255), cubo1, 5, 1)
        clock.tick(FPS)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    testa()