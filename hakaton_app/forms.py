from django import forms




class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя',
            }
        )
    )
    password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }
        )
    )

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя',
            }
        )
    )
    password = forms.CharField(
        label='Password',
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }
        )
    )
    password2 = forms.CharField(
        label='Repeat password',
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль',
            }
        )
    )
    first_name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }
        )
    )
    last_name = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }
        )
    )
    emale = forms.EmailField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'email',
            }
        )
    )

    def clean_password2(self):
        cd = self.data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class ProblemForm(forms.Form):
    lat = forms.FloatField(
        min_value=-90,
        max_value=90,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Широта',
            }
        )
    )
    lng = forms.FloatField(
        min_value=-180,
        max_value=180,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Долгота',
            }
        )
    )
    description = forms.CharField(
        max_length=1500,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Описание проблемы',
                "style": "height: 200px; width: 70%"
            }
        )
    )
    problem_type = forms.ChoiceField(
        required=True,
        choices=(
            ("1", "Общая проблема"),
            ("2", "Мусор"),
            ("3", "Яма на дороге"),
        )
    )
