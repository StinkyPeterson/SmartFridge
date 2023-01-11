from django import forms
from .models import Images
class ScanForm(forms.Form):
    qrcode_string = forms.CharField()

class ScanImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image']