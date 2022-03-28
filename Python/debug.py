import pygame

#Importo i vari file e classi necessarie
import main

# Importo le variabili Globali
import global_var as GLOB


class Debug():
    def log(self, flag):

        if flag:
            
            pygame.draw.rect(GLOB.screen, (0,255,255), main.player.mesh, int(1*GLOB.MULT))

            sprint = GLOB.Player_speed > GLOB.Player_default_speed
            keys_pressed = pygame.key.get_pressed()

            key = ""

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
            
            FPS_TEXT = main.get_font(8*int(GLOB.MULT)).render("FPS: "+str(int(main.clock.get_fps())), True, "white")
            FPS_RECT = FPS_TEXT.get_rect(center=(GLOB.screen_width-40*GLOB.MULT, 20*GLOB.MULT))

            DROP_TEXT = main.get_font(5*int(GLOB.MULT)).render("DROP "+str(100-int(main.clock.get_fps()*100/GLOB.FPS))+"%", True, "red")
            DROP_RECT = DROP_TEXT.get_rect(center=(GLOB.screen_width-95*GLOB.MULT, 20*GLOB.MULT))

            KEY_TEXT = main.get_font(10*int(GLOB.MULT)).render(key, True, "blue")
            KEY_RECT = KEY_TEXT.get_rect(center=(GLOB.screen_width-140*GLOB.MULT, 20*GLOB.MULT))


            GLOB.screen.blit(KEY_TEXT, KEY_RECT)

            if int(main.clock.get_fps()) <= (GLOB.FPS-(GLOB.FPS/20)):
                #print("Gli fps sono scesi: "+str(clock.get_fps()))
                GLOB.screen.blit(DROP_TEXT, DROP_RECT)
                

            GLOB.screen.blit(FPS_TEXT, FPS_RECT)

            if keys_pressed[pygame.K_o]:
                GLOB.Moff -= 1

            if keys_pressed[pygame.K_p]:
                GLOB.Moff += 1

            if GLOB.Player_proportion <= 0.2:
                GLOB.Player_proportion = 0.2
            elif GLOB.Player_proportion >= 10:
                GLOB.Player_proportion = 10

            RUN_TEXT = main.get_font(8*int(GLOB.MULT)).render("V-A: "+str(round(GLOB.Player_speed, 1)), True, "white")
            RUN_RECT = RUN_TEXT.get_rect(center=(40*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(RUN_TEXT, RUN_RECT)

            POS_TEXT = main.get_font(8*int(GLOB.MULT)).render("x/y: "+str(int(main.player.getPositionX()-main.cam.getPositionX()))+" | "+str(int(main.player.getPositionY()-main.cam.getPositionY())), True, "white")
            POS_RECT = POS_TEXT.get_rect(center=(200*GLOB.MULT, 20*GLOB.MULT))

            GLOB.screen.blit(POS_TEXT, POS_RECT)
        