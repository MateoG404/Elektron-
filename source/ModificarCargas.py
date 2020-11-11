from tkinter import *
from tkinter import messagebox

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

valores=[[1.0,2.0,3.0],[4.0,5.0,6.0]]
numeroActualCargas=len(valores)#Determina cuantas cargas existen 
modificarValores(numeroActualCargas)
