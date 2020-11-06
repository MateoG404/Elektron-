#Project Elektron
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt 
import numpy as np 
import scipy.integrate as sciInt


Data = [[None, None, None], [None, None, None], [None, None, None],
        [None, None, None], [None, None, None], [None, None, None]]

Graphics = {}

def principal():
    # Los botones y ventanas son globales pues en otras funciones han de modificarse
    global principalWind 
    global newButton 
    global oldButton
    global aboutButton


    #Window Characteristics
    principalWind = Tk()
    principalWind.resizable (False,False)
    principalWind.geometry("1000x600")

    #Icon and Title 
    principalWind.title("ELEKTRON")
    principalWind.iconbitmap("./images/logo.ico")
    
    #Background image
    backgroundImage = PhotoImage(file = "./images/background.gif")
    background = Label(image = backgroundImage)
    background.place(x = 0, y = 0)

    #Title Program
    firstTitle = Label(principalWind,text="ELEKTRON",font=("Fredericka the Great",55),bg="#FFFFFF")
    firstTitle.place(x = 280 , y = 10)

    #New Project
    newButton = Button(principalWind,text = "Nuevo Proyecto",font=("Fredericka the Great",20),bg="#21244e",fg="#FFFFFF",width=15,height=1,command = lambda : Charges() )
    newButton.place(x = 365, y = 243)

    #Old Project
    oldButton = Button(principalWind,text = "Cargar Proyecto",font=("Fredericka the Great",20),bg="#21244e",fg="#FFFFFF",width=15,height=1,command = lambda : ReadProject())
    oldButton.place(x = 365, y = 406)
    
    #Se crea una lista con los widgets a modificar, para posteriormente mandarlos a la función about y que alli se modifiquen 
    lista = [oldButton,newButton]
    #About

    aboutButton = Button(principalWind,text = "About",font=("Fredericka the Great",15),bg="#21244e",fg="#FFFFFF",width=6,height=1,command = lambda: AboutFunction(lista,principalWind))
    aboutButton.place(x = 20 , y = 540)

    principalWind.mainloop()

def CreateProject():
    print("rear proyecto")

def ReadProject():
    print("Leer proyecto")

def AboutFunction(lista,window):
    #Se agrega el boton de regresar 
    global regresarButton

    regresarButton = Button(window,text = "Regresar",font=("Fredericka the Great",15),bg="#21244e",fg="#FFFFFF",width=7,height=1,command = lambda: Regresar())
    regresarButton.place(x = 20 , y = 540)

    #Se borran cada uno de los widgets presentes en la lista 
    for i in lista:
        print(i)
        i.destroy()
    

    # Se muestra el label con los nombres y versión del programa

    rectangule = Label(window,bg="#325163",width=78,height = 28) # Rectangulo más claro
    rectangule.place(x = 230, y = 110 )

    rectangule2 = Label(window,bg="#091b27",width=79,height= 28) # Rectangulo más oscuro
    rectangule2.place(x = 215, y = 100)

    #Textos 

    textos = Label (window,font=("Fredericka the Great",15),fg="#FFFFFF",bg="#091b27", text =   "Jhon Silva Zabala \n "
                                                                                                "jhsilvaz@unal.edu.co \n " 
                                                                                                "\nJuan David Ochoa Acosta  \n"
                                                                                                " juochoaa@unal.edu.co\n "
                                                                                                "\n Jacksen Jesus Narvaez Coral\n"
                                                                                                " janarvaez@unal.edu.co\n "
                                                                                                "\n Mateo Gutiérrez Melo\n"
                                                                                                "mgutierrezca@unal.edu.co \n " 
                                                                                                " \n \n Version 1.0"
    )
    textos.place(x= 370, y = 130)

def Regresar(n):
    print("Hola")
### Mateo 

##Jackesen ##
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
    
    plt.show() 

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
            print("Here")
            #print(f'Carga {a+1}:\t{mag} μC \t x = {x} \t y = {y}')
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
    MapWind = Tk()
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

##Juan##
"""Funciones que me vayan surgiendo"""

def Magnitud(Cx,Cy):
    return np.sqrt(Cx**2+Cy**2)

def Unitario(C1,C2):
    return C1/Magnitud(C1, C2)

def Seno_Mag(Cx,Cy):
    return Cy/np.sqrt((Magnitud(Cx, Cy))**3)

def Coseno_Mag(Cx,Cy):
    return Cx/np.sqrt((Magnitud(Cx, Cy))**3)

def Potencial(Q,Cx,Cy,Gx,Gy):
    return k*Q/Magnitud(Gx-Cx,Gy-Cy)

