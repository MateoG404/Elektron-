from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


def enter1(root):
    global entries
    entries = []
    NumCharges = tk.Entry(root)
    NumCharges.place(x=190, y=130, relwidth=0.1, relheight=0.1)
    entries.append(('Number of Charges: ', NumCharges))
    return entries


def Validate(A, ents):
    if (int(A) >= 0 and int(A) <= 6):
         lambda event, e=ents: fetch(e)
    else:
        messagebox.showwarning("Error", "Entrada fuera de rango")


def fetch(entries):
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print('%s: "%s"' % (field, text))


def Setting():
    settingWind = Tk()
    settingWind.resizable(False, False)
    settingWind.geometry("400x330")

    #Title
    settingWind.title("ELEKTRON")
    #settingWind.iconphoto(False, tk.PhotoImage(file='./logo.png'))

    #Title Wind
    TitleWind = Label(
        settingWind, text="Configuracion del sistema:", bg="#FFFFFF")
    TitleWind.place(x=110, y=15, relwidth=0.48, relheight=0.1)

    #Number of Charges
    #global Number_of_Charges
    ChargesLabel = Label(settingWind, text="Numero de Cargas:", bg="#FFFFFF")
    ChargesLabel.place(x=126, y=80, relwidth=0.4, relheight=0.08)
    ents = enter1(settingWind)
    #settingWind.bind('<Return>', lambda: [Validate(int(ents[0][1].get()), ents), fetch(ents)])

    #NumCharges = Entry(settingWind)
    #NumCharges.place(x=190, y=130, relwidth=0.1, relheight=0.1)
    #Number_of_Charges=[]
    #print(NumCharges.get())
    #Number_of_Charges.append(NumCharges.get())

    #NumberCharges=int(NumbCharges)
    ValButton = Button(settingWind, text="Ok", command=lambda: [
                       Validate(int(ents[0][1].get()), ents), fetch(ents)])
    #ValButton = Button(settingWind, text="Ok", command=lambda :print(NumCharges.get()))
    ValButton.place(x=188, y=200)
    #Restictions
    Restriction1 = ttk.Label(
        settingWind, text="El maximo de cargas permitidas es 6.")
    Restriction1.place(x=78, y=170, relwidth=0.63, relheight=0.1)

    #ButtonS
    NextButton = Button(settingWind, text="Sig", command=Charges)
    NextButton.place(x=245, y=233)
    PreviousButton = Button(settingWind, text="Ant")
    PreviousButton.place(x=127, y=233)
    MenuButton = Button(settingWind, text="Menu")
    MenuButton.place(x=183, y=233)

    settingWind.mainloop()


