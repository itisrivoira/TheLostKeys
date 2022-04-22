import pygame, os
import global_var as GLOB
import main

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

        # self.__load_images("MappaGioco/Tileset/Tileset_Muri/Tiles")
        self.__loadCollisions()


        self.tiles_oggetti = {}

    def __loadCollisions(self):

        def riempi(percorso):
            FileNames = os.listdir(percorso)

            # Ordino i file e gli appendo ad una lista, in modo che le animazioni siano lineari e ordinate
            FileNames.sort()

            for filename in FileNames:
                if filename[-3] == "p" and filename[-2] == "n" and filename[-1] == "g":
                    self.tiles_immagini.append(filename)

        def caricaCollisione():
            for value in range(len(self.tiles_immagini)):
                val = 8
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

                len_tileX = (self.tiles_risoluzione/2.5 - startx)
                len_tileY = (self.tiles_risoluzione/2.5 - starty)
                #len_tileY = 1 # da risolvere
                self.tiles_collisioni[value] = (starty//len_tileX, startx//len_tileY, endy, endx)

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
                if filename[-3] == "p" and filename[-2] == "n" and filename[-1] == "g":
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
            pygame.draw.rect(GLOB.screen, (0,255,0), chunck_render, 4)

        for valore_y in range(len(lista)):

            x = self.posX
            for valore_x in range(len(lista[valore_y])):
                condition = lista[valore_y][valore_x] == var

                if condition and object != None:
                    if str(type(self.tiles_immagini_sprite[var])) == "<class 'pygame.Surface'>" and len(self.tiles_immagini_sprite) > 1:
                        GLOB.screen.blit(self.tiles_immagini_sprite[var], (main.cam.getPositionX()+x * GLOB.MULT, main.cam.getPositionY()+y * GLOB.MULT))
                        #print("\n- Render | Oggetto a schermo!", self.tiles_immagini_sprite[var])

                if hitbox != None:
                    oggetto = pygame.Rect((main.cam.getPositionX()+(x+self.tiles_collisioni[var][0]) * GLOB.MULT),(main.cam.getPositionY()+(y + self.tiles_collisioni[var][1]) * GLOB.MULT), self.tiles_collisioni[var][2]/value, self.tiles_collisioni[var][3]/value)
                    

                    # if main.animazione.flag_reverse and not main.animazione.flag_caricamento:
                    #     print(main.animazione.flag_reverse)
                    #     main.animazione.ImpostaSfondo()
                

                    if condition and (oggetto.colliderect(chunck_render)):
                        #print("- Render | Collisione Oggetto Impostata!", collisione,"\n")
                        if hitbox:
                            main.player.HasCollision(oggetto)
                            if GLOB.Debug:
                                pygame.draw.rect(GLOB.screen, (255,0,0), oggetto, int(1*GLOB.MULT))
                        
                        if not hitbox:
                            main.player.HasCollision(oggetto)
                            main.player.HasInteraction(chunck_render, oggetto, var)

                            if main.player.evento == "porta":
                                main.player.evento = None
                                main.stanze.setToDefault()
                                
                                if GLOB.Stanza == "Chimica":
                                    main.stanze.flag_Fisica = True
                                    print(main.stanze.pos_portaP, main.stanze.pos_portaC)
                                    main.animazione.ImpostaSfondo()

                                if GLOB.Stanza == "Fisica":
                                    main.stanze.flag_Chimica = True
                                    print(main.stanze.pos_portaP, main.stanze.pos_portaC)
                                    main.animazione.ImpostaSfondo()

                                print(GLOB.Default_Map)

                                main.player.x = main.stanze.pos_portaP[0] * GLOB.MULT
                                main.player.y = main.stanze.pos_portaP[1] * GLOB.MULT

                                main.cam.x = main.stanze.pos_portaC[0] * GLOB.MULT
                                main.cam.y = main.stanze.pos_portaC[1] * GLOB.MULT
                                main.animazione.iFinished = False

                            if GLOB.Debug:
                                pygame.draw.rect(GLOB.screen, (0,255,0), oggetto, int(1*GLOB.MULT))


                x += self.tiles_risoluzione

            y += self.tiles_risoluzione

    def render_gamemapCollision(self, object, lista, var, collisione):
        self.render(lista, object, var, collisione)

    # def render_object(self, event):
    #     lista_chiavi = list(self.tiles_oggetti.keys())

    #     for value in range(len(lista_chiavi)):
    #         condition =  str(type(self.tiles_oggetti.get(lista_chiavi[value])[0])) == "<class 'pygame.Surface'>"
    #         #print(str(lista_chiavi[value])+" | "+str(condition))
    #         if condition:
                
    #             try:      
    #                 if  self.tiles_oggetti.get(lista_chiavi[value])[2] == None:
    #                     collisione = (0, 0, self.tiles_risoluzione, self.tiles_risoluzione)
    #                 else:
    #                     collisione = self.tiles_oggetti.get(lista_chiavi[value])[2]

    #                 self.render(lista = event, object = self.tiles_oggetti.get(lista_chiavi[value])[0], var = self.tiles_oggetti.get(lista_chiavi[value])[1], hitbox = collisione)
    #                 #print(str(lista_chiavi[value])+" | Oggetto Caricato!")
    #             except KeyError:
    #                 #print(str(lista_chiavi[value])+" | Errore nel caricare l'oggetto")
    #                 pass

    def render_map(self, pos):
        GLOB.screen.blit(self.tiles_mappa, (main.cam.getPositionX() + pos[0] * GLOB.MULT, main.cam.getPositionY() + pos[1] * GLOB.MULT))
        self.posX = pos[0]
        self.posY = pos[1]

    def render_objects(self, pos):
        if GLOB.Default_object != None:
            GLOB.screen.blit(self.tiles_mappaOggetti, (main.cam.getPositionX() + pos[0] * GLOB.MULT, main.cam.getPositionY() + pos[1] * GLOB.MULT))