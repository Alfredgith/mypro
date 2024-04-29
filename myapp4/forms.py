from django import forms
from .models import has

class myhas(forms.ModelForm):
      class Meta:
            model=has
            fields='__all__'

