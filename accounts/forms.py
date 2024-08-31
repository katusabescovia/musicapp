# from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = get_user_model()
        model = CustomUser
        fields = (
            "username",
            "email",
            "profile_pic",
            "password1",
            "password2",
            "bio",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta():
        model = CustomUser
        fields =  (
            "username",
            "email",
            "profile_pic",
            "bio",
        )


