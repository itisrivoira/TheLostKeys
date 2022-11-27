from __modules__ import *
import global_var as G

# import main

"""

    ---  FILE DEL MENU PRINCIPALE DELl'AVVIO DEL GIOCO	---

"""

TextView = PrintLine(font = "../Assets/font/font.ttf", color="White", size=10)

def play():
    
    G.Flags["playbutton"] = False
    G.Audio.Music["Rain"].stop()
    # main.inizializza()
    # main.main()
        
    
def options():
    G.Audio.Music["Rain"].stop()

    while True:
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        
        FULLSCREEN = "FULLSCREEN "
        PERFORMANCE = "PERFORMANCE "
        
        TEXT_FULLSCREEN = FULLSCREEN + ("ON" if not G.Flags["Fullscreen"] else "OFF")
            
        TEXT_PERFORMANCE = PERFORMANCE + ("ON" if not G.Flags["Performance"] else "OFF")
            
        
            
        BG_Option = pygame.image.load(Background_path + "Menu.png").convert()
        BG_Option = pygame.transform.scale(BG_Option, (DEF.getScreenResolution()[0], DEF.getScreenResolution()[1]))

        G.setCharacter()
        DEF.getScreen().blit(BG_Option, (0,0))

        CHARACTER = pygame.image.load(os.path.join("../Assets/Characters/Preview",G.scelta_char+".png")).convert_alpha()

        Scala = 2.5 * DEF.getScreenMolt()

        character_width = CHARACTER.get_width() * Scala
        character_height = CHARACTER.get_height() * Scala
        CHARACTER = pygame.transform.scale(CHARACTER, (character_width, character_height))

        DEF.getScreen().blit(CHARACTER, (DEF.getScreenResolution()[0]/2-character_width/2,50*DEF.getScreenMolt()))

        TextView.setSize(12), TextView.setPos((DEF.getScreenResolution()[0], 150 * DEF.getScreenMolt()))
        TextView.Print(G.scelta_char)

        TextView.setSize(8), TextView.setPos((DEF.getScreenResolution()[0], DEF.getScreenResolution()[1] + 160 * DEF.getScreenMolt()))
        TextView.Print("Velocita'")
        
        Bar((DEF.getScreenResolution()[0]/2, (DEF.getScreenResolution()[1] + 190 * DEF.getScreenMolt())/2), "Green", G.Stats[G.scelta_char]["Velocita"], None).update()


        # MATERIE'

        posX_tabella = (DEF.getScreenResolution()[0] - 80 * DEF.getScreenMolt()) * 2
        posY_tabella = (DEF.getScreenMolt() * 48) * 2
        scala_tabella = 1.5
        molt = 1.2


        chiavi = list(G.Stats[G.scelta_char].keys())[:-2]
        for materia in chiavi:
            
            Bar(((posX_tabella)/2, (posY_tabella * molt)/2), "Green", G.Stats[G.scelta_char][materia], scala_tabella).update()

            TextView.setSize(8), TextView.setPos((posX_tabella, posY_tabella * (molt - 0.25)))
            TextView.Print(materia)
            
            
            molt += 0.5
            posY_tabella += 0.5



        Rchange = Button(image=None, pos=(DEF.getScreenResolution()[0]/2+50*DEF.getScreenMolt(), DEF.getScreenResolution()[1]/2+15*DEF.getScreenMolt()), 
                            text_input=">", font=get_font(20*int(DEF.getScreenMolt())), base_color="White", hovering_color="red", scale=2)

        Rchange.changeColor(OPTIONS_MOUSE_POS)
        Rchange.update()

        Lchange = Button(image=None, pos=(DEF.getScreenResolution()[0]/2-50*DEF.getScreenMolt(), DEF.getScreenResolution()[1]/2+15*DEF.getScreenMolt()), 
                            text_input="<", font=get_font(20*int(DEF.getScreenMolt())), base_color="White", hovering_color="red", scale=2)

        Lchange.changeColor(OPTIONS_MOUSE_POS)
        Lchange.update()


        posY_tabella = DEF.getScreenMolt() * 48

        
        TextView.setSize(8), TextView.setPos((160 * DEF.getScreenMolt(), posY_tabella * 2))
        TextView.Print("EFFETTI SONORI")
        
        Bar((80*DEF.getScreenMolt(), posY_tabella*1.3), "#4287f5", (G.Audio.getGlobalVolumeSound() * 10) // G.Audio.getMaxVolume(), 1.2).update()
        
                
        TextView.setSize(8), TextView.setPos((160 * DEF.getScreenMolt(), posY_tabella * 3.7))
        TextView.Print("MUSICA")
        
        Bar((80 * DEF.getScreenMolt(), posY_tabella*2.1), "#4287f5", (G.Audio.getGlobalVolumeMusic() * 10) // G.Audio.getMaxVolume(), 1.2).update()


        AUDIOPLUS_BUTTON = Button(image=None, pos=(93*DEF.getScreenMolt(), posY_tabella*1.5), 
                            text_input="+", font=get_font(8*int(DEF.getScreenMolt())), base_color="#d7fcd4", hovering_color="White", scale=1)

        AUDIOLESS_BUTTON = Button(image=None, pos=(63*DEF.getScreenMolt(), posY_tabella*1.5), 
                            text_input="-", font=get_font(8*int(DEF.getScreenMolt())), base_color="#d7fcd4", hovering_color="White", scale=1)

        MUSICPLUS_BUTTON = Button(image=None, pos=(93*DEF.getScreenMolt(), posY_tabella*2.3), 
                            text_input="+", font=get_font(8*int(DEF.getScreenMolt())), base_color="#d7fcd4", hovering_color="White", scale=1)

        MUSICLESS_BUTTON = Button(image=None, pos=(63*DEF.getScreenMolt(), posY_tabella*2.3), 
                            text_input="-", font=get_font(8*int(DEF.getScreenMolt())), base_color="#d7fcd4", hovering_color="White", scale=1)

        AUDIOPLUS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        AUDIOPLUS_BUTTON.update()

        AUDIOLESS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        AUDIOLESS_BUTTON.update()

        MUSICPLUS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        MUSICPLUS_BUTTON.update()

        MUSICLESS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        MUSICLESS_BUTTON.update()

        res = 2
        ScreenRes1 = Button(image=pygame.image.load(GuiPath + "Select Rect.png").convert_alpha(), pos=(50*DEF.getScreenMolt(), DEF.getScreenResolution()[1]/2+75*DEF.getScreenMolt()), 
                    text_input=str(G.DF_width * res)+" x "+str(G.DF_height * res), font=get_font(4*int(DEF.getScreenMolt())), base_color="White", hovering_color="#2f3131", scale=4)

        ScreenRes1.changeColor(OPTIONS_MOUSE_POS)
        ScreenRes1.update()

        res = 3
        ScreenRes2 = Button(image=pygame.image.load(GuiPath + "Select Rect.png").convert_alpha(), pos=(110*DEF.getScreenMolt(), DEF.getScreenResolution()[1]/2+75*DEF.getScreenMolt()), 
                    text_input=str(G.DF_width * res)+" x "+str(G.DF_height * res), font=get_font(4*int(DEF.getScreenMolt())), base_color="White", hovering_color="#2f3131", scale=4)

        ScreenRes2.changeColor(OPTIONS_MOUSE_POS)
        ScreenRes2.update()

        res = 4
        ScreenRes3 = Button(image=pygame.image.load(GuiPath + "Select Rect.png").convert_alpha(), pos=(50*DEF.getScreenMolt(), DEF.getScreenResolution()[1]/2+90*DEF.getScreenMolt()), 
                    text_input=str(G.DF_width * res)+" x "+str(G.DF_height * res), font=get_font(4*int(DEF.getScreenMolt())), base_color="White", hovering_color="#2f3131", scale=4)

        ScreenRes3.changeColor(OPTIONS_MOUSE_POS)
        ScreenRes3.update()

        res = 5
        ScreenRes4 = Button(image=pygame.image.load(GuiPath + "Select Rect.png").convert_alpha(), pos=(110*DEF.getScreenMolt(), DEF.getScreenResolution()[1]/2+90*DEF.getScreenMolt()), 
                    text_input=str(G.DF_width * res)+" x "+str(G.DF_height * res), font=get_font(4*int(DEF.getScreenMolt())), base_color="White", hovering_color="#2f3131", scale=4)

        ScreenRes4.changeColor(OPTIONS_MOUSE_POS)
        ScreenRes4.update()


        Screen_FULL = Button(image=pygame.image.load(GuiPath + "Select Rect.png").convert_alpha(), pos=(80*DEF.getScreenMolt(), DEF.getScreenResolution()[1]/2+110*DEF.getScreenMolt()), 
                    text_input=TEXT_FULLSCREEN, font=get_font(7*int(DEF.getScreenMolt())), base_color="White", hovering_color="#2f3131", scale=2)

        Screen_FULL.changeColor(OPTIONS_MOUSE_POS)
        Screen_FULL.update()
        
        
        PERFORMANCE = Button(image=pygame.image.load(GuiPath + "Select Rect.png").convert_alpha(), pos=(80*DEF.getScreenMolt(), DEF.getScreenResolution()[1]/2+55*DEF.getScreenMolt()), 
            text_input=TEXT_PERFORMANCE, font=get_font(7*int(DEF.getScreenMolt())), base_color="White", hovering_color="#2f3131", scale=2)

        PERFORMANCE.changeColor(OPTIONS_MOUSE_POS)
        PERFORMANCE.update()
        



        OPTIONS_BACK = Button(image=None, pos=(DEF.getScreenResolution()[0]/2, 255*DEF.getScreenMolt()), 
                            text_input="BACK", font=get_font(20*int(DEF.getScreenMolt())), base_color="White", hovering_color="Grey", scale=2)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update()

        flag_screen = False

        def setFullScreen():
            G.Flags["Fullscreen"] = not G.Flags["Fullscreen"]

        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_F11:
                    flag_screen = True
                    setFullScreen()

            if event.type == pygame.MOUSEBUTTONDOWN:
                flag_screen = False

                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    G.Audio.Sounds["back"].play()
                    main_menu()

                if Rchange.checkForInput(OPTIONS_MOUSE_POS):
                    G.Scelta+=1
                    G.Audio.Sounds["option"].play()

                    if G.Scelta > 4:
                        G.Scelta = 0

                if Lchange.checkForInput(OPTIONS_MOUSE_POS):
                    G.Scelta-=1
                    G.Audio.Sounds["option"].play()

                    if G.Scelta < 0:
                        G.Scelta = 4

                if ScreenRes1.checkForInput(OPTIONS_MOUSE_POS):
                    DEF.setMultipliers(screen_multiplier = 2)
                    flag_screen = True

                if ScreenRes2.checkForInput(OPTIONS_MOUSE_POS):
                    DEF.setMultipliers(screen_multiplier = 3)
                    flag_screen = True

                if ScreenRes3.checkForInput(OPTIONS_MOUSE_POS):
                    DEF.setMultipliers(screen_multiplier = 4)
                    flag_screen = True

                if ScreenRes4.checkForInput(OPTIONS_MOUSE_POS):
                    DEF.setMultipliers(screen_multiplier = 5)
                    flag_screen = True
                
                if Screen_FULL.checkForInput(OPTIONS_MOUSE_POS):
                    G.Audio.Sounds["option"].play()
                    setFullScreen()
                    
                if PERFORMANCE.checkForInput(OPTIONS_MOUSE_POS):
                    G.Audio.Sounds["option"].play()
                    
                    G.Flags["Performance"] = not G.Flags["Performance"]
                    G.setFPS()
                    

            if flag_screen:
                setPioggia()

            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_ESCAPE]:
                main_menu()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate([AUDIOPLUS_BUTTON, AUDIOLESS_BUTTON, MUSICPLUS_BUTTON, MUSICLESS_BUTTON]):
                    if button.checkForInput(OPTIONS_MOUSE_POS):
                        
                        if i < 2 and not G.Audio.isMaxVolume(G.Audio.getGlobalVolumeSound()):
                            G.Audio.Sounds["option"].play()
                        elif i >= 2 and not G.Audio.isMaxVolume(G.Audio.getGlobalVolumeMusic()):
                            G.Audio.Sounds["option"].play()
                
                if AUDIOPLUS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    G.Audio.AddSoundVolume(G.Audio.getMaxVolume()/10)

                if AUDIOLESS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    G.Audio.AddSoundVolume(-G.Audio.getMaxVolume()/10)

                if MUSICPLUS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    G.Audio.AddMusicVolume(G.Audio.getMaxVolume()/10)

                if MUSICLESS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    G.Audio.AddMusicVolume(-G.Audio.getMaxVolume()/10)
                
        CHARACTER = pygame.transform.scale(CHARACTER, (character_width, character_height))
                
        DEF.Update()

def setPioggia():
    global rain
    rain = Rain(DEF.getScreen(), height = int(60 * DEF.getScreenMolt()), speed = 6 * DEF.getScreenMolt(), color = (152, 164, 184, 255), numdrops = 270)

def main_menu():
    pygame.mouse.set_visible(True)
    
    # Musica Background
    G.Audio.setVolume("Rain", 0.1)
    G.Audio.Music["Rain"].play(-1)


    BG_School = pygame.image.load(Background_path + "ScuolaHorror.png").convert()
    BG_School = pygame.transform.scale(BG_School, (BG_School.get_width()*DEF.getScreenMolt()/4,BG_School.get_height()*DEF.getScreenMolt()/4))

    BG_Cloud = pygame.image.load(Background_path + "Nuvola.png").convert_alpha()
    BG_Cloud = pygame.transform.scale(BG_Cloud, (BG_Cloud.get_width()*DEF.getScreenMolt()/4,BG_Cloud.get_height()*DEF.getScreenMolt()/4))

    setPioggia()

    BG_Menu = pygame.image.load(Background_path + "sfondo.png").convert()
    BG_Menu = pygame.transform.scale(BG_Menu, (DEF.getScreenResolution()[0], DEF.getScreenResolution()[1]))

    while True:

        DEF.getScreen().blit(BG_Menu, (0, 0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        TextView.setColor("#e9eef7")
        TextView.setPos((DEF.getScreenResolution()[0]/3, 140 * DEF.getScreenMolt()))
        TextView.Print(G.TITLE.upper())

        PLAY_BUTTON = Button(image=pygame.image.load(Button_path + "Play Rect.png").convert_alpha(), pos=(DEF.getScreenResolution()[0]/6, 110*DEF.getScreenMolt()), 
                            text_input="", font=get_font(10*int(DEF.getScreenMolt())), base_color="#d7fcd4", hovering_color="White", scale=1.5)
        
        OPTIONS_BUTTON = Button(image=pygame.image.load(Button_path + "Options Rect.png").convert_alpha(), pos=(DEF.getScreenResolution()[0]/6, 150*DEF.getScreenMolt()), 
                            text_input="", font=get_font(10*int(DEF.getScreenMolt())), base_color="#d7fcd4", hovering_color="White", scale=1.5)
        
        QUIT_BUTTON = Button(image=pygame.image.load(Button_path + "Quit Rect.png").convert_alpha(), pos=(DEF.getScreenResolution()[0]/6, 190*DEF.getScreenMolt()), 
                            text_input="", font=get_font(10*int(DEF.getScreenMolt())), base_color="#d7fcd4", hovering_color="White", scale=1.5)

        #DEF.getScreen().blit(BG_School, (DEF.getScreenResolution()[0]/3-5*DEF.getScreenMolt(), DEF.getScreenResolution()[1]-BG_School.get_height()))
        DEF.getScreen().blit(BG_School, (DEF.getScreenResolution()[0]/3, 0))


        DEF.getScreen().blit(BG_Cloud, (DEF.getScreenResolution()[0]/3, 0))

        # Draw rain
        dirtyrects = rain.Timer(time.time())

        # Update the screen for the dirty rectangles only
        pygame.display.update(dirtyrects)

        DEF.getScreen().blit(BG_Cloud, (DEF.getScreenResolution()[0]/3, 0))
        
        
        # Alert dati salvati
        alert = pygame.image.load(GuiPath + "selezione.png").convert_alpha()
        alert = pygame.transform.scale(alert, (alert.get_width() * DEF.getScreenMolt(), alert.get_height() * DEF.getScreenMolt()))
        
        
        Selezione_TEXT = get_font(4*int(DEF.getScreenMolt())).render("Vuoi caricare i dati salvati?", True, "#e9eef7")
        Selezione_RECT = Selezione_TEXT.get_rect(center=(DEF.getScreenResolution()[0]/2 - Selezione_TEXT.get_width()/2 + Selezione_TEXT.get_width()/2, DEF.getScreenResolution()[1]/2 - alert.get_height()/2 + 20*DEF.getScreenMolt()))
        
        Selezione1 = Button(image=None, pos=(DEF.getScreenResolution()[0]/2 - alert.get_width()/2 + Selezione_TEXT.get_width()/2 + 15*DEF.getScreenMolt(), DEF.getScreenResolution()[1]/2 - alert.get_height()/2 + 60*DEF.getScreenMolt()), 
                    text_input="si'", font=get_font(4*int(DEF.getScreenMolt())), base_color="White", hovering_color="Yellow", scale=2)
        
        Selezione2 = Button(image=None, pos=(DEF.getScreenResolution()[0]/2 - alert.get_width()/2 + Selezione_TEXT.get_width()/2 + 75*DEF.getScreenMolt(), DEF.getScreenResolution()[1]/2 - alert.get_height()/2 + 60*DEF.getScreenMolt()), 
                    text_input="no", font=get_font(4*int(DEF.getScreenMolt())), base_color="White", hovering_color="Yellow", scale=2)
        
        
        Selezione3 = Button(image=None, pos=(DEF.getScreenResolution()[0]/2 - alert.get_width()/2 + alert.get_width(), DEF.getScreenResolution()[1]/2 - alert.get_height()/2), 
                text_input="X", font=get_font(3*int(DEF.getScreenMolt())), base_color="White", hovering_color="Red", scale=2)
        
       
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.changeScale(MENU_MOUSE_POS, 1.1)
            button.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
    
                if event.key == pygame.K_F2:
                    G.Audio.Music["Rain"].stop()
                    intro()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    G.Audio.Sounds["option"].play()
                    
                    if not G.AlertSalva:
                        play()
                    
                    G.Flags["playbutton"] = True
                    

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    G.Flags["playbutton"] = False
                    G.Audio.Sounds["menu"].play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                    
                if G.Flags["playbutton"]:
                    if Selezione1.checkForInput(MENU_MOUSE_POS):
                        G.Audio.Sounds["menu"].play()
                        G.CaricaPartita = True
                        play()
                        
                    if Selezione2.checkForInput(MENU_MOUSE_POS):
                        G.Audio.Sounds["menu"].play()
                        G.CaricaPartita = False
                        play()
                        
                    if Selezione3.checkForInput(MENU_MOUSE_POS):
                        G.Audio.Sounds["menu"].play()
                        G.Flags["playbutton"] = False

        # TUONO evento randomico
        if random.randint(0, (100 * G.FPS)) >= (98 * G.FPS):
            tuono = pygame.image.load(Background_path + "tuono.png").convert()
            tuono = pygame.transform.scale(tuono, (tuono.get_width()*DEF.getScreenMolt(), tuono.get_height()*DEF.getScreenMolt()))
            
            tuonoSound =    [
                                G.Audio.Sounds["thunder"], 
                                G.Audio.Sounds["thunder2"]
                            ]

            random.choice(tuonoSound).play()

            DEF.getScreen().blit(tuono, (0, 0))
            
            
        if G.Flags["playbutton"]:
            if G.Flags["AlertSalva"]:
                
                DEF.getScreen().blit(alert, (DEF.getScreenResolution()[0]/2 - alert.get_width()/2, DEF.getScreenResolution()[1]/2 - alert.get_height()/2))

                DEF.getScreen().blit(Selezione_TEXT, Selezione_RECT)
                
                Selezione1.changeColor(MENU_MOUSE_POS)
                Selezione1.update()
                Selezione1.changeColor(MENU_MOUSE_POS)
                
                Selezione2.changeColor(MENU_MOUSE_POS)
                Selezione2.update()
                Selezione2.changeColor(MENU_MOUSE_POS)
                
                Selezione3.changeColor(MENU_MOUSE_POS)
                Selezione3.update()
                Selezione3.changeColor(MENU_MOUSE_POS)
                


        
        DEF.Update()



def SetVideoToFalse():
    global VideoFinito, video
    VideoFinito = True
    video.close()


def intro():
    global VideoFinito, video
    
    video = Video(VideoPath+"Presentazione.mp4")
    video.set_size((DEF.getScreenResolution()[0], DEF.getScreenResolution()[1]))
    delay_video = Delay(video.duration - 3.8, SetVideoToFalse)
    
    VideoFinito = False
    while not VideoFinito:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                SetVideoToFalse()
                
        delay_video.Start()
        video.draw(DEF.getScreen(), (0, 0))
                
        DEF.Update()
                
    main_menu()


intro()