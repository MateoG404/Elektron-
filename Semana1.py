from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


Data = [[None, None, None], [None, None, None], [None, None, None],
        [None, None, None], [None, None, None], [None, None, None]]
Graphics = {}


def Representation(ElectricField, FieldLines, Equipotential):
    if (ElectricField.get()):
        Graphics["Vectorial Field"] = True
    else:
        Graphics["Vectorial Field"] = False
    if (FieldLines.get()):
        Graphics["Field Lines"] = True
    else:
        Graphics["Field Lines"] = False
    if (Equipotential.get()):
        Graphics["Equipotential Lines"] = True
    else:
        Graphics["Equipotential Lines"] = False
    print(Graphics)


def ValidateType(x):
    try:
        float(x)
        return 1
    except (ValueError, TypeError):
        return 0


def ErrorCount(Matriz):
    P = 0
    for i in range(len(Matriz)):
        A = Matriz[i][0].get()
        B = Matriz[i][1].get()
        C = Matriz[i][2].get()
        if (A == '' and B == '' and C == ''):
            pass
        elif(ValidateType(A) == 1 and ValidateType(B) == 1 and ValidateType(C) == 1):
            pass
        else:
            P += 1
    if P == 0:
        return True
    else:
        return False


def Validate(entries, Data):

    for i in range(len(entries)):
        for j in range(3):
            A = entries[i][j].get()
            if A != '':
                if ValidateType(A) == 1:
                    Data[i][j] = float(A)
                else:
                    messagebox.showwarning(
                        "Error", f"¡Ups! {A} no es una entrada válida. Inténtalo de nuevo ...")
            else:
                pass
    print(Data)


def fetch(entries):
    for a in range(len(entries)):
        mag = entries[a][0].get()
        x = entries[a][1].get()
        y = entries[a][2].get()
        if (ValidateType(mag) == 1 and ValidateType(x) == 1 and ValidateType(y) == 1):
            print(f'Carga {a+1}:\t{mag} μC \t x = {x} \t y = {y}')
        elif (mag == '' and x == '' and y == ''):
            pass
        else:
            print(f'Carga {a+1}: Dato no valido.')


def enter1(root):

    global entries

    entries = []

    Charge1 = Label(root, text=" 1 ", bg="#FFFFFF")
    Charge1.place(x=54, y=100, relwidth=0.08, relheight=0.08)
    Charge2 = Label(root, text=" 2 ", bg="#FFFFFF")
    Charge2.place(x=54, y=130, relwidth=0.08, relheight=0.08)
    Charge3 = Label(root, text=" 3 ", bg="#FFFFFF")
    Charge3.place(x=54, y=160, relwidth=0.08, relheight=0.08)
    Charge4 = Label(root, text=" 4 ", bg="#FFFFFF")
    Charge4.place(x=54, y=190, relwidth=0.08, relheight=0.08)
    Charge5 = Label(root, text=" 5 ", bg="#FFFFFF")
    Charge5.place(x=54, y=220, relwidth=0.08, relheight=0.08)
    Charge6 = Label(root, text=" 6 ", bg="#FFFFFF")
    Charge6.place(x=54, y=250, relwidth=0.08, relheight=0.08)

    charge1 = []
    charge2 = []
    charge3 = []
    charge4 = []
    charge5 = []
    charge6 = []

    #Magnitude Charges
    MagCharge1 = Entry(root)
    MagCharge1.place(x=135, y=100, relwidth=0.12, relheight=0.08)
    charge1.append(MagCharge1)
    MagCharge2 = Entry(root)
    MagCharge2.place(x=135, y=130, relwidth=0.12, relheight=0.08)
    charge2.append(MagCharge2)
    MagCharge3 = Entry(root)
    MagCharge3.place(x=135, y=160, relwidth=0.12, relheight=0.08)
    charge3.append(MagCharge3)
    MagCharge4 = Entry(root)
    MagCharge4.place(x=135, y=190, relwidth=0.12, relheight=0.08)
    charge4.append(MagCharge4)
    MagCharge5 = Entry(root)
    MagCharge5.place(x=135, y=220, relwidth=0.12, relheight=0.08)
    charge5.append(MagCharge5)
    MagCharge6 = Entry(root)
    MagCharge6.place(x=135, y=250, relwidth=0.12, relheight=0.08)
    charge6.append(MagCharge6)
    #Coordinates

    X1 = Entry(root)
    X1.place(x=230, y=100, relwidth=0.12, relheight=0.08)
    charge1.append(X1)
    Y1 = Entry(root)
    Y1.place(x=300, y=100, relwidth=0.12, relheight=0.08)
    charge1.append(Y1)
    X2 = Entry(root)
    X2.place(x=230, y=130, relwidth=0.12, relheight=0.08)
    charge2.append(X2)
    Y2 = Entry(root)
    Y2.place(x=300, y=130, relwidth=0.12, relheight=0.08)
    charge2.append(Y2)
    X3 = Entry(root)
    X3.place(x=230, y=160, relwidth=0.12, relheight=0.08)
    charge3.append(X3)
    Y3 = Entry(root)
    Y3.place(x=300, y=160, relwidth=0.12, relheight=0.08)
    charge3.append(Y3)
    X4 = Entry(root)
    X4.place(x=230, y=190, relwidth=0.12, relheight=0.08)
    charge4.append(X4)
    Y4 = Entry(root)
    Y4.place(x=300, y=190, relwidth=0.12, relheight=0.08)
    charge4.append(Y4)
    X5 = Entry(root)
    X5.place(x=230, y=220, relwidth=0.12, relheight=0.08)
    charge5.append(X5)
    Y5 = Entry(root)
    Y5.place(x=300, y=220, relwidth=0.12, relheight=0.08)
    charge5.append(Y5)
    X6 = Entry(root)
    X6.place(x=230, y=250, relwidth=0.12, relheight=0.08)
    charge6.append(X6)
    Y6 = Entry(root)
    Y6.place(x=300, y=250, relwidth=0.12, relheight=0.08)
    charge6.append(Y6)

    entries.append(charge1)
    entries.append(charge2)
    entries.append(charge3)
    entries.append(charge4)
    entries.append(charge5)
    entries.append(charge6)

    return tuple(entries)


