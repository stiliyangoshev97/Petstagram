from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

UserModel = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())


    def clean_password(self):
        self.user = authenticate(
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Wrong email or password!')

    def save(self):
        return self.user


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email",)



