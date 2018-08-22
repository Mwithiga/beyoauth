from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
	username = forms.CharField(label="username")
	password = forms.CharField(label= "password", widget=forms.PasswordInput)


# class UserRegistrationForm(forms.ModelForm):
# 	email = forms.EmailField(max_length=200, help_text='Required')
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         #From User fields
#         fields = ('username', 'first_name', 'email')

    

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
   
    def clean(self):
    	if 'password' in self.cleaned_data and 'password1' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['password1']:
    		raise forms.ValidationError("The password does not match ")
    	return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1')

   