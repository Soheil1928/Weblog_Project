from django import forms
from django.contrib.auth.models import User
from blog_app.models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'password1', 'password2', 'first_name', 'last_name' , 'email']
        
    # البته به روش فرم قسمت بلاگ هم میشه ویجت ها رو تعریف کرد
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'


class EditRegisterForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name' , 'email', 'last_login', 'is_active', 'date_joined']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
        }