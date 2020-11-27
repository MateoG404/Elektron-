def ventanaGraficas(fig,numero):
    global toolBar
    #Ventana Windows
    global principalWindGraphs
    principalWindGraphs=Tk()
    principalWindGraphs .resizable (0,0)
    principalWindGraphs .configure(bg="white")
    principalWindGraphs .geometry("800x600")
    # Titulo e icono
    principalWindGraphs .title("ELEKTRON")
    principalWindGraphs .iconbitmap("./images/logo.ico")

    #Contenedor de opciones
    optionsFrame=Frame(principalWindGraphs , bg="#21244e")
    optionsFrame.config(width="250",height="600")
    optionsFrame.pack(side=LEFT,fill="both",expand="yes")
    modificarButton=Button(optionsFrame,text = "Modificar",font=("Bahnschrift Light",11),bg="#FFFFFF",fg="#000000",width=10,height=1, command = lambda: modificarValores(numero))
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
    line.mpl_connect('button_press_event', onclick)#Evennto para capturar coordenada
    toolBar=NavigationToolbar2Tk(line, graphs)
    toolBar.update()
    line.get_tk_widget().pack(side=TOP, fill=BOTH,expand=1)
    line.draw()
    line.get_tk_widget().pack(side=LEFT, fill=BOTH,expand=1)
    principalWindGraphs.mainloop()
    principalWindGraphs.protocol("WM_DELETE_WINDOW", salir)


def onclick(event):
    global toolBar
    x, y = event.xdata, event.ydata
    if(x!=None and y!=None and NumObjects<6 and toolBar._active!="PAN" and toolBar._active!="ZOOM"):
        master=Tk()
        print(x,y)
        añadirCarga(NumObjects,master,round(x,2),round(y,2))
        
def actualizarCargas(frame, numero,master):
    global principalWindGraphs
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

    Field.clear()
    print(CharObject)
    principalWindGraphs.destroy()
    master.destroy()
    construirGraficas()
    
def añadirCarga(numero, master,x,y):
    global principalWindGraphs
    if numero<6:
        numero+=1
        CharObject.append([x,y,0])
        try:
            master.destroy()
        except:
            pass
        modificarValores(numero)
    else:
        messagebox.showerror(message="No se permiten más cargas", title="Elektron")
        
def eliminarCarga(numeroCarga,numero,ven):
    global CharObject
    global principalWindGraphs
    try:
        CharObject.pop(int(numeroCarga)-1)
        numero-=1 
        ven.destroy()
        modificarValores(numero)
    except:
        messagebox.showerror(message="El valor ingresado es invalido", title="Elektron")

def panelEliminarCarga(numero, master):
    global principalWindGraphs
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
   
   def paneles(numero, master):
    global principalWindGraphs
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
    agregarButton=Button(frame,text = "Agregar Carga",font=("Bahnschrift Light",11),bg="#31B821",fg="#FFFFFF",width=12,height=1, command = lambda: añadirCarga(numero, master,0,0))
    agregarButton.pack(side="left")

    #Eliminar carga
    eliminarButton=Button(frame,text = "Eliminar Carga",font=("Bahnschrift Light",11),bg="#E71919",fg="#FFFFFF",width=12,height=1, command = lambda: panelEliminarCarga(numero, master))
    eliminarButton.pack(side="right")

    #Aceptar
    aceptarButton=Button(frame,text = "Aceptar",font=("Bahnschrift Light",11),bg="#21244e",fg="#FFFFFF",width=10,height=1, command = lambda: actualizarCargas(frame, numero,master))
    aceptarButton.pack()
    return master

#Crea la ventana principal
def modificarValores(numeroActualCargas):
    global principalWindGraphs
    global master
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
 
 def salir():
    plt.close()

def comprobarEntrada(event):
    charCorrectos=[".","0","1","2","3","4","5","6","7","8","9","-",8,13,9,37,38,39,40,13,46]
    en=event.widget
    if event.char not in charCorrectos and event.keycode not in charCorrectos:
        en.insert(0,"")
        en.delete(0,"end")
        messagebox.showerror(message="Solo valores numéricos", title="Tkinter")    
