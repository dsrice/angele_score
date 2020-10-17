from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput

from bowring.models.events import Event
class NewForm(forms.Form):
    """
    新規投球作成画面
    """

    name = forms.CharField()
    event_date = forms.DateField(widget=DateTimePickerInput(format="%Y-%m-%d"))
    id = forms.IntegerField(required=False)

    def edit(self, event_id=None):
        super(NewForm, self).__init__()
        if event_id:
            event = Event.objects.get(id=event_id)
            self.fields["name"].initial = event.name
            self.fields["event_date"].initial = event.event_date
            self.fields["id"].initial = event.id