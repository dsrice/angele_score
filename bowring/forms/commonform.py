from django import forms


class CommonForm(forms.Form):
    api_token = forms.CharField()
