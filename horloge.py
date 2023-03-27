from datetime import datetime



now = datetime.now()

print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

heure_courante = (0, 0, 0)

def regler_heure(nouvelle_heure):
    global heure_courante
    heure_courante = nouvelle_heure

def afficher_heure():
    print(heure_courante)

import time

heure_courante = (0, 0, 0)
alarme = (0, 0, 0)

def regler_heure(nouvelle_heure):
    global heure_courante
    heure_courante = nouvelle_heure

def regler_alarme(heure_alarme):
    global alarme
    alarme = heure_alarme

def afficher_heure():
    print(heure_courante)

def verifier_alarme():
    global heure_courante
    while True:
        heure_courante = time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec
        if heure_courante == alarme:
            print("L'alarme sonne!")
            break
        time.sleep(1)

