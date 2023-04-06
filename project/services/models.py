from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to= 'services')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True, verbose_name="Modificado")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']