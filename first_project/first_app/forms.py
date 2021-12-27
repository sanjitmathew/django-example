from django import forms
from .models import WebPage, UserInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    """ Model form for inbuilt user details """

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserInfoForm(forms.ModelForm):
    """ Model form for storing picture """

    class Meta:
        model = UserInfo
        fields = ('pic',)


class WebForm(forms.ModelForm):
    """ Form to fill in web pages """

    class Meta:
        model = WebPage
        fields = '__all__'


class LoginForm(forms.Form):
    """ Form for login page """

    user_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    reenter_password = forms.CharField(
                                        label='Reenter the password',
                                         widget=forms.PasswordInput()
                                         )
