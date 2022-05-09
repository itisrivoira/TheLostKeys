import global_var as GLOB
import pygame, sys
from pygame import mixer

"""
    ---  Classe genera un pulsante a schermo un pulsante cliccabile	---
"""

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font/font.ttf", size)

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, scale):
    	
		if image != None:
			self.image_w, self.image_h = image.get_width()*GLOB.MULT/scale, image.get_height()*GLOB.MULT/scale
			self.image = pygame.transform.scale(image, (self.image_w, self.image_h))
		else:
			self.image = image

		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

	def changeScale(self, position, value):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.image = pygame.transform.scale(self.image, (self.image_w * value, self.image_h * value))
			self.x_pos -= value
			self.y_pos -= value
		else:
			self.image = pygame.transform.scale(self.image, (self.image_w, self.image_h))
			self.x_pos += value
			self.y_pos += value
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

"""
    ---  Classe genera una barra (usata per le statistiche)	e ne imposta il riempimento ---
"""

class Bar():
	def __init__(self, pos, color, number, div):

		self.x_pos = pos[0]
		self.y_pos = pos[1]

		self.color = color
		self.number = number
		self.div = div

		if number > 10:
			self.number = 10
		elif number < 0:
			self.number = 0

		if div == None:
			self.div = 1
		elif div > 8:
			self.div = 8
		elif div < 1:
			self.div = 1

		self.image = pygame.image.load("assets/BarraCompletamento.png")
		self.image = pygame.transform.scale(self.image, (self.image.get_width()*GLOB.MULT/self.div, self.image.get_height()*GLOB.MULT/self.div))
		
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

		if number != 0:
			
			self.BarScore = pygame.Rect(self.x_pos-85*GLOB.MULT/self.div, self.y_pos-3*GLOB.MULT/self.div, 17*GLOB.MULT*self.number/self.div, 6*GLOB.MULT/self.div)
			
		self.BarGrey = pygame.Rect(self.x_pos-85*GLOB.MULT/self.div, self.y_pos-3*GLOB.MULT/self.div, 170*GLOB.MULT/self.div, 6*GLOB.MULT/self.div)

	def update(self, screen):
		pygame.draw.rect(GLOB.screen, "Grey", self.BarGrey)

		if self.number != 0:
			pygame.draw.rect(GLOB.screen, self.color, self.BarScore)
		
		screen.blit(self.image, self.rect)


def get_font(size): # Returns Press-Start-2P in the desired size
	return pygame.font.Font("font/font.ttf", size)

