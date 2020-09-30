from django import forms


class HomeForm(forms.Form):
    """
    ホーム画面
    """
    email = forms.EmailField(label="メールアドレス")
