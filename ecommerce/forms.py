from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'input100 ','placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100','placeholder':'Password'}))

class RegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'input100 ','placeholder':'Username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100 ','placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100 ','placeholder':'Password'}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class': 'input100 ','placeholder':'Confirm Password'}))
    account=forms.ChoiceField(choices=(('Buyer', 'Buyer'),('Seller','Seller')),widget=forms.Select(attrs={'class':'input100'}))
    
    def clean_username(self):
        username=self.cleaned_data.get("username")
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username already exists")
        return username
    
    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get("password")
        password2=self.cleaned_data.get("password2")
        if(password!=password2):
            raise forms.ValidationError("Passwords must match")
        else:
            return data
    