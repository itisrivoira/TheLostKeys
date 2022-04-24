import pygame, sys, os

FPS = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920,1080))

lista = []
dizionario = {}

val = 8
def riempi(percorso):
        FileNames = os.listdir(percorso)

        print(FileNames)

        # Ordino i file e gli appendo ad una lista, in modo che le animazioni siano lineari e ordinate
        FileNames.sort()

        for filename in FileNames:
            if filename[-3] == "p":
                lista.append(filename)

def caricaCollisione():
    global startx, starty, endx, endy, centerx, centery
    for value in range(len(lista)):
        print(lista[value])
        cubo = pygame.image.load(path+"/"+lista[value]).convert()
        centerx, centery = screen.get_width()/2 - cubo.get_width()/2, screen.get_height()/2 - cubo.get_height()/2
        # cubo1 = cubo.set_colorkey((249, 80, 6))

        # cubo1 = cubo.get_rect(center = (screen.get_width()/2, screen.get_height()/2))

        var = pygame.PixelArray(cubo)

        #print(var)

        x, y = 0, 0

        startx ,starty = 0, 0
        endx, endy = 0, 0

        for colorey in var:
            # print(colorey)
            x = 0
            for colorex in colorey:
                if colorex == 65280:
                    startx, starty = x, y
                    print("X: ",x, startx ,endx)
                    print("Y: ", y, starty, endy)

                if colorex == 16711680:
                    endx, endy = x - startx, y - starty
                    print("X: ",x, startx ,endx)
                    print("Y: ", y, starty, endy)

                x += val

            y += val

        dizionario[value] = (centerx + starty, centery + startx, endy + val, endx + val)


path = "Collisioni"
riempi(path)
print("\n\nla lista ",lista)
caricaCollisione()

print(dizionario)

# (0, 224, 1024, 480)
#center = (screen.get_width()/2, screen.get_height()/2)
var = 28
cubo = pygame.image.load(path+"/"+lista[var]).convert()
cubo = pygame.transform.scale(cubo, (cubo.get_width() * val, cubo.get_height() * val))

# 17, 13
cubo2 = pygame.Rect(centerx, centery, cubo.get_width(), cubo.get_height())
# cubo1 = pygame.Rect(centerx + startx1 - cubo.get_width()/2 - val*2, centery + starty1 + cubo.get_height()/2 + val*2, endx1 - val*4, endy2 + val)
cubo1 = pygame.Rect(dizionario[var])
print(startx, starty)
print(endx, endy)


def testa():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        print("Rettangolo:",startx, starty, endx, endy)
        screen.fill((12,24,36))
        screen.blit(cubo, (centerx, centery))
        pygame.draw.rect(screen, (255, 255, 0), cubo2, 5)
        pygame.draw.rect(screen, (255, 255, 255), cubo1, 5)
        clock.tick(FPS)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    testa()