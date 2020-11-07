# Import Libraries 

from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt 
import numpy as np 
import scipy.integrate as sciInt


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
    backgroundImage = PhotoImage(file = "./images/background.gif",master = principalWind )
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

def Charges():
    global ChargesWind
    # Delete the principal Window 
    principalWind.destroy()

    
    #Data entry window
    ChargesWind = Tk()
    ChargesWind.resizable(False, False)
    ChargesWind.geometry("1000x600")

    #Title
    ChargesWind.title("ELEKTRON")
    #ChargesWind.iconbitmap("/home/jacksen/Documents/Fourth semester/Introduction to the computer sciences and programation/Proyecto/Codigo/imagenes/logo.ico")

    #Background image
    backgroundImage = PhotoImage(file = "./images/background.gif",master = ChargesWind)
    background = Label(image = backgroundImage)
    background.place(x = 0, y = 0)
    

    #Title Wind
    TitleWind = Label(ChargesWind, text="Cargas eléctricas",font=("Fredericka the Great",40),bg="#FFFFFF")
    TitleWind.place(x = 270, y=15)

    Chargetitle = Label(ChargesWind, text="Carga",font=("Fredericka the Great",25), bg="#FFFFFF",fg="#7400FF")
    Chargetitle.place(x = 150 , y = 120 ) 
    
    Magtitle = Label(ChargesWind, text="Magnitud",font=("Fredericka the Great",25), bg="#FFFFFF",fg="#7400FF")
    Magtitle.place(x = 350 , y = 120 )

    Coortitle = Label(ChargesWind, text="Coordenadas",font=("Fredericka the Great",25), bg="#FFFFFF",fg="#7400FF")
    Coortitle.place(x = 630, y = 120 )

    XCoor = Label(ChargesWind, text="X",font=("Fredericka the Great",15), bg="#FFFFFF",fg="#7400FF")
    XCoor.place(x = 680, y = 160 )

    YCoor = Label(ChargesWind, text="Y",font=("Fredericka the Great",15), bg="#FFFFFF",fg="#7400FF")
    YCoor.place(x = 750 , y = 160)

    # Put the numbers to the charges
    ents = enter1(ChargesWind)
    
    #ButtonS
    MenuButton = Button(ChargesWind, text="Menú",font=("Fredericka the Great",15),bg="#21244e",fg="#FFFFFF",width=10,height = 1, command = lambda:[principal(),ChargesWind.destroy()])
    MenuButton.place(x = 200, y=530)

    ValidButton = Button(ChargesWind, text="Guardar",font=("Fredericka the Great",15),bg="#21244e",fg="#FFFFFF",width=10,height = 1, command=lambda: [Validate(ents, Data), fetch(ents), NextWindows(ents)])
    ValidButton.place(x = 400, y = 530)

    HelpButton = Button(ChargesWind, text="About",font=("Fredericka the Great",15),bg="#21244e",fg="#FFFFFF",width=10,height = 1, command=lambda: messagebox.showinfo(
        'Informacion', 'El maximo de cargas permitidas es 6, deja los cuadros sin diligenciar en caso de requerir un numero menor de cargas.'))
    HelpButton.place(x = 600, y=530)
    
    ChargesWind.mainloop()

