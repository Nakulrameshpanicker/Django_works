from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app1.models import Custom

class RegisterForm(UserCreationForm):
    roles=(('student','Student'),('teacher','Teacher'))
    role=forms.ChoiceField(choices=roles)
    class Meta:
        model = Custom
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name','phone','role']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = ''


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()