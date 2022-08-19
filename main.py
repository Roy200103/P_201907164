from Curs import CRUD_Cursos

#from Curs import Curso
crudCursos = CRUD_Cursos()




#rut = input('ingrese ruta: ')
ca = crudCursos.leerCursos('Archivo de Prueba.LFP')

for curso in ca:
    print(curso.getCodigo(),' ', curso.getNombre(), ' ', curso.getObligatorio())


