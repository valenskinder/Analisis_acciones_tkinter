#Programa que permite obtener datos desde la API de Yahoo Finance.
#Recordar instalar yfinance, pandas, matploitlib
# pip install yfinance
# pip install pandas
# pip install matplotlib

from calendar import c
from tkinter import *
from tkinter import messagebox #importo de tkinter para poder hacer una ventana emergente
from tkinter import ttk
import matplotlib.pyplot as plt 
#Importo librerias necesarias para el trabajo
import yfinance as yf #Importamos la biblioteca
import pandas as pd #importo la libreria panda

root=Tk() #Creacion raiz

root.title("Yahoo Finance")
root.geometry ("600x600")

#Incluimos panel para la pestañas

pestanas= ttk.Notebook (root)
pestanas.pack(fill="both", expand="yes")

#Creamos pestañas
p0=ttk.Frame(pestanas)

#Agregamos pestañas

pestanas.add (p0, text="Principal")

#CREACION DE FUNCIONES

def InfoAdicional(): #Funcion para mostrar aviso en una ventana emergente. Tengo que llamar con un command desde el subelemento
    #de AYUDA, Acerca de...
    
    messagebox.showinfo("Yahoo Finance","Adquisición de datos historicos de acciones de empresas ")

def SalirAplicacion (): #Funcion para que pregunta si se desea salir o no de la aplicacion.
    
    valor=messagebox.askquestion("Salir","Desea salir de la aplicacion?")

    #Si el elijo si, la variable valor tiene el valor de "yes"

    if valor=="yes": 
        root.destroy() #Para  el programa.

def extraerDatos():

    #Extraigo sigla de empresa
    e=entryEmpresa.get()
    
    #Extraigo año, mes y dia inicial
    ai=anio1.get()
    mi=mes1.get()
    di=dia1.get()

    #Extraigo año, mes y dia inicial
    af=anio2.get()
    mf=mes2.get()
    df=dia2.get()

    datos=[e,ai,mi,di,af,mf,df]

    return datos

def anadir():
    
    #**************FRAME PARA PESTAÑA P1**********************

    datosR=extraerDatos() #Llamo a la funcion extraerDatos y lo guardo en un array

    start=datosR[1]+"-"+datosR[2]+"-"+datosR[3] #Concateno para obtener la fecha de inicio
    end=datosR[4]+"-"+datosR[5]+"-"+datosR[6] #Concateno para obtener la fecha de fin
    
    df=yf.download(datosR[0], start, end) #Obtengo solamente el cierre ajustado
    
    fig,ax=plt.subplots(1,2,figsize=(12,5))

    fig.suptitle("GRAFICOS",fontsize=20) #TITULO DEL GRÁFICO

    ax[0].plot(df.index,df["Adj Close"],label="META")
    ax[0].set_xlabel("Años",fontsize=10)
    ax[0].set_ylabel("Precio cierre USD",fontsize=10)

    ax[1].boxplot(df["Adj Close"])
    ax[1].set_xlabel(datosR[0],fontsize=10)
    ax[1].set_ylabel("Precio cierre USD",fontsize=10)
    
    fig.show()
    
    #Primero creamos un frame que contenga todo.
    
    #Calculo maximo, mínimo y mediana

    diaMax=str(df["Adj Close"].idxmax())
    diaMin=str(df["Adj Close"].idxmin())

    Q1=df["Adj Close"].quantile(q=.25)
    Q3=df["Adj Close"].quantile(q=.75)

    IQR=Q3-Q1

    atipicos=(Q3+(1.5*IQR)).round(2)

    text1="El valor máximo de la accion fue: "+str(df["Adj Close"].max().round(2))+" y sucedio el: "+diaMax[0:10]
    text2="El valor minimo de la accion fue: "+str(df["Adj Close"].min().round(2))+" y sucedio el: "+diaMin[0:10]
    text3="El valor de la mediana del precio la accion es: "+ str(df["Adj Close"].median().round(2))
    text4="Los valores atipicos están por arriba de: "+str(atipicos)

    labelMax.config(text=text1)
    labelMin.config(text=text2)
    labelMed.config(text=text3)
    labelAtip.config(text=text4)

    c=c+1

    print(c)

    
#Creacion del menu.

barraMenu=Menu (root) #Creacion de variable, y le decimos a donde va a pertenecer (root).

root.config (menu=barraMenu)

#Establecemos cuantos elementos va a contener el menu.

archivoMenu=Menu (barraMenu,tearoff=0) #Con tearoff es para eliminar una linea dentro del submenu.

archivoMenu.add_command(label="Salir",command=SalirAplicacion)

barraMenu.add_cascade (label="Archivo",menu=archivoMenu)

#Elemento AYUDA

archivoAyuda=Menu (barraMenu,tearoff=0)

#Creamos subelementos para AYUDA

archivoAyuda.add_command(label="Acerca de...",command=InfoAdicional)#Con command llamo a la funcion para mostrar la ventana emergente.

#Especificamos los nombres de cada elemento del menu de la siguiente manera:

