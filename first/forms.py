from django.forms import ModelForm
from models import Medicament


class MedicamentForm(ModelForm):
	class Meta:
		model=Medicament
		exclude=("image",)


class SignUpForm(ModelForm):
    user_name = forms.CharField(max_length=128, help_text="Introduceti nume utilizator")
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(max_length=128, help_text="Introduceti email")
    first_name = forms.CharField(max_length=128, help_text="Introduceti prenume")
    last_name = forms.CharField(max_length=128, help_text="Introduceti nume")

    class Meta:
    	model=User

class LogInForm(ModelForm):
	user_name = forms.CharField(max_length=128, help_text="Introduceti nume utilizator")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
    	model=User
    	fields=('user_name', 'password',)    		


   

		