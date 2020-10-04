from django import forms

from bowring.models import Event

class HomeForm(forms.Form):
    """
    ホーム画面
    """
    email = forms.EmailField(label="メールアドレス")
    events = Event.objects.all()