from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class MailTest(TestCase):
    def setUp(self):
        data = dict(name="andre",
                    cpf="381.247.492-16",
                    email="andre.souza@aluno.riogrande.ifrs.edu.br",
                    phone="53 981426326")

        self.response = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_sender(self):
        expect = "contato@eventif.com.br"
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventif.com.br', 'andre.souza@aluno.riogrande.ifrs.edu.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['andre',
                    '381.247.492-16',
                    'andre.souza@aluno.riogrande.ifrs.edu.br',
                    '53 981426326']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
