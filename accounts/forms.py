from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder': 'abc@gmail.com'}))
    password1 = forms.CharField(label=("Password"),required=True)
    
    # # help_text=password_validation.password_validators_help_text_html(),

    password2 = forms.CharField(label=("Password confirmation"),required=True,widget=forms.PasswordInput,strip=False)
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        help_texts = {
            'username': None,
            'email': None,
            
            
        }