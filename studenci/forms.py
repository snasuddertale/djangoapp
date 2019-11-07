from django import forms

class UserLoginForm(forms.Form):
    login = forms.CharField(
        label="Twój login",
        max_length=(20),
        widget=forms.TextInput()
    )

class UserUczelniaForm(forms.Form):
    nazwa = forms.CharField(
        label="Twoja uczelnia",
        max_length=(40),
        widget=forms.TextInput()
    )