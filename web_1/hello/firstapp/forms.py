from django import forms

class UserForm(forms.Form):
 combo_text = forms.CharField(label="Введите URL", max_length=20)
