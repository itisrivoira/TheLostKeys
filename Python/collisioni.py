import pygame, os
import global_var as GLOB
import main, eventi

class Map():
    def __init__(self, risoluzione, path):
        self.path = path
        self.tiles_risoluzione = risoluzione
        self.tiles_mappa = pygame.Surface((0,0))
        self.tiles_mappaOggetti = pygame.Surface((0,0))
        self.tiles_muri = pygame.Surface((0,0))
        self.tiles_immagini = []
        self.tiles_immagini_sprite = []
        self.tiles_collisioni = {}
        self.posX = 0
        self.posY = 0
        self.divisore = 2

        
        self.valore_fluttua = 0
        self.valore_fluttua_max = 1
        self.flag_fluttua = False

        self.check_objects = False

        self.__loadCollisions()


        self.tiles_oggetti = {}

    def __loadCollisions(self):

        def riempi(percorso):
            FileNames = os.listdir(percorso)

            FileNames.sort()
            for filename in FileNames:
                if filename[-3::] == "png" and (filename[:4] == "tile"):
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
                
                colore_inizio = 65280
                colore_fine = 16711680

                for colorey in var:
                    # print(colorey)
                    x = 0

                    # ------- VERDE ------- 
                    for colorex in colorey:
                        if colorex == colore_inizio:
                            startx, starty = x, y
                            # print("X: ",x, startx ,endx)
                            # print("Y: ", y, starty, endy)

                        # ------- ROSSO ------- 
                        if colorex == colore_fine:
                            endx, endy = x - startx, y - starty
                            # print("X: ",x, startx ,endx)
                            # print("Y: ", y, starty, endy)

                        x += val

                    y += val

                val_res = 28.8

                self.tiles_collisioni[value] = (starty/val_res * GLOB.MULT, startx/val_res * GLOB.MULT, endy/3 * GLOB.MULT, endx/3 * GLOB.MULT)

        riempi("Collisioni")
        caricaCollisione()

    def load_map(self, path):
        self.tiles_mappa = pygame.image.load(path).convert()
        self.tiles_mappa = pygame.transform.scale(self.tiles_mappa, (self.tiles_mappa.get_width() * GLOB.MULT / self.divisore, self.tiles_mappa.get_height() * GLOB.MULT / self.divisore))
        GLOB.Mappa_Immagine = self.tiles_mappa

    def load_objects(self, path):
        if path == None:
            return
        try:
            self.tiles_mappaOggetti = pygame.image.load(path).convert_alpha()
            self.tiles_mappaOggetti = pygame.transform.scale(self.tiles_mappaOggetti, (self.tiles_mappa.get_width(), self.tiles_mappa.get_height()))
            GLOB.Oggetti_Immagine = self.tiles_mappaOggetti
        
        except FileNotFoundError:
            GLOB.Default_object = None
        
    def load_walls(self, path):
        if path == None:
            return
        
        try:
            self.tiles_muri = pygame.image.load(path).convert_alpha()
            self.tiles_muri = pygame.transform.scale(self.tiles_muri, (self.tiles_mappa.get_width(), self.tiles_mappa.get_height()))
            
            if not "1" in GLOB.Stanza:
                GLOB.Muri_Immagine = self.tiles_muri
                
            
        except FileNotFoundError:
            GLOB.Default_walls = None

    def render(self, var, hitbox):
        x = self.posX
        y = self.posY
        value = 9.9 / GLOB.MULT
        chunck = 40 * GLOB.MULT
        chunck_render = pygame.Rect(main.player.x + 7 * GLOB.MULT /GLOB.Player_proportion, main.player.y + 19 * GLOB.MULT /GLOB.Player_proportion, chunck, chunck)
        
        lista = GLOB.Mappa[0]
        
        if GLOB.MonsterCanSpawn and GLOB.MonsterSpawning and GLOB.Stanza == GLOB.MonsterActualRoom:
            chunck_render_m = pygame.Rect(main.mostro.x + 7* GLOB.MULT /GLOB.Player_proportion + main.cam.getPositionX(),  main.mostro.y + 19 * GLOB.MULT /GLOB.Player_proportion + main.cam.getPositionY(), chunck, chunck)
        else:
            chunck_render_m = False

        if GLOB.Debug:
            pygame.draw.rect(GLOB.screen, (0,255,0), chunck_render, int(GLOB.MULT))
            
            if GLOB.MonsterCanSpawn and GLOB.MonsterSpawning and GLOB.Stanza == GLOB.MonsterActualRoom:
                pygame.draw.rect(GLOB.screen, (0,0,255), chunck_render_m, int(GLOB.MULT))

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


                if hitbox != None:        
                    collisione_t = pygame.Rect((main.cam.getPositionX()+ x * GLOB.MULT),(main.cam.getPositionY()+ y * GLOB.MULT), self.tiles_risoluzione * GLOB.MULT, self.tiles_risoluzione * GLOB.MULT)

                    if condition and GLOB.enigmi_risolti:
                        
                        self.check_objects = False
                        
                        for i in range(len(GLOB.enigmi_risolti)):
                            chiavetta = GLOB.chiavette.get(GLOB.enigmi_risolti[i], [-1])
                            if chiavetta[0] == var and chiavetta[1] and not "chiavetta-"+str(chiavetta[0] - GLOB.chiavetta_start + 1) in GLOB.inventario.keys():
                                self.check_objects = True
                                GLOB.screen.blit(GLOB.chiavette[GLOB.enigmi_risolti[i]][2], (x * GLOB.MULT + main.cam.getPositionX() + self.tiles_risoluzione, y * GLOB.MULT + main.cam.getPositionY() + self.valore_fluttua * GLOB.MULT))
                                main.player.HasInteraction(chunck_render, collisione_t, var)
                                
                        if self.check_objects:
                            GLOB.PlayerCanCollect = True
                        else:
                            GLOB.PlayerCanCollect = False
                                

                    if GLOB.Debug and GLOB.ShowGrid:
                        pygame.draw.rect(GLOB.screen, (255,255,255), collisione_t, int(1))

                    if GLOB.MonsterCanSpawn and GLOB.MonsterSpawning and GLOB.Stanza == GLOB.MonsterActualRoom:
                        
                        if chunck_render_m != False:
                            controllo_collisione = condition and ((collisione_t.colliderect(chunck_render)) or (collisione_t.colliderect(chunck_render_m)))

                            if chunck_render_m.colliderect(chunck_render) and GLOB.PlayerIsHidden:
                                GLOB.PlayerIsHidden = False
                                main.mostro.IAttacking = True
                                main.mostro.aggr = True
                                main.mostro.IseePlayer = True
                                main.Gui.door_sound.play()

                        
                        
                    else:
                        controllo_collisione = condition and (collisione_t.colliderect(chunck_render))
                        

                    if controllo_collisione:
                        collisione = pygame.Rect((main.cam.getPositionX()+(x+self.tiles_collisioni[var][0]) * GLOB.MULT),(main.cam.getPositionY()+(y + self.tiles_collisioni[var][1]) * GLOB.MULT), self.tiles_collisioni[var][2]/value, self.tiles_collisioni[var][3]/value)

                        if hitbox:
                            main.player.HasCollision(collisione)
                            
                            if GLOB.MonsterCanSpawn and GLOB.MonsterSpawning and GLOB.Stanza == GLOB.MonsterActualRoom:
                                main.mostro.HasCollision(collisione)

                            if GLOB.Debug:
                                pygame.draw.rect(GLOB.screen, (255,0,0), collisione, int(GLOB.MULT))
                                
                        if GLOB.PlayerCanInteract:
                            GLOB.PlayerCanInteract = False
                        
                        if not hitbox:
                            if var < GLOB.chiavetta_start:
                                main.player.HasCollision(collisione)
                                main.player.HasInteraction(chunck_render, collisione, var)

                                if GLOB.MonsterCanSpawn and GLOB.MonsterSpawning and GLOB.Stanza == GLOB.MonsterActualRoom:
                                    main.mostro.HasCollision(collisione)
                                    
                                    if chunck_render_m != False:
                                        main.mostro.HasInteraction(chunck_render_m, collisione, var)


                            if main.animazione.iFinished == True:
                                eventi.testa()
                                
                                if chunck_render_m != False:
                                    if not (GLOB.Stanza in GLOB.enigmi_risolti and (var >= 56 and var <= 111)) and not (var >= 140 and var <= 152) and not collisione_t.colliderect(chunck_render_m):
                                        GLOB.PlayerCanInteract = True
                                else:
                                    if not (GLOB.Stanza in GLOB.enigmi_risolti and (var >= 56 and var <= 111)) and not (var >= 140 and var <= 152):
                                        GLOB.PlayerCanInteract = True

                            if GLOB.Debug:
                                pygame.draw.rect(GLOB.screen, (0,255,0), collisione, int(GLOB.MULT))
                                
                    if not controllo_collisione:
                        if GLOB.PlayerCanInteract and GLOB.PlayerIsMoving:
                            GLOB.PlayerCanInteract = False

                x += self.tiles_risoluzione

            y += self.tiles_risoluzione

    def render_map(self, pos):
        GLOB.screen.blit(self.tiles_mappa, (main.cam.getPositionX() + pos[0] * GLOB.MULT, main.cam.getPositionY() + pos[1] * GLOB.MULT))
        self.posX = pos[0]
        self.posY = pos[1]

    def render_objects(self, pos):
        GLOB.Oggetti_Immagine = self.tiles_mappaOggetti
        if GLOB.Default_object != None:
            GLOB.screen.blit(self.tiles_mappaOggetti, (main.cam.getPositionX() + pos[0] * GLOB.MULT, main.cam.getPositionY() + pos[1] * GLOB.MULT))
            
            
    def render_walls(self, pos):
        if GLOB.Default_walls != None and not GLOB.Enigma:
            GLOB.Muri_Immagine = self.tiles_muri
            try:
                GLOB.screen.blit(self.tiles_muri, (main.cam.getPositionX() + pos[0] * GLOB.MULT, main.cam.getPositionY() + pos[1] * GLOB.MULT))
            
            except FileNotFoundError:
                GLOB.Default_walls = None