from django.shortcuts import render


def subscribe(request):
    if request.method == 'POST':
        return render(request, "subscriptions/subscription_form.html")
        # se for inscrever lidar cm isso
    else:
        return render(request, "subscriptions/subscription_form.html")
