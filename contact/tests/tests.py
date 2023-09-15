from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.template.loader import render_to_string
from contact.form import ContactForm

# Create your tests here.


class testeGet(TestCase):

    def test_pagina_inicial(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)


class testePostValido(TestCase):

    def test_post_valido(self):
        data = {
            'name': 'andre',
            'cpf': '381.247.492-16',
            'email': 'andre.souza@aluno.riogrande.ifrs.edu.br',
            'phone': '53 981426326'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)


class testePostInvalido(TestCase):

    def test_post_invalido(self):
        data = {
            'name': '',
            'cpf': '381.247.492-16',
            'email': 'andre.souza@aluno.riogrande.ifrs.edu.br',
            'phone': '53 981426326'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'name',
                             'This field is required.')


class testeEmail(TestCase):
    def test_envio_email(self):
        mail.send_mail(
            'Confirmação de inscrição',
            'corpo',
            'contato@eventif.com.br',
            ['andre.souza@aluno.riogrande.ifrs.edu.br'],
            fail_silently=False,
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Confirmação de inscrição')
