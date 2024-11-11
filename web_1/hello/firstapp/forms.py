from django import forms

from .models import File # для работы с файлами
class FileForm(forms.ModelForm):
 class Meta:
    model = File
    fields = '__all__'


class UserForm(forms.Form):
 name = forms.CharField(label="Имя клиента",
 widget=forms.TextInput(attrs={"class": "myfield"}))
 age = forms.IntegerField(label="Возраст клиента",
 widget=forms.NumberInput(attrs={"class": "myfield"}))
