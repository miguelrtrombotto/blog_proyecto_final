from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del post'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido del post', 'rows': 5}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }
