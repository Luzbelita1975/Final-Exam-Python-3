import os

#Clases y metodos

class Persona (object):

 def __init__(self, nombre, apellido, dni, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.edad = edad
    
    
class Docente (Persona):
     
     n=true #si esta en true significa que debo cargar nueva especialidad, sino dejo lo que tiene cargado
     especialidad = input("Ingrese especialidad del docente:  ")
     if n == true:
         print ("Cargo especialidad de docente")
     else:
         print  ("No cargo nada")
         
# creo un objeto de la clase Docente llamado profesor
profesor = Docente();
#agrego un objeto de la clase Docente llamado profesor a la lista de profesores
profesores.append (profesor) 

# defino set y get para especialidad 
def setEspecialidad (self ,especialidadNueva):
        self.especialidad = especialidadNueva
        
def getEspecialidad (self):
        return self.especialidad 
            
def __str__(self):
        """Devuelve una cadena representativa de docente"""
        return "%s: %s, %s %s, %s." % (
            self.__doc__[25:34], str(self.especialidad)
            
class Estudiante(Persona):
    
         
#metodo calcular cuota

def calcularCuota ():
         pass
             
class ActividadExtra:
    
    def __init__(self, actividad,cantidadHoras,costo):
        self.actividad
        self.cantidadHoras
        self.costo    
                 
        mensaje = input ("El alumno tiene actividad extracurricular ? s/n")
        
        if mensaje == "s":
        
        actividad = input ("Ingrese tipo de actividad extracurricula (Educacion Fisica, Teatro o Musica): ")
        
        if actividad =="Educacion Fisica":
            cantidadHoras = input("Ingrese Cantidad de Horas (Educ.Fisica hasta 4 hs semanales):  ")
            costo = cantidadHoras * 700
            return costo
        elif actividad =="Teatro":
            cantidadHoras = input("Ingrese Cantidad de Horas (Teatro hasta 6hs semanales):  ")
            costo = cantidadHoras * 100
            return costo
        elif actividad =="Musica":
            cantidadHoras = input("Ingrese Cantidad de Horas (Musica hasta 4 hs semanales):  ")
            costo = cantidadHoras * 800
            return costo
            
        elif mensaje == "n":
            print ("El alumno no realiza ninguna actividad extracurricular")
             


class Curso:
    def __init__(self,anio):
        self.anio         
        self.profesores = []
        self.estudiantes = [] 
        
        
        #metodos de la clase Curso
        
        anio = input ("Ingrese el año correspondiente:  (1. primer año, 2. segundo año, etc.")
        
        
        def agregarDocente():
            
        docente.append (docente)    
        
        def agregarEstudiante():
        
        estudiantes.append (estudiante) 
        
        def calcularRecaudacion():
                pass         
    
class GestionAcademica ():
    
def __init__ (self):
        
self.={} # definimos un diccionario para almacenar los datos

    
def menu (self):
          
#Limpiamos la pantalla
os.system("cls")

print('Software de Gestion Academica')

#Creamos una variable opcion que va a empezar valiendo 0
#De esta forma, forzamos el comienzo del while. 
opcion = 0

while opcion != 5:
    print('--------------------------------------')
    print ("     Sistema de Gestion Academica    ")
    print('--------------------------------------')
    print('1.Carga de datos')
    print('2.Agregar Curso')
    print('3.Informe de Recaudacion')
    print('4.Mostrar todo')
    print('5.Salir')
    print('---------------------')
    opcion = int(input('Ingrese una opcion: '))
    while opcion < 1 or opcion > 5:
        print ("Se ingreso un valor incorrecto.")
        opcion = int(input('Ingrese una opcion:'))
        
    #Estructura condicional que se va a encargar de elegir el código a ejecutar de acuerdo al código que ingrese el usuario
    if opcion == 1:
        self.cargar()
    elif opcion == 2:
         pass
    elif opcion == 3:
        pass    
    elif opcion == 4:
        pass        
    if opcion == 5:
        print ("Programa finalizado")
        print ("")
        
        def cargar():
          
          
         nombre = input("Ingrese nombre:  ")
         apellido = input("Ingrese apellido:  ")
         dni = input("Ingrese dni:  ")
         edad = input("Ingrese edad:  ")
       
          
          
          
          
                   
        def agregarCurso(self):
          pass 
           
           
           
           
           
            
        def mostrar (self):
        print("______________________________________________")        
        print("Listado completo de Cursos")
        
        for anio in self.cursoss:
            print(anio, self.cursoss[anio])
        print("______________________________________________")
            
        def recaudacion (self):
              
              opcion = input ("Ingrese el curso para realizar el calculo:  ")
              if opcion in self.cursoss:
                pass
                
                
                print("La recaudacion es;",total)
        else:
            print("No existe el curso seleccionado")
              
        
'''bloque principal'''
gestionacademica = GestionAcademica()
GestionAcademica.menu()