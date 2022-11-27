from screen import *
from audio import *
from flags import *
from stats import *

# DEFAULT VALUES:
Default_path = '../Assets/Map/Building'
Map = []

Scelta = 0

KeyPressed = ""

PlayerContRoom = 0
MonsterContRoom = 0

SecondDiffPos = 10



def setFPS():
   global MoltTime, Default_DeltaTime, FPS, Performance
   
   if Flags["Performance"]:
      MoltTime += 1
   else:
      MoltTime -= 1
      
   DEF.setMultipliers(time_multiplier = MoltTime)

def setCharacter():

   global Player_speed, Player_default_speed, PlayerRun_speed, scelta_char, scelta_rep
   
   Player_speed = 2 * DEF.getScreenMolt() / DEF.getTimeMolt() * DEF.getDeltaTime() / Player_proportion
   Player_default_speed = Player_speed
   
   scelta_char = list(Stats.keys())[Scelta]
   PlayerRun_speed = 1 + Stats[scelta_char]["Velocita"]/10

def setMonster():
   global Monster_speed, MonsterRun_speed, Monster_default_speed
   
   # -- MOSTRO
   Monster_speed = Player_default_speed - (0.75 * DEF.getScreenMolt() / DEF.getTimeMolt() * DEF.getDeltaTime())
   Monster_default_speed = Monster_speed
   MonsterRun_speed = PlayerRun_speed

setFPS()
setCharacter()
setMonster()


def setResources():
   global score, score_seconds, tentativo, Record
   global inventario, Inventory_support

   global codice, codice_archivio, ShowCodice

   global enigmi_da_risolvere, enigmi_risolti
   global chiavette, chiavetta_start, chiavetta_end
   global RandomKey, RandomRoom
   global oggetti, oggetti_start, oggetti_end

   global MonsterActualFloor, MonsterActualRoom, MonsterSpawning, MonsterIntro, MonsterCanChangeRoom
   global MonsterHasSeenPlayer, MonsterAggr, MonsterIsAttacking
   
   global Default_Character, PlayerCanInteract, PlayerInteract, PlayerTextInteract, PlayerCanMove, PlayerCanRun, PlayerCanHide, PlayerIsHidden, PlayerIsMoving, PLayerMovement, PlayerIsWalking, PlayerIsRunning, PlayerCanCollect
   global Piano, Stanza, Default_path, Default_Map, Default_object, Default_walls, Default_collisions
   
   global stanze_da_visitare, stanze_visitate
   
   global TimerMin, TimerSec
   global PlayerXSpawn, PlayerYSpawn
   global CamXSpawn, CamYSpawn, CamPosX, CamPosY
   global MonsterXSpawn, MonsterYSpawn
   
   global Mappa_Immagine, Muri_Immagine, Oggetti_Immagine
   
   global ShowIntro

   # -- CODICI ---
   
   codice_archivio = False
   
   value_cod_max = 9999
   codice = str(random.randint(0, value_cod_max))
   
   l = "0"
   z = len(str(value_cod_max)) - len(codice)


   for i in range(z):
      codice = l + str(codice)
      
      
      
   ShowCodice = False

   # --- SCORE ---

   score = 0
   score_seconds = 0

   # Apri il file in modalita lettura
   if not os.path.exists("score.txt"):
      with open('score.txt', 'w') as f:
         f.write("Record:\n0")
      f.close()
      
   with open('score.txt', 'r') as f:
      f_contest = f.readlines()
      Record = f_contest[1]
   f.close()

   # --- ENIGMI ---

   tentativo = {}
   enigmi_da_risolvere = ["Fisica", "1A", "WC-Femmine", "AulaMagna", "AulaProfessori", "LabInfo", "4A", "AulaVideo", "LabInformatica", "Ripostiglio", "1D", "Corridoio3", "Chimica", "Archivio"]
   enigmi_risolti = []

   # --- INVENTARIO ---


   # CHIAVETTE

   chiavette = {}
   chiavetta_start = 140
   molt_chiavetta = 2

   # CHIAVETTE CON POSSIBILE SOLUZIONE
   lista_chiavette = [4, 2, 5, 7, 8, 9, 11, 12]
   RandomKey = "chiavetta-" + str(random.choice(lista_chiavette))


   for i in enigmi_da_risolvere:
      tentativo[i] = 0
      
      if enigmi_da_risolvere.index(i)+1 <= 12:
         immagine = py.image.load("../Assets/Elements/Collectibles/chiavetta-" + str(enigmi_da_risolvere.index(i) + 1)+".png").convert_alpha()
         immagine = py.transform.scale(immagine, (immagine.get_width() * DEF.getScreenMolt() * molt_chiavetta, immagine.get_height() * DEF.getScreenMolt() * molt_chiavetta))
         chiavette[i] = (chiavetta_start, True, immagine, (enigmi_da_risolvere.index(i) + 1))
         chiavetta_start += 1
         chiavetta_end = chiavetta_start
         
         if "chiavetta-" + str(enigmi_da_risolvere.index(i) + 1) == RandomKey:
               RandomRoom = i
               
         # print( "| " + str(i)+": "  + str(chiavette[i][0])+" - " + str(chiavette[i][1])+ "| - chiavetta-" + str(enigmi_da_risolvere.index(i) + 1))

   chiavetta_start = 140

   #  -- STANZE --
   
   stanze_da_visitare = ["Chimica", "Fisica", "Archivio", "1A", "1D", "AulaMagna", "AulaProfessori", "LabInfo", "WC-Femmine", "WC-Maschi", "4A", "AulaVideo", "LabInformatica", "Ripostiglio"]
   stanze_visitate = []



   # OGGETTI

   oggetti = {}
   oggetti_start = 154
   molt_oggetto = 2
   oggetti_end = 4

   for i in range(oggetti_end):
      immagine = py.image.load("../Assets/Elements/Collectibles/oggetto-" + str(i)+".png").convert_alpha()
      immagine = py.transform.scale(immagine, (immagine.get_width() * DEF.getScreenMolt() * molt_oggetto, immagine.get_height() * DEF.getScreenMolt() * molt_oggetto))
      oggetti[i] = (oggetti_start, True, immagine)
      oggetti_start += 1
      # print( "| " + str(i)+": "  + str(oggetti[i][0])+" - " + str(oggetti[i][1])+ "| ")

   oggetti_start = 154
   oggetti_end = oggetti_start + oggetti_end

   PlayerCanCollect = False


   inventario = {}
   Inventory_support = {}
      
   Default_Character = 'Characters/Senex/WalkOrizontal/Walk0.png'

   Piano = "1-PianoTerra"
   Stanza = "Corridoio1"
   Default_Map = Default_path + '/1-PianoTerra/Corridoio1/png/Corridoio.png'
   Default_object = None
   Default_walls = Default_path + '/1-PianoTerra/Corridoio1/png/CorridoioMuri.png'
   Default_collisions = 'Corridoio_Collisioni.csv'

   PlayerCanMove = True
   PlayerCanRun = True
   PlayerCanHide = True
   PlayerIsHidden = False
   PlayerInteract = False
   PlayerCanInteract = False
   PlayerTextInteract = "Interagisci"

   PlayerIsWalking = True
   PlayerIsRunning = False
   PlayerIsMoving = False

   PLayerMovement = {
         
   "up": False, 
   "down": False, 
   "left": False, 
   "right": False, 
         
   }
   
   ShowIntro = True
   
   MonsterActualFloor = "1-PianoTerra"
   MonsterActualRoom = "Corridoio1"
   MonsterSpawning = False
   MonsterIntro = True
   MonsterCanChangeRoom = False
   
   MonsterHasSeenPlayer = False
   MonsterAggr = False
   MonsterIsAttacking = False
   
   TimerMin, TimerSec = 15, 0
   PlayerXSpawn, PlayerYSpawn = 200 * DEF.getScreenMolt(), 100 * DEF.getScreenMolt()
   CamXSpawn, CamYSpawn = 130 * DEF.getScreenMolt(), -167 * DEF.getScreenMolt()
   MonsterXSpawn, MonsterYSpawn = 160 * DEF.getScreenMolt(), 120 * DEF.getScreenMolt()
   
   CamPosX = 0
   CamPosY = 0

   Mappa_Immagine = None
   Oggetti_Immagine = None
   Muri_Immagine = None

