import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk 
import numpy as np 
import scipy.integrate as sciInt
from tkinter import *
import sys
"""Funciones Matemáticas"""

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
    for i in range(0, NumObjects):
        ETx+=k*CharObject[i][2]*Coseno_Mag(y[0]-CharObject[i][0], y[1]-CharObject[i][1])
        ETy+=k*CharObject[i][2]*Seno_Mag(y[0]-CharObject[i][0], y[1]-CharObject[i][1])
        i+=1
    return [Unitario(ETx, ETy),Unitario(ETy, ETx)]
  
def TresTristesTigres(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            for k in range(0,6):
                if i==CharObject[k][0] and j==CharObject[k][1]:
                    A[i][j]=2
                else:
                    A[i][j]=-(-A[i][j])**(1/2)
    return A

"""Plot propierties"""

def DoPlot(x0,xf,y0,yf):
    Field.xaxis.set_ticks([])        
    Field.yaxis.set_ticks([])        
    Field.axis([x0, xf, y0, yf])     
    Field.set_aspect('equal')        

"""Creating grid for vector und equipotencial plots"""

def Space(x0,xf,y0,yf):
    if Show[1]==True:
        n=500
    else:
        n=20
    return [np.linspace(x0, xf, n),np.linspace(y0, yf, n)]
    
""""Defining Potencial as Plot"""

def Voltaje():
    V=0
    for i in range(0,NumObjects): 
        V+=Potencial(CharObject[i][2],CharObject[i][0],CharObject[i][1],X,Y)
    try:
        V1=np.log(V)+100
        V2=-np.log(-V)-100
    except RuntimeWarning:
        print()
    return [V1,V2]

"""Rendering charges"""

def PointCharge():
    for i in range(0,NumObjects):
        if CharObject[i][2]>0:
            plt.plot(CharObject[i][0], CharObject[i][1], "ro", ms=3*(CharObject[i][2])**(1/3))
        else:
            plt.plot(CharObject[i][0], CharObject[i][1], "bo", ms=3*(-CharObject[i][2])**(1/3))

"""VECTOR FIELD DIAGRAM""" 

def VecField(x,y):
    ETx,ETy=np.meshgrid(x,y)
    print("-------------")
    for i in range(0,NumObjects):   
        Ex=k*CharObject[i][2]*Coseno_Mag(X-CharObject[i][0], Y-CharObject[i][1])
        Ey=k*CharObject[i][2]*Seno_Mag(X-CharObject[i][0], Y-CharObject[i][1])
        ETx+=Ex
        ETy+=Ey
    ETx_u=Unitario(ETx, ETy)
    ETy_u=Unitario(ETy, ETx)
    Field.quiver(X, Y, ETx_u, ETy_u, scale=30)

"""LINE FIELD DIAGRAM""" 

def LineField(): 
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
            while (Limits[0]<r.y[0] and r.y[0]<Limits[1]) and (Limits[2]<r.y[1] and r.y[1]<Limits[3]):
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
#Beta para evitar ingreso de letras por un evento de teclado
def comprobarEntrada(event):
    charCorrectos=[".","0","1","2","3","4","5","6","7","8","9","-",8,13,9]
    en=event.widget
    if event.char not in charCorrectos and event.keycode not in charCorrectos:
        en.insert(0,"")
        en.delete(0,"end")
        messagebox.showerror(message="Solo valores numéricos", title="Tkinter")

#Aumenta en 1 el numero de cargas y añade un arreglo([valores en 0])
#a valores
def añadirCarga(numero, master,principalGraphs):
    if numero<6:
        numero+=1
        CharObject.append([0,0,0])
        master.destroy()
        modificarValores(numero,principalGraphs)
    else:
        messagebox.showerror(message="No se permiten más cargas", title="Elektron")

#Actualiza los datos que han sido modificado en valos
#funcion llamada por el boton aceptar de panel de modificar cargas
def actualizarCargas(frame, numero,master,principalGraphs):
    global CharObject
    global fig
    CharObject=[]
    valoresCargaN=[]
    principal=frame.pack_slaves()[0:numero]
    for frPrincipal in principal:
        for wid in frPrincipal.place_slaves()[0:3]:
            valoresCargaN.insert(0,float(wid.get()))
        CharObject.append(valoresCargaN)
        valoresCargaN=[]
    #fig, (Field) = plt.subplots(ncols= 1, figsize =(7, 7))#Creating plot
    Field.clear()
    print(CharObject)
    principalGraphs.destroy()
    master.destroy()
    construirGraficas()

#Elimina la carga de valores en la posicion numeroIngresado-1:funcion llamada por el boton aceptar
#del panel de eliminar cargas
def eliminarCarga(numeroCarga,numero,ven,principalGraphs):
    global CharObject
    try:
        CharObject.pop(int(numeroCarga)-1)
        numero-=1 
        ven.destroy()
        modificarValores(numero,principalGraphs)
    except:
        messagebox.showerror(message="El valor ingresado es invalido", title="Elektron")

# Crea el panel para eliminar cargas
def panelEliminarCarga(numero, master,principalGraphs):
    if numero>1:
        master.destroy()
        #Ventana Windows
        deleteWind = Tk()
        deleteWind.resizable (0,0)
        deleteWind.configure(bg="white")
        deleteWind.geometry("250x200")
        # Titulo e icono
        deleteWind.title("ELEKTRON")
        deleteWind.iconbitmap(r"C:\Users\John Silva\Desktop\Python\proyectoElektron\data\logo_Elektron.ico")
        
        #Ingrese
        Label(deleteWind,text="Ingrese la carga que desea eliminar",font=("Bahnschrift Light",10),bg="#FFFFFF", fg="#21244e").place(x=20, y=50)  
        
        #Numero de carga que desea eliminar
        numeroCarga=Entry(deleteWind, fg="#4A4A4A", font=("Bahnschrift Light",9))
        numeroCarga.place(x=50, y=100)
        
        #Ok button
        aceptarButton=Button(deleteWind,text = "Aceptar",font=("Bahnschrift Light",11),bg="#21244e",fg="#FFFFFF",width=8,height=1,command = lambda:eliminarCarga(numeroCarga.get(), numero, deleteWind,principalGraphs))
        aceptarButton.place(x=85,y=150)
    else:
        messagebox.showerror(message="No se permite eliminar más cargas", title="Elektron")

#Paneles correspondientes al numero de cargas
def paneles(numero, master,principalGraphs):
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
    frame=Frame(canvas,bg="#FFFFFF")
    frame.pack(fill="both",expand="yes")
    canvas.create_window((0,0),window=frame)
    for i in range(numero):
        #Crear contenedor  
        contenedor=Frame(frame)
        contenedor.pack()
        contenedor.config(bg="white",width="375", heigh="200")

        #Nombre de cada carga Y LABEL´s 
        Label(contenedor,text="Carga "+str(i+1),font=("Fredericka the Great",22),bg="#FFFFFF", fg="#21244e").place(x=25, y=70)
        Label(contenedor,text="X",font=("Bahnschrift Light",9),bg="#FFFFFF", fg="#21244e").place(x=160, y=35)
        Label(contenedor,text="Y",font=("Bahnschrift Light",9),bg="#FFFFFF", fg="#21244e").place(x=160, y=80)
        Label(contenedor,text="MAGNITUD(μC)",font=("Bahnschrift Light",9),bg="#FFFFFF", fg="#21244e").place(x=160, y=125)

        #Entrada de datos

        posicionX=Entry(contenedor, fg="#4A4A4A", font=("Bahnschrift Light",9))
        posicionX.place(x=160, y=55)
        posicionX.insert(0, CharObject[i][0])
        posicionX.bind("<Key>",comprobarEntrada)#Evento para comprobar que no sean letras

        posicionY=Entry(contenedor, fg="#4A4A4A", font=("Bahnschrift Light",9))
        posicionY.place(x=160, y=100)
        posicionY.insert(0, CharObject[i][1])
        posicionY.bind("<Key>",comprobarEntrada)#Evento para comprobar que no sean letras

        magnitud=Entry(contenedor, fg="#4A4A4A", font=("Bahnschrift Light",9))
        magnitud.place(x=160, y=145)
        magnitud.insert(0, CharObject[i][2])
        magnitud.bind("<Key>",comprobarEntrada)#Evento para comprobar que no sean letras
        
    
    #Agregar carga
    agregarButton=Button(frame,text = "Agregar Carga",font=("Bahnschrift Light",11),bg="#31B821",fg="#FFFFFF",width=12,height=1, command = lambda: añadirCarga(numero, master,principalGraphs))
    agregarButton.pack(side="left")

    #Eliminar carga
    eliminarButton=Button(frame,text = "Eliminar Carga",font=("Bahnschrift Light",11),bg="#E71919",fg="#FFFFFF",width=12,height=1, command = lambda: panelEliminarCarga(numero, master,principalGraphs))
    eliminarButton.pack(side="right")

    #Aceptar
    aceptarButton=Button(frame,text = "Aceptar",font=("Bahnschrift Light",11),bg="#21244e",fg="#FFFFFF",width=10,height=1, command = lambda: actualizarCargas(frame, numero,master, principalGraphs))
    aceptarButton.pack()
    return master

#Crea la ventana principal
def modificarValores(numeroActualCargas,principalGraphs):
    #Ventana Windows
    principalWind = Tk()
    principalWind.resizable (0,0)
    principalWind.configure(bg="white")
    principalWind.geometry("400x250")
    # Titulo e icono
    principalWind.title("ELEKTRON")
    principalWind.iconbitmap(r"C:\Users\John Silva\Desktop\Python\proyectoElektron\data\logo_Elektron.ico")

    #Agregar paneles necesarios
    principalWind=paneles(numeroActualCargas, principalWind,principalGraphs)
    principalWind.mainloop()
def salir():
    plt.close()

def ventanaGraficas(fig,numero):
    #Ventana Windows
    principalWindGraphs=Tk()
    principalWindGraphs .resizable (0,0)
    principalWindGraphs .configure(bg="white")
    principalWindGraphs .geometry("800x600")
    # Titulo e icono
    principalWindGraphs .title("ELEKTRON")
    principalWindGraphs .iconbitmap(r"C:\Users\John Silva\Desktop\Python\proyectoElektron\data\logo_Elektron.ico")

    #Contenedor de opciones
    optionsFrame=Frame(principalWindGraphs , bg="#21244e")
    optionsFrame.config(width="250",height="600")
    optionsFrame.pack(side=LEFT,fill="both",expand="yes")
    modificarButton=Button(optionsFrame,text = "Modificar",font=("Bahnschrift Light",11),bg="#FFFFFF",fg="#000000",width=10,height=1, command = lambda: modificarValores(numero,principalWindGraphs))
    modificarButton.place(x="60",y="550")
    
    #Canvas 
    canvas=Canvas(optionsFrame)
    canvas.configure(width="250", height="500",bg="#21244e",bd=0,highlightthickness=0,relief="ridge")
    canvas.pack(side=LEFT, anchor="n",expand="yes")
    
    #Scroll vertical
    yscroll=Scrollbar(optionsFrame, command=canvas.yview)
    yscroll.pack(side=RIGHT, fill="y")
    canvas.configure(yscrollcommand=yscroll.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #Contenedor de cantidad de cargas
    frame=LabelFrame(canvas)
    frame.configure(width="250", height="500",bg="#21244e",bd=0,highlightthickness=0,relief="ridge")
    frame.pack(fill="both",expand="yes")
    canvas.create_window((0,0),window=frame)
    for i in range(numero):
        #Crear contenedor  
        contenedor=LabelFrame(frame,text="Carga "+str(i+1),font=("Fredericka the Great",10),fg="#FFFFFF")
        contenedor.pack()
        contenedor.config(bg="#21244e",width="250", heigh="150")

        #Propiedades de cada carga 
        Label(contenedor,text="X: "+str(CharObject[i][0]),font=("Bahnschrift Light",10),bg="#21244e", fg="#FFFFFF").place(x=50, y=25)
        Label(contenedor,text="Y: "+str(CharObject[i][1]),font=("Bahnschrift Light",10),bg="#21244e", fg="#FFFFFF").place(x=50, y=50)
        Label(contenedor,text="MAGNITUD(μC): "+str(CharObject[i][2]),font=("Bahnschrift Light",10),bg="#21244e", fg="#FFFFFF").place(x=50, y=75)

    #Contenedor de graficas
    graphs = Frame(principalWindGraphs)
    graphs.pack(side=RIGHT)

    #Añadir figura a tkinter
    line = FigureCanvasTkAgg(fig,graphs)
    toolBar=NavigationToolbar2Tk(line, graphs)
    toolBar.update()
    line.get_tk_widget().pack(side=TOP, fill=BOTH,expand=1)
    line.draw()
    line.get_tk_widget().pack(side=LEFT, fill=BOTH,expand=1)
    principalWindGraphs .protocol("WM_DELETE_WINDOW", salir)
    principalWindGraphs .mainloop()
    
def construirGraficas():
    global NumObjects
    print(len(CharObject))
    NumObjects=len(CharObject)
    if Show[0]==True or Show[1]==True:#Creating grid if necessary
        Vec=Space(Limits[0],Limits[1],Limits[2],Limits[3])  
        X, Y = np.meshgrid(Vec[0], Vec[1])
    if Show[0]==True: 
        VecField(Vec[0],Vec[1])

    if Show[1]==True:
        V_e=Voltaje()
        plt.contour(X, Y, V_e[0], 30, colors='k', linestyles="solid")
        plt.contour(X, Y, V_e[1], 30, colors='k')#Porque tenia 20

    if Show[2]==True:
        LineField()
    
    if Show[3]==True:
        PointCharge()  
    DoPlot(Limits[0],Limits[1],Limits[2],Limits[3]) 
    ventanaGraficas(fig, NumObjects)

CharObject=[[-2,0,-30],[2,0,-30],[0,2,30],[0,-2,30]]#Info charges
NumObjects=len(CharObject)
k=1/(4*8.854*10**(-12)*np.pi)#Constant NM2/muC2
Show=[False,True,True,True,False] #Show in plot: vecField, Equi, LineDiagram, Charges, Potencial
Limits=[-5,5,-5,5]#Limits grid
Vec=Space(Limits[0],Limits[1],Limits[2],Limits[3])  
X, Y = np.meshgrid(Vec[0], Vec[1])
fig, (Field) = plt.subplots(ncols= 1, figsize =(7, 7))#Creating plot
construirGraficas()
