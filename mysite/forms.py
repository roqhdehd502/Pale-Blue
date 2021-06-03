from django.contrib.auth.forms import UserCreationForm
# 장고의 유저 관련 내장 모델
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username',
                'password1',
                'password2',
                'email',
                'first_name',
                'last_name'
                ]