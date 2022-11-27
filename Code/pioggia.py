from __modules__ import *
import global_var as G

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
            raindropscale = random.randint(5*DEF.getScreenMolt(), 15*DEF.getScreenMolt()) / 100.0
            w, h = 3, int(raindropscale * self.height)
            # The bigger the raindrop, the faster it moves.
            velocity = raindropscale * self.speed/10.0
            pic = pygame.Surface((w, h), pygame.SRCALPHA, 32).convert_alpha()
            colorinterval = float(self.color[3] * raindropscale)/h
            r, g, b = self.color[:3]
            for j in range(h):
                # The smaller the raindrop, the dimmer it is.
                a = int(colorinterval * j)
                pic.fill( (r, g, b, a), (1, j, w-2, 1) )
                pygame.draw.circle(pic, (r, g, b, a), (1, h-2), 2)
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
            self.pos = [random.random() * DEF.getScreenResolution()[0] + DEF.getScreenResolution()[0]/3, -random.randint(-DEF.getScreenResolution()[1], DEF.getScreenResolution()[1]) + 80 * DEF.getScreenMolt()]
            self.currentspeed = speed

        def SetSpeed(self, speed):
            ' Speed up or slow down the drop'
            self.speed = speed
            self.velocity = self.scale * self.speed/10.0

        def Reset(self):
            ' Restart the drop at the top of the screen.'
            self.pos = [random.random() * DEF.getScreenResolution()[0] + DEF.getScreenResolution()[0]/3, -random.random() * self.size[1] - self.size[1] + 80 * DEF.getScreenMolt()]
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
            if self.pos[1] > DEF.getScreenResolution()[1]-40*DEF.getScreenMolt():
                self.Reset()
            return r

def main():
    # Initialize pygame
    pygame.init()
    pygame.key.set_repeat(500, 30)
    screen = pygame.display.set_mode((DEF.getScreenResolution()[0], DEF.getScreenResolution()[1]), 0, 32)

    # Create rain generator
    rain = Rain(screen, height = 160, speed = 12, color = (152, 164, 184, 255), numdrops = 260)
    print ('right arrow to increase speed, left arrow to decrease speed.')

    # Main loop
    quitgame = 0
    while not quitgame:

        # Emulate CPU usage.
        # Commenting this out will no longer matter,
        # as the raindrops update on a timer.
        time.sleep(.01)

        # Draw rain
        dirtyrects = rain.Timer(time.time())

        # Update the screen for the dirty rectangles only
        pygame.display.update(dirtyrects)

        # Fill the background with the dirty rectangles only
        for r in dirtyrects:
            screen.fill((0, 0, 0), r)

        # Look for user events
        pygame.event.pump()
        for e in pygame.event.get():
            if e.type in [pygame.QUIT, pygame.MOUSEBUTTONDOWN]:
                quitgame = 1
                break
            elif e.type == pygame.KEYDOWN:
                if e.key == 27:
                    quitgame = 1
                    break
                elif e.key in [pygame.K_LEFT, pygame.K_UP]:
                    rain.AdjustSpeed(-1)
                elif e.key in [pygame.K_RIGHT, pygame.K_DOWN]:
                    rain.AdjustSpeed(1)

    # Terminate pygame
    pygame.quit()

if __name__ == "__main__":
    main()