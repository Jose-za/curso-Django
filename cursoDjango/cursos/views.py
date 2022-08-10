from django.shortcuts import render, get_object_or_404
from .models import Cursos
from cursos.forms import cursosForms

# Create your views here.
def cursos(request):
    cursos=Cursos.objects.all()
    return render(request, "cursos/principal.html", {'cursos':cursos})
#Indicamos el lugar donde se renderizará el resultado de esta vista

# Eliminar Curso
def eliminarCurso(request, i,
    confirmacion='cursos/eliminarCurso.html'):
    curso = get_object_or_404(Cursos, i=i)
    if request.method=='POST':
        curso.delete()
        cursos=Cursos.objects.all()
        return render(request,"cursos/principal.html",
            {'cursos':cursos})
    return render(request, confirmacion, {'object':curso})

# Editar

def consultarCurso(request, i):
    curso = Cursos.objects.get(i=i)
    return render(request, 'cursos/editarCurso.html', {'curso': curso})

def editarCurso(request, i):
    curso = get_object_or_404(Cursos, i=i)
    form = cursosForms(request.POST, instance=curso)
    
    if form.is_valid():
        form.save()
        cursos = Cursos.objects.all()
        return render(request, 'cursos/principal.html', {'cursos': cursos})
    return render(request, 'cursos/editarCurso.html', {'curso':curso })
