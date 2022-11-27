from __modules__ import *

def fill(path):
   FileNames = os.listdir(path)

   try:
      FileNames.sort(key=lambda f: int(re.sub('\D', '', f)))
   except:
      FileNames.sort()
      
   sorted(FileNames)

   files = []
   
   for filename in FileNames:
      if "." in filename:
         files.append(filename)
      
   return files