def NextWindows(Condition):
    a = ErrorCount(Condition)
    if a == 1:
        Map()
    else:
        pass


def Charges():
    #Data entry window
    ChargesWind = Tk()
    ChargesWind.resizable(False, False)
    ChargesWind.geometry("400x330")

    #Title
    ChargesWind.title("ELEKTRON")
    #ChargesWind.iconbitmap("/home/jacksen/Documents/Fourth semester/Introduction to the computer sciences and programation/Proyecto/Codigo/imagenes/logo.ico")

    #Background image
    #backgroundImage = PhotoImage(file="/home/jacksen/Documents/Fourth semester/Introduction to the computer sciences and programation/Proyecto/Codigo/imagenes/background.gif", master=ChargesWind)
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

    ents = enter1(ChargesWind)

    #ButtonS
    MenuButton = Button(ChargesWind, text="Menu")
    MenuButton.place(x=222, y=290)
    ValidButton = Button(ChargesWind, text="Ok", command=lambda: [Validate(ents, Data), fetch(ents), NextWindows(ents)])
    ValidButton.place(x=173, y=290)
    HelpButton = Button(ChargesWind, text="About", command=lambda: messagebox.showinfo(
        'Informacion', 'El maximo de cargas permitidas es 6, deja los cuadros sin diligenciar en caso de requerir un numero menor de cargas.'))
    HelpButton.place(x=104, y=290)

    ChargesWind.mainloop()


def Map():
    #Data entry window
    MapWind = tk.Toplevel()
    MapWind.resizable(False, False)
    MapWind.geometry("400x330")

    #Title
    MapWind.title("ELEKTRON")

    #Background image
    #backgroundImageM = PhotoImage(file="/home/jacksen/Documents/Fourth semester/Introduction to the computer sciences and programation/Proyecto/Codigo/imagenes/background.gif", master=MapWind)
    #backgroundd = Label(image=backgroundImageM)
    #backgroundd.place(x=0, y=0)

    #Title Wind
    TitleWind = Label(MapWind, text="Analisis y Grafica: ", bg="#FFFFFF")
    TitleWind.place(x=110, y=15, relwidth=0.48, relheight=0.1)
    Statement = Label(MapWind, text="Escoge el tipo de representacion que deseas graficar: ", bg="#FFFFFF")
    Statement.place(x=10, y=55)
    ElectricField = IntVar()    # 1 si, 0 no
    Equipotential = IntVar()   # 1 si, 0 no
    FieldLines = IntVar()   # 1 si, 0 no
    CheckEF = Checkbutton(MapWind, text="Campo Vectorial",
                          variable=ElectricField, onvalue=1, offvalue=0)
    CheckEF.place(x=20, y=100)
    CheckEL = Checkbutton(MapWind, text="Lineas De Campo",
                          variable=FieldLines, onvalue=1, offvalue=0)
    CheckEL.place(x=20, y=130)
    CheckEP = Checkbutton(MapWind, text="Lineas Equipotenciales",
                          variable=Equipotential, onvalue=1, offvalue=0)
    CheckEP.place(x=20, y=160)

    #ButtonS
    MenuButton = Button(MapWind, text="Menu")
    MenuButton.place(x=222, y=290)
    ValidButton = Button(MapWind, text="Ok", command=lambda:  Representation(
        ElectricField, FieldLines, Equipotential))
    ValidButton.place(x=173, y=290)
    AntButton = Button(MapWind, text="Ant", command=Charges)
    AntButton.place(x=115, y=290)

    MapWind.mainloop()

Charges()
