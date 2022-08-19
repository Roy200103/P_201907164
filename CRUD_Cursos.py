
from Curs import Cursp

class CRUD_Cursos:
        
    
    
    

    def leerCursos(self, ruta):
        
        
        with open(ruta) as Objeto:
             Lcs = Objeto.readlines()
             print(Lcs)
       
        cursos=[]                   
        for Lc in Lcs:
            dat = Lc.split(',')               
            lcurso = Cursp(dat[0], dat[1], dat[2], dat[3], dat[4], dat[5], dat[6].rstrip('\n'))
            cursos.append(lcurso)
        return cursos   
        
        
             