from tkinter import*
import time
import winsound

#  Titre et taille de la police
app_horloge = Tk()
app_horloge.title("horloge")
app_horloge.geometry("420x150")
app_horloge.resizable(1,1)

# Police de l'heure et ses couleurs
text_font = ("Boulder",50,'bold')
background = "Blue"
foreground = "#363529"
border_widht = 20
# combinaison de toutes les éléments pour définir le label de nos éléments
label = Label(app_horloge, font=text_font, bg=background, fg=foreground, bd=border_widht)
label.grid(row=0, column=1)

# Définition de la fonction principale de l'horloge
def horloge():
    temps = time.strftime("%H:%M:%S")
    label.config(text=temps)
    label.after(200, horloge)

    if "%H" == 18:
        if "%M" == 29:
            if "%S" == 10:
                time.strftime("bip bip bip")

horloge()
app_horloge.mainloop()