barraMenu.add_cascade (label="Ayuda",menu=archivoAyuda)

#####################CREACIÓN DE ELEMENTOS VISUALES####################################

#FRAME PARA EL TITULO
frameTitulo=Frame (p0) #Creacion del frame.
frameTitulo.pack() #Empaquetamiento del frame.

label1=Label (p0,text="Evaluación de precio de cierre de empresas", font=("arial",18))
label1.pack(anchor="center",padx=20,pady=20)

#FRAME PARA INDICAR EMPRESA

frameMenu=Frame (p0) #Creacion del frame.
frameMenu.pack(padx=10,pady=2)


frameEmpresa=Label(frameMenu,text="Simbolo empresa", font=("arial",12))
frameEmpresa.grid(row=0,column=0,padx=10,pady=2)

entryEmpresa=Entry (frameMenu,justify="right",width=10) #cuadro de texto año inicio
entryEmpresa.grid (row=0,column=1,padx=5,pady=5)
entryEmpresa.insert (0,"MELI")   #Para insertar el valor predeterminado

separador1=ttk.Separator(frameMenu,orient=HORIZONTAL)
separador1.grid (row=1,column=0,sticky="EW",columnspan=4,padx=10,pady=10)


#FRAME PARA SELECCION DE FECHAS

frameFecha=Frame (p0) #Creacion del frame.
frameFecha.pack() #Empaquetamiento del frame.

label2=Label (frameFecha,text="Fecha inicio", font=("arial",12))
label2.grid(row=0, column=0,padx=10,pady=2)

separador1=ttk.Separator(frameFecha,orient=HORIZONTAL)
separador1.grid (row=1,column=0,sticky="EW",columnspan=4,padx=10,pady=10)

anio1= Entry (frameFecha,justify="right",width=4) #cuadro de texto año inicio
anio1.grid (row=2,column=0,padx=5,pady=5)
anio1.insert (0,"2015")   #Para insertar el valor predeterminado

anio1Label=Label (frameFecha,text="Año", font=("arial",8))
anio1Label.grid (row=3,column=0)

mes1= Entry (frameFecha,justify="right",width=4) #cuadro de texto mes inicio
mes1.grid (row=2,column=1,padx=5,pady=5)
mes1.insert (0,"01")   #Para insertar el valor predeterminado

mes1Label=Label (frameFecha,text="Mes", font=("arial",8))
mes1Label.grid (row=3,column=1)

dia1= Entry (frameFecha,justify="right",width=4) #cuadro de texto día inicio
dia1.grid (row=2,column=2,padx=45,pady=5)
dia1.insert (0,"01")   #Para insertar el valor predeterminado

dia1Label=Label (frameFecha,text="Día", font=("arial",8))
dia1Label.grid (row=3,column=2)

#FECHA FIN

label3=Label (frameFecha,text="Fecha fin", font=("arial",12))
label3.grid(row=5, column=0,padx=10,pady=2)

separador2=ttk.Separator(frameFecha,orient=HORIZONTAL)
separador2.grid (row=6,column=0,sticky="EW",columnspan=4,padx=10,pady=10)

anio2= Entry (frameFecha,justify="right",width=4) #cuadro de texto año inicio
anio2.grid (row=7,column=0,padx=5,pady=5)
anio2.insert (0,"2022")   #Para insertar el valor predeterminado

anio2Label=Label (frameFecha,text="Año", font=("arial",8))
anio2Label.grid (row=8,column=0)

mes2= Entry (frameFecha,justify="right",width=4) #cuadro de texto mes inicio
mes2.grid (row=7,column=1,padx=5,pady=5)
mes2.insert (0,"01")   #Para insertar el valor predeterminado

mes2Label=Label (frameFecha,text="Mes", font=("arial",8))
mes2Label.grid (row=8,column=1)

dia2= Entry (frameFecha,justify="right",width=4) #cuadro de texto día inicio
dia2.grid (row=7,column=2,padx=45,pady=5)
dia2.insert (0,"01")   #Para insertar el valor predeterminado

dia2Label=Label (frameFecha,text="Día", font=("arial",8))
dia2Label.grid (row=8,column=2)

#FRAME PARA BOTONES

frameBotones=Frame (p0) #Creacion del frame.
frameBotones.pack() #Empaquetamiento del frame.

boton1=Button (frameBotones,text="Evaluar",width=15,height=2,command=anadir)
boton1.grid(row=0,column=0,padx=10,pady=10)

frameResultados=Frame (p0) #Creacion del frame.
frameResultados.pack() #Empaquetamiento del frame.

labelResultado=Label (frameResultados,text="", font=("arial",12))
labelResultado.grid (row=0,column=0)

labelMax=Label (frameResultados, font=("arial",12))
labelMax.grid (row=0,column=0)

labelMin=Label (frameResultados, font=("arial",12))
labelMin.grid (row=1,column=0)

labelMed=Label (frameResultados, font=("arial",12))
labelMed.grid (row=2,column=0)

labelAtip=Label (frameResultados, font=("arial",12))
labelAtip.grid (row=3,column=0)


root.mainloop()