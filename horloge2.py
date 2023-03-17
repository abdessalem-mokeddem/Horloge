import string
import time 
import datetime

def afficher_heure(mode_24h=True):

    while True:

        heure_actuelle = time.localtime()[3:6]
        
        if not mode_24h:
            heures = heure_actuelle[0] % 12 or 12  
            minutes = heure_actuelle[1]
            secondes = heure_actuelle[2]
            am_pm = "AM" if heure_actuelle[0] < 12 else "PM"
            heure_formattee = f"{heures:02}:{minutes:02}:{secondes:02} {am_pm}"
        else:
            heure_formattee = time.strftime("%H:%M:%S", heure_actuelle)
        
      
        date = time.localtime()[:3]
        mois = [date[1]]
        date_formattee = f"{date[2]} {mois} {date[0]}"
    




tuples = (14, 44, 30)

def afficher_heures (tuples):

    heures_listes = list(tuples)

     
    while True :

        heures_listes[2] += 1
        time.sleep(1)
        print(heures_listes)

        if heures_listes [2] == 60:
            heures_listes [2] = 0
            heures_listes[1] += 1

        if  heures_listes [1] == 60:
                heures_listes [1] = 0
                heures_listes[0] += 1

        if  heures_listes [0] == 24:
                heures_listes [0] = 0


        break

def regler_alarme(alarme):

    while True:

        heure_actuelle = time.localtime()[3:6]  
        if heure_actuelle == alarme:
            print("ALARME SONNE :", alarme)
            break
                                            
afficher_heures (tuples)