class Dialoghi():
	def __init__(self, personaggio, descrizione, text_speed):
		
		self.personaggio = personaggio
		self.descr = descrizione
		self.descr = descrizione.split("\n")
		self.descr = "".join(self.descr)

		
		self.descr = self.descr.split(" ")

		for var in range(len(self.descr)):

			if self.descr[var] == "VAR":
				# print("Trovato")
				self.descr[var] = GLOB.scelta_char

		self.descr = " ".join(self.descr)

		
		self.delay = 0

		self.descrizione = ""
		self.descrizione1 = ""
		self.descrizione2 = ""
		self.descrizione3 = ""

		# print(self.descr.split(" "))
		# print(len(self.descr.split(" ")))

		# self.lunghezza = self.descr.split(" ")

		self.r0 = False
		self.r1 = False
		self.r2 = False
		self.r3 = False

		self.value = 64
		self.valore = 0
		self.flag_capo = True

		self.cooldown_interm = 0
		self.interm = 0

		if text_speed == 1:
			self.text_speed = 0.1
		elif text_speed == 2:
			self.text_speed = 0.2
		elif text_speed == 3:
			self.text_speed = 0.25
		elif text_speed == 4:
			self.text_speed = 0.5
		elif text_speed == 5:
			self.text_speed = 1
		else:
			self.text_speed = 0.1

		self.contatore = 0

		self.ritardo = 0

		self.CanIplay_sound = True
		self.play_sound = False
		self.cooldown_suono = 0
		self.MaxCooldwon_suono = 0

		self.descr = [self.descr[i:i+1] for i in range(0, len(self.descr), 1)]
		#print(self.descr)
    		
		self.Nome_TEXT = get_font(7*int(GLOB.MULT)).render(self.personaggio, True, "Black")
		self.Nome_RECT = self.Nome_TEXT.get_rect(center=(70*GLOB.MULT, GLOB.screen_height-10*GLOB.MULT))

		self.vignetta = pygame.image.load("Dialoghi/Characters/"+self.personaggio+".png").convert_alpha()
		self.vignetta = pygame.transform.scale(self.vignetta, (self.vignetta.get_width()*GLOB.MULT*2, self.vignetta.get_height()*GLOB.MULT*2))

		self.sfondo = pygame.image.load("assets/Dialoghi.png").convert_alpha()
		self.sfondo = pygame.transform.scale(self.sfondo, (self.sfondo.get_width()*GLOB.MULT, self.sfondo.get_height()*GLOB.MULT))

		self.keySound = mixer.Sound("suoni/char-sound.wav")
		self.keySound.set_volume(0.01*GLOB.AU)

	def __effetto_testo(self):
    		
		# Elenco le varie condizioni (limite massimo di caratteri)

		# if self.descrizione.split(" ") == self.lunghezza[0]:
		# 	pass
		
		# self.value = int((len(self.lunghezza)*len(self.descr))/192)
		# print(self.value)
    		
		self.condition0 = self.contatore < self.value
		self.condition1 = self.contatore >= self.value and self.contatore < self.value * 2
		self.condition2 = self.contatore >= self.value * 2 and self.contatore < self.value * 3
		self.condition3 = self.contatore >= self.value * 3 and self.contatore < self.value * 4
    		
		max = not int((self.delay+1)) > len(self.descr)

		valuex, valuey = 70, 55
		distanza_righe = 12.5

		def Condition(event):
			return self.descr[self.value*event-self.valore] != " " and self.descr[self.value*event-self.valore] != "." and (self.contatore >= self.value*event-self.valore and self.contatore < self.value*event)

		def Cerca(event):
			for value in range(len(self.descr)):
				if self.descr[self.value*event-1-value] == " " and self.flag_capo:
					#print("Trovato buco: ",value)
					self.flag_capo = False
					self.valore = value
    		

		def ScriviTesto1():
			self.descrizione += self.descr[int(round(self.delay, 1))]

			self.Descrizione_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione, True, "White")
			self.Descrizione_RECT = self.Descrizione_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey)*GLOB.MULT))

			self.r0 = True

		def ScriviTesto2():
			self.descrizione1 += self.descr[int(round(self.delay, 1))]

			self.Descrizione1_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione1, True, "White")
			self.Descrizione1_RECT = self.Descrizione1_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey-distanza_righe)*GLOB.MULT))

			self.r1 = True

		def ScriviTesto3():
			self.descrizione2 += self.descr[int(round(self.delay, 1))]

			self.Descrizione2_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione2, True, "White")
			self.Descrizione2_RECT = self.Descrizione2_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey-distanza_righe*2)*GLOB.MULT))

			self.r2 = True

		def ScriviTesto4():
			self.descrizione3 += self.descr[int(round(self.delay, 1))]

			self.Descrizione3_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione3, True, "White")
			self.Descrizione3_RECT = self.Descrizione3_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey-distanza_righe*3)*GLOB.MULT))

			self.r3 = True
		

		# vado a confrontare se il delay corisponde ad un numero intero e non decimale e anche se non ha superato il valore massimo della lista

		if int(self.delay+0.1) == round(self.delay, 1) and max and self.ritardo == 0:

			# CoolDown indicato per eseguire il suono		
			if self.MaxCooldwon_suono != 0:
				if self.cooldown_suono >= 0 and self.cooldown_suono <= self.MaxCooldwon_suono:
					self.cooldown_suono +=1
					self.play_sound = False
				else:
					self.play_sound = True
					self.cooldown_suono = 0
			else:
				self.play_sound = True

			if self.play_sound and self.CanIplay_sound:
				self.keySound.play()

			# Prima riga

			if self.condition0:
				#print("prima condizione")
				if len(self.descr) >= self.value:
        		
					Cerca(1)

					if Condition(1):
						ScriviTesto2()
					else:
						ScriviTesto1()
				else:
					ScriviTesto1()

				self.flag_capo = True

			# Seconda riga
			
			elif self.condition1:
				#print("seconda condizione")
				if len(self.descr) >= self.value*2:
            		
					Cerca(2)

					if Condition(2):
						ScriviTesto3()
					else:
						ScriviTesto2()
				else:
					ScriviTesto2()
				self.flag_capo = True

			# Terza riga

			elif self.condition2:
				#print("terza condizione")
				if len(self.descr) >= self.value*3:
            		
					Cerca(3)

					if Condition(3):
						ScriviTesto4()
					else:
						ScriviTesto3()
				else:
					ScriviTesto3()
				self.flag_capo = True

			elif self.condition3:
				#print("terza condizione")
				ScriviTesto4()

			# contatore che serve a controllare quanti caratteri sono stati inseriti
			self.contatore += 1

			"""if self.contatore >= self.value and self.descrizione[-1] != "" and self.descrizione[-1] != "=" and self.descrizione[-1] != " ":
				self.descrizione += " ="
				self.Descrizione_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione, True, "White")

			if self.contatore >= self.value*2 and self.descrizione1[-1] != "" and self.descrizione1[-1] != "=" and self.descrizione1[-1] != " ":
				self.descrizione1 += " ="
				self.Descrizione1_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione1, True, "White")

			if self.contatore >= self.value*3 and self.descrizione2[-1] != "" and self.descrizione2[-1] != "=" and self.descrizione2[-1] != " ":
				self.descrizione2 += " ="
				self.Descrizione2_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione2, True, "White")

			if self.contatore >= self.value*4 and self.descrizione3[-1] != "" and self.descrizione3[-1] != "=" and self.descrizione3[-1] != " ":
				self.descrizione3 += " ="
				self.Descrizione3_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione3, True, "White")"""
			
		# Delay aggiuntivo per dei caratteri particolari indicati
		if max and self.descr[int(round(self.delay, 1))] != "." and self.descr[int(round(self.delay, 1))] != "?" and self.descr[int(round(self.delay, 1))] != "!" or self.ritardo == 1:
			self.delay += + self.text_speed
			self.ritardo = 0
		else:
			self.ritardo += self.text_speed

		
		#print("Delay: "+str(round(self.delay, 1))+" | Intero: "+str(int(self.delay+0.1))+" | Lunghezza: "+str(len(self.descr))+" | Contatore: "+str(self.contatore)+" | Max: "+str((self.delay+1)))

	def stampa(self):

		clock = pygame.time.Clock()
		
		possoIniziare = False

		while not possoIniziare:
    		
			self.__effetto_testo()

			GLOB.screen.blit(self.sfondo, (0, GLOB.screen_height-self.sfondo.get_height()))
			GLOB.screen.blit(self.vignetta, (42.5*GLOB.MULT, GLOB.screen_height-self.vignetta.get_height()-18*GLOB.MULT))
			GLOB.screen.blit(self.Nome_TEXT, self.Nome_RECT)
			
			if self.r0:
				GLOB.screen.blit(self.Descrizione_TEXT, self.Descrizione_RECT)

			if self.r1:
				GLOB.screen.blit(self.Descrizione1_TEXT, self.Descrizione1_RECT)

			if self.r2:
				GLOB.screen.blit(self.Descrizione2_TEXT, self.Descrizione2_RECT)

			if self.r3:
				GLOB.screen.blit(self.Descrizione3_TEXT, self.Descrizione3_RECT)

			avanza = Button(image=pygame.image.load("assets/tasello.png").convert(), pos=(132*GLOB.MULT,  GLOB.screen_height-12*GLOB.MULT), 
								text_input="", font=pygame.font.Font("font/font.ttf", (8*int(GLOB.MULT))), base_color="White", hovering_color="#d7fcd4", scale=1.8)

			if self.interm == 0 or self.cooldown_interm != GLOB.FPS / 10:
				avanza.update(GLOB.screen)
				self.cooldown_interm += 0.25

			self.interm += 1
			
			if self.interm >= GLOB.FPS and self.cooldown_interm == GLOB.FPS / 10:
				self.interm = 0
				self.cooldown_interm = 0

			for event in pygame.event.get():
				keys_pressed = pygame.key.get_pressed()
    
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

    				
				if event.type == pygame.MOUSEBUTTONDOWN or keys_pressed[pygame.K_SPACE]:
					possoIniziare = True

				#delay.ActualState()


			pygame.display.flip() # ti permette di aggiornare una area dello schermo per evitare lag e fornire piu' ottimizzazione
			pygame.display.update()

			clock.tick(GLOB.FPS) # setto i FramesPerSecond


