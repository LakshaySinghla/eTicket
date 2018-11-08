from django import forms

class SignupForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100)
	email = forms.EmailField(label = 'Email',max_length=100)
	password = forms.CharField(label='Password', max_length=100)
	cpassword = forms.CharField(label='Confirm Password', max_length=100)

class LoginForm(forms.Form):
	email = forms.CharField(label='Email Id', max_length=100)
	password = forms.CharField(label='Password', max_length=100)