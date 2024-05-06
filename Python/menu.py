import pygame, sys, os, time, random
from components import Alert, Button, Bar, Delay
from pygame import mixer
import global_var as GLOB

from pyvidplayer import Video
from global_var import screen
import main
from pioggia import Rain

pygame.init()

"""

    ---  FILE DEL MENU PRINCIPALE DELl'AVVIO DEL GIOCO	---

"""

def get_font(size):
    return pygame.font.Font("font/font.ttf", size)


def setPioggia():
    global rain
    rain = Rain(screen, height = int(60 * GLOB.MULT), speed = 6 * GLOB.MULT, color = (152, 164, 184, 255), numdrops = 270)

def play():
    
    GLOB.playbutton = False
    mixer.music.stop()
    main.inizializza()
    main.main()

def options():
    mixer.music.stop()

    while True:
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        if not GLOB.Fullscreen:
            TEXT_FULLSCREEN = "FULLSCREEN ON"
        else:
            TEXT_FULLSCREEN = "FULLSCREEN OFF"
            
        if not GLOB.Performance:
            TEXT_PERFORMANCE = "PERFORMANCE ON"
        else:
            TEXT_PERFORMANCE = "PERFORMANCE OFF"
            
        # if not GLOB.CaricaPartita:
        #     TEXT_LOADGAME = "LOAD GAME ON"
        # else:
        #     TEXT_LOADGAME = "LOAD GAME OFF"
            
        BG_Option = pygame.image.load("assets/Menu.png").convert()
        BG_Option = pygame.transform.scale(BG_Option, (GLOB.screen_width, GLOB.screen_height))

        GLOB.setCharacter()

        NAME_TEXT = get_font(11*int(GLOB.MULT)).render(GLOB.scelta_char, True, "#e9eef7")
        NAME_RECT = NAME_TEXT.get_rect(center=(GLOB.screen_width/2, 80*GLOB.MULT))

        screen.blit(BG_Option, (0,0))

        screen.blit(NAME_TEXT, NAME_RECT)

        # OPTIONS_TEXT = get_font(25*int(GLOB.MULT)).render("MENU OPZIONI", True, "White")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(GLOB.screen_width/2, 20*GLOB.MULT))
        # screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        CHARACTER = pygame.image.load(os.path.join("Characters_Image",GLOB.scelta_char+".png")).convert_alpha()

        Scala = 2.5 * GLOB.MULT

        character_width = CHARACTER.get_width() * Scala
        character_height = CHARACTER.get_height() * Scala
        CHARACTER = pygame.transform.scale(CHARACTER, (character_width, character_height))

        screen.blit(CHARACTER, (GLOB.screen_width/2-character_width/2,50*GLOB.MULT))


        # VELOCITA'

        #TESTO
        Velocita_TEXT = get_font(6*int(GLOB.MULT)).render("Velocita'", True, "#e9eef7")
        Velocita_RECT = Velocita_TEXT.get_rect(center=(GLOB.screen_width/2, GLOB.screen_height/2+80*GLOB.MULT))

        screen.blit(Velocita_TEXT, Velocita_RECT)

        #BARRA
        Velocita = Bar((GLOB.screen_width/2, GLOB.screen_height/2+95*GLOB.MULT), "Green", GLOB.Stats[GLOB.Scelta][0], None)
        Velocita.update(screen)


        # MATERIE'

        posX_tabella = GLOB.screen_width-80*GLOB.MULT
        posY_tabella = GLOB.MULT*45
        scala_tabella = 1.5

        #BARRA Chimica
        Chimica = Bar((posX_tabella, posY_tabella*1.2), "Green", GLOB.Stats[GLOB.Scelta][1], scala_tabella)
        Chimica.update(screen)

        #BARRA Storia
        Storia = Bar((posX_tabella, posY_tabella*1.7), "Green", GLOB.Stats[GLOB.Scelta][2], scala_tabella)
        Storia.update(screen)

        #BARRA Inglese
        Inglese = Bar((posX_tabella, posY_tabella*2.2), "Green", GLOB.Stats[GLOB.Scelta][3], scala_tabella)
        Inglese.update(screen)

        #BARRA Fisica
        Fisica = Bar((posX_tabella, posY_tabella*2.7), "Green", GLOB.Stats[GLOB.Scelta][4], scala_tabella)
        Fisica.update(screen)

        #BARRA Matematica
        Matematica = Bar((posX_tabella, posY_tabella*3.2), "Green", GLOB.Stats[GLOB.Scelta][5], scala_tabella)
        Matematica.update(screen)

        #BARRA Informatica
        Informatica = Bar((posX_tabella, posY_tabella*3.7), "Green", GLOB.Stats[GLOB.Scelta][6], scala_tabella)
        Informatica.update(screen)

        #BARRA Italiano
        Italiano = Bar((posX_tabella, posY_tabella*4.2), "Green", GLOB.Stats[GLOB.Scelta][7], scala_tabella)
        Italiano.update(screen)

        #BARRA Sistemi
        Sistemi = Bar((posX_tabella, posY_tabella*4.7), "Green", GLOB.Stats[GLOB.Scelta][8], scala_tabella)
        Sistemi.update(screen)

        #BARRA TPSIT
        TPSIT = Bar((posX_tabella, posY_tabella*5.2), "Green", GLOB.Stats[GLOB.Scelta][9], scala_tabella)
        TPSIT.update(screen)

        #TESTO
        Chimica_TEXT = get_font(6*int(GLOB.MULT)).render("Chimica", True, "#e9eef7")
        Chimica_RECT = Chimica_TEXT.get_rect(center=(posX_tabella, posY_tabella))

        screen.blit(Chimica_TEXT, Chimica_RECT)

        #TESTO
        Storia_TEXT = get_font(6*int(GLOB.MULT)).render("Storia", True, "#e9eef7")
        Storia_RECT = Storia_TEXT.get_rect(center=(posX_tabella, posY_tabella*1.5))

        screen.blit(Storia_TEXT, Storia_RECT)

        #TESTO
        Inglese_TEXT = get_font(6*int(GLOB.MULT)).render("Inglese", True, "#e9eef7")
        Inglese_RECT = Inglese_TEXT.get_rect(center=(posX_tabella, posY_tabella*2))

        screen.blit(Inglese_TEXT, Inglese_RECT)

        #TESTO
        Fisica_TEXT = get_font(6*int(GLOB.MULT)).render("Fisica", True, "#e9eef7")
        Fisica_RECT = Fisica_TEXT.get_rect(center=(posX_tabella, posY_tabella*2.5))

        screen.blit(Fisica_TEXT, Fisica_RECT)

        #TESTO
        Matematica_TEXT = get_font(6*int(GLOB.MULT)).render("Matematica", True, "#e9eef7")
        Matematica_RECT = Matematica_TEXT.get_rect(center=(posX_tabella, posY_tabella*3))

        screen.blit(Matematica_TEXT, Matematica_RECT)

        #TESTO
        Informatica_TEXT = get_font(6*int(GLOB.MULT)).render("Informatica", True, "#e9eef7")
        Informatica_RECT = Informatica_TEXT.get_rect(center=(posX_tabella, posY_tabella*3.5))

        screen.blit(Informatica_TEXT, Informatica_RECT)

        #TESTO
        Italiano_TEXT = get_font(6*int(GLOB.MULT)).render("Italiano", True, "#e9eef7")
        Italiano_RECT = Italiano_TEXT.get_rect(center=(posX_tabella, posY_tabella*4))

        screen.blit(Italiano_TEXT, Italiano_RECT)

        #TESTO
        Sistemi_TEXT = get_font(6*int(GLOB.MULT)).render("Sistemi", True, "#e9eef7")
        Sistemi_RECT = Sistemi_TEXT.get_rect(center=(posX_tabella, posY_tabella*4.5))

        screen.blit(Sistemi_TEXT, Sistemi_RECT)

        #TESTO
        TPSIT_TEXT = get_font(6*int(GLOB.MULT)).render("TPSIT", True, "#e9eef7")
        TPSIT_RECT = TPSIT_TEXT.get_rect(center=(posX_tabella, posY_tabella*5))

        screen.blit(TPSIT_TEXT, TPSIT_RECT)



        Rchange = Button(image=None, pos=(GLOB.screen_width/2+50*GLOB.MULT, GLOB.screen_height/2+15*GLOB.MULT), 
                            text_input=">", font=get_font(20*int(GLOB.MULT)), base_color="White", hovering_color="#414141", scale=2)

        Rchange.changeColor(OPTIONS_MOUSE_POS)
        Rchange.update(screen)

        Lchange = Button(image=None, pos=(GLOB.screen_width/2-50*GLOB.MULT, GLOB.screen_height/2+15*GLOB.MULT), 
                            text_input="<", font=get_font(20*int(GLOB.MULT)), base_color="White", hovering_color="#414141", scale=2)

        Lchange.changeColor(OPTIONS_MOUSE_POS)
        Lchange.update(screen)



        AUDIO_TEXT = get_font(8*int(GLOB.MULT)).render("EFFETTI SONORI", True, "#e9eef7")
        AUDIO_RECT = AUDIO_TEXT.get_rect(center=(80*GLOB.MULT, posY_tabella))

        MUSICA_TEXT = get_font(8*int(GLOB.MULT)).render("MUSICA", True, "#e9eef7")
        MUSICA_RECT = MUSICA_TEXT.get_rect(center=(80*GLOB.MULT, posY_tabella*2))

        #BARRA AUDIO
        AUDIO = Bar((80*GLOB.MULT, posY_tabella*1.3), "#4287f5", GLOB.AU, 1.2)
        AUDIO.update(GLOB.screen)


        #BARRA MUSICA
        MUSICA = Bar((80*GLOB.MULT, posY_tabella*2.3), "#4287f5", GLOB.MU, 1.2)
        MUSICA.update(GLOB.screen)


        GLOB.screen.blit(AUDIO_TEXT, AUDIO_RECT)
        GLOB.screen.blit(MUSICA_TEXT, MUSICA_RECT)


        AUDIOPLUS_BUTTON = Button(image=None, pos=(93*GLOB.MULT, posY_tabella*1.5), 
                            text_input="+", font=get_font(6*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        AUDIOLESS_BUTTON = Button(image=None, pos=(63*GLOB.MULT, posY_tabella*1.5), 
                            text_input="-", font=get_font(6*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        MUSICPLUS_BUTTON = Button(image=None, pos=(93*GLOB.MULT, posY_tabella*2.5), 
                            text_input="+", font=get_font(6*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        MUSICLESS_BUTTON = Button(image=None, pos=(63*GLOB.MULT, posY_tabella*2.5), 
                            text_input="-", font=get_font(6*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1)

        AUDIOPLUS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        AUDIOPLUS_BUTTON.update(screen)

        AUDIOLESS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        AUDIOLESS_BUTTON.update(screen)

        MUSICPLUS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        MUSICPLUS_BUTTON.update(screen)

        MUSICLESS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        MUSICLESS_BUTTON.update(screen)

        color_selected = "#f0ff1e"
        Screen_480x270 = Button(image=pygame.image.load("assets/Select Rect.png").convert_alpha(), pos=(50*GLOB.MULT, GLOB.screen_height/2+75*GLOB.MULT), 
                    text_input=f"{GLOB.DF_width*1} x {GLOB.DF_height*1}", font=get_font(3*int(GLOB.MULT)), base_color = color_selected if int(GLOB.RESOLUTION) == 1 else "White" , hovering_color="#2f3131", scale=4)

        Screen_480x270.changeColor(OPTIONS_MOUSE_POS)
        Screen_480x270.update(screen)

        Screen_960x540 = Button(image=pygame.image.load("assets/Select Rect.png").convert_alpha(), pos=(110*GLOB.MULT, GLOB.screen_height/2+75*GLOB.MULT), 
                    text_input=f"{GLOB.DF_width*2} x {GLOB.DF_height*2}", font=get_font(3*int(GLOB.MULT)), base_color = color_selected if int(GLOB.RESOLUTION) == 2 else "White", hovering_color="#2f3131", scale=4)

        Screen_960x540.changeColor(OPTIONS_MOUSE_POS)
        Screen_960x540.update(screen)

        Screen_1440x810 = Button(image=pygame.image.load("assets/Select Rect.png").convert_alpha(), pos=(50*GLOB.MULT, GLOB.screen_height/2+90*GLOB.MULT), 
                    text_input=f"{GLOB.DF_width*3} x {GLOB.DF_height*3}", font=get_font(3*int(GLOB.MULT)), base_color = color_selected if int(GLOB.RESOLUTION) == 3 else "White", hovering_color="#2f3131", scale=4)

        Screen_1440x810.changeColor(OPTIONS_MOUSE_POS)
        Screen_1440x810.update(screen)


        Screen_1920x1080 = Button(image=pygame.image.load("assets/Select Rect.png").convert_alpha(), pos=(110*GLOB.MULT, GLOB.screen_height/2+90*GLOB.MULT), 
                    text_input=f"{GLOB.DF_width*4} x {GLOB.DF_height*4}", font=get_font(3*int(GLOB.MULT)), base_color = color_selected if int(GLOB.RESOLUTION) == 4 else "White", hovering_color="#2f3131", scale=4)

        Screen_1920x1080.changeColor(OPTIONS_MOUSE_POS)
        Screen_1920x1080.update(screen)


        Screen_FULL = Button(image=pygame.image.load("assets/Select Rect.png").convert_alpha(), pos=(80*GLOB.MULT, GLOB.screen_height/2+110*GLOB.MULT), 
                    text_input=TEXT_FULLSCREEN, font=get_font(6*int(GLOB.MULT)), base_color="White", hovering_color="#2f3131", scale=2)

        Screen_FULL.changeColor(OPTIONS_MOUSE_POS)
        Screen_FULL.update(screen)
        
        
        PERFORMANCE = Button(image=pygame.image.load("assets/Select Rect.png").convert_alpha(), pos=(80*GLOB.MULT, GLOB.screen_height/2+55*GLOB.MULT), 
            text_input=TEXT_PERFORMANCE, font=get_font(6*int(GLOB.MULT)), base_color="White", hovering_color="#2f3131", scale=2)

        PERFORMANCE.changeColor(OPTIONS_MOUSE_POS)
        PERFORMANCE.update(screen)
        
        
        # LOAD_GAME = Button(image=pygame.image.load("assets/Select Rect.png").convert_alpha(), pos=(80*GLOB.MULT, GLOB.screen_height/2), 
        #     text_input=TEXT_LOADGAME, font=get_font(6*int(GLOB.MULT)), base_color="White", hovering_color="#2f3131", scale=2)

        # LOAD_GAME.changeColor(OPTIONS_MOUSE_POS)
        # LOAD_GAME.update(screen)        




        OPTIONS_BACK = Button(image=None, pos=(GLOB.screen_width/2, 255*GLOB.MULT), 
                            text_input="BACK", font=get_font(20*int(GLOB.MULT)), base_color="White", hovering_color="Grey", scale=2)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        flag_screen = False

        def setFullScreen():
            
            GLOB.MULT = 4 * GLOB.MULT_INCREMENT
            GLOB.setScreenSize((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF)
            GLOB.Fullscreen = not GLOB.Fullscreen


        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                GLOB.Quit()


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_F11:
                    flag_screen = True
                    setFullScreen()

            if event.type == pygame.MOUSEBUTTONDOWN:
                flag_screen = False

                option_sound = mixer.Sound("suoni/char-sound.wav")
                option_sound.set_volume(0.16*GLOB.AU)

                back_sound = mixer.Sound("suoni/back-sound.wav")
                back_sound.set_volume(0.16*GLOB.AU)

                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    back_sound.play()
                    main_menu()

                if Rchange.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.Scelta+=1
                    option_sound.play()

                    if GLOB.Scelta>4:
                        GLOB.Scelta=0

                if Lchange.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.Scelta-=1
                    option_sound.play()

                    if GLOB.Scelta<0:
                        GLOB.Scelta=4

                if Screen_480x270.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.Fullscreen = False
                    GLOB.MULT = 1 * GLOB.MULT_INCREMENT
                    flag_screen = True

                if Screen_960x540.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.Fullscreen = False
                    GLOB.MULT = 2 * GLOB.MULT_INCREMENT
                    flag_screen = True

                if Screen_1440x810.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.Fullscreen = False
                    GLOB.MULT = 3 * GLOB.MULT_INCREMENT
                    flag_screen = True

                if Screen_1920x1080.checkForInput(OPTIONS_MOUSE_POS):
                    GLOB.Fullscreen = False
                    GLOB.MULT = 4 * GLOB.MULT_INCREMENT
                    flag_screen = True
                
                if Screen_FULL.checkForInput(OPTIONS_MOUSE_POS):
                    option_sound.play()
                    
                    flag_screen = True
                    setFullScreen()
                    
                if PERFORMANCE.checkForInput(OPTIONS_MOUSE_POS):
                    option_sound.play()
                    
                    if GLOB.Performance:
                        GLOB.Performance = False
                    else:
                        GLOB.Performance = True
                        
                    GLOB.setFPS()

            if flag_screen:
                global rain
                
                GLOB.RESOLUTION = GLOB.MULT / GLOB.MULT_INCREMENT
                
                GLOB.screen_width = GLOB.DF_width * GLOB.RESOLUTION
                GLOB.screen_height = GLOB.DF_height * GLOB.RESOLUTION
                
                if (GLOB.screen_width, GLOB.screen_height) >= (GLOB.MAX_width, GLOB.MAX_height):
                    GLOB.MULT = GLOB.MAX_width // GLOB.DF_width
                    GLOB.screen_width = GLOB.MAX_width
                    GLOB.screen_height = GLOB.MAX_height
                    GLOB.Fullscreen = True
                    
                if GLOB.Fullscreen:
                    GLOB.MULT = 4 * GLOB.MULT_INCREMENT
                
                GLOB.setScreenSize((0, 0) if GLOB.Fullscreen else (GLOB.screen_width, GLOB.screen_height), pygame.FULLSCREEN | pygame.DOUBLEBUF if GLOB.Fullscreen else pygame.DOUBLEBUF)
                setPioggia()


            button_sound = mixer.Sound("suoni/option-sound.wav")
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_ESCAPE]:
                main_menu()

            if event.type == pygame.MOUSEBUTTONDOWN and AUDIOPLUS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                GLOB.AU += 1

                if GLOB.AU > 10:
                    GLOB.AU = 10

                button_sound.set_volume(0.16*GLOB.AU)
                button_sound.play()

            if event.type == pygame.MOUSEBUTTONDOWN and AUDIOLESS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                GLOB.AU -= 1

                if GLOB.AU < 0:
                    GLOB.AU = 0
                
                button_sound.set_volume(0.16*GLOB.AU)
                button_sound.play()

            if event.type == pygame.MOUSEBUTTONDOWN and MUSICPLUS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                GLOB.MU += 1

                if GLOB.MU > 10:
                    GLOB.MU = 10

                button_sound.set_volume(0.16*GLOB.MU)
                button_sound.play()

            if event.type == pygame.MOUSEBUTTONDOWN and MUSICLESS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                GLOB.MU -= 1

                if GLOB.MU < 0:
                    GLOB.MU = 0
                
                button_sound.set_volume(0.16*GLOB.MU)
                button_sound.play()

        CHARACTER = pygame.transform.scale(CHARACTER, (character_width, character_height))
                
        pygame.display.flip()
        pygame.display.update()

def main_menu():
    pygame.mouse.set_visible(True)
    
    # Imposto una musica di background
    mixer.music.load("suoni/Rain-sound.wav")
    mixer.music.set_volume(0.01*GLOB.AU)
    mixer.music.play(-1)	# La setto a -1 che indica un loop quindi a infinito

    BG_School = pygame.image.load("assets/ScuolaHorror.png").convert()
    BG_School = pygame.transform.scale(BG_School, (BG_School.get_width()*GLOB.MULT/4,BG_School.get_height()*GLOB.MULT/4))

    BG_Cloud = pygame.image.load("assets/Nuvola.png").convert_alpha()
    BG_Cloud = pygame.transform.scale(BG_Cloud, (BG_Cloud.get_width()*GLOB.MULT/4,BG_Cloud.get_height()*GLOB.MULT/4))

    setPioggia()

    # Settaggio del Clock
    clock = pygame.time.Clock()
    quit_alert = None
    
    while True:

        #time.sleep(.01)

        BG_Menu = pygame.image.load("assets/sfondo.png").convert()
        BG_Menu = pygame.transform.scale(BG_Menu, (GLOB.screen_width, GLOB.screen_height))

        screen.blit(BG_Menu, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(9*int(GLOB.MULT)).render(GLOB.TITLE.upper(), True, "#e9eef7")
        MENU_RECT = MENU_TEXT.get_rect(center=(GLOB.screen_width/6, 70*GLOB.MULT))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png").convert_alpha(), pos=(GLOB.screen_width/6, 110*GLOB.MULT), 
                            text_input="", font=get_font(9*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1.5)
        
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png").convert_alpha(), pos=(GLOB.screen_width/6, 150*GLOB.MULT), 
                            text_input="", font=get_font(9*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1.5)
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png").convert_alpha(), pos=(GLOB.screen_width/6, 190*GLOB.MULT), 
                            text_input="", font=get_font(9*int(GLOB.MULT)), base_color="#d7fcd4", hovering_color="White", scale=1.5)

        screen.blit(MENU_TEXT, MENU_RECT)

        #screen.blit(BG_School, (GLOB.screen_width/3-5*GLOB.MULT, GLOB.screen_height-BG_School.get_height()))
        screen.blit(BG_School, (GLOB.screen_width/3, 0))


        screen.blit(BG_Cloud, (GLOB.screen_width/3, 0))

        # Draw rain
        dirtyrects = rain.Timer(time.time())

        # Update the screen for the dirty rectangles only
        pygame.display.update(dirtyrects)

        screen.blit(BG_Cloud, (GLOB.screen_width/3, 0))
        
        
        
        # Alert dati salvati
        alert = pygame.image.load("assets/selezione.png").convert_alpha()
        alert = pygame.transform.scale(alert, (alert.get_width() * GLOB.MULT, alert.get_height() * GLOB.MULT))
        
        Selezione_TEXT = get_font(4*int(GLOB.MULT)).render("Vuoi caricare i dati salvati?", True, "#e9eef7")
        Selezione_RECT = Selezione_TEXT.get_rect(center=(GLOB.screen_width/2 - Selezione_TEXT.get_width()/2 + Selezione_TEXT.get_width()/2, GLOB.screen_height/2 - alert.get_height()/2 + 20*GLOB.MULT))
        
        distance = 35
        altezza = 20
        Selezione1 = Button(image=None, pos=(GLOB.screen_width/2 - distance * GLOB.MULT, GLOB.screen_height/2 + altezza * GLOB.MULT), 
                    text_input="si'", font=get_font(4*int(GLOB.MULT)), base_color="White", hovering_color="Yellow", scale=2)
        
        Selezione2 = Button(image=None, pos=(GLOB.screen_width/2 + distance * GLOB.MULT, GLOB.screen_height/2 + altezza * GLOB.MULT), 
                    text_input="no", font=get_font(4*int(GLOB.MULT)), base_color="White", hovering_color="Yellow", scale=2)
        
        
        Selezione3 = Button(image=None, pos=(GLOB.screen_width/2 + alert.get_width()/2, GLOB.screen_height/2 - alert.get_height()/2), 
                text_input="X", font=get_font(5*int(GLOB.MULT)), base_color="White", hovering_color="Red", scale=2)
        
        
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.changeScale(MENU_MOUSE_POS, 1.1)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GLOB.Quit()
                
            if event.type == pygame.KEYDOWN:
    
                if event.key == pygame.K_ESCAPE:
                    mixer.music.stop()
                    intro()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_sound = mixer.Sound("suoni/menu-sound.wav")
                button_sound.set_volume(0.16*GLOB.AU)
                
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    button_sound.play()
                    
                    if not GLOB.AlertSalva:
                        play()
                    
                    GLOB.playbutton = True
                    

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    GLOB.playbutton = False
                    button_sound.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    quit_alert = Alert("Vuoi uscire?", (lambda: GLOB.Quit(), lambda: "", lambda: ""))
                    
                if GLOB.playbutton:
                    if Selezione1.checkForInput(MENU_MOUSE_POS):
                        button_sound.play()
                        GLOB.CaricaPartita = True
                        play()
                        
                    if Selezione2.checkForInput(MENU_MOUSE_POS):
                        button_sound.play()
                        GLOB.CaricaPartita = False
                        play()
                        
                    if Selezione3.checkForInput(MENU_MOUSE_POS):
                        button_sound.play()
                        GLOB.playbutton = False
                        
        if quit_alert != None:

            if quit_alert.Print() >= 1:
                quit_alert = None

        # TUONO evento randomico
        if random.randint(0, (100 * GLOB.FPS)) >= (98 * GLOB.FPS):
            tuono = pygame.image.load("assets/tuono.png").convert()
            tuono = pygame.transform.scale(tuono, (tuono.get_width()*GLOB.MULT, tuono.get_height()*GLOB.MULT))

            val = 0.16 * GLOB.AU

            tuonoSound = [mixer.Sound("suoni/thunder-sound.wav"), mixer.Sound("suoni/thunder-sound2.wav")]

            tuonoSound[0].set_volume(val)
            tuonoSound[1].set_volume(val)

            random.choice(tuonoSound).play()

            screen.blit(tuono, (0, 0))
            
            
        if GLOB.playbutton:
            if GLOB.AlertSalva:
                
                screen.blit(alert, (GLOB.screen_width/2 - alert.get_width()/2, GLOB.screen_height/2 - alert.get_height()/2))

                screen.blit(Selezione_TEXT, Selezione_RECT)
                
                Selezione1.changeColor(MENU_MOUSE_POS)
                Selezione1.update(screen)
                Selezione1.changeColor(MENU_MOUSE_POS)
                
                Selezione2.changeColor(MENU_MOUSE_POS)
                Selezione2.update(screen)
                Selezione2.changeColor(MENU_MOUSE_POS)
                
                Selezione3.changeColor(MENU_MOUSE_POS)
                Selezione3.update(screen)
                Selezione3.changeColor(MENU_MOUSE_POS)
                


        
        clock.tick(GLOB.FPS)

        pygame.display.flip()



def SetVideoToFalse():
    global VideoFinito, video, delay_video
    VideoFinito = True
    delay_video.ReStart()
    video.close()


def intro():
    global VideoFinito, video, delay_video
    
    video = Video("video/Presentazione.mp4")
    
    duration = round(video.duration - (1.5 + 0.7 * GLOB.MULT), 2)
    
    video.set_size((GLOB.screen_width, GLOB.screen_height))
    delay_video = Delay(duration, SetVideoToFalse)

    VideoFinito = False
    while not VideoFinito:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                GLOB.Quit()
            
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                SetVideoToFalse()
                
        video.draw(GLOB.screen, (0, 0))
        delay_video.Start()
        pygame.time.Clock().tick(GLOB.FPS)
        pygame.display.flip()
                
    main_menu()


intro()