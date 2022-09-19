from django import forms

class CalculateForm(forms.Form):
    field1 = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
    field2 = forms.CharField(required=True, max_length=500, min_length=3, strip=True)