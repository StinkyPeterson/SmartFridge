from django import forms

class ScanForm(forms.Form):
    qrcode_string = forms.CharField()