# risposte (risposta1, risposta2, risposta3)
class Dialoghi_Interattivi():
	def __init__(self, tipo_enigma, personaggio, oggetto, descrizione, suggerimento, risposte, soluzione, difficolta, text_speed):
		self.tipo = tipo_enigma
		self.oggetto = oggetto
		# self.personaggio = personaggio
		self.personaggio = "Verga"
		# self.oggetto = "Narratore"

		self.full_description = descrizione
		self.full_suggeriment = suggerimento

		self.testo_suggerimento = self.full_suggeriment.split("|")

		self.descr = descrizione.split("\n")
		self.sugg = suggerimento.split("\n")
		self.risposte = risposte

		self.number_solution = soluzione - 1
		self.number_selection = 0
		self.number_selected = 0

		self.soluzione = self.risposte[soluzione-1]
		self.descr = "".join(self.descr)
		self.difficolta = difficolta

		self.descr = descrizione.split(" ")	
		for var in range(len(self.descr)):
			if self.descr[var] == "VAR":
				self.descr[var] = GLOB.scelta_char
		self.descr = " ".join(self.descr)

		self.sugg = suggerimento.split(" ")	
		for var in range(len(self.sugg)):
			if self.sugg[var] == "VAR":
				self.sugg[var] = GLOB.scelta_char
		self.sugg = " ".join(self.sugg)

		self.delay = 0

		self.descrizione = ""
		self.descrizione1 = ""
		self.descrizione2 = ""
		self.descrizione3 = ""

		self.r0 = False
		self.r1 = False
		self.r2 = False
		self.r3 = False

		self.value = 86
		self.valore = 0
		self.flag_capo = True
		self.isFinished = False

		self.cooldown_interm = 0
		self.interm = 0

		if text_speed == 1:
			self.text_speed = 0.1
		elif text_speed == 2:
			self.text_speed = 0.2
		elif text_speed == 3:
			self.text_speed = 0.25
		elif text_speed == 4:
			self.text_speed = 0.5
		elif text_speed == 5:
			self.text_speed = 1
		else:
			self.text_speed = 0.1

		self.contatore = 0

		self.ritardo = 0

		self.CanIplay_sound = True
		self.play_sound = False
		self.cooldown_suono = 0
		self.MaxCooldwon_suono = 0

		self.descr = [self.descr[i:i+1] for i in range(0, len(self.descr), 1)]
		#print(self.descr)

		self.background = pygame.image.load("assets/Dialoghi-Sfondo1.png").convert()
		self.background = pygame.transform.scale(self.background, (self.background.get_width()*GLOB.MULT, self.background.get_height()*GLOB.MULT))

		val = 5

		self.vignetta = pygame.image.load("Dialoghi/Characters/"+self.oggetto+".png").convert_alpha()
		self.vignetta = pygame.transform.scale(self.vignetta, (self.vignetta.get_width()*GLOB.MULT*val, self.vignetta.get_height()*GLOB.MULT*val))

		self.scelte = pygame.image.load("assets/vignetta-risposta.png").convert_alpha()
		self.scelte = pygame.transform.scale(self.scelte, (self.scelte.get_width()*GLOB.MULT, self.scelte.get_height()*GLOB.MULT))

		self.sfondo = pygame.image.load("assets/dialoghi-risposta.png").convert_alpha()
		self.sfondo = pygame.transform.scale(self.sfondo, (self.sfondo.get_width()*GLOB.MULT, self.sfondo.get_height()*GLOB.MULT))

		self.keySound = mixer.Sound("suoni/char-sound.wav")
		self.keySound.set_volume(0.01*GLOB.AU)

		self.val_oggetto_max = 12
		self.val_oggetto = self.val_oggetto_max + 1
		self.flag_sali = True
		self.flag_scendi = False

		self.risultato = None
		self.suggerimento = False

		vel = 0.01
		self.class_sfoca = Sfoca(vel)
		self.class_desfoca = Sfoca(val)
		self.class_sfoca.val_scurisci = 0
		self.suggerimento_sfondo = pygame.Surface((GLOB.screen_width, GLOB.screen_height))

	def __effetto_testo(self):
    		
		# Elenco le varie condizioni (limite massimo di caratteri)

		# if self.descrizione.split(" ") == self.lunghezza[0]:
		# 	pass
		
		# self.value = int((len(self.lunghezza)*len(self.descr))/192)
		# print(self.value)
    		
		self.condition0 = self.contatore < self.value
		self.condition1 = self.contatore >= self.value and self.contatore < self.value * 2
		self.condition2 = self.contatore >= self.value * 2 and self.contatore < self.value * 3
		self.condition3 = self.contatore >= self.value * 3 and self.contatore < self.value * 4
    		
		max = not int((self.delay+1)) > len(self.descr)

		valuex, valuey = 45, 55
		distanza_righe = 12.5

		def Condition(event):
			return self.descr[self.value*event-self.valore] != " " and self.descr[self.value*event-self.valore] != "." and (self.contatore >= self.value*event-self.valore and self.contatore < self.value*event)

		def Cerca(event):
			for value in range(len(self.descr)):
				if self.descr[self.value*event-1-value] == " " and self.flag_capo:
					#print("Trovato buco: ",value)
					self.flag_capo = False
					self.valore = value
    		

		def ScriviTesto1():
			self.descrizione += self.descr[int(round(self.delay, 1))]

			self.Descrizione_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione, True, "White")
			self.Descrizione_RECT = self.Descrizione_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey)*GLOB.MULT))

			self.r0 = True

		def ScriviTesto2():
			self.descrizione1 += self.descr[int(round(self.delay, 1))]

			self.Descrizione1_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione1, True, "White")
			self.Descrizione1_RECT = self.Descrizione1_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey-distanza_righe)*GLOB.MULT))

			self.r1 = True

		def ScriviTesto3():
			self.descrizione2 += self.descr[int(round(self.delay, 1))]

			self.Descrizione2_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione2, True, "White")
			self.Descrizione2_RECT = self.Descrizione2_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey-distanza_righe*2)*GLOB.MULT))

			self.r2 = True

		def ScriviTesto4():
			self.descrizione3 += self.descr[int(round(self.delay, 1))]

			self.Descrizione3_TEXT = get_font(4*int(GLOB.MULT)).render(self.descrizione3, True, "White")
			self.Descrizione3_RECT = self.Descrizione3_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, GLOB.screen_height-(valuey-distanza_righe*3)*GLOB.MULT))

			self.r3 = True
		

		# vado a confrontare se il delay corisponde ad un numero intero e non decimale e anche se non ha superato il valore massimo della lista

		if int(self.delay+0.1) == round(self.delay, 1) and max and self.ritardo == 0:

			# CoolDown indicato per eseguire il suono		
			if self.MaxCooldwon_suono != 0:
				if self.cooldown_suono >= 0 and self.cooldown_suono <= self.MaxCooldwon_suono:
					self.cooldown_suono +=1
					self.play_sound = False
				else:
					self.play_sound = True
					self.cooldown_suono = 0
			else:
				self.play_sound = True

			if self.play_sound and self.CanIplay_sound:
				self.keySound.play()

			# Prima riga

			if self.condition0:
				#print("prima condizione")
				if len(self.descr) >= self.value:
        		
					Cerca(1)

					if Condition(1):
						ScriviTesto2()
					else:
						ScriviTesto1()
				else:
					ScriviTesto1()

				self.flag_capo = True

			# Seconda riga
			
			elif self.condition1:
				#print("seconda condizione")
				if len(self.descr) >= self.value*2:
            		
					Cerca(2)

					if Condition(2):
						ScriviTesto3()
					else:
						ScriviTesto2()
				else:
					ScriviTesto2()
				self.flag_capo = True

			# Terza riga

			elif self.condition2:
				#print("terza condizione")
				if len(self.descr) >= self.value*3:
            		
					Cerca(3)

					if Condition(3):
						ScriviTesto4()
					else:
						ScriviTesto3()
				else:
					ScriviTesto3()
				self.flag_capo = True

			elif self.condition3:
				#print("terza condizione")
				ScriviTesto4()

			# contatore che serve a controllare quanti caratteri sono stati inseriti
			self.contatore += 1
			
		# Delay aggiuntivo per dei caratteri particolari indicati
		if max and self.descr[int(round(self.delay, 1))] != "." and self.descr[int(round(self.delay, 1))] != "?" and self.descr[int(round(self.delay, 1))] != "!" or self.ritardo == 1:
			self.delay += self.text_speed
			self.ritardo = 0
		else:
			self.ritardo += self.text_speed

		
		#print("Delay: "+str(round(self.delay, 1))+" | Intero: "+str(int(self.delay+0.1))+" | Lunghezza: "+str(len(self.descr))+" | Contatore: "+str(self.contatore)+" | Max: "+str((self.delay+1)))

	def __object_animation(self):

		if int(self.val_oggetto) <= -self.val_oggetto_max:
			self.flag_sali = False
			self.flag_scendi = True

		elif int(self.val_oggetto) >= self.val_oggetto_max:
			self.flag_sali = True
			self.flag_scendi = False

		if self.flag_scendi:
			self.flag_sali = False
			self.val_oggetto += 0.1 * GLOB.MULT

		elif self.flag_sali:
			self.flag_scendi = False
			self.val_oggetto -= 0.1 * GLOB.MULT


	def __check_score(self):
		# print("tentativo: ", GLOB.tentativo+1)

		if self.risultato:
	
			if self.difficolta == "Facile":
					
				if GLOB.tentativo == 0:
					GLOB.score += 10
				elif GLOB.tentativo == 1:
					GLOB.score += 5
				elif GLOB.tentativo == 2:
					GLOB.score += 2

			elif self.difficolta == "Medio":
				
				if GLOB.tentativo == 0:
					GLOB.score += 40
				elif GLOB.tentativo == 1:
					GLOB.score += 20
				elif GLOB.tentativo == 2:
					GLOB.score += 10

			elif self.difficolta == "Difficile":
					
				if GLOB.tentativo == 0:
					GLOB.score += 60
				elif GLOB.tentativo == 1:
					GLOB.score += 30
				elif GLOB.tentativo == 2:
					GLOB.score += 15
		else:
    		
			if self.difficolta == "Facile":
    			
				if GLOB.tentativo > 2:
					GLOB.score_seconds = -45

			if self.difficolta == "Medio":
        			
				if GLOB.tentativo > 2:
					GLOB.score_seconds = -30


			if self.difficolta == "Difficile":
        			
				if GLOB.tentativo > 2:
					GLOB.score_seconds = -20
			
			# print("secondi tolti")

	def stampa(self):

		clock = pygame.time.Clock()
		
		possoIniziare = False

		while not possoIniziare:
    		
			self.__effetto_testo()

			if not self.class_sfoca.flag_reverse:
				self.__object_animation()

			if self.contatore == len(self.descr):
				self.isFinished = True
				
			GLOB.screen.blit(self.background, (0,0))
			GLOB.screen.blit(self.sfondo, (0, GLOB.screen_height-self.sfondo.get_height()))

			
			if self.class_sfoca.iFinished:
				self.class_sfoca.flag_reverse = False
				self.class_sfoca.val_scurisci = 0

			if not self.class_sfoca.flag_reverse:
				val = 5
				self.vignetta = pygame.image.load("Dialoghi/Characters/"+self.oggetto+".png").convert_alpha()
				self.vignetta = pygame.transform.scale(self.vignetta, (self.vignetta.get_width()*GLOB.MULT*val, self.vignetta.get_height()*GLOB.MULT*val))
				GLOB.screen.blit(self.vignetta, (110*GLOB.MULT, 50*GLOB.MULT + self.val_oggetto))

			if self.class_sfoca.flag_reverse:			
				val = 4
				transparenza = 40

				self.vignetta = pygame.image.load("Characters_Image/"+self.personaggio+".png").convert_alpha()
				self.vignetta = pygame.transform.scale(self.vignetta, (self.vignetta.get_width()*GLOB.MULT*val, self.vignetta.get_height()*GLOB.MULT*val))
				GLOB.screen.blit(self.vignetta, (65*GLOB.MULT, 1*GLOB.MULT))

				self.suggerimento_sfondo.fill((255,255,255))
				self.suggerimento_sfondo.set_alpha(transparenza)

				GLOB.screen.blit(self.suggerimento_sfondo, (0,0))

				for suggerimento in self.testo_suggerimento:

					self.dialogo_suggerimento = Dialoghi(self.personaggio, suggerimento, 3)
					self.dialogo_suggerimento.stampa()
				
				self.class_sfoca.flag_reverse = False
				self.class_sfoca.val_scurisci = 0
				self.suggerimento = False

			TRY_TEXT = get_font(6*int(GLOB.MULT)).render(str(GLOB.tentativo+1)+"° tentativo", True, "white")
			TRY_RECT = TRY_TEXT.get_rect(center=(50*GLOB.MULT, 20*GLOB.MULT))

			GLOB.screen.blit(TRY_TEXT, TRY_RECT)

			if not self.class_sfoca.flag_reverse:

			
				if self.r0:
					GLOB.screen.blit(self.Descrizione_TEXT, self.Descrizione_RECT)

				if self.r1:
					GLOB.screen.blit(self.Descrizione1_TEXT, self.Descrizione1_RECT)

				if self.r2:
					GLOB.screen.blit(self.Descrizione2_TEXT, self.Descrizione2_RECT)

				if self.r3:
					GLOB.screen.blit(self.Descrizione3_TEXT, self.Descrizione3_RECT)


			if self.isFinished:
				GLOB.Enigma = False
				
				if not self.suggerimento:
					GLOB.screen.blit(self.scelte, (280*GLOB.MULT, 12 * GLOB.MULT))
					
				distanza_righe = 23
				valuex, valuey = 138, 30

				font_size = 4
				# print(self.risposte)

				default_color = "#c2c2c2"
				selected_color = "White"

				def imposta_colore(num_risposta):
					if self.number_selection == num_risposta:
						return selected_color	
					else:
						return default_color


				self.RISPOSTA_TEXT = get_font(font_size*int(GLOB.MULT)).render(self.risposte[0], True, imposta_colore(0))
				self.RISPOSTA_RECT = self.RISPOSTA_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, (valuey+distanza_righe)*GLOB.MULT))

				self.RISPOSTA1_TEXT = get_font(font_size*int(GLOB.MULT)).render(self.risposte[1], True, imposta_colore(1))
				self.RISPOSTA1_RECT = self.RISPOSTA1_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, (valuey+distanza_righe*2)*GLOB.MULT))

				self.RISPOSTA2_TEXT = get_font(font_size*int(GLOB.MULT)).render(self.risposte[2], True, imposta_colore(2))
				self.RISPOSTA2_RECT = self.RISPOSTA2_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, (valuey+distanza_righe*3)*GLOB.MULT))

				self.RISPOSTA3_TEXT = get_font(font_size*int(GLOB.MULT)).render(self.risposte[3], True, imposta_colore(3))
				self.RISPOSTA3_RECT = self.RISPOSTA3_TEXT.get_rect(center=(GLOB.screen_width/2+valuex*GLOB.MULT, (valuey+distanza_righe*4)*GLOB.MULT))

				GLOB.screen.blit(self.RISPOSTA_TEXT, self.RISPOSTA_RECT)
				GLOB.screen.blit(self.RISPOSTA1_TEXT, self.RISPOSTA1_RECT)
				GLOB.screen.blit(self.RISPOSTA2_TEXT, self.RISPOSTA2_RECT)
				GLOB.screen.blit(self.RISPOSTA3_TEXT, self.RISPOSTA3_RECT)

			avanza = Button(image=pygame.image.load("assets/tasello.png").convert(), pos=(80*GLOB.MULT,  GLOB.screen_height-12*GLOB.MULT), 
								text_input="", font=pygame.font.Font("font/font.ttf", (8*int(GLOB.MULT))), base_color="White", hovering_color="#d7fcd4", scale=1.8)

			if self.interm == 0 or self.cooldown_interm != GLOB.FPS / 10:
				avanza.update(GLOB.screen)
				self.cooldown_interm += 0.25

			self.interm += 1
			
			if self.interm >= GLOB.FPS and self.cooldown_interm == GLOB.FPS / 10:
				self.interm = 0
				self.cooldown_interm = 0

			if self.suggerimento:
				self.class_sfoca.disegna()

			for event in pygame.event.get():
				keys_pressed = pygame.key.get_pressed()
    
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()


				if keys_pressed[pygame.K_i] and self.isFinished:
					self.suggerimento = True

    				
				if keys_pressed[pygame.K_ESCAPE]:
					possoIniziare = True


				if keys_pressed[pygame.K_SPACE] and not self.isFinished:
					if self.CanIplay_sound:
						self.__init__(self.tipo, self.personaggio, self.oggetto, self.full_description, self.full_suggeriment, self.risposte, self.number_solution + 1, self.difficolta, 5)
						self.CanIplay_sound = False
						self.isFinished = True

				if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_RIGHT]:
					self.number_selection += 1

					if self.number_selection > len(self.risposte) - 1:
						self.number_selection = 0


				if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_LEFT]:
					self.number_selection -= 1

					if self.number_selection < 0:
						self.number_selection = len(self.risposte) - 1


				if keys_pressed[pygame.K_RETURN] and self.isFinished:
					self.number_selected = self.number_selection
					# print(GLOB.tentativo)

					if self.number_selected == self.number_solution:
						# print("Risposta Esatta!!")
						self.risultato = True
						self.__check_score()
						GLOB.tentativo = 0
					else:
						# print("-- Risposta Errata --")
						self.risultato = False
						self.__check_score()
						GLOB.tentativo += 1

					possoIniziare = True
					

				#delay.ActualState()


			pygame.display.flip() # ti permette di aggiornare una area dello schermo per evitare lag e fornire piu' ottimizzazione

			clock.tick(GLOB.FPS) # setto i FramesPerSecond

