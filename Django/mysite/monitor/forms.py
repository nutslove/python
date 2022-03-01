from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(labed='mail')
    age = forms.IntegerField(labed='age')