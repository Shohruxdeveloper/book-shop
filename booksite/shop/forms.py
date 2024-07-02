from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Books, Category

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))

    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Confirm Password"}))
    user_role = forms.Select(attrs={'class': "form-control"})

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'password', 'confirm_password', 'user_role')

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return password


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))
    address = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Address"}))
    email = forms.EmailField(widget=forms.TextInput({"class": "form-control", "placeholder": "Email"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control", "placeholder": "Image"}))

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'address', 'email', 'image')


class User_registerForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))

    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'first_name', 'last_name', 'password', 'confirm_password')

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return password


class CreateBookForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput({"class":"form-control","placeholder":"nomi"}))
    description = forms.CharField(widget=forms.Textarea({"class":"form-control","placeholder":"Matni"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
    price = forms.DecimalField(widget=forms.NumberInput({"class": "form-control"}))
    quantity = forms.IntegerField(widget=forms.NumberInput({"class": "form-control"}))
    class Meta:
        model = Books
        fields = ('name', 'author', 'price','quantity','image','description','category')


class UsersEditForm(forms.ModelForm):
    user_role = forms.CharField(widget=forms.Select(choices=User.USER_ROLE_CHOICES, attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ['user_role']






