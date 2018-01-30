# Register your models here.
#Vamos a editar admin para poder acceder

from django.contrib import admin
from .models import Post

admin.site.register(Post)

# luego vamos a ejecutar en la consola para que corrar el servidor web

