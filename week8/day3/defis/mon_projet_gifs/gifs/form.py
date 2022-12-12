from django import forms
from .models import catégorie



class gifsForm(forms.Form):
    uploader_name = forms.CharField(
        required=False, 
        widget = forms.Textarea(
            attrs={
                 'placeholder': 'Entrer votre uploader_name ici'
            })
        )

    titre = forms.CharField(
        required=False, 
        widget = forms.Textarea(
            attrs={
                 'placeholder': 'Entrer votre titre ici'
            })
        )
    
    url = forms.URLField(
        required=False, 
        
        )

    
    category = forms.ModelMultipleChoiceField(queryset=catégorie.objects.all())

    # class Meta:
    #     model=Service
    #     fields='__all__'

class catégorieForm(forms.Form):
    nom = forms.CharField(
        required=False, 
        widget = forms.Textarea(
            attrs={
                 'placeholder': 'Entrer votre nom ici'
            })
        )