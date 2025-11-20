from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    eliminar_imagen = forms.BooleanField(required=False, label="Eliminar imagen")
    
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen']