class Timer():	
	def __init__(self, minutes, molt_sec, event):
		self.__max = minutes
		self.__minimal = 0
		self.__minutes = minutes
		self.__seconds = 0
		self.__decrement = molt_sec
		self.__function = event
		self.__flag = True

		self.__testo1 = ""
		self.__testo2 = ":"

    #print(self.min, self.max, self.increment, self.function)

	def Start(self):
		if self.__flag:
			self.__seconds -= self.__decrement

			if self.__seconds <= 0:
				self.__seconds = 60 * GLOB.FPS
				self.__minutes -= 1

			if self.__seconds/GLOB.FPS < 10:
				self.__testo2 = ":0"
			else:
				self.__testo2 = ":"

			if self.__minutes < 10:
				self.__testo1 = "0"
			else:
				self.__testo1 = ""

			if int(self.getMinutes()) < self.__minimal:
				self.__minutes = self.__minimal
				self.__function()
				self.Pause()

	def ReStart(self):
		if not self.__flag:
			self.__flag = True
			self.__minutes = self.__max

	def Pause(self):
		self.__flag = False

	def DePause(self):
		self.__flag = True

	def AddSeconds(self, value):
		if (self.getSeconds() + value) >= 60 or (self.getSeconds() + value) <= 0:
			if value < 0:
				parse_value = -0.9999
			else:
				parse_value = +0.9999

			self.__minutes += int(value/60 + parse_value)
			
			m =  value//GLOB.FPS

			var = value - (m * 60)
			d = self.getSeconds() + var - 60
			
			self.__seconds += var * GLOB.FPS

			if self.getSeconds() >= 59:
				self.__seconds = d * GLOB.FPS

			# if value != (m * 60):
			# 	self.__minutes -= 1

		else:
			self.__seconds += value * GLOB.FPS
		
		GLOB.score_seconds = 0

	def Stop(self):
		self.__init__(self.__max_sec, self.__molt_sec, self.__function)

	def Show(self):
		testo = get_font(12*int(GLOB.MULT)).render((self.__testo1+str(self.__minutes)+str(self.__testo2)+str(int(self.__seconds/GLOB.FPS))), True, "White")
		GLOB.screen.blit(testo, (GLOB.screen_width/2 - testo.get_width()/2, 35 * GLOB.MULT))

	def getSeconds(self):
		return self.__seconds / GLOB.FPS
    	
	def getMinutes(self):
		return self.__minutes

	def ActualState(self):
		if self.__flag:
			print("| Current Second: %d | Min Seconds: %d | Function: %s |" %(self.getSeconds() * self.getMinutes() * 60, self.__minimal/GLOB.FPS, self.__function))

