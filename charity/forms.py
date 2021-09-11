from django import forms


class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')


class CustomUserRegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), label='')
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname'}), label='')
