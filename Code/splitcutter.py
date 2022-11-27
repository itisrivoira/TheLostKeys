from PIL import Image
from itertools import product
import os

path = "../Assets/Elements/Collisions/"

def tile(filename, dir_in, dir_out, d):
   name, ext = os.path.splitext(filename)
   img = Image.open(os.path.join(dir_in, filename))
   w, h = img.size

   grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
   
   incr = 0
   
   tot = (h//d) * (w//d)
   
   for i, j in grid:
      
      prec = len(str(tot)) - len(str(incr))
      prec = "0" * prec
      
      box = (j, i, j+d, i+d)
      out = os.path.join(dir_out, f'tile{prec}{incr}{ext}')
      img.crop(box).save(out)
      
      incr += 1
      
   print("\nPrinted",tot,"tiles\n")

tile( 

      filename = "mappa.png", 
      dir_in = path, 
      dir_out = path, 
      d = 32
      
   )