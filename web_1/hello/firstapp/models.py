from django.db import models

class File(models.Model):
 title = models.CharField(max_length=100,
 verbose_name="Описание файла",)
 file = models.FileField(upload_to='files',
 verbose_name="Файл PDF",
 null=True, blank=True)
 def __str__(self):
    return self.title


class Person(models.Model):
 name = models.CharField(max_length=20, verbose_name="Имя клиента")
 age = models.IntegerField(verbose_name="Возраст клиента")
 objects = models.Manager()
 DoesNotExist = models.Manager

class Company(models.Model):
 name = models.CharField(max_length=30)
 
class Product(models.Model):
 company = models.ForeignKey(Company, on_delete=models.CASCADE)
 name = models.CharField(max_length=30)
 price = models.IntegerField()

class User(models.Model):
 name = models.CharField(max_length=20)

class Account(models.Model):
 login = models.CharField(max_length=20)
 password = models.CharField(max_length=20)
 user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)



# Create your models here.
