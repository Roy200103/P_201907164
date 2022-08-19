
class Cursp:
    
    def __init__(self, codigo, nombre, prerrequisito, obligatorio, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerrequisito = prerrequisito
        self.obligatorio = obligatorio
        self.semestre = semestre
        self.creditos = creditos
        self.estado = estado

    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre
    
    def getPrerrequisito(self):
        return self.prerrequisito

    def getObligatorio(self):
        return self.obligatorio
    
    def getSemestre(self):
        return self.semestre
    
    def getCreditos(self):
        return self.creditos
    
    def getEstado(self):
        return self.estado
    
    def setCodigo(self, Codigo):
        self.codigo = Codigo

    def setNombre(self, Nombre):
        self.nombre = Nombre
    
    def setPrerrequisito(self, Prerrequisito):
        self.prerrequisito = Prerrequisito

    def setObligatorio(self, Obligatorio):
        self.obligatorio = Obligatorio
    
    def setSemestre(self, Semestre):
        self.semestre = Semestre
    
    def setCreditos(self, Creditos):
        self.creditos = Creditos

    def setEstado(self, Estado):
        self.estado = Estado

class CRUD_Cursos:
    #Lectura del Archivo
    def leerCursos(self, ruta):
         
        with open(ruta) as Objeto:
             Lcs = Objeto.readlines()
             print(Lcs)
        curos1 = [] 
        cursos = []                   
        for Lc in Lcs:
            dat = Lc.split(',')               
            lcurso = Cursp(dat[0], dat[1], dat[2], dat[3], dat[4], dat[5], dat[6].rstrip('\n'))
            cursos.append(lcurso)
        
        #verificacion de cursos repetidos
        longitud = len(cursos)
        for i in range(longitud):
           item = cursos[i].getCodigo()
           for j in range(i + 1, longitud):
                item1 = cursos[j].getCodigo()
                if item == item1:
                    print(item + 'Repetido')
                    curos1.append([i, item])
                    
        #print(curos1)
        #Eliminación de la lista cursos[] los cursos repetidos 
        cont = 0
        for i in range(len(curos1)):
            if cursos[curos1[i][0]].getCodigo() == curos1[i][1]:
                cursos.pop(curos1[i][0])
                cont += 1       
            elif cursos[(curos1[i][0] - cont)].getCodigo() == curos1[i][1]:
                cursos.pop((curos1[i][0]-cont))
                cont += 1
    
        return cursos


        
        
                


            
             
                            
               
                           
            
                        
                        
                    
        
