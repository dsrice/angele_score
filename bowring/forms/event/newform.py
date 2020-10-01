from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput

class NewForm(forms.Form):
    """
    新規投球作成画面
    """

    name = forms.CharField()
    event_date = forms.DateField(widget=DateTimePickerInput())