def enter1(root):
    
    global entries

    entries = []

    Charge1 = Label(root, text=" 1 ",font=("Fredericka the Great",20), bg="#FFFFFF")
    Charge1.place(x=180, y = 200)
    Charge2 = Label(root, text=" 2 ",font=("Fredericka the Great",20), bg="#FFFFFF")
    Charge2.place(x=180, y = 250)
    Charge3 = Label(root, text=" 3 ",font=("Fredericka the Great",20), bg="#FFFFFF")
    Charge3.place(x=180, y = 300)
    Charge4 = Label(root, text=" 4 ",font=("Fredericka the Great",20), bg="#FFFFFF")
    Charge4.place(x=180, y = 350)
    Charge5 = Label(root, text=" 5 ",font=("Fredericka the Great",20), bg="#FFFFFF")
    Charge5.place(x=180, y = 400)
    Charge6 = Label(root, text=" 6 ",font=("Fredericka the Great",20), bg="#FFFFFF")
    Charge6.place(x=180, y = 450)
    
    charge1 = []
    charge2 = []
    charge3 = []
    charge4 = []
    charge5 = []
    charge6 = []

    #Magnitude Charges
    MagCharge1 = Entry(root)
    MagCharge1.place(x=350, y=200)
    charge1.append(MagCharge1)
    MagCharge2 = Entry(root)
    MagCharge2.place(x=350, y=250)
    charge2.append(MagCharge2)
    MagCharge3 = Entry(root)
    MagCharge3.place(x=350, y=300)
    charge3.append(MagCharge3)
    MagCharge4 = Entry(root)
    MagCharge4.place(x=350, y=350)
    charge4.append(MagCharge4)
    MagCharge5 = Entry(root)
    MagCharge5.place(x=350, y=400)
    charge5.append(MagCharge5)
    MagCharge6 = Entry(root)
    MagCharge6.place(x=350, y=450)
    charge6.append(MagCharge6)
    #Coordinates
    
    X1 = Entry(root)
    X1.place(x=670, y=200,width=50, height=20)
    charge1.append(X1)
    Y1 = Entry(root)
    Y1.place(x=740, y=200,width=50, height=20)
    charge1.append(Y1)
    X2 = Entry(root)
    X2.place(x=670, y=250,width=50, height=20)
    charge2.append(X2)
    Y2 = Entry(root)
    Y2.place(x=740, y=250,width=50, height=20)
    charge2.append(Y2)
    X3 = Entry(root)
    X3.place(x=670, y=300,width=50, height=20)
    charge3.append(X3)
    Y3 = Entry(root)
    Y3.place(x=740, y=300,width=50, height=20)
    charge3.append(Y3)
    X4 = Entry(root)
    X4.place(x=670, y=350,width=50, height=20)
    charge4.append(X4)
    Y4 = Entry(root)
    Y4.place(x=740, y=350,width=50, height=20)
    charge4.append(Y4)
    X5 = Entry(root)
    X5.place(x=670, y=400,width=50, height=20)
    charge5.append(X5)
    Y5 = Entry(root)
    Y5.place(x=740, y=400,width=50, height=20)
    charge5.append(Y5)
    X6 = Entry(root)
    X6.place(x=670, y=450,width=50, height=20)
    charge6.append(X6)
    Y6 = Entry(root)
    Y6.place(x=740, y=450,width=50, height=20)
    charge6.append(Y6)
    
    entries.append(charge1)
    entries.append(charge2)
    entries.append(charge3)
    entries.append(charge4)
    entries.append(charge5)
    entries.append(charge6)
    
    return tuple(entries)
    
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
 
def NextWindows(Condition):
    a = ErrorCount(Condition)
    if a == 1:
        #Destroy the last window 
        ChargesWind.destroy()

        Map()
    else:
        pass

def Map():
    #Data entry window
    MapWind = Tk()
    MapWind.resizable(False, False)
    MapWind.geometry("1000x600")

    #Title
    MapWind.title("ELEKTRON")

    #Background image
    backgroundImage = PhotoImage(file = "./images/background.gif",master = MapWind)
    background = Label(image = backgroundImage)
    background.place(x = 0, y = 0)

    #Title Wind
    TitleWind = Label(MapWind, text="Análisis y Gráficas ",font=("Fredericka the Great",35), bg="#FFFFFF")
    TitleWind.place(x=250, y=15, relwidth=0.48, relheight=0.1)
    Statement = Label(MapWind, text="Escoge el tipo de representación que deseas graficar: ",font=("Fredericka the Great",25), bg="#FFFFFF",fg="#7400FF")
    Statement.place(x=100, y=100)
    ElectricField = IntVar()    # 1 si, 0 no
    Equipotential = IntVar()   # 1 si, 0 no
    FieldLines = IntVar()   # 1 si, 0 no

    CheckEF = Checkbutton(MapWind, text="Campo Vectorial",font=("Fredericka the Great",20), bg="#FFFFFF",fg="#0C0009",variable=ElectricField, onvalue=1, offvalue=0)
    CheckEF.place(x=300, y=180)
    CheckEL = Checkbutton(MapWind, text="Lineas De Campo",font=("Fredericka the Great",20), bg="#FFFFFF",fg="#0C0009",variable=FieldLines, onvalue=1, offvalue=0)
    CheckEL.place(x=300, y=250)
    CheckEP = Checkbutton(MapWind, text="Lineas Equipotenciales",font=("Fredericka the Great",20), bg="#FFFFFF",fg="#0C0009",variable=Equipotential, onvalue=1, offvalue=0)
    CheckEP.place(x=300, y=320)

    #ButtonS
    MenuButton = Button(MapWind, text="Menú",font=("Fredericka the Great",15),bg="#21244e",fg="#FFFFFF",width=10,height = 1,)
    MenuButton.place(x=250, y=500)

    ValidButton = Button(MapWind, text="Guardar",font=("Fredericka the Great",15),bg="#21244e",fg="#FFFFFF",width=10,height = 1, command=lambda:  Representation( ElectricField, FieldLines, Equipotential))
    ValidButton.place(x= 400, y=500)
    
    AntButton = Button(MapWind, text="Regresar",font=("Fredericka the Great",15),bg="#21244e",fg="#FFFFFF",width=10,height = 1, command=Charges)
    AntButton.place(x=550, y=500)

    MapWind.mainloop()


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

