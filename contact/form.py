from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nome")
    phone = forms.CharField(label="Telefone")
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)