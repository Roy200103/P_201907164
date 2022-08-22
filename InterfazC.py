from msilib.schema import Class
from pickle import SETITEMS
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from webbrowser import get


from CRUD_Cursos import Crud_Cursos



''' PANTALLA PRINCIPAL '''
class VentPrin:
    def __init__(self):
        self.vent = Tk()
        self.vent.resizable(False,False)
        self.vent.title('Practica 1 LFP B+')
        self.Centrar(self.vent, 600, 500)
        self.vent.geometry('600x500')
        self.vent.configure(bg='IndianRed1')
        self.Ventana()
#102027
    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.frame = Frame(height=500, width=500)
        self.frame.config(bg='steel blue')
        self.frame.pack(padx=25, pady=25)
        Label(self.frame, text="Lenguajes Formales y de Programación\nRoyer Estuardo Mendoza Arriola\n201907164", font=('Times New Roman',14), fg='Black', bg='AntiqueWhite3', width=45).place(x=25, y=30)
        Button(self.frame, text="Cargar Archivo", command=self.IrPantallaCA ,  font=('Times New Roman',14), fg='#000000', bg= 'burlywood3', width=20).place(x=150, y=150)
        Button(self.frame, text="Gestionar Cursos", command=self.IrPantallaGC , font=('Times New Roman',14), fg='#000000', bg='burlywood3', width=20).place(x=150, y=210)
        Button(self.frame, text="Conteo de creditos",  font=('Times New Roman',14), fg='#000000', bg='burlywood3', width=20).place(x=150, y=270)
        Button(self.frame, text="Salir", command=self.Salirapp,  font=('Times New Roman',14), fg='#000000', bg='burlywood3', width=20).place(x=150, y=330)
        self.frame.mainloop()
    
    
    
    def IrPantallaCA(self):
       
        self.vent.destroy()
        CarA()
    
    def IrPantallaGC(self):
       
        self.vent.destroy()
        GestCurs()
    
    def Salirapp(self):
        self.vent.destroy()
