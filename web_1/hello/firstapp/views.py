from .forms import UserForm
from django.shortcuts import redirect, render
from django.http import *
from .models import Person
from .models import File
from .forms import FileForm





# загрузка аудио файлов
# def form_up_audio(request):
#  if request.method == 'POST':
#   form = AudioForm(request.POST, request.FILES)
#   if form.is_valid():
#     form.save()
#  my_text = 'Загруженные аудио файлы'
#  form = AudioForm()
#  file_obj = AudioFile.obj_audio.all()
#  context = {'my_text': my_text, "file_obj": file_obj, "form": form}
#  return render(request, 'firstapp/form_up_audio.html', context)
# # удаление аудио файлов из БД
# def delete_audio(request, id):
#   try:
#     audio = AudioFile.obj_audio.get(id=id)
#     audio.delete()
#     return redirect('form_up_audio')
#   except Person.DoesNotExist:
#     return HttpResponseNotFound("<h2>Объект не найден</h2>")
# # загрузка видео файлов
# def form_up_video(request):
#  if request.method == 'POST':
#   form = VideoForm(request.POST, request.FILES)
#   if form.is_valid():
#     form.save()
#  my_text = 'Загруженные видео файлы'
#  form = VideoForm()
#  file_obj = VideoFile.obj_video.all()
#  context = {'my_text': my_text, "file_obj": file_obj, "form": form}
#  return render(request, 'firstapp/form_up_video.html', context)
# удаление видео файлов из БД
# def delete_video(request, id):
#   try:
#     video = VideoFile.obj_video.get(id=id)
#     video.delete()
#     return redirect('form_up_video')
#   except Person.DoesNotExist:
#    return HttpResponseNotFound("<h2>Объект не найден</h2>")
# загрузка файлов pdf
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
 
def edit_form(request):
 my_form = UserForm()
 context = {"form": my_form}
 return render(request, "firstapp/my_form.html", context)

def my_form(request):
 my_form = UserForm()
 context = {"form": my_form}
 return render(request, "firstapp/my_form.html", context)





def about(request):
 return HttpResponse("<h2>О сайте</h2>")

def contact(request):
 return HttpResponse("<h2>Koнтaкты</h2>")

def products(request, productid=1):
 output = "<h2>Продукт № {0}</h2>".format(productid)
 return HttpResponse(output)

def users(request, id=1, name='Максим'):
 output = "<h2>Пользователь</h2><h3>id: {0}. Имя: {1}</h3>".format(id, name)
 return HttpResponse(output)



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
    return render(request, "firstapp/index.html", {"form": userform})
 

def index(request):
 userform = UserForm()
 if request.method == "POST":
   userform = UserForm(request.POST)
   if userform.is_valid():
      name = userform.cleaned_data["name"]
      return HttpResponse("<h2>Имя введено коррректно –{0}</h2>".format(name))
 return render(request, "firstapp/index.html", {"form": userform})



def create(request):
 if request.method == "POST":
  klient = Person()
  klient.name = request.POST.get("name")
  klient.age = request.POST.get("age")
  klient.save()
 return HttpResponseRedirect("/")

def edit(request, id):
 try:
  person = Person.objects.get(id=id)

  if request.method == "POST":
   person.name = request.POST.get("name")
   person.age = request.POST.get("age")
   person.save()
   return HttpResponseRedirect("/")
  else:
   return render(request, "edit.html", {"person": person})
 except Person.DoesNotExist:
   return HttpResponseNotFound("<h2>Клиент не найден</h2>")
 
def delete(request, id):
 try:
   person = Person.objects.get(id=id)
   person.delete()
   return HttpResponseRedirect("/")
 except Person.DoesNotExist:
   return HttpResponseNotFound("<h2>Клиент не найден</h2>")