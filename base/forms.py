# base/forms.py

from django import forms
from .models import UserDetail

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['first_name', 'mid_name', 'last_name', 'country', 'about_you', 'projects', 'skills', 'experience', 'interests', 'phone_number']
