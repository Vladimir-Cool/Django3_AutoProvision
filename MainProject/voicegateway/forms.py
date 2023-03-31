from django.forms import ModelForm, TextInput, Select, NumberInput, ClearableFileInput
from django.core.exceptions import ValidationError

from .models import AudiocodesMP112, MainGateway, TypeGateway, LoginPasswordGW


class FormMainGateway(ModelForm):

    class Meta:
        model = MainGateway
        fields = ['name_gw', 'type', 'ip', 'mac']

        widgets = {
            'name_gw': TextInput(attrs={
                'class': 'form-control'
            }),
            'type': Select(attrs={
                'class': 'form-select'
            }),
            'ip': TextInput(attrs={
                'class': 'form-control'
            }),
            'mac': TextInput(attrs={
                'class': 'form-control'
            })
        }
#Валидация для MAC адреса нужно написать функцию
    #def clean_mac(self):


class FormTypeGateway(ModelForm):

    class Meta:
        model = TypeGateway
        fields = ['name_type', 'softswitch', 'ports', 'template_file']

        widgets = {
            'name_type': TextInput(attrs={
                'class': 'form-control'
            }),
            'softswitch': TextInput(attrs={
                'class': 'form-control'
            }),
            'ports': TextInput(attrs={
                'class': 'form-control'
            }),
            'template_file': ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }


class FormLoginPasswordGW(ModelForm):

    class Meta:
        model = LoginPasswordGW
        fields = ['login', 'password', 'gateway', 'number_ports']

        widgets = {
            'login': TextInput(attrs={
                'class': 'form-control'
            }),
            'password': TextInput(attrs={
                'class': 'form-control'
            }),
            'gateway': Select(attrs={
                'class': 'form-select'
            }),
            'number_ports': NumberInput(attrs={
                'class': 'form-control'
            })
        }



class FormAudiocodesMP112(ModelForm):

    class Meta:
        model = AudiocodesMP112
        fields = ['name', 'type', 'ip', 'mac', 'login1', 'password1', 'login2', 'password2', 'description']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'ip': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ip адресс'
            }),
            'type': Select(attrs={
                'class': 'form-select'
            }),
            'mac': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'MAC адресс'
            }),
            'login1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            'password1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
            'login2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            'password2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Коментарий'
            }),
        }


    def clean_name(self):
        new_name = self.cleaned_data['name'].lower()
        if new_name == 'create':
            raise ValidationError('"create" не допустимое Название')

        return new_name