# var = 0

# def miaFunzione():
#     global var
#     var += 1
#     print(var)

# delay = Delay(sec = 3, event = miaFunzione)

class Delay():
    def __init__(self, sec, event):
        self.__min = 0
        self.__max = sec * GLOB.FPS
        self.__increment = 1
        self.__function = event
        self.__flag = True
        self.__times = 0

    # | Avvia il delay -> Poi si interromperà |
    def Start(self):
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) >= self.__max:
                self.__function()
                self.__flag = False

    # | Restarta il delay |
    def ReStart(self):
        if not self.__flag:
            self.__min = 0
            self.__flag = True

    # | Imposta il delay a infinito |
    def Infinite(self):
        self.ReStart()
        self.Start()

    def TotTimes(self, val):
        if self.__times <= val:
            self.ReStart()
            self.Start()
            self.__times += 1

    # | Stampa lo stato attuale del delay |
    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/GLOB.FPS, self.__max/GLOB.FPS, self.__function))


class Sfoca():
    def __init__(self, vel):
        self.flag_changeBg = True 
        self.__vel = vel
        self.__delay = Delay(sec = self.__vel, event = self.sgrana)
        self.superficie = pygame.surface.Surface((GLOB.screen_width, GLOB.screen_height))
        self.superficie.fill((255,255,255))
        
        self.val_scurisci = 0

        self.flag_reverse = False
        self.iFinished = False

    def Start(self):
        self.__delay.Infinite()

    def sgrana(self):

        if not self.iFinished:

            val_incremento = 5
            val_max = 310
            val_min = 50

            if not self.flag_reverse:
                self.val_scurisci += val_incremento
            else:
                self.val_scurisci -= val_incremento

            if self.val_scurisci >= val_max:
                self.val_scurisci = val_max
                self.flag_reverse = True
            elif self.val_scurisci <= val_min and self.flag_reverse:
                self.val_scurisci = val_min
                self.flag_reverse = False
                self.iFinished = True

            self.superficie.set_alpha(self.val_scurisci)


    def disegna(self):
    
        self.Start()
        GLOB.screen.blit(self.superficie, (0, 0))


