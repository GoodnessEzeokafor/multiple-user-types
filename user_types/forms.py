from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class BuyerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_buyer = True
        if commit:
            user.save()
        return user

class SellerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = True
        if commit:
            user.save()
        return user


