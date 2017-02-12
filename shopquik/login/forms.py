from django.forms import ModelForm
from django import forms
from login.models import Item, User


class UserForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    # username = forms.CharField(max_length=30)
    email = forms.EmailField(widget=forms.EmailInput,label="email")
    password = forms.CharField(widget=forms.PasswordInput,label="password")

    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'password']

class SignInForm(forms.Form):
    """
    Login form
    """
    email = forms.EmailField(widget=forms.widgets.TextInput)
    # password1 = forms.CharField(widget=forms.widgets.PasswordInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        # fields = ['email', 'password1']
        fields = ['email', 'password']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_name']