class Risultato():
	def __init__(self, text, color, size, delay_scomparsa):
		self.text = text
		self.color = color
		self.size = size

		self.show = True
		self.sec = delay_scomparsa
		self.delay = Delay(self.sec, self.Stop)
		self.isFinished = False

		self.surface = pygame.Surface((GLOB.screen_width, GLOB.screen_height))

	def Stop(self):
		self.isFinished = True
		self.show = False

	def Start(self):
		self.delay.Start()
		self.disegna()

	def ReStart(self):
		self.__init__(self.text, self.color, self.size, self.sec)

	def ChangeParamatrer(self, text, color, size):
		self.text = text
		self.color = color
		self.size = size
		
	def disegna(self):
		transparenza = 120
		altezza = 2
	
		if self.show:
			self.surface.fill((0,0,0))
			self.surface.set_alpha(transparenza)

			GLOB.screen.blit(self.surface, (0,0))

			RISULTATO_TEXT = get_font(self.size*int(GLOB.MULT)).render(self.text, True, self.color)
			RISULTATO_POS = (GLOB.screen_width/2 - RISULTATO_TEXT.get_width()/2, GLOB.screen_height/3 - RISULTATO_TEXT.get_height()/2)

			CONTORNO_TEXT = get_font(self.size*int(GLOB.MULT)).render(self.text, True, "Black")
			CONTORNO_POS = (GLOB.screen_width/2 - CONTORNO_TEXT.get_width()/2, GLOB.screen_height/3 - CONTORNO_TEXT.get_height()/2 + altezza * GLOB.MULT)

			GLOB.screen.blit(CONTORNO_TEXT, CONTORNO_POS)
			GLOB.screen.blit(RISULTATO_TEXT, RISULTATO_POS)