setResources()


# Game Management

def SaveGame():
   global AlertSalva
   
   # Apri il file in modalita lettura
   if not os.path.exists("dati.txt"):
      with open('dati.txt', 'w') as f:
         AlertSalva = True
         f.write("")
   
   with open('dati.txt', 'w') as f:
      f.write("""
         
--- DATI SALVATI ---
   - Giocatore:
      Giocatore Piano = |""" + str(Piano) + """|
      Giocatore Stanza = |""" + str(Stanza) + """|
      Default_Map = |""" + str(Default_Map) + """|
      Default_object = |""" + str(Default_object) + """|
      Default_walls = |""" + str(Default_walls) + """|
      Default_collisions = |""" + str(Default_collisions) + """|
      Enigmi da risolvere = |""" + str(enigmi_da_risolvere) + """|
      Enigmi risolti = |""" + str(enigmi_risolti) + """|
      Stanze da visitare = |""" + str(stanze_da_visitare) + """|
      Stanze visitate = |""" + str(stanze_visitate) + """|
      Inventario = |""" + str(Inventory_support) + """|
      Scelta = |""" + str(Scelta) + """|
      Giocatore X = |""" + str(PlayerXSpawn) + """|
      Giocatore Y = |""" + str(PlayerYSpawn) + """|
   
   - Camera:
      Camera X = |""" + str(CamXSpawn) + """|
      Camera Y = |""" + str(CamYSpawn) + """|
   
   - Mostro:
      Mostro Piano = |""" + str(MonsterActualFloor) + """|
      Mostro Stanza = |""" + str(MonsterActualRoom) + """|
      Mostro isSpawned = |""" + str(MonsterSpawning) + """|
      Mostro HasSeenPlayer = |""" + str(MonsterHasSeenPlayer) + """|
      Mostro Aggr = |""" + str(MonsterAggr) + """|
      Mostro IsAttacking = |""" + str(MonsterIsAttacking) + """|
      Mostro X = |""" + str(MonsterXSpawn) + """|
      Mostro Y = |""" + str(MonsterYSpawn) + """|
      
      
   - Timer:
      Minuti = |""" + str(TimerMin) + """|
      Secondi = |""" + str(TimerSec) + """|
      
   - Score:
      ActualScore = |""" + str(score) + """|
      ShowCodice = |""" + str(ShowCodice) + """|
      
   - Comands:
      ShowIntro = |""" + str(ShowIntro) + """|
      MonsterIntro = |""" + str(MonsterIntro) + """|
      
   - USB Keys:
      RandomKey = |""" + str(RandomKey) + """|
                  
         """)
      
      f.close()
   
