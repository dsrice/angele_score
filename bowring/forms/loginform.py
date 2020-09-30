from django import forms


class LoginForm(forms.Form):
    """
    ログイン画面
    """
    email = forms.EmailField(label="メールアドレス")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)