class GUI():
	def __init__(self):
		self.speed = GLOB.PlayerRun_speed

		val = 1
		self.first = pygame.image.load("assets/gui-1.png").convert_alpha()
		self.first = pygame.transform.scale(self.first, (self.first.get_width()/val * GLOB.MULT, self.first.get_height()/val * GLOB.MULT))

		self.second = pygame.image.load("assets/gui-2.png").convert()
		self.second = pygame.transform.scale(self.second, (self.second.get_width()/val * GLOB.MULT, self.second.get_height()/val * GLOB.MULT))
	
		self.third = pygame.image.load("assets/gui-3.png").convert_alpha()
		self.third = pygame.transform.scale(self.third, (self.third.get_width()/val * GLOB.MULT, self.third.get_height()/val * GLOB.MULT))

		self.bar = pygame.image.load("assets/gui-4.png").convert_alpha()
		self.bar = pygame.transform.scale(self.bar, (self.bar.get_width()/val * GLOB.MULT, self.bar.get_height()/val * GLOB.MULT))

		val_player = 1.8

		self.player = pygame.image.load("Dialoghi/Characters/"+GLOB.scelta_char+".png").convert_alpha()
		self.player = pygame.transform.scale(self.player, (self.player.get_width() * val_player * GLOB.MULT, self.player.get_height() * val_player * GLOB.MULT))

		self.max = self.bar.get_width() - GLOB.MULT

		self.color_bar = "#64ad5a"

		self.recupero = 3.7 - self.speed

		self.barra_esaurita = pygame.Rect((84 * GLOB.MULT, GLOB.screen_height - 22 * GLOB.MULT, self.bar.get_width(), self.bar.get_height()))
		self.barra_stamina = pygame.Rect((84 * GLOB.MULT, GLOB.screen_height - 22 * GLOB.MULT, self.max, self.bar.get_height()))

	def __stamina_calculation(self):
    		
		divisore = 3.5

		if GLOB.PlayerIsRunning:
			self.max -= self.speed * GLOB.MULT / divisore
		
		elif not GLOB.PlayerIsRunning and self.max < self.bar.get_width() - GLOB.MULT:
			self.max += self.recupero


		if self.max > self.bar.get_width() - GLOB.MULT - 1:
			self.max = self.bar.get_width() - GLOB.MULT
			GLOB.PlayerCanRun = True
			self.color_bar = "#64ad5a"
		
		elif self.max <= 0:
			self.max = 0
			GLOB.PlayerCanRun = False
			self.color_bar = "#ada55a"

		self.barra_esaurita = pygame.Rect((84 * GLOB.MULT, GLOB.screen_height - 22 * GLOB.MULT, self.bar.get_width(), self.bar.get_height()))
		self.barra_stamina = pygame.Rect((84 * GLOB.MULT, GLOB.screen_height - 22 * GLOB.MULT, self.max, self.bar.get_height()))
	
	def show(self):
    		
		if not GLOB.isPaused and GLOB.PlayerCanMove:
			self.__stamina_calculation()
    		
		GLOB.screen.blit(self.first, (0, GLOB.screen_height - self.first.get_height()))
		GLOB.screen.blit(self.second, (34 * GLOB.MULT, GLOB.screen_height - 63 * GLOB.MULT))
		GLOB.screen.blit(self.player, (33.6 * GLOB.MULT, GLOB.screen_height - 65 * GLOB.MULT))
		GLOB.screen.blit(self.third, (22 * GLOB.MULT, GLOB.screen_height - 75 * GLOB.MULT))

		altezza = 2 * GLOB.MULT
		size = 8

		
		if GLOB.scelta_char == "Dark Angel":
			name = "Dark"
		else:
			name = GLOB.scelta_char
    
		NAME_TEXT = get_font(size*int(GLOB.MULT)).render(name, True, "White")
		NAME_POS = (37 * GLOB.MULT, GLOB.screen_height - 20 * GLOB.MULT)

		CNAME_TEXT = get_font(size*int(GLOB.MULT)).render(name, True, "Black")
		CNAME_POS = (37 * GLOB.MULT, GLOB.screen_height - 20 * GLOB.MULT + altezza)


		if self.max <= 0:
			pygame.draw.rect(GLOB.screen, "#ad5a5a", self.barra_esaurita)

		pygame.draw.rect(GLOB.screen, self.color_bar, self.barra_stamina)
		GLOB.screen.blit(self.bar, (84 * GLOB.MULT, GLOB.screen_height - 22 * GLOB.MULT))

		GLOB.screen.blit(CNAME_TEXT, CNAME_POS)
		GLOB.screen.blit(NAME_TEXT, NAME_POS)


