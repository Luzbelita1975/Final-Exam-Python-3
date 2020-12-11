import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class GestionAcademica:
    #Constructor de la clase App 
    def __init__(self):   
        self.ventana = tk.Tk() #Creamos la ventana
        self.ventana.title("Gestion Academica")
        self.cuaderno = ttk.Notebook(self.ventana) #Creamos el cuaderno
        
        #creamos la lista de objetos Curso
         self._curso = []
        
        
        
        
        #llamada a los metodos que se van a ejecutar
        self.carga_curso() 
        self.agregar_curso() 
        self.calculo_recaudacion_curso() 
        self.mostrar_todo() 
        self.cuaderno.grid(column=0, row=0, padx=10, pady=10) 
        self.ventana.mainloop() #Mostramos la ventana
              
    #Metodos de la clase app
    def carga_curso(self):
        self.pagina1 = ttk.Frame(self.cuaderno) #Creamos la pagina 1
        self.cuaderno.add(self.pagina1, text="Carga de Cursos") #Agregamos la pagina al cuaderno
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Curso") #Creamos un LabelFrame, un label que encierra al resto de elementos        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Año (1,2,3,etc.):") 
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga = tk.StringVar() #Capturamos el nombre de la persona
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar) #Llama al metodo agregar
        self.boton1.grid(column=1, row=2, padx=4, pady=4)
        
        
    def agregar_curso(self):
        self.pagina1 = ttk.Frame(self.cuaderno) #Creamos la pagina 1
        self.cuaderno.add(self.pagina1, text="Carga de Datos Curso") #Agregamos la pagina al cuaderno
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Artículo") #Creamos un LabelFrame, un label que encierra al resto de elementos        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Descripción:") 
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga = tk.StringVar() #Capturamos la descripción del articulo
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Precio:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga=tk.StringVar() #Capturamos el precio del articulo
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar) #Llama al metodo agregar
        self.boton1.grid(column=1, row=2, padx=4, pady=4)
        
        
        
    def calculo_recaudacion_curso(self):
        self.pagina1 = ttk.Frame(self.cuaderno) #Creamos la pagina 1
        self.cuaderno.add(self.pagina1, text="Carga de Estudiantes") #Agregamos la pagina al cuaderno
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Artículo") #Creamos un LabelFrame, un label que encierra al resto de elementos        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Descripción:") 
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga = tk.StringVar() #Capturamos la descripción del articulo
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Precio:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga=tk.StringVar() #Capturamos el precio del articulo
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar) #Llama al metodo agregar
        self.boton1.grid(column=1, row=2, padx=4, pady=4)
        
        
    def mostrar_todo(self):
        self.pagina2 = ttk.Frame(self.cuaderno) #Creamos la pagina 2
        self.cuaderno.add(self.pagina2, text="Recaudacion por Curso") #La agregamos al cuaderno
        self.labelframe1 = ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo = tk.StringVar() #Capturamos el código del arituclo
        self.entrycodigo = ttk.Entry(self.labelframe1, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion = tk.StringVar() 
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcion, state="readonly") #'readonly' permite mostrar info en el Entry pero no modificarla
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe1, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
            
        

    def agregar(self):
        datos = (self.descripcioncarga.get(), self.preciocarga.get()) #Creamos una tupla con los datos cargados
        #self.conexion.alta(datos) #Se los damos al objeto ConnectionDB para que de la alta en la BD
        mb.showinfo("Información", "Los datos fueron cargados") #Mostramos una ventana avisando que se cargo la información
        self.descripcion.set("") #Vaciamos el campo de descricon
        self.precio.set("") #Vaciamos el campo de precio


    
    def consultar(self):
        datos = (self.codigo.get(), ) #Creamos la tupla con el código de consulta
        respuesta = self.conexion.consulta(datos) #Le enviamos el código al objeto ConnectionDB para que haga la busqueda
        if len(respuesta)>0: #
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

app = GestionAcademica()


#Constructores de cada clase que voy a trabajar, le faltan los metodos, recordar que van en lista de objetos


                        
                            