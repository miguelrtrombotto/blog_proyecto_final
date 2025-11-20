from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_creacion', 'fecha_actualizacion']
    search_fields = ['titulo', 'contenido']
    list_filter = ['fecha_creacion', 'fecha_actualizacion']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
