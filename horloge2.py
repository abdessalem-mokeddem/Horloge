import time

mode_12h = False  
pause = False  
alarme = None  

def afficher_heure(heure):

    global mode_12h

    if mode_12h:

        heure12h = time.strftime("%I:%M:%S %p", heure)

        print(heure12h)

    else:

        heure24h = time.strftime("%H:%M:%S", heure)

        print(heure24h)

def regler_heure(heure):

    global pause

    pause = False

    while not pause:

        heure_actuelle = time.localtime()

        afficher_heure(heure_actuelle)

        if alarme == heure_actuelle[3:6]:

            print("Alarme!")

        time.sleep(1)

def regler_alarme(heure):

    global alarme

    alarme = heure

def changer_mode(mode):

    global mode_12h

    mode_12h = mode

def mettre_en_pause():

    global pause
    pause = True

# Exemple d'utilisation:
regler_heure((16, 30, 0))  
regler_alarme((17, 0, 0))  
changer_mode(True)  
mettre_en_pause()  

