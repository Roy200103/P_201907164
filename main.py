from CRUD_Cursos import Crud_Cursos
from InterfazC import *
#from Curs import Curso
crudCursos = Crud_Cursos()
px = VentPrin()

#cargaA = CarA()






#rut = input('ingrese ruta: ')
ca = crudCursos.leerCursos('Archivo de Prueba.LFP')

for curso in ca:
    print(curso.getCodigo(),' ', curso.getNombre(), ' ', curso.getPrerrequisito() , ' ', curso.getObligatorio())

ag = crudCursos.agregarCurs('777', 'Org. Lenguajes y compiladores', ['771','962','796'], 1, 5, 4, -1)

for curso in ag:
    print(curso.getCodigo(),' ', curso.getNombre(), ' ', curso.getPrerrequisito() , ' ', curso.getObligatorio())

#ec = crudCursos.editarCurs('777')
#for curso in ec:
#    print(curso.getCodigo(),' ', curso.getNombre(), ' ', curso.getPrerrequisito() , ' ', curso.getObligatorio())

mc = crudCursos.mostrarCurso('147')
print('--------------------------------------------------------------------------------------------')
elc = crudCursos.eliminarCurso('147')
for curso in elc:
    print(curso.getCodigo(),' ', curso.getNombre(), ' ', curso.getPrerrequisito() , ' ', curso.getObligatorio() , ' ', curso.getSemestre() , ' ', curso.getCreditos(), ' ', curso.getEstado())
print('-------------------------------------------------------------')
#cca = crudCursos.conteoCA(3)

liscur = crudCursos.listarCursos()

for curso in liscur:
    print(curso.getCodigo(),' ', curso.getNombre(), ' ', curso.getPrerrequisito() , ' ', curso.getObligatorio() , ' ', curso.getSemestre() , ' ', curso.getCreditos(), ' ', curso.getEstado())

print('--------------------------------------------------------------------------')
#ccsn = crudCursos.conteoCAS(5)
print('-------------------------------------------------------------------------')
#ccs = crudCursos.creditosSem(5)

#for curso in liscur:
 #   print(curso.getCodigo(),' ', curso.getNombre(), ' ', curso.getPrerrequisito() , ' ', curso.getObligatorio())

#ñprint(len(liscur))