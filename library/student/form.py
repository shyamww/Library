from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db import transaction


from account.models import Student,User
from account.models import branch,year_choice


class UpdateProfile(forms.Form):
    First_name = forms.CharField(required=False)
    Last_name = forms.CharField(required=False)
    Email = forms.EmailField(required=False)
    Branch = forms.ChoiceField(required=False, choices=branch)
    RollNo = forms.CharField(required=False)
    MobileNo = forms.CharField(max_length=12)
    ProfilePicture = forms.ImageField(required=False)





# class ProfilePictureChangeForm(forms.Form):
#     UpdateProfilePicture = forms.ImageField(required=True)
