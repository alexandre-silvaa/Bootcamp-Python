from django import forms
from .models import User

# modelForm - form baseado na model

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome','telefone','email'] 

# form.Form