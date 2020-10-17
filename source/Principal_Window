#Project Elektron
from tkinter import *

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
    newButton = Button(principalWind,text = "Nuevo Proyecto",font=("Fredericka the Great",20),bg="#21244e",fg="#FFFFFF",width=15,height=1,command = lambda : CreateProject())
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

def Regresar():
    print("Regreso")
    
principal()
