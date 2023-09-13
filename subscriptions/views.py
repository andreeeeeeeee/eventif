from django.template.loader import render_to_string
from subscriptions.form import SubscriptionForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.conf import settings
from django.core import mail


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subject = 'Confirmação de inscrição'
            from_email = settings.DEFAULT_FROM_EMAIL
            email = form.cleaned_data['email']
            template_name = 'subscriptions/subscription_email.txt'
            context = form.cleaned_data

            body = render_to_string(template_name, context)
            mail.send_mail(subject, body, from_email, [from_email, email])

            messages.success(request, 'Inscrição realizada com sucesso!')
            return HttpResponseRedirect('/inscricao/')
    else:
        form = SubscriptionForm()

    return render(request, 'subscriptions/subscription_form.html', {'form': form})
