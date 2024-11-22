from .forms import UserForm
from django.shortcuts import redirect, render
from django.http import *
from .models import Person, File, AudioFile, Image, VideoFile
from .forms import FileForm, VideoForm, AudioForm, ImageForm


def form_up_img(request):
 if request.method == 'POST':
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
    form.save()
 my_text = 'Загруженные изображения'
 my_img = Image.obj_img.all()
 form = ImageForm()
 context = {'my_text': my_text, "my_img": my_img, "form": form}
 return render(request, 'firstapp/form_up_img.html', context)

def delete_img(request, id):
 try:
  img = Image.obj_img.get(id=id)
  img.delete()
  return redirect('form_up_img')
 except Person.DoesNotExist:
  return HttpResponseNotFound("<h2>Объект не найден</h2>")

def index(request):
 my_text = 'Изучаем модели Django'
 people_kol = Person.object_person.count()
 context = {'my_text': my_text, "people_kol": people_kol}
 return render(request, "firstapp/index.html", context)

def my_form(request):
 if request.method == "POST": # пользователь отправил данные
  form = UserForm(request.POST) # создание экземпляра формы
  if form.is_valid(): # проверка валидности формы
   form.save() # запись данных в БД
 # остаемся на той же странице, обновляем форму
 # Загрузить форму для ввода клиентов
 my_text = 'Сведения о клиентах'
 people = Person.object_person.all()
 form = UserForm()
 context = {'my_text': my_text, "people": people, "form": form}
 return render(request, "firstapp/my_form.html", context)


def form_up_audio(request):
 if request.method == 'POST':
  form = AudioForm(request.POST, request.FILES)
  if form.is_valid():
    form.save()
 my_text = 'Загруженные аудио файлы'
 form = AudioForm()
 file_obj = AudioFile.obj_audio.all()
 context = {'my_text': my_text, "file_obj": file_obj, "form": form}
 return render(request, 'firstapp/form_up_audio.html', context)


def delete_audio(request, id):
 try:
  audio = AudioFile.obj_audio.get(id=id)
  audio.delete()
  return redirect('form_up_audio')
 except Person.DoesNotExist:
  return HttpResponseNotFound("<h2>Объект не найден</h2>")

def form_up_video(request):
 if request.method == 'POST':
  form = VideoForm(request.POST, request.FILES)
  if form.is_valid():
    form.save()
 my_text = 'Загруженные видео файлы'
 form = VideoForm()
 file_obj = VideoFile.obj_video.all()
 context = {'my_text': my_text, "file_obj": file_obj, "form": form}
 return render(request, 'firstapp/form_up_video.html', context)


def delete_video(request, id):
 try:
  video = VideoFile.obj_video.get(id=id)
  video.delete()
  return redirect('form_up_video')
 except Person.DoesNotExist:
  return HttpResponseNotFound("<h2>Объект не найден</h2>")




def form_up_pdf(request):
 if request.method == 'POST':
  form = FileForm(request.POST, request.FILES)
  if form.is_valid():
    form.save()
 my_text = 'Загруженные файлы'
 form = FileForm()
 file_obj = File.objects.all()
 context = {'my_text': my_text, "file_obj": file_obj, "form": form}
 return render(request, 'firstapp/form_up_pdf.html', context)
# удаление файлов из БД
def delete_pdf(request, id):
 try:
  pdf = File.objects.get(id=id)
  pdf.delete()
  return redirect('form_up_pdf')
 except Person.DoesNotExist:
  return HttpResponseNotFound("<h2>Объект не найден</h2>")
 
def edit_form(request, id):
 person = Person.object_person.get(id=id)
 # Если пользователь вернул отредактированные данные
 if request.method == "POST":
  person.name = request.POST.get("name")
  person.age = request.POST.get("age")
  person.save()
  return redirect('my_form')
 # Если пользователь отправляет данные на редактирование
 data = {"person": person}
 return render(request, "edit_form.html", context=data)

def delete(request, id):
 try:
  person = Person.object_person.get(id=id)
  person.delete()
  return redirect('my_form')
 except Person.DoesNotExist:
  return HttpResponseNotFound("<h2>Объект не найден</h2>")







def about(request):
 return HttpResponse("<h2>О сайте</h2>")

def contact(request):
 return HttpResponse("<h2>Koнтaкты</h2>")






def about(request):
 return HttpResponse("About")

def contact(request):
 return HttpResponseRedirect("/About")

def details(request):
 return HttpResponsePermanentRedirect("/")




def index(request):
 if request.method == "POST":
    name = request.POST.get("name") # получить значения поля Имя
    age = request.POST.get("age") # значения поля Возраст
    output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст – {1}</h3>".format(name, age)
    return HttpResponse(output)
 else:
    userform = UserForm()
    return render(request, "my_form.html", {"form": userform})
 

def index(request):
 userform = UserForm()
 if request.method == "POST":
   userform = UserForm(request.POST)
   if userform.is_valid():
      name = userform.cleaned_data["name"]
      return HttpResponse("<h2>Имя введено коррректно –{0}</h2>".format(name))
 return render(request, "firstapp/index.html", {"form": userform})