def LoadGame(flag):
   global score, score_seconds, tentativo, Record
   global inventario, Inventory_support

   global codice, codice_archivio, ShowCodice

   global enigmi_da_risolvere, enigmi_risolti
   global chiavette, chiavetta_start, chiavetta_end
   global RandomKey, RandomRoom
   global oggetti, oggetti_start, oggetti_end

   global MonsterActualFloor, MonsterActualRoom, MonsterSpawning, MonsterIntro, MonsterCanChangeRoom
   global MonsterHasSeenPlayer, MonsterAggr, MonsterIsAttacking
   
   global Default_Character, PlayerCanInteract, PlayerInteract, PlayerTextInteract, PlayerCanMove, PlayerCanRun, PlayerCanHide, PlayerIsHidden, PlayerIsMoving, PLayerMovement, PlayerIsWalking, PlayerIsRunning, PlayerCanCollect
   global Piano, Stanza, Default_Map, Default_object, Default_walls, Default_collisions
   
   global stanze_da_visitare, stanze_visitate
   
   global TimerMin, TimerSec
   global PlayerXSpawn, PlayerYSpawn
   global CamXSpawn, CamYSpawn
   global MonsterXSpawn, MonsterYSpawn
   
   global Scelta, ShowIntro
   
   if flag and os.path.exists("dati.txt"):
      
      
      with open('dati.txt', 'r') as f:
         f_contest = f.readlines()
         
         
         def cont(v):
               g = f_contest[v].split("=")[1]
               g = "".join(g)
               return g.split("|")[1]
         
         
         Piano, Stanza = cont(4), cont(5)
         Default_Map, Default_object, Default_walls, Default_collisions = cont(6), cont(7), cont(8), cont(9)
         enigmi_da_risolvere, enigmi_risolti = ast.literal_eval(cont(10)), ast.literal_eval(cont(11))
         stanze_da_visitare = ast.literal_eval(cont(12))
         stanze_visitate = ast.literal_eval(cont(13))
         
         Inventory_support = ast.literal_eval(cont(14))
         
         for i in range(len(Inventory_support)):
               
               if "chiavetta" in Inventory_support[i][0]:
                  molt_oggetto = 2
                  immagine = py.image.load("./Collectibles/"+ str(Inventory_support[i][0]) + ".png").convert_alpha()
                  immagine = py.transform.scale(immagine, (immagine.get_width() * DEF.getScreenMolt() * molt_oggetto, immagine.get_height() * DEF.getScreenMolt() * molt_oggetto))
                  inventario[Inventory_support[i][0]] = (immagine, Inventory_support[i][1], Inventory_support[i][2])
               
               else:
                  tipo = 0
                  if "Ghiaccio" in Inventory_support[i][0]:
                     tipo = 0
                  elif "Libro" in Inventory_support[i][0]:
                     tipo = 1
                  elif "Chiave" in Inventory_support[i][0]:
                     tipo = 3
                  
                  inventario[Inventory_support[i][0]] = (oggetti[tipo][2], Inventory_support[i][1], Inventory_support[i][2])

         
         
         Scelta = int(cont(15))
         PlayerXSpawn, PlayerYSpawn = float(cont(16)) * DEF.getScreenMolt(), float(cont(17)) * DEF.getScreenMolt()
         
         CamXSpawn, CamYSpawn = float(cont(20)) * DEF.getScreenMolt(), float(cont(21)) * DEF.getScreenMolt()
         
         MonsterActualFloor, MonsterActualRoom = cont(24), cont(25)
         MonsterSpawning, MonsterHasSeenPlayer, MonsterAggr, MonsterIsAttacking = ast.literal_eval(cont(26)), ast.literal_eval(cont(27)), ast.literal_eval(cont(28)), ast.literal_eval(cont(29))
         MonsterXSpawn, MonsterYSpawn = float(cont(30)) * DEF.getScreenMolt(), float(cont(31)) * DEF.getScreenMolt()
         
         TimerMin, TimerSec = int(cont(35)), float(cont(36))
         
         score = int(cont(39))
         ShowCodice = ast.literal_eval(cont(40))
         
         ShowIntro = ast.literal_eval(cont(43))
         MonsterIntro = ast.literal_eval(cont(44))
         
         RandomKey = cont(47)
         
      f.close()