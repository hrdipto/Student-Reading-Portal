from django import forms

class Userform(forms.Form):
    username= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control form-control-user',
				   'id':'exampleInputUsername', 'placeholder': 'Enter Email Address...'}))
    password= forms.CharField(max_length=100,
                           widget= forms.PasswordInput
                           (attrs={'class':'form-control form-control-user',
				   'id':'exampleInputPassword', 'placeholder': 'Password'}))