#----------------------------------------------------------------------------------------------                   
class CarA:
    
        def __init__(self):
            self.ventCA = Tk()
            self.ventCA.resizable(False,False)
            self.ventCA.title('Cargar Archivo')
            self.Centrar(self.ventCA, 600, 500)
            self.ventCA.geometry('500x300')
            self.ventCA.configure(bg='IndianRed1')
            self.Ventana()
            
            
    
        def Centrar(self, r, ancho, alto):
            altura_pantalla = r.winfo_screenheight()
            ancho_pantalla = r.winfo_screenwidth()

            x = (ancho_pantalla // 2) - (ancho // 2)
            y = (altura_pantalla // 2) - (alto // 2)
            r.geometry(f'+{x}+{y}')

        def Ventana(self):
            agregarruta = Crud_Cursos()
            
            ruta = StringVar()
            self.frame = Frame(height=500, width=450)
            self.frame.config(bg='steel blue')
            self.frame.pack(padx=25, pady=25)
            rut= Entry(self.frame , textvariable= ruta ,font=('Times New Roman',12), width='35'  ).place(x='130', y='65')
            Label(self.frame, text="Ruta de archivo", font=('Times New Roman',13), fg='#000000', bg= 'AntiqueWhite3',    width=12 ).place(x=10, y=65)
            Button(self.frame, text="Abrir", command= lambda: agregarruta.leerCursos(ruta.get())  , font=('Times New Roman',12), fg='#000000', bg='White', width=10).place(x=170, y=150)
            Button(self.frame, text="Regresar", command=self.IrPantallaP ,  font=('Times New Roman',10), fg='#000000', bg='Red', width=7).place(x=355, y=198)
            self.frame.mainloop()
            
            
        
                

        def IrPantallaP(self):
            self.ventCA.destroy()
            VentPrin()
        

#----------------------------------------------------------------------------------------------
class GestCurs:
    def __init__(self):
        self.ventGC = Tk()
        self.ventGC.resizable(False,False)
        self.ventGC.title('Practica 1 LFP B+')
        self.Centrar(self.ventGC, 600, 500)
        self.ventGC.geometry('600x500')
        self.ventGC.configure(bg='IndianRed1')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        listarcur = Crud_Cursos()
        self.frame = Frame(height=500, width=500)
        self.frame.config(bg='steel blue')
        self.frame.pack(padx=25, pady=25)
        Label(self.frame, text="Gestion de Cursos", font=('Times New Roman',16), fg='#000000', bg='AntiqueWhite3', width=30).place(x=65, y=20)
        Button(self.frame, text="Listar Cursos" , command= listarcur.listarCursos ,  font=('Times New Roman',14), fg='#000000', bg= 'burlywood', width=20).place(x=150, y=70)
        Button(self.frame, text="Agregar Curso", command= self.IrPantallaAgC,  font=('Times New Roman',14), fg='#000000', bg='burlywood', width=20).place(x=150, y=140)
        Button(self.frame, text="Editar Curso",  font=('Times New Roman',14), fg='#000000', bg='burlywood', width=20).place(x=150, y=210)
        Button(self.frame, text="Eliminar Curso", command= self.IrPantallaElmC , font=('Times New Roman',14), fg='#000000', bg='burlywood', width=20).place(x=150, y=280)
        Button(self.frame, text="Regresar", command= self.IrPantallaP ,  font=('Times New Roman',14), fg='#000000', bg='Red', width=20).place(x=150, y=350)
        self.frame.mainloop()

    def IrPantallaP(self):
            self.ventGC.destroy()
            VentPrin()
    def IrPantallaLC(self):
            self.ventGC.destroy()
            ListarCur()
    def IrPantallaAgC(self):
            self.ventGC.destroy()
            AgCurs()
    def IrPantallaElmC(self):
            self.ventGC.destroy()
            ElimCur()
#****************************************************************************************************************************
class ListarCur:
    def __init__(self):
        self.ventLC = Tk()
        self.ventLC.resizable(False,False)
        self.ventLC.title('Practica 1 LFP B+')
        self.Centrar(self.ventLC, 600, 500)
        self.ventLC.geometry('600x500')
        self.ventLC.configure(bg='IndianRed1')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):

        cruCur = Crud_Cursos()
        cur = cruCur.listarCursos()
        tl  = len(cur)
        self.frame = Frame(height=500, width=500)
        self.frame.config(bg='steel blue')
        self.frame.pack(padx=25, pady=25)
        Label(self.frame, text="Listado de Cursos", font=('Times New Roman',16), fg='#000000', bg='AntiqueWhite3', width=30).place(x=65, y=20)
        Button(self.frame, text="Regresar", command= self.IrPantallaP ,  font=('Times New Roman',14), fg='#000000', bg='Red', width=20).place(x=350, y=350)
        tabla = ttk.Treeview(self.frame, columns=('#0','#1','#2','#3','#4','#5','#6'), height=7)

        style = ttk.Style()
        style.configure(
            'Treeview',
            background = 'silver',
            foreground = 'black',
            rowheight = 25,
            fielbackground = 'silver'
        )
        style.map(
            'Treeview',
            background = [('selected', 'green')]
        )

        tabla.grid(row= tl, column=0, columnspan=2)
        tabla.column('#0', width = 50)
        tabla.column('#1', width = 110, anchor = CENTER)
        tabla.column('#2', width = 80, anchor = CENTER)
        tabla.column('#3', width = 70, anchor = CENTER)
        tabla.column('#4', width = 70, anchor = CENTER)
        tabla.column('#5', width = 70, anchor = CENTER)
        tabla.column('#6', width = 70, anchor = CENTER)
        

        tabla.heading("#0", text = 'Codigo', anchor = CENTER)
        tabla.heading("#1", text = 'Nombre', anchor = CENTER)
        tabla.heading('#2', text = 'Prerrequisitos', anchor = CENTER)
        tabla.heading('#3', text = 'Obligatorio', anchor = CENTER)
        tabla.heading('#4', text = 'Semestre', anchor = CENTER)
        tabla.heading('#5', text = 'Creditos', anchor = CENTER)
        tabla.heading('#6', text = 'Estado', anchor = CENTER)
        ## AQUI SE MANDA A LLAMAR A LA FUNCION QUE NOS DEVUELVE TODOS LOS CURSOS
        cur = cruCur.listarCursos()
        for cu in cur:
            tabla.insert("",END, text='Curso', values=(str(cu.getCodigo()) , cu.getNombre() , cu.getPrerrequisito(), cu.getObligatorio(), cu.getSemestre(), cu.getCreditos(), cu.getEstado()))
        
        
        self.frame.mainloop()

    def IrPantallaP(self):
            self.ventLC.destroy()
            VentPrin()

#****************************************************************************************************************************
class AgCurs:
    def __init__(self):
        self.ventAC = Tk()
        self.ventAC.resizable(False,False)
        self.ventAC.title('Practica 1 LFP B+')
        self.Centrar(self.ventAC, 600, 500)
        self.ventAC.geometry('600x500')
        self.ventAC.configure(bg='IndianRed1')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        agregarcurso = Crud_Cursos()

        codigo = StringVar()
        nombre = StringVar()
        prerre = StringVar()
        semes = IntVar()
        opcio = IntVar()
        cred = IntVar()
        esta = IntVar()

        self.frame = Frame(height=500, width=500)
        self.frame.config(bg='steel blue')
        self.frame.pack(padx=25, pady=25)
        Label(self.frame, text="Agregar  Curso", font=('Times New Roman',16), fg='#000000', bg='AntiqueWhite3', width=30).place(x=65, y=20)
        Label(self.frame, text="Codigo", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=70)
        Label(self.frame, text="Nombre", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=110)
        Label(self.frame, text="Prerrequisito", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=150)
        Label(self.frame, text="Semestre", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=190)
        Label(self.frame, text="Opcionalidad", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=230)
        Label(self.frame, text="Creditos", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=270)
        Label(self.frame, text="Estado", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=310)
        cod= Entry(self.frame , textvariable= codigo ,font=('Times New Roman',12), width='35'  ).place(x='180', y='70')
        nom = Entry(self.frame , textvariable= nombre ,font=('Times New Roman',12), width='35'  ).place(x='180', y='110')
        prer= Entry(self.frame , textvariable= prerre ,font=('Times New Roman',12), width='35'  ).place(x='180', y='150')
        sem = Entry(self.frame , textvariable= semes ,font=('Times New Roman',12), width='35'  ).place(x='180', y='190')
        opc = Entry(self.frame , textvariable= opcio ,font=('Times New Roman',12), width='35'  ).place(x='180', y='230')
        cre = Entry(self.frame , textvariable= cred ,font=('Times New Roman',12), width='35'  ).place(x='180', y='270')
        est = Entry(self.frame , textvariable= esta ,font=('Times New Roman',12), width='35'  ).place(x='180', y='310')
        
        Button(self.frame, text="Agregar", command= lambda: agregarcurso.agregarCurs(codigo.get(), nombre.get(), prerre.get(), semes.get(), opcio.get(), cred.get(), esta.get()), font=('Times New Roman',14), fg='#000000', bg='White', width=20).place(x=150, y=365)
        Button(self.frame, text="Regresar", command= self.IrPantallaG ,  font=('Times New Roman',12), fg='#000000', bg='Red', width=7).place(x=400, y=400)
        self.frame.mainloop()

    def IrPantallaG(self):
            self.ventAC.destroy()
            GestCurs()
    
    #*****************************************************************************************************************************************++
    class EdCurs:
        def __init__(self):
            self.ventEC = Tk()
            self.ventEC.resizable(False,False)
            self.ventEC.title('Practica 1 LFP B+')
            self.Centrar(self.ventEC, 600, 500)
            self.ventEC.geometry('600x500')
            self.ventEC.configure(bg='IndianRed1')
            self.Ventana()

        def Centrar(self, r, ancho, alto):
            altura_pantalla = r.winfo_screenheight()
            ancho_pantalla = r.winfo_screenwidth()

            x = (ancho_pantalla // 2) - (ancho // 2)
            y = (altura_pantalla // 2) - (alto // 2)
            r.geometry(f'+{x}+{y}')

        def Ventana(self):
            editarcurso = Crud_Cursos()

            codigo = StringVar()
            nombre = StringVar()
            prerre = StringVar()
            semes = IntVar()
            opcio = IntVar()
            cred = IntVar()
            esta = IntVar()

            self.frame = Frame(height=500, width=500)
            self.frame.config(bg='steel blue')
            self.frame.pack(padx=25, pady=25)
            Label(self.frame, text="Editar  Curso", font=('Times New Roman',16), fg='#000000', bg='AntiqueWhite3', width=30).place(x=65, y=20)
            Label(self.frame, text="Codigo", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=70)
            Label(self.frame, text="Nombre", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=110)
            Label(self.frame, text="Prerrequisito", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=150)
            Label(self.frame, text="Semestre", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=190)
            Label(self.frame, text="Opcionalidad", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=230)
            Label(self.frame, text="Creditos", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=270)
            Label(self.frame, text="Estado", font=('Times New Roman',12), fg='#000000', bg='AntiqueWhite3', width=15).place(x=20, y=310)
            cod= Entry(self.frame , textvariable= codigo ,font=('Times New Roman',12), width='35'  ).place(x='180', y='70')
            nom = Entry(self.frame , textvariable= nombre ,font=('Times New Roman',12), width='35'  ).place(x='180', y='110')
            prer= Entry(self.frame , textvariable= prerre ,font=('Times New Roman',12), width='35'  ).place(x='180', y='150')
            sem = Entry(self.frame , textvariable= semes ,font=('Times New Roman',12), width='35'  ).place(x='180', y='190')
            opc = Entry(self.frame , textvariable= opcio ,font=('Times New Roman',12), width='35'  ).place(x='180', y='230')
            cre = Entry(self.frame , textvariable= cred ,font=('Times New Roman',12), width='35'  ).place(x='180', y='270')
            est = Entry(self.frame , textvariable= esta ,font=('Times New Roman',12), width='35'  ).place(x='180', y='310')
        
            Button(self.frame, text="Agregar", command= lambda: editarcurso.agregarCurs(codigo.get(), nombre.get(), prerre.get(), semes.get(), opcio.get(), cred.get(), esta.get()), font=('Times New Roman',14), fg='#000000', bg='White', width=20).place(x=150, y=365)
            Button(self.frame, text="Regresar", command= self.IrPantallaG ,  font=('Times New Roman',12), fg='#000000', bg='Red', width=7).place(x=400, y=400)
            self.frame.mainloop()

        def IrPantallaG(self):
            self.ventAC.destroy()
            GestCurs()
#*******************************************************************************************************************************************
class ElimCur:
    
        def __init__(self):
            self.ventElC = Tk()
            self.ventElC.resizable(False,False)
            self.ventElC.title('Cargar Archivo')
            self.Centrar(self.ventElC, 600, 500)
            self.ventElC.geometry('500x300')
            self.ventElC.configure(bg='IndianRed1')
            self.Ventana()
            
            
    
        def Centrar(self, r, ancho, alto):
            altura_pantalla = r.winfo_screenheight()
            ancho_pantalla = r.winfo_screenwidth()

            x = (ancho_pantalla // 2) - (ancho // 2)
            y = (altura_pantalla // 2) - (alto // 2)
            r.geometry(f'+{x}+{y}')

        def Ventana(self):
            eliminarcur = Crud_Cursos()
            
            codigo = StringVar()
            self.frame = Frame(height=500, width=450)
            self.frame.config(bg='steel blue')
            self.frame.pack(padx=25, pady=25)
            cod= Entry(self.frame , textvariable= codigo ,font=('Times New Roman',12), width='35'  ).place(x='130', y='65')
            Label(self.frame, text="Código del Curso", font=('Times New Roman',13), fg='#000000', bg= 'AntiqueWhite3',    width=12 ).place(x=10, y=65)
            Button(self.frame, text="Eliminar", command= lambda: eliminarcur.eliminarCurso(codigo.get())  , font=('Times New Roman',12), fg='#000000', bg='White', width=10).place(x=170, y=150)
            Button(self.frame, text="Regresar", command=self.IrPantallaP ,  font=('Times New Roman',10), fg='#000000', bg='Red', width=7).place(x=355, y=198)
            self.frame.mainloop()
            
            
        
                

        def IrPantallaP(self):
            self.ventElC.destroy()
            GestCurs()