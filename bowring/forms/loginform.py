from django import forms


class LoginForm(forms.Form):
    """
    ログイン画面
    """
    loginid = forms.CharField(label="ユーザ名")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)
