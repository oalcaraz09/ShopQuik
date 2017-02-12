from django.forms import ModelForm
from shopquik.models import User
from shopquik.models import Item

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name']
