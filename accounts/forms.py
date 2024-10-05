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
        
        labels = {
            "username": "Choose a username",
            "email": "Enter your email address",
            "profile_pic": "Upload your profile picture",
            "bio": "Tell us a bit about yourself",
        }
        help_texts = {
            "username": "Required. 150 characters or fewer.",
            "email": "Required. A valid email address.",
            "bio": "Optional. Maximum 500 characters.",
        }
        widgets = {
            "username": forms.TextInput(attrs={"class":"username1"}),
            "email": forms.EmailInput(attrs={"class":" username1"}),
            "bio": forms.Textarea(attrs={"rows": 5, "cols": 50, "class": "form-control username1"}),
        }

        


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "profile_pic",
            "bio",
        )
    
