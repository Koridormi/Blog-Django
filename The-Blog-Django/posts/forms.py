from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titulo',
            'description': 'Descripción',
            'image': 'Imagen'
        }
        help_texts = {
            'image': 'Opcional. Selecciona una imagen de hasta 5 MB.'
        }
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'})
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image and image.size > 5_000_000:
            raise forms.ValidationError('La imagen no puede superar los 5 MB.')

        return image