from django import forms
from .models import VideoFile # для работы с файлами видео
from .models import File # для работы с файлами
from .models import AudioFile # для работы с файлами аудио

class AudioForm(forms.ModelForm):
 class Meta:
    model = AudioFile
    fields = '__all__'

class FileForm(forms.ModelForm):
 class Meta:
    model = File
    fields = '__all__'


class VideoForm(forms.ModelForm):
 class Meta:
    model = VideoFile
    fields = '__all__'


class UserForm(forms.Form):
 name = forms.CharField(label="Имя клиента",
 widget=forms.TextInput(attrs={"class": "myfield"}))
 age = forms.IntegerField(label="Возраст клиента",
 widget=forms.NumberInput(attrs={"class": "myfield"}))