def Charges():
    #Setting.withdraw()
    ChargesWind = Tk()
    ChargesWind.resizable(False, False)
    ChargesWind.geometry("400x330")

    #Title
    ChargesWind.title("ELEKTRON")

    #Background image
    #backgroundImage = PhotoImage(file="/home/jacksen/Documents/Fourth semester/Introduction to the computer sciences and programation/Proyecto/Codigo/backgraund.gif")
    #background = Label(image=backgroundImage)
    #background.place(x=0, y=0)

    #Title Wind
    TitleWind = Label(ChargesWind, text="Cargas electricas:", bg="#FFFFFF")
    TitleWind.place(x=110, y=15, relwidth=0.48, relheight=0.1)
    Magtitle = Label(ChargesWind, text="Magnitud", bg="#FFFFFF")
    Magtitle.place(x=120, y=55, relwidth=0.2, relheight=0.06)
    Coortitle = Label(ChargesWind, text="Coordenadas", bg="#FFFFFF")
    Coortitle.place(x=220, y=55, relwidth=0.35, relheight=0.06)
    XCoor = Label(ChargesWind, text="X", bg="#FFFFFF")
    XCoor.place(x=241, y=78, relwidth=0.07, relheight=0.05)
    YCoor = Label(ChargesWind, text="Y", bg="#FFFFFF")
    YCoor.place(x=309, y=78, relwidth=0.07, relheight=0.05)
    Chargetitle = Label(ChargesWind, text="Carga", bg="#FFFFFF")
    Chargetitle.place(x=40, y=55, relwidth=0.15, relheight=0.06)

    #Charges
    Charge1 = Label(ChargesWind, text=" 1 ", bg="#FFFFFF")
    Charge1.place(x=54, y=100, relwidth=0.08, relheight=0.08)
    Charge2 = Label(ChargesWind, text=" 2 ", bg="#FFFFFF")
    Charge2.place(x=54, y=130, relwidth=0.08, relheight=0.08)
    Charge3 = Label(ChargesWind, text=" 3 ", bg="#FFFFFF")
    Charge3.place(x=54, y=160, relwidth=0.08, relheight=0.08)
    Charge4 = Label(ChargesWind, text=" 4 ", bg="#FFFFFF")
    Charge4.place(x=54, y=190, relwidth=0.08, relheight=0.08)
    Charge5 = Label(ChargesWind, text=" 5 ", bg="#FFFFFF")
    Charge5.place(x=54, y=220, relwidth=0.08, relheight=0.08)
    Charge6 = Label(ChargesWind, text=" 6 ", bg="#FFFFFF")
    Charge6.place(x=54, y=250, relwidth=0.08, relheight=0.08)

    #Magnitude Charges
    MagCharge1 = Entry(ChargesWind)
    MagCharge1.place(x=135, y=100, relwidth=0.12, relheight=0.08)
    MagCharge2 = Entry(ChargesWind)
    MagCharge2.place(x=135, y=130, relwidth=0.12, relheight=0.08)
    MagCharge3 = Entry(ChargesWind)
    MagCharge3.place(x=135, y=160, relwidth=0.12, relheight=0.08)
    MagCharge4 = Entry(ChargesWind)
    MagCharge4.place(x=135, y=190, relwidth=0.12, relheight=0.08)
    MagCharge5 = Entry(ChargesWind)
    MagCharge5.place(x=135, y=220, relwidth=0.12, relheight=0.08)
    MagCharge6 = Entry(ChargesWind)
    MagCharge6.place(x=135, y=250, relwidth=0.12, relheight=0.08)

    #Coordinates
    X1 = Entry(ChargesWind)
    X1.place(x=230, y=100, relwidth=0.12, relheight=0.08)
    Y1 = Entry(ChargesWind)
    Y1.place(x=300, y=100, relwidth=0.12, relheight=0.08)
    X2 = Entry(ChargesWind)
    X2.place(x=230, y=130, relwidth=0.12, relheight=0.08)
    Y2 = Entry(ChargesWind)
    Y2.place(x=300, y=130, relwidth=0.12, relheight=0.08)
    X3 = Entry(ChargesWind)
    X3.place(x=230, y=160, relwidth=0.12, relheight=0.08)
    Y3 = Entry(ChargesWind)
    Y3.place(x=300, y=160, relwidth=0.12, relheight=0.08)
    X4 = Entry(ChargesWind)
    X4.place(x=230, y=190, relwidth=0.12, relheight=0.08)
    Y4 = Entry(ChargesWind)
    Y4.place(x=300, y=190, relwidth=0.12, relheight=0.08)
    X5 = Entry(ChargesWind)
    X5.place(x=230, y=220, relwidth=0.12, relheight=0.08)
    Y5 = Entry(ChargesWind)
    Y5.place(x=300, y=220, relwidth=0.12, relheight=0.08)
    X6 = Entry(ChargesWind)
    X6.place(x=230, y=250, relwidth=0.12, relheight=0.08)
    Y6 = Entry(ChargesWind)
    Y6.place(x=300, y=250, relwidth=0.12, relheight=0.08)

    #ButtonS
    NextButton = Button(ChargesWind, text="Sig")
    NextButton.place(x=223, y=290)
    PreviousButton = Button(ChargesWind, text="Ant", command=Setting)
    PreviousButton.place(x=105, y=290)
    MenuButton = Button(ChargesWind, text="Menu")
    MenuButton.place(x=160, y=290)

    ChargesWind.mainloop()


#Validate(int(input("a")))
Setting()
print(entries)
#print(Number_of_Charges)
