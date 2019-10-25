from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _


class RegistrationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("Пароли не совпадают."),
    }
    username = forms.CharField(label=_("Имя пользователя:"))
    password1 = forms.CharField(label=_("Придумайте пароль:"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Подтвердите пароль:"),
                                widget=forms.PasswordInput,
                                help_text=_("Выедите тот же пароль, что и ранее."))


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Имя пользователя:"))
    password = forms.CharField(label=_("Пароль:"), widget=forms.PasswordInput)