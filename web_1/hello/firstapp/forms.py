from django import forms
from .models import VideoFile # для работы с файлами видео
from .models import File # для работы с файлами
from .models import AudioFile # для работы с файлами аудио
from .models import Person
from .models import Image # для работы с изображениями

class ImageForm(forms.ModelForm):
 class Meta:
    model = Image
    fields = '__all__'
 # fields = ['title', 'image']

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


class UserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']


