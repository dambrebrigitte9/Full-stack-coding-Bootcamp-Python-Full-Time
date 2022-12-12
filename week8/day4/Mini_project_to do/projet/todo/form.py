from django import forms
from .models import categorie

class TodoForm(forms.Form):
    title = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'placeholder': 'votre titre'
                })
            )

    uploader_name = forms.CharField(
            widget = forms.Textarea(
                attrs={
                    'placeholder': 'votre nom'
                })
            )

    date_completion = forms.DateField(label="",input_formats=['%d/%m/%Y'],required=False,widget= forms.TextInput(attrs={'placeholder':'31/12/2000'}))
    deadline_date = forms.DateField(label="",input_formats=['%d/%m/%Y'],required=False,widget= forms.TextInput(attrs={'placeholder':'31/12/2000'}))


    
    category = forms.ModelMultipleChoiceField(queryset=categorie.objects.all())
    has_been_done = forms.BooleanField()