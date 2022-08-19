
from Curs import Cursp

class Crud_Cursos:
    #Lectura del Archivo
    def __init__(self):
        self.cursos=[] 

    def leerCursos(self, ruta):
         
        with open(ruta) as Objeto:
             Lcs = Objeto.readlines()
             print(Lcs)
        curos1 = [] 
        #cursos = []                   
        for Lc in Lcs:
            dat = Lc.split(',')               
            lcurso = Cursp(dat[0], dat[1], dat[2].split(';'), dat[3], dat[4], dat[5], dat[6].rstrip('\n'))
            self.cursos.append(lcurso)
        
        #verificacion de cursos repetidos
        longitud = len(self.cursos)
        for i in range(longitud):
           item = self.cursos[i].getCodigo()
           for j in range(i + 1, longitud):
                item1 = self.cursos[j].getCodigo()
                if item == item1:
                    print(item + 'Repetido')
                    curos1.append([i, item])
                    
        #print(curos1)
        #Eliminación de la lista cursos[] los cursos repetidos 
        cont = 0
        for i in range(len(curos1)):
            if self.cursos[curos1[i][0]].getCodigo() == curos1[i][1]:
                self.cursos.pop(curos1[i][0])
                cont += 1       
            elif self.cursos[(curos1[i][0] - cont)].getCodigo() == curos1[i][1]:
                self.cursos.pop((curos1[i][0]-cont))
                cont += 1
    
        return self.cursos

    def agregarCurs(self, acodigo, anombre, aprerrequisito, aobligatorio, asemestre, acreditos, aestado):
         
        nuevoCurso = Cursp(acodigo, anombre, aprerrequisito, aobligatorio, asemestre, acreditos, aestado)
        self.cursos.append(nuevoCurso)

        return self.cursos
    
    def editarCurs(self, ecodigo):
        for i in range(len(self.cursos)):
            if self.cursos[i].getCodigo() == ecodigo:
                enombre = input("Nombre: ")
                eprerrequisito = input("Prerrequisisto: ")
                eobligatorio = int(input("Obligatorio: "))
                esemestre = int(input("Semestre: "))
                ecreditos = int(input("Creditos: "))
                eestado = int(input("Estado: "))
                editarCurso = Cursp(ecodigo, enombre, eprerrequisito, eobligatorio, esemestre, ecreditos, eestado)
                self.cursos[i] = editarCurso
                print('Curso Editado')
                return self.cursos
    
    def mostrarCurso(self, mcodigo):
        for i in range(len(self.cursos)):
            if self.cursos[i].getCodigo() == mcodigo:
                print(self.cursos[i].getCodigo(),' ', self.cursos[i].getNombre(), ' ', self.cursos[i].getPrerrequisito() , ' ', self.cursos[i].getObligatorio() , ' ', self.cursos[i].getSemestre() , ' ', self.cursos[i].getCreditos() , ' ', self.cursos[i].getEstado() )
    
    def eliminarCurso(self, elcodigo):
        for i in range(len(self.cursos)):
            if self.cursos[i].getCodigo() == elcodigo:
                self.cursos.pop(i)
                break
        return self.cursos