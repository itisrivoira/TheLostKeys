import pygame, os
import global_var as GLOB
import main, eventi

class Map():
    def __init__(self, risoluzione, path):
        self.path = path
        self.tiles_risoluzione = risoluzione
        self.tiles_mappa = pygame.Surface((0,0))
        self.tiles_mappaOggetti = pygame.Surface((0,0))
        self.tiles_immagini = []
        self.tiles_immagini_sprite = []
        self.tiles_collisioni = {}
        self.posX = 0
        self.posY = 0
        self.divisore = 2

        
        self.valore_fluttua = 0
        self.valore_fluttua_max = 1
        self.flag_fluttua = False


        # self.__load_images("MappaGioco/Tileset/Tileset_Muri/Tiles")
        self.__loadCollisions()


        self.tiles_oggetti = {}

    def __loadCollisions(self):

        def riempi(percorso):
            FileNames = os.listdir(percorso)

            # Ordino i file e gli appendo ad una lista, in modo che le animazioni siano lineari e ordinate
            FileNames.sort()

            for filename in FileNames:
                if (filename[-3] == "p" and filename[-2] == "n" and filename[-1] == "g") and (filename[0] == "t" and filename[1] == "i" and filename[2] == "l" and filename[3] == "e"):
                    self.tiles_immagini.append(filename)

        def caricaCollisione():
            for value in range(len(self.tiles_immagini)):
                val = self.tiles_risoluzione / GLOB.MULT
                rettangolo = pygame.image.load("Collisioni/"+self.tiles_immagini[value]).convert()
                var = pygame.PixelArray(rettangolo)

                #print(var)
                x, y = 0, 0

                startx ,starty = 0, 0
                endx, endy = 0, 0

                for colorey in var:
                    # print(colorey)
                    x = 0

                    # ------- VERDE ------- 
                    for colorex in colorey:
                        if colorex == 65280:
                            startx, starty = x, y
                            # print("X: ",x, startx ,endx)
                            # print("Y: ", y, starty, endy)

                        # ------- ROSSO ------- 
                        if colorex == 16711680:
                            endx, endy = x - startx, y - starty
                            # print("X: ",x, startx ,endx)
                            # print("Y: ", y, starty, endy)

                        x += val

                    y += val

                val_res = 28.8

                self.tiles_collisioni[value] = (starty/val_res * GLOB.MULT, startx/val_res * GLOB.MULT, endy/3 * GLOB.MULT, endx/3 * GLOB.MULT)

        riempi("Collisioni")
        caricaCollisione()
        # print(self.tiles_collisioni)


    def __load_images(self, path):

        lista = []

        def riempi(percorso):
            FileNames = os.listdir(percorso)

            # Ordino i file e gli appendo ad una lista, in modo che le animazioni siano lineari e ordinate
            FileNames.sort()

            for filename in FileNames:
                if (filename[-3] == "p" and filename[-2] == "n" and filename[-1] == "g") and (filename[0] == "t" and filename[1] == "i" and filename[2] == "l" and filename[3] == "e"):
                    lista.append(filename)

            #print(self.path+self.tiles_oggetti[event][0]+".png")
            #print(self.tiles_immagini_sprite)
        
        riempi(path)
        
        for value in range(len(lista)):
            if str(type(lista[value])) != "<class 'pygame.Surface'>":
                v = pygame.image.load(path+"/"+lista[value]).convert_alpha()
                v = pygame.transform.scale(v, (v.get_width() * GLOB.MULT, v.get_height() * GLOB.MULT))
                self.tiles_immagini_sprite.append(v)

        #print(self.tiles_immagini_sprite)

    def load_map(self, path):
        self.tiles_mappa = pygame.image.load(path).convert()
        self.tiles_mappa = pygame.transform.scale(self.tiles_mappa, (self.tiles_mappa.get_width() * GLOB.MULT / self.divisore, self.tiles_mappa.get_height() * GLOB.MULT / self.divisore))

    def load_objects(self, path):
        if path == None:
            return
        self.tiles_mappaOggetti = pygame.image.load(path).convert_alpha()
        self.tiles_mappaOggetti = pygame.transform.scale(self.tiles_mappaOggetti, (self.tiles_mappa.get_width(), self.tiles_mappa.get_height()))

    def render(self, lista, object, var, hitbox):
        x = self.posX
        y = self.posY
        value = 9.9 / GLOB.MULT
        chunck = 32 * GLOB.MULT
        chunck_render = pygame.Rect(main.player.x + 12 * GLOB.MULT /GLOB.Player_proportion, main.player.y + 25 * GLOB.MULT /GLOB.Player_proportion, chunck, chunck)

        if GLOB.Debug:
            pygame.draw.rect(GLOB.screen, (0,255,0), chunck_render, int(GLOB.MULT))

        for valore_y in range(len(lista)):

            x = self.posX
            for valore_x in range(len(lista[valore_y])):
                condition = lista[valore_y][valore_x] == var

                if self.valore_fluttua >= self.valore_fluttua_max:
                    self.valore_fluttua = self.valore_fluttua_max
                    self.flag_fluttua = False
                elif self.valore_fluttua <= -self.valore_fluttua_max:
                    self.valore_fluttua = -self.valore_fluttua_max
                    self.flag_fluttua = True

                if self.flag_fluttua:
                    self.valore_fluttua += 0.00001
                else:
                    self.valore_fluttua -= 0.00001

                

                if condition and object != None:
                    if str(type(self.tiles_immagini_sprite[var])) == "<class 'pygame.Surface'>" and len(self.tiles_immagini_sprite) > 1:
                        GLOB.screen.blit(self.tiles_immagini_sprite[var], (main.cam.getPositionX()+x * GLOB.MULT, main.cam.getPositionY()+y * GLOB.MULT))
                        #print("\n- Render | Oggetto a schermo!", self.tiles_immagini_sprite[var])
                        

                if condition:
                    chavetta = pygame.Rect((main.cam.getPositionX()+(x+self.tiles_collisioni[var][0]) * GLOB.MULT),(main.cam.getPositionY()+(y + self.tiles_collisioni[var][1]) * GLOB.MULT), self.tiles_collisioni[var][2]/value, self.tiles_collisioni[var][3]/value)
                    try:
                        if var >= GLOB.chiavetta_start and GLOB.chiavette[GLOB.enigmi_risolti[0]][1]:
                            GLOB.screen.blit(GLOB.chiavette[GLOB.enigmi_risolti[0]][2], (x * GLOB.MULT + main.cam.getPositionX() + self.tiles_risoluzione, y * GLOB.MULT + main.cam.getPositionY() + self.valore_fluttua * GLOB.MULT))
                            main.player.HasInteraction(chunck_render, chavetta, var)
                    except IndexError:
                        pass

                if hitbox != None:
                    oggetto = pygame.Rect((main.cam.getPositionX()+ x * GLOB.MULT),(main.cam.getPositionY()+ y * GLOB.MULT), self.tiles_risoluzione * GLOB.MULT, self.tiles_risoluzione * GLOB.MULT)

                    if GLOB.Debug and GLOB.ShowGrid:
                        pygame.draw.rect(GLOB.screen, (255,255,255), oggetto, int(1))

                    if condition and (oggetto.colliderect(chunck_render)):
                        collisione = pygame.Rect((main.cam.getPositionX()+(x+self.tiles_collisioni[var][0]) * GLOB.MULT),(main.cam.getPositionY()+(y + self.tiles_collisioni[var][1]) * GLOB.MULT), self.tiles_collisioni[var][2]/value, self.tiles_collisioni[var][3]/value)
                        #print("- Render | Collisione Oggetto Impostata!", collisione,"\n")

                        if hitbox:
                            main.player.HasCollision(collisione)
                            if GLOB.Debug:
                                pygame.draw.rect(GLOB.screen, (255,0,0), collisione, int(GLOB.MULT))
                        
                        if not hitbox:
                            if var < GLOB.chiavetta_start:
                                main.player.HasCollision(collisione)
                                main.player.HasInteraction(chunck_render, collisione, var)

                            if main.animazione.iFinished == True:
                                eventi.testa()

                            if GLOB.Debug:
                                pygame.draw.rect(GLOB.screen, (0,255,0), collisione, int(GLOB.MULT))


                x += self.tiles_risoluzione

            y += self.tiles_risoluzione

    def render_gamemapCollision(self, object, lista, var, collisione):
        self.render(lista, object, var, collisione)

    def render_map(self, pos):
        GLOB.screen.blit(self.tiles_mappa, (main.cam.getPositionX() + pos[0] * GLOB.MULT, main.cam.getPositionY() + pos[1] * GLOB.MULT))
        self.posX = pos[0]
        self.posY = pos[1]

    def render_objects(self, pos):
        if GLOB.Default_object != None:
            GLOB.screen.blit(self.tiles_mappaOggetti, (main.cam.getPositionX() + pos[0] * GLOB.MULT, main.cam.getPositionY() + pos[1] * GLOB.MULT))