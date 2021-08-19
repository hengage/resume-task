from django import forms
from django.forms import widgets


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        error_messages={'required': 'Please enter your name'},
        widget=forms.TextInput(attrs={'placeholder':'your name'})
        )

    subject = forms.CharField(
        max_length=255,
         required=False,
         widget=forms.TextInput(attrs={'placeholder':'subject'})
         )
    senders_email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'email'})
        )

    message = forms.CharField(
    required=True,
    widget=forms.Textarea(attrs={'placeholder':'message', 'rows':18})
        )



    