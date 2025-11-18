from django import forms

class AdditionForm(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()


class Bf(forms.Form):
    n=forms.IntegerField()
    height=forms.IntegerField()
    weight=forms.IntegerField()

class SignupForms(forms.Form):
    name=forms.CharField()
    psw=forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField()
    phone=forms.IntegerField()
    add=forms.CharField(widget=forms.Textarea)
    gender_choices=(('male','Male'),('female','Female'))
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)