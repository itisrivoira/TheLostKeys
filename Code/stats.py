"""

   ---   FILE DELLA GESTIONE STATISTICHE   ---

"""


Senex_Evaluations = { 
                     
                        "Chimica": 8,
                        "Storia": 6,
                        "Inglese": 7,
                        "Fisica": 3,
                        "Matematica": 6, 
                        "Informatica": 6,
                        "Italiano": 5,
                        "Sistemi": 4,
                        "TPSIT": 10 
                        
                     }

Seima_Evaluations = { 
                     
                        "Chimica": 8,
                        "Storia": 10,
                        "Inglese": 8,
                        "Fisica": 9,
                        "Matematica": 10, 
                        "Informatica": 10,
                        "Italiano": 8,
                        "Sistemi": 10,
                        "TPSIT": 10 
                        
                     }


Aleks_Evaluations = { 
                     
                        "Chimica": 10,
                        "Storia": 10,
                        "Inglese": 6,
                        "Fisica": 2,
                        "Matematica": 7, 
                        "Informatica": 8,
                        "Italiano": 10,
                        "Sistemi": 7,
                        "TPSIT": 2 
                        
                     }

Beppe_Evaluations = { 
                     
                        "Chimica": 2,
                        "Storia": 8,
                        "Inglese": 4,
                        "Fisica": 2,
                        "Matematica": 6, 
                        "Informatica": 6,
                        "Italiano": 5,
                        "Sistemi": 9,
                        "TPSIT": 7 
                        
                     }

Dark_Evaluations  = { 
                     
                        "Chimica": 8,
                        "Storia": 7,
                        "Inglese": 9,
                        "Fisica": 10,
                        "Matematica": 8, 
                        "Informatica": 6,
                        "Italiano": 7,
                        "Sistemi": 6,
                        "TPSIT": 2 
                        
                     }


def updateStats(max):
   global Stats
   
   Stats =  { 
            "Senex":      Senex_Evaluations, 
            "Seima":      Seima_Evaluations, 
            "Aleks":      Aleks_Evaluations, 
            "Beppe":      Beppe_Evaluations, 
            "Dark Angel": Dark_Evaluations 
         }
   
   
   for dictionary in Stats.values():
      values = dictionary.values()
      dictionary["Velocita"] = (int(max - (sum(values)) / len(values)))

Max = 13
updateStats(Max)

if __name__ == "__main__":
   print(Stats)