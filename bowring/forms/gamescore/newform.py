from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput

from bowring.models.events import Event


class NewForm(forms.Form):
    """
    新規投球作成画面
    """

    gamescore = None
    event_id = forms.CharField()
    gamecount = forms.IntegerField()
    framecount = forms.IntegerField()
    throwcount = forms.IntegerField()
