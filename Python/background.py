import pygame, sys, time, random
from pygame import mixer

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920,1080))

FPS = 60
AU = 5
MULT = 4


thunder = False

offset = 40 * MULT

mixer.init()
mixer.music.load("suoni/Rain-sound.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.01*AU)

class Rain():

   def __init__(self, screen, height, speed, color, numdrops):
      'Create and reuse raindrop particles'
      self.screen     = screen
      self.drops      = []
      self.height     = height
      self.speed      = speed
      self.color      = color
      self.numdrops   = numdrops

      for i in range(self.numdrops):
         # Randomize the size of the raindrop.
         raindropscale = random.randint(int(5*MULT), int(15*MULT)) / 100.0
         w, h = 3, int(raindropscale * self.height)
         # The bigger the raindrop, the faster it moves.
         velocity = raindropscale * self.speed/10.0
         pic = pygame.Surface((w, h), pygame.SRCALPHA, 32).convert_alpha()
         colorinterval = float(self.color[3] * raindropscale)/(h+1)
         r, g, b = self.color[:3]
         for j in range(h):
               # The smaller the raindrop, the dimmer it is.
               a = int(colorinterval * j)
               pic.fill( 
                           (r if r <= 255 else 255, g if g <= 255 else 255, b if b <= 255 else 255, a if a <= 255 else 255), 
                           (1, j, w-2, 1) 
                     )
               
               pygame.draw.circle  (   pic, 
                                       (r if r <= 255 else 255, g if g <= 255 else 255, b if b <= 255 else 255, a if a <= 255 else 255), 
                                       (1, h-2), 
                                       2
                                 )
               
         drop = Rain.Drop(self.speed, velocity, pic)
         self.drops.append(drop)

   def Timer(self, now):
      ' Render the rain'
      dirtyrects = []
      for drop in self.drops:
         r = drop.Render(self.screen, now)
         if r:
               i = r.collidelist(dirtyrects)
               if i > -1:
                  dirtyrects[i].union_ip(r)
               else:
                  dirtyrects.append(r)
      return dirtyrects


   def AdjustSpeed(self, adj):
      newspeed = self.speed + adj
      newspeed = max(1, newspeed)
      newspeed = min(100, newspeed)
      self.speed = newspeed
      for drop in self.drops:
         drop.SetSpeed(newspeed)
      print ('Rain speed: %d' % newspeed)


   class Drop():
      ' Rain drop used by rain generator'
      nexttime = 0   # The next time the raindrop will draw
      interval = .01 # How frequently the raindrop should draw

      def __init__(self, speed, scale, pic):
         ' Initialize the rain drop'
         self.speed = speed
         self.scale = scale
         self.pic = pic
         self.size = pic.get_size()
         self.SetSpeed(speed)
         self.pos = [random.random() * (screen.get_width() + offset), -random.randint(-int(screen.get_height() + offset), int(screen.get_height() + offset)) + 80 * int(MULT)]
         self.currentspeed = speed

      def SetSpeed(self, speed):
         ' Speed up or slow down the drop'
         self.speed = speed
         self.velocity = self.scale * self.speed/10.0

      def Reset(self):
         ' Restart the drop at the top of the screen.'
         self.pos = [random.random() * (screen.get_width() + offset), -random.random() * self.size[1] - self.size[1] + 80 * MULT]
         self.currentspeed = self.speed

      def Render(self, screen, now):
         ' Draw the rain drop'
         if now < self.nexttime:
               return None
         self.nexttime = now + self.interval
         oldrect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]+self.currentspeed)
         self.pos[1] += self.currentspeed
         newrect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
         r = oldrect.union(newrect)
         screen.blit(self.pic, self.pos)
         self.currentspeed += self.velocity
         if self.pos[1] > screen.get_height() + offset -40*MULT:
               self.Reset()
         return r


tuono = pygame.image.load("assets/tuono.png").convert()
tuono = pygame.transform.scale(tuono, (tuono.get_width()*MULT, tuono.get_height()*MULT))


sfondo = pygame.image.load("assets/SfondoScuola.png").convert()
sfondo = pygame.transform.scale(sfondo, (sfondo.get_width()*MULT/2, sfondo.get_height()*MULT/2))



rain = Rain(screen, height = int(60 * MULT - offset), speed = 6 * MULT, color = (152, 164, 184, 255), numdrops = 270)


clouds = pygame.image.load("assets/Cloud.png").convert_alpha()
clouds = pygame.transform.scale(clouds, (clouds.get_width()*MULT/2,clouds.get_height()*MULT/2))

sec = 0.15
delay = sec * FPS
act_sec = delay + 1

def quit():
   pygame.quit()
   sys.exit()

def testa():
   global sfondo, clouds, tuono, rain, thunder
   global act_sec, delay
   
   while True:
      
      screen.blit(sfondo, (0, 0))
      
      for event in pygame.event.get():
         
         if event.type == pygame.QUIT:
            quit()
         
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               quit()

      if (random.randint(0, (100 * FPS)) >= (98 * FPS)) and thunder:
         act_sec = 0
         
         
         val = 0.16 * AU

         tuonoSound = [mixer.Sound("suoni/thunder-sound.wav"), mixer.Sound("suoni/thunder-sound2.wav")]

         tuonoSound[0].set_volume(val)
         tuonoSound[1].set_volume(val)

         random.choice(tuonoSound).play()
         
      dirtyrects = rain.Timer(time.time())

      screen.blit(clouds, (0, 0))
      
      if act_sec < delay and thunder:
         act_sec += 1
         screen.blit(tuono, (0, 0))

      # Update the screen for the dirty rectangles only
      pygame.display.update(dirtyrects)
         
      clock.tick(FPS)
      pygame.display.flip()

if __name__ == "__main__":
   pygame.init()
   testa()

