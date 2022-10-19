from tkinter import *
from tokenize import Double
from PIL import Image, ImageFilter, ImageTk

#Se crea la ventana donde iran los elementos 
ventana = Tk()
ventana.title("Pupuseria la bendición")
ventana.geometry("800x600")
ventana.configure(bg="#2E86C1")
#se configuran las imagenes 
queso= Image.open(r"C:\Users\ec133\Desktop\parcial\queso.jpeg")
queso=queso.filter(ImageFilter.SHARPEN)
render=ImageTk.PhotoImage(queso)
reducida = queso.resize((100,100), Image.Resampling.LANCZOS)
render= ImageTk.PhotoImage(reducida)

revuelta= Image.open(r"C:\Users\ec133\Desktop\parcial\REVUELTA-TIPICOS-MARGOTH.jpg")
revuelta=revuelta.filter(ImageFilter.SHARPEN)
render1=ImageTk.PhotoImage(revuelta)
reducida = revuelta.resize((100,100), Image.Resampling.LANCZOS)
render1= ImageTk.PhotoImage(reducida)

fq= Image.open(r"C:\Users\ec133\Desktop\parcial\pupusas-de-frijol-con-queso.jpg")
fq=fq.filter(ImageFilter.SHARPEN)
render2=ImageTk.PhotoImage(fq)
reducida1 = fq.resize((100,100), Image.Resampling.LANCZOS)
render2= ImageTk.PhotoImage(reducida1)

fq= Image.open(r"C:\Users\ec133\Desktop\parcial\pupusas-de-frijol-con-queso.jpg")
fq=fq.filter(ImageFilter.SHARPEN)
render2=ImageTk.PhotoImage(fq)
reducida1 = fq.resize((100,100), Image.Resampling.LANCZOS)
render2= ImageTk.PhotoImage(reducida1)

soda= Image.open(r"C:\Users\ec133\Desktop\parcial\soda.jpeg")
soda=soda.filter(ImageFilter.SHARPEN)
render3=ImageTk.PhotoImage(soda)
reducida1 = fq.resize((100,100), Image.Resampling.LANCZOS)
render3= ImageTk.PhotoImage(reducida1)

soda= Image.open(r"C:\Users\ec133\Desktop\parcial\soda.jpeg")
soda=soda.filter(ImageFilter.SHARPEN)
render3=ImageTk.PhotoImage(soda)
reducida2 = soda.resize((100,100), Image.Resampling.LANCZOS)
render3= ImageTk.PhotoImage(reducida2)

choco= Image.open(r"C:\Users\ec133\Desktop\parcial\chocolate.jpeg")
choco=choco.filter(ImageFilter.SHARPEN)
render4=ImageTk.PhotoImage(choco)
reducida3 = choco.resize((100,100), Image.Resampling.LANCZOS)
render4= ImageTk.PhotoImage(reducida3)

fres= Image.open(r"C:\Users\ec133\Desktop\parcial\fresco.jpeg")
fres=fres.filter(ImageFilter.SHARPEN)
render5=ImageTk.PhotoImage(fres)
reducida4 = fres.resize((100,100), Image.Resampling.LANCZOS)
render5= ImageTk.PhotoImage(reducida4)
#se cren las funciones para los radio buttons 
opcion=IntVar()
bebida=IntVar()
domicilio=IntVar()

def pupusas():
    global especialidad
    global pupas
    o=opcion.get()

    if o==1:
        pupas=0.7
        especialidad = "Queso"
    elif o==2:
        pupas=0.65
        especialidad = "F/Q"
    elif o==3:
        pupas=0.6
        especialidad = "revuelta"
    else :
        pupas=0
        especialidad = ""

def bebidas():
    global tipo
    global bebi
    b=bebida.get()
    if b==4:
        bebi=0.75
        tipo="gaseosa"
    elif b==5:
        bebi=0.5
        tipo="chocolate"
    elif b==6:
        bebi=0.60
        tipo="fresco"
    else :
        bebi=0

def domic():
    global domicili
    d=domicilio.get()
    if d == 1:
        domicili=1.5
    elif d==2:
        domicili=0
 


def total():
    totpupas=float(cantidad.get())*pupas

    total=totpupas+bebi+domicili

    print("Producto     Cantidad      Precio" )
    print(especialidad,"          ",cantidad.get(),"          ","$",totpupas)
    print(tipo,"      ","-","      ","$",bebi)
    print("domicilio","      ","-","      ","$",domicili)
    print("total                   ","$",total)





#Se agregan los radio buttons 
radio1=Radiobutton(ventana, text="QUESO" , value=1 ,command=pupusas, variable=opcion)
radio2=Radiobutton(ventana, text="F/Q" , value=2, command=pupusas, variable=opcion)
radio3=Radiobutton(ventana, text="REVUELTAS" , value=3,command=pupusas , variable=opcion)
radio4=Radiobutton(ventana, text="Gaseosa" , value=4 ,command=bebidas, variable=bebida)
radio5=Radiobutton(ventana, text="Chocolate" , value=5 ,command=bebidas, variable=bebida)
radio6=Radiobutton(ventana, text="Fresco" , value=6,command=bebidas , variable=bebida)
radio7=Radiobutton(ventana, text="si" , value=1 ,command=domic, variable=domicilio)
radio8=Radiobutton(ventana, text="no" , value=2,command=domic ,variable=domicilio)

#Se agrega el boton de imprimir factura y el entry para saber cuantas pupusas se ordenaron 
cantidad=StringVar()
btn=Button(ventana, text="imprimir factura", command=total)

cant=Entry(ventana, font=10, bg="white", textvariable=cantidad)



#Se crean los labels donde iran las imagenes y ademas se pocisiona todo lo que ira dentro de la ventana 
lb=Label(ventana,text="Especialidades de pupusas", background="#5DADE2")
lb.place(x=240, y=10)
lb1=Label(ventana, image=render)
lb1.place(x=50, y=40)
lb2=Label(ventana, image=render1)
lb2.place(x=250, y=40)
lb3=Label(ventana, image=render2)
lb3.place(x=450, y=40)
lb4=Label(ventana,text="Bebidas", background="#5DADE2")
lb4.place(x=300, y=190)
lb5=Label(ventana, image=render3)
lb5.place(x=50, y=220)
lb6=Label(ventana, image=render4)
lb6.place(x=250, y=220)
lb7=Label(ventana, image=render5)
lb7.place(x=450, y=220)
radio1.place(x=50, y=150)
radio2.place(x=250, y=150)
radio3.place(x=450, y=150)
radio4.place(x=50, y=330)
radio5.place(x=250, y=330)
radio6.place(x=450, y=330)
lb8=Label(ventana,text="Domicilio", background="#5DADE2")
lb8.place(x=10, y=370)
radio7.place(x=65, y=370)
radio8.place(x=100, y=370)
btn.place(x=700, y=500)
lb8=Label(ventana,text="Cantidad", background="#5DADE2")
lb8.place(x=650, y=40)
cant.place(x=650, y=60, width=100)

ventana.mainloop()