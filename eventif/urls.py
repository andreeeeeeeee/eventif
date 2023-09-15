from django.contrib import admin
from django.urls import path
from contact.views import contact
from core.views import home
from subscriptions.views import subscribe

urlpatterns = [
    path('', home),
    path('inscricao/', subscribe),
    path("contato/", contact, name = 'contact'),
    path("admin/", admin.site.urls),
]
