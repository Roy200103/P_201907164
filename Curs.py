
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


        
        
                


            
             
                            
               
                           
            
                        
                        
                    
        
