from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import List

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        # This is done to override the initially defined __init__ method of this class
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            'username',
            'email',
            'password1',
            'password2',
            Submit('submit', 'Register')
        )


class AddItemForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['movie_name', 'platform_name']

    def __init__(self, *args, **kwargs):
        # This is done to override the initially defined __init__ method of this class
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            'movie_name',
            'platform_name',
            Submit('submit', 'Submit')
        )
# for model = Post:
# When model = Post is used in the Meta class of a form, it means that the form is associated with a Django model called
# Post. This form is typically used to create, update, or delete instances of the Post model. It automatically generates
# form fields based on the fields defined in the Post model.