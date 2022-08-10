from django.utils import timezone
from django.db import models

# Create your models here.
class Cursos(models.Model):
    i = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.TextField(max_length=20,verbose_name="Nombre completo")
    curso = models.TextField(max_length=20,verbose_name="Nombre del curso")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    email = models.EmailField(max_length=200,verbose_name="Correo Electrónico")
    tiempo = models.BooleanField(verbose_name="Deseas obtener el curso intensivo")
    fecha = models.DateField(
        default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)#Fecha y tiempo
    update = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
    
    def __str__(self):
        return self.curso