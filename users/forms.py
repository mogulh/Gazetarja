from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    termat_dhe_kushtet_e_perdorimit = forms.BooleanField()

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("Emaili i shënuar është aktualisht i regjistruar ")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'termat_dhe_kushtet_e_perdorimit']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'gjinia', 'ditlindja']
        widgets = {
        'ditlindja': DateInput(attrs={'type': 'date'})
    }