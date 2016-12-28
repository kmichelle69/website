from django import forms
from .models import NewRepairForm

class NameForm(forms.ModelForm):
    error_css_class = 'error'

    category = forms.ChoiceField(choices=NewRepairForm.CATEGORIES, required=True )

    class Meta:
        model = NewRepairForm
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'Title': 'description'}),
            'serial_number': forms.TextInput(attrs={'Title': 'Serial Number', 'required': True})
        }
