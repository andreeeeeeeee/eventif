from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.conf import settings
from django.core import mail
from subscriptions.form import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        formulario = SubscriptionForm(request.POST)
        if formulario.is_valid():
            subject = 'Confirmação de inscrição'
            from_email = settings.DEFAULT_FROM_EMAIL
            email = formulario.cleaned_data['email']
            template_name = 'subscription_email.txt'
            context = formulario.cleaned_data

            body = render_to_string(template_name, context)
            mail.send_mail(subject, body, from_email, [from_email, email])

            messages.success(request, 'Inscrição realizada com sucesso!')
            return HttpResponseRedirect('/inscricao/')
    else:
        formulario = SubscriptionForm()

    return render(request, 'subscription_form.html', {'form': formulario})