def E_integral(t,y,CharObject):
    ETx=0
    ETy=0
    i=0
    while CharObject[i][2]!=0:   
        ETx+=k*CharObject[i][2]*Coseno_Mag(y[0]-CharObject[i][0], y[1]-CharObject[i][1])
        ETy+=k*CharObject[i][2]*Seno_Mag(y[0]-CharObject[i][0], y[1]-CharObject[i][1])
        i+=1
    return [Unitario(ETx, ETy),Unitario(ETy, ETx)]


"""Creating Storage Charge's info"""

CharObject=[[0]*3 for d in range(0,6)] #Colums: x0,y0,charge ; Rows: Objects

"""Getting info of the charges themselves"""

NumObjects=2

CharObject[0][0]=2
CharObject[0][1]=0
CharObject[0][2]=30

CharObject[1][0]=-2
CharObject[1][1]=0
CharObject[1][2]=-30

CharObject[2][0]=0
CharObject[2][1]=2
CharObject[2][2]=0

CharObject[3][0]=3
CharObject[3][1]=2
CharObject[3][2]=0

CharObject[4][0]=0
CharObject[4][1]=0
CharObject[4][2]=0

CharObject[5][0]=2
CharObject[5][1]=1
CharObject[5][2]=0

k=1/(4*8.854*10**(-12)*3.1415)

"""User Configuration"""

#Show in plot

vecfield=True
equi=False
linefield=True

charges=False
voltage=False 

#Limits grid
x0=-5 
xf=5
y0=-5
yf=5

"""Creating grid for vector und equipotencial plots"""

if equi==True or vecfield==True:
    if equi==True:
        n=100
    else:
        n=20
    x = np.linspace(x0, xf, n)
    y = np.linspace(y0, yf, n)
    X, Y = np.meshgrid(x, y)
    
"""Creating plot"""

fig, (Field) = plt.subplots(ncols= 1, figsize =(7, 7)) 
    
"""VECTOR FIELD DIAGRAM""" 

if vecfield==True: 
    
    #Creating unit vectors in the grid
    
    ETx,ETy=np.meshgrid(x, y)
    for i in range(0,NumObjects):   
        Ex=k*CharObject[i][2]*Coseno_Mag(X-CharObject[i][0], Y-CharObject[i][1])
        Ey=k*CharObject[i][2]*Seno_Mag(X-CharObject[i][0], Y-CharObject[i][1])
        ETx+=Ex
        ETy+=Ey
    ETx_u=Unitario(ETx, ETy)
    ETy_u=Unitario(ETy, ETx)
    
    #ploting unit vectors
    
    Field.quiver(X, Y, ETx_u, ETy_u, scale=30)
    
"""EQUIPOTENCIALS DIAGRAM"""

if equi==True:
    
    #Defining Potencial
    
    V=0
    for i in range(0,NumObjects): 
        V+=Potencial(CharObject[i][2],CharObject[i][0],CharObject[i][1],X,Y)
        
    #Ploting Equipotencials
        
    plt.contour(X, Y, V, 500, colors='k', linestyles="solid")
    
"""LINE FIELD DIAGRAM""" 
   
if linefield==True:
    R0=0.1
    for i in range(0,NumObjects):
        dt=0.1
        if CharObject[i][2]<0:
            dt=-dt
        for theta in np.linspace(0, 2*np.pi*15/16, 16):
            r=sciInt.ode(E_integral)
            r.set_f_params(CharObject)
            x=[ CharObject[i][0] + np.cos(theta)*R0 ]
            w=[ CharObject[i][1] + np.sin(theta)*R0 ]
            r.set_initial_value([x[0],w[0]])
            while (x0<r.y[0] and r.y[0]<xf) and (y0<r.y[1] and r.y[1]<xf):
                r.integrate(r.t+dt)
                x.append(r.y[0])
                w.append(r.y[1])
                a=0
                for j in range(0,NumObjects):
                    if Magnitud(r.y[0]-CharObject[j][0], r.y[1]-CharObject[j][1])<R0:
                        a=1
                        break
                if a==1:
                    break
            plt.plot(x, w, "k")
    
"""Rendering Charges"""

if charges==True:
    for i in range(0,NumObjects):
        if CharObject[i][2]>0:
            plt.plot(CharObject[i][0], CharObject[i][1], "ro", ms=5*np.sqrt(CharObject[i][2]))
        else:
            plt.plot(CharObject[i][0], CharObject[i][1], "bo", ms=5*np.sqrt(-CharObject[i][2]))
    
"""Plot propierties"""

Field.xaxis.set_ticks([])        
Field.yaxis.set_ticks([])        
Field.axis([x0, xf, y0, yf])     
Field.set_aspect('equal')        

"""show figure""" 

## 

principal()