class MiniMap():
	def __init__(self):
		self.path_floor = "Mappa/Floors/"
		self.path_characters = "Mappa/Characters/"

		self.pos_player = 0, 0
		print(GLOB.Piano, GLOB.Stanza)

	def update(self):
		if GLOB.Piano == "0-PianoSegreto":
			self.path_image = "Piano-0"
		
		elif GLOB.Piano == "1-PianoTerra":
			self.path_image = "Piano-1"

			if GLOB.Stanza == "Chimica":
				self.pos_player = 360 * GLOB.MULT, 65 * GLOB.MULT

			if GLOB.Stanza == "Fisica":
				self.pos_player = 310 * GLOB.MULT, 65 * GLOB.MULT

			if GLOB.Stanza == "Corridoio":
				self.pos_player = 310 * GLOB.MULT, 125 * GLOB.MULT

			if GLOB.Stanza == "Archivio":
				self.pos_player = 120 * GLOB.MULT, 320 * GLOB.MULT

		elif GLOB.Piano == "2-PrimoPiano":
			self.path_image = "Piano-2"

		elif GLOB.Piano == "3-SecondoPiano":
			self.path_image = "Piano-3"

		elif GLOB.Piano == "4-Esterno":
			self.path_image = "Piano-4"

		clock = pygame.time.Clock()


		self.image = pygame.image.load(self.path_floor + self.path_image + ".png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (self.image.get_width() * GLOB.MULT, self.image.get_height() * GLOB.MULT))

		
		value = 1

		self.character = pygame.image.load(self.path_characters + GLOB.scelta_char + ".png").convert_alpha()
		self.character = pygame.transform.scale(self.character, (self.character.get_width() * GLOB.MULT * value, self.character.get_height() * GLOB.MULT * value))

		possoIniziare = False

		r = 1.5

		while not possoIniziare:
			for event in pygame.event.get():
				keys_pressed = pygame.key.get_pressed()
    
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if keys_pressed[pygame.K_ESCAPE]:
					possoIniziare = True

			GLOB.screen.blit(self.image, (0, 0))
			pygame.draw.circle(GLOB.screen, "#496e55", (self.pos_player[0] + self.character.get_width()/2, self.pos_player[1] + self.character.get_height()/2), self.character.get_height() / r, 0)
			GLOB.screen.blit(self.character, self.pos_player)

			clock.tick(GLOB.FPS)
			pygame.display.flip()