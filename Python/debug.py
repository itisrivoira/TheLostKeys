import pygame, os, sys

#Importo i vari file e classi necessarie
import main

# Importo le variabili Globali
import global_var as GLOB


class Debug():
    def log(self):

        if GLOB.Debug:

            GLOB.ShowFps = True
            GLOB.ShowDropFrames = True
            
            pygame.draw.rect(GLOB.screen, (0,255,255), main.player.mesh, int(1*GLOB.MULT))

            sprint = GLOB.Player_speed > GLOB.Player_default_speed
            keys_pressed = pygame.key.get_pressed()

            key = GLOB.KeyPressed.upper()


            if main.player.getUpPress():
                key = "↑"
            elif main.player.getDownPress():
                key = "↓"
            elif main.player.getLeftPress():
                key = "←"
            elif main.player.getRightPress():
                key = "→"

            if sprint:
                key = "|"+key+"|"

            KEY_TEXT = main.get_font(10*int(GLOB.MULT)).render(key, True, "blue")
            KEY_RECT = KEY_TEXT.get_rect(center=(GLOB.screen_width-140*GLOB.MULT, 20*GLOB.MULT))


            GLOB.screen.blit(KEY_TEXT, KEY_RECT)

            if keys_pressed[pygame.K_o]:
                GLOB.Moff -= 1

            if keys_pressed[pygame.K_p]:
                GLOB.Moff += 1

            if GLOB.Player_proportion <= 0.2:
                GLOB.Player_proportion = 0.2
            elif GLOB.Player_proportion >= 10:
                GLOB.Player_proportion = 10

            RUN_TEXT = main.get_font(5*int(GLOB.MULT)).render("V-A: "+str(round(GLOB.Player_speed, 1)), True, "white")
            RUN_RECT = RUN_TEXT.get_rect(center=(295*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(RUN_TEXT, RUN_RECT)

            STATUS_TEXT = main.get_font(5*int(GLOB.MULT)).render("Is Running: "+str(GLOB.PlayerCanRun)+" | Can Run: "+str(GLOB.PlayerCanRun), True, "white")
            STATUS_RECT = STATUS_TEXT.get_rect(center=(295*GLOB.MULT, 30*GLOB.MULT))

           # GLOB.screen.blit(STATUS_TEXT, STATUS_RECT)

            POS_TEXT = main.get_font(8*int(GLOB.MULT)).render("x/y: "+str(int((main.player.getPositionX()-main.cam.getPositionX())/GLOB.MULT))+" | "+str(int((main.player.getPositionY()-main.cam.getPositionY())/GLOB.MULT)), True, "white")
            POS_RECT = POS_TEXT.get_rect(center=(200*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(POS_TEXT, POS_RECT)

            POSP_TEXT = main.get_font(5*int(GLOB.MULT)).render("Player - x/y: "+str(int(main.player.getPositionX()/GLOB.MULT))+" | "+str(int(main.player.getPositionY()/GLOB.MULT)), True, "Red")
            POSP_RECT = POS_TEXT.get_rect(center=(70*GLOB.MULT, 40*GLOB.MULT))

            GLOB.screen.blit(POSP_TEXT, POSP_RECT)

            POSC_TEXT = main.get_font(5*int(GLOB.MULT)).render("Cam - x/y: "+str(int(main.cam.getPositionX()/GLOB.MULT))+" | "+str(int(main.cam.getPositionY()/GLOB.MULT)), True, "Blue")
            POSC_RECT = POS_TEXT.get_rect(center=(70*GLOB.MULT, 60*GLOB.MULT))

            GLOB.screen.blit(POSC_TEXT, POSC_RECT)

            ENIGMA_TEXT = main.get_font(3*int(GLOB.MULT)).render(str(GLOB.enigmi_risolti), True, "White")
            ENIGMA_RECT = ENIGMA_TEXT.get_rect(center=(320*GLOB.MULT, 40*GLOB.MULT))

            GLOB.screen.blit(ENIGMA_TEXT, ENIGMA_RECT)

            INVENTARIO_TEXT = main.get_font(3*int(GLOB.MULT)).render(str(GLOB.inventario.keys()), True, "White")
            INVENTARIO_RECT = INVENTARIO_TEXT.get_rect(center=(100*GLOB.MULT, 90*GLOB.MULT))

            GLOB.screen.blit(INVENTARIO_TEXT, INVENTARIO_RECT)

            main.cam.ShowCam()

        if GLOB.ShowScore:
            SCORE_TEXT = main.get_font(6*int(GLOB.MULT)).render("score: "+str(GLOB.score), True, "white")
            SCORE_RECT = SCORE_TEXT.get_rect(center=(50*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(SCORE_TEXT, SCORE_RECT)


        if GLOB.ShowFps:
            FPS_TEXT = main.get_font(8*int(GLOB.MULT)).render("FPS: "+str(int(main.clock.get_fps())), True, "white")
            FPS_RECT = FPS_TEXT.get_rect(center=(GLOB.screen_width-40*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(FPS_TEXT, FPS_RECT)

        if GLOB.ShowDropFrames:

            DROP_TEXT = main.get_font(5*int(GLOB.MULT)).render("DROP "+str(100-int(main.clock.get_fps()*100/GLOB.FPS))+"%", True, "red")
            DROP_RECT = DROP_TEXT.get_rect(center=(GLOB.screen_width-95*GLOB.MULT, 20*GLOB.MULT))

            if int(main.clock.get_fps()) <= (GLOB.FPS-(GLOB.FPS/20)):
                GLOB.screen.blit(DROP_TEXT, DROP_RECT)
                GLOB.Drop_Frames = True
            else:
                GLOB.Drop_Frames = False