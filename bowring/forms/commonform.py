from django import forms

class CommonForm(forms.Form):
    username = forms.CharField()

