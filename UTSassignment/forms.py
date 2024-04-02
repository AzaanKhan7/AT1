# forms.py

from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class CategorySelectionForm(forms.Form):
    CATEGORIES = [
        ('sports', 'Sports'),
        ('gaming', 'Gaming'),
        ('art', 'Art'),
        ('music', 'Music'),
    ]
    categories = forms.MultipleChoiceField(
        label='Select Categories',
        choices=CATEGORIES,
        widget=forms.CheckboxSelectMultiple,
    )