NumObjects = 1

CharObject[0][0]=2
CharObject[0][1]=0
CharObject[0][2]=30

CharObject[1][0]=-2
CharObject[1][1]=0
CharObject[1][2]=-30

CharObject[2][0]=0
CharObject[2][1]=2
CharObject[2][2]=9

CharObject[3][0]=3
CharObject[3][1]=2
CharObject[3][2]=9

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
linefield=False

charges=True
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

#Beta para evitar ingreso de letras por un evento de teclado
def comprobarEntrada(event):
    charCorrectos=[".","0","1","2","3","4","5","6","7","8","9",8,13,9]
    en=event.widget
    if event.char not in charCorrectos and event.keycode not in charCorrectos:
        en.insert(0,"")
        en.delete(0,"end")
        messagebox.showerror(message="Solo valores numéricos", title="Tkinter")

#Aumenta en 1 el numero de cargas y añade un arreglo([valores en 0])
#a valores
def añadirCarga(numero, master):
    global valores
    if numero<6:
        numero+=1
        valores.append([0,0,0])
        master.destroy()
        modificarValores(numero)
    else:
        messagebox.showerror(message="No se permiten más cargas", title="Elektron")

#Actualiza los datos que han sido modificado en valos
#funcion llamada por el boton aceptar de panel de modificar cargas
def actualizarCargas(frame, numero):
    global valores
    valores=[]
    valoresCargaN=[]
    principal=frame.pack_slaves()[0:numero]
    for frPrincipal in principal:
        for wid in frPrincipal.place_slaves()[0:3]:
            valoresCargaN.insert(0,float(wid.get()))
        valores.append(valoresCargaN)
        valoresCargaN=[]
    print(valores)

#Elimina la carga de valores en la posicion numeroIngresado-1:funcion llamada por el boton aceptar
#del panel de eliminar cargas
def eliminarCarga(numeroCarga,numero,ven):
    global valores
    try:
        valores.pop(int(numeroCarga)-1)
        numero-=1 
        ven.destroy()
        modificarValores(numero)
    except:
        messagebox.showerror(message="El valor ingresado es invalido", title="Elektron")

# Crea el panel para eliminar cargas
def panelEliminarCarga(numero, master):
    global valores
    if numero>1:
        master.destroy()
        #Ventana Windows
        deleteWind = Tk()
        deleteWind.resizable (0,0)
        deleteWind.configure(bg="white")
        deleteWind.geometry("250x200")
        # Titulo e icono
        deleteWind.title("ELEKTRON")
        deleteWind.iconbitmap("./images/logo.ico")
        
        #Ingrese
        Label(deleteWind,text="Ingrese la carga que desea eliminar",font=("Bahnschrift Light",10),bg="#FFFFFF", fg="#21244e").place(x=20, y=50)  
        
        #Numero de carga que desea eliminar
        numeroCarga=Entry(deleteWind, fg="#4A4A4A", font=("Bahnschrift Light",9))
        numeroCarga.place(x=50, y=100)
        
        #Ok button
        aceptarButton=Button(deleteWind,text = "Aceptar",font=("Bahnschrift Light",11),bg="#21244e",fg="#FFFFFF",width=8,height=1,command = lambda:eliminarCarga(numeroCarga.get(), numero, deleteWind))
        aceptarButton.place(x=85,y=150)
    else:
        messagebox.showerror(message="No se permite eliminar más cargas", title="Elektron")

