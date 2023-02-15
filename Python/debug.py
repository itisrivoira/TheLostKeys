import pygame, os, sys

#Importo i vari file e classi necessarie
import main

# Importo le variabili Globali
import global_var as GLOB


class Debug():
    def log(self):
        
        if GLOB.Debug:
            GLOB.ShowRecord = False
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

            KEY_TEXT = main.get_font(12*int(GLOB.MULT+0.9)).render(key, True, "#ffffff", "#00000048")
            KEY_RECT = KEY_TEXT.get_rect(center=(GLOB.screen_width-120*GLOB.MULT, 20*GLOB.MULT))


            GLOB.screen.blit(KEY_TEXT, KEY_RECT)

            if keys_pressed[pygame.K_o]:
                GLOB.Moff -= 1

            if keys_pressed[pygame.K_p]:
                GLOB.Moff += 1

            if GLOB.Player_proportion <= 0.2:
                GLOB.Player_proportion = 0.2
            elif GLOB.Player_proportion >= 10:
                GLOB.Player_proportion = 10

            RUN_TEXT = main.get_font(2*int(GLOB.MULT+0.9)).render("V-A: "+str(round(GLOB.Player_speed, 1)), True, "white")
            RUN_RECT = RUN_TEXT.get_rect(center=(295*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(RUN_TEXT, RUN_RECT)

            STATUS_TEXT = main.get_font(2*int(GLOB.MULT+0.9)).render("Is Walking: "+str(GLOB.PlayerIsWalking)+" | Is Running: "+str(GLOB.PlayerIsRunning), True, "white")
            STATUS_RECT = STATUS_TEXT.get_rect(center=(295*GLOB.MULT, 60*GLOB.MULT))

            # GLOB.screen.blit(STATUS_TEXT, STATUS_RECT)

            POS_TEXT = main.get_font(5*int(GLOB.MULT+0.9)).render("x/y: "+str(int((main.player.getPositionX()-main.cam.getPositionX())/GLOB.MULT))+" | "+str(int((main.player.getPositionY()-main.cam.getPositionY())/GLOB.MULT)), True, "white")
            POS_RECT = POS_TEXT.get_rect(center=(200*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(POS_TEXT, POS_RECT)

            POSP_TEXT = main.get_font(3*int(GLOB.MULT+0.9)).render("Player - x/y: "+str(int(main.player.getPositionX()/GLOB.MULT))+" | "+str(int(main.player.getPositionY()/GLOB.MULT)), True, "Red")
            POSP_RECT = POS_TEXT.get_rect(center=(70*GLOB.MULT, 40*GLOB.MULT))

            GLOB.screen.blit(POSP_TEXT, POSP_RECT)

            POSC_TEXT = main.get_font(3*int(GLOB.MULT+0.9)).render("Cam - x/y: "+str(int(main.cam.getPositionX()/GLOB.MULT))+" | "+str(int(main.cam.getPositionY()/GLOB.MULT)), True, "Blue")
            POSC_RECT = POS_TEXT.get_rect(center=(70*GLOB.MULT, 60*GLOB.MULT))

            GLOB.screen.blit(POSC_TEXT, POSC_RECT)

            main.cam.ShowCam()
            
            
            DIFF_TEXT = main.get_font(3*int(GLOB.MULT+0.9)).render("Secondi: "+str(GLOB.SecondDiffPos), True, "#fffb23")
            DIFF_RECT = DIFF_TEXT.get_rect(center=(50*GLOB.MULT, 50*GLOB.MULT))
            
            SEC_TEXT = main.get_font(3*int(GLOB.MULT+0.9)).render("Secondi Rit: "+str(GLOB.Val_sec), True, "#23fff4")
            SEC_RECT = SEC_TEXT.get_rect(center=(110*GLOB.MULT, 50*GLOB.MULT))

            GLOB.screen.blit(DIFF_TEXT, DIFF_RECT)
            GLOB.screen.blit(SEC_TEXT, SEC_RECT)
            
        else:
            GLOB.ShowRecord = True

        if GLOB.ShowScore:
            SCORE_TEXT = main.get_font(6*int(GLOB.MULT+0.9)).render("score: "+str(GLOB.score), True, "white")
            SCORE_RECT = SCORE_TEXT.get_rect(center=(50*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(SCORE_TEXT, SCORE_RECT)

        if GLOB.ShowRecord:
            RECORD_TEXT = main.get_font(6*int(GLOB.MULT+0.9)).render("Record: "+str(GLOB.Record), True, "white")
            RECORD_RECT = RECORD_TEXT.get_rect(center=(140*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(RECORD_TEXT, RECORD_RECT)

        if GLOB.ShowFps:
            FPS_TEXT = main.get_font(6*int(GLOB.MULT+0.9)).render("FPS: "+str(int(main.clock.get_fps())), True, "white")
            FPS_RECT = FPS_TEXT.get_rect(center=(GLOB.screen_width-40*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(FPS_TEXT, FPS_RECT)
            
        if GLOB.ShowCodice:
            COD_TEXT = main.get_font(6*int(GLOB.MULT+0.9)).render(str(GLOB.codice), True, "White")
            COD_RECT = COD_TEXT.get_rect(center=(GLOB.screen_width/2, 13*GLOB.MULT))
            
            COV_TEXT = main.get_font(6*int(GLOB.MULT+0.9)).render(str(GLOB.codice), True, "Black")
            COV_RECT = COV_TEXT.get_rect(center=(GLOB.screen_width/2, 14*GLOB.MULT))

            GLOB.screen.blit(COV_TEXT, COV_RECT)
            GLOB.screen.blit(COD_TEXT, COD_RECT)

        if GLOB.ShowDropFrames and GLOB.Debug:

            DROP_TEXT = main.get_font(3*int(GLOB.MULT+0.9)).render("DROP "+str(100-int(main.clock.get_fps()*100/GLOB.FPS))+"%", True, "red")
            DROP_RECT = DROP_TEXT.get_rect(center=(GLOB.screen_width-95*GLOB.MULT, 20*GLOB.MULT))

            if int(main.clock.get_fps()) <= (GLOB.FPS-(GLOB.FPS/20)):
                GLOB.screen.blit(DROP_TEXT, DROP_RECT)
                GLOB.Drop_Frames = True
            else:
                GLOB.Drop_Frames = False