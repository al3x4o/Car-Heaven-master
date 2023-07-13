from django import forms
from django.forms import TextInput, PasswordInput, NumberInput

from car_collection.web.models import Car
from car_collection.accounts.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username','first_name', 'last_name', 'email', 'age', 'password')
        labels = {
            "username": "Username",
            "last_name": "Last Name",
            "password": "Password"
        }
        widgets = {
            "username": TextInput(attrs={'placeholder': 'Username', 'autocomplete': 'off'}),
            "first_name": TextInput(attrs={'placeholder': 'First Name', 'autocomplete': 'off'}),
            "last_name": TextInput(attrs={'placeholder': 'Last Name(Optional)', 'autocomplete': 'off'}),
            "email": TextInput(attrs={'placeholder': 'Email', 'autocomplete': 'on'}),
            "age": NumberInput(attrs={'placeholder': 'Age', 'autocomplete': 'on'}),
            "password": PasswordInput(
                attrs={'placeholder': 'Password', 'autocomplete': 'off', 'data-toggle': 'password'}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(ProfileCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Car.objects \
                .all() \
                .delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