#Paneles correspondientes al numero de cargas
def paneles(numero, master):
    global valores
    #Contenedor pirncipal
    principal=LabelFrame(master)
    principal.pack(fill="both",expand="yes")
    
    #Canvas 
    canvas=Canvas(principal)
    canvas.configure(width="390", height="250")
    canvas.place(x=0,y=0)

    #Scroll vertical
    yscroll=Scrollbar(principal, command=canvas.yview)
    yscroll.pack(sid=RIGHT, fill="y")
    canvas.configure(yscrollcommand=yscroll.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #Contenedor de cantidad de cargas
    frame=Frame(canvas)
    frame.pack(fill="both",expand="yes")
    canvas.create_window((0,0),window=frame)
    for i in range(numero):
        #Crear contenedor  
        contenedor=Frame(frame)
        contenedor.pack()
        contenedor.config(bg="white",width="375", heigh="200")

        #Nombre de cada carga Y LABEL´s 
        Label(contenedor,text="Carga "+str(i+1),font=("Fredericka the Great",22),bg="#FFFFFF", fg="#21244e").place(x=25, y=70)
        Label(contenedor,text="MAGNITUD(μC)",font=("Bahnschrift Light",9),bg="#FFFFFF", fg="#21244e").place(x=160, y=35)
        Label(contenedor,text="X",font=("Bahnschrift Light",9),bg="#FFFFFF", fg="#21244e").place(x=160, y=80)
        Label(contenedor,text="Y",font=("Bahnschrift Light",9),bg="#FFFFFF", fg="#21244e").place(x=160, y=125)

        #Entrada de datos
        magnitud=Entry(contenedor, fg="#4A4A4A", font=("Bahnschrift Light",9))
        magnitud.place(x=160, y=55)
        magnitud.insert(0, valores[i][0])
        magnitud.bind("<Key>",comprobarEntrada)#Evento para comprobar que no sean letras

        posicionX=Entry(contenedor, fg="#4A4A4A", font=("Bahnschrift Light",9))
        posicionX.place(x=160, y=100)
        posicionX.insert(0, valores[i][1])
        posicionX.bind("<Key>",comprobarEntrada)#Evento para comprobar que no sean letras

        posicionY=Entry(contenedor, fg="#4A4A4A", font=("Bahnschrift Light",9))
        posicionY.place(x=160, y=145)
        posicionY.insert(0, valores[i][2])
        posicionY.bind("<Key>",comprobarEntrada)#Evento para comprobar que no sean letras
        
    
    #Agregar carga
    agregarButton=Button(frame,text = "Agregar Carga",font=("Bahnschrift Light",11),bg="#31B821",fg="#FFFFFF",width=12,height=1, command = lambda: añadirCarga(numero, master))
    agregarButton.pack(side="left")

    #Eliminar carga
    eliminarButton=Button(frame,text = "Eliminar Carga",font=("Bahnschrift Light",11),bg="#E71919",fg="#FFFFFF",width=12,height=1, command = lambda: panelEliminarCarga(numero, master))
    eliminarButton.pack(side="right")

    #Aceptar
    aceptarButton=Button(frame,text = "Aceptar",font=("Bahnschrift Light",11),bg="#21244e",fg="#FFFFFF",width=10,height=1, command = lambda: actualizarCargas(frame, numero))
    aceptarButton.pack()
    return master

#Crea la ventana principal
def modificarValores(numeroActualCargas):
    #Ventana Windows
    principalWind = Tk()
    principalWind.resizable (0,0)
    principalWind.configure(bg="white")
    principalWind.geometry("400x250")
    # Titulo e icono
    principalWind.title("ELEKTRON")
    principalWind.iconbitmap("./images/logo.ico")

    #Agregar paneles necesarios
    principalWind=paneles(numeroActualCargas, principalWind)
    principalWind.mainloop()
                                                        
 
#### VARIABLES ####  

valores = [[1.0,2.0,3.0],[4.0,5.0,6.0]]
numeroActualCargas=len(valores)#Determina cuantas cargas existen 
Data = [[None, None, None], [None, None, None], [None, None, None],
        [None, None, None], [None, None, None], [None, None, None]]

Graphics = {}

#modificarValores(numeroActualCargas)
                                                  
principal()

