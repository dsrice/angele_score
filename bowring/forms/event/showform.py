from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput

from bowring.models import Event

class ShowForm(forms.Form):
    """
    新規投球作成画面
    """

    event = Event

    def __init__(self, event_id):
        super(ShowForm, self).__init__()
        self.event = Event.objects.get(id=event_id)
