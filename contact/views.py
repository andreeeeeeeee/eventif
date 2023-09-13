from .form import ContactForm
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        formulario = ContactForm(request.POST)

        if formulario.is_valid():
            sender_email = formulario.cleaned_data['email']
            recipient_emails = [settings.DEFAULT_FROM_EMAIL, sender_email]
            subject = 'EventIF - Contato'
            message_body = render_to_string(
                'contact_email.txt', {'contact_data': formulario.cleaned_data})
            mail.send_mail(subject, message_body,
                           sender_email, recipient_emails)

            messages.success(request, 'Mensagem enviada!')
            return redirect('/contact/')
    else:
        formulario = ContactForm()

    return render(request, 'contact_form.html', {'form': formulario})
