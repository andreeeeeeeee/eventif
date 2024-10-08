from datetime import datetime
from django.test import TestCase
from subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="andre",
            cpf="381.247.492-16",
            email="andre.souza@aluno.riogrande.ifrs.edu.br",
            phone="53 981426326"
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('andre', str(self.obj))

    def test_paid_default_false(self):
        self.assertEqual(False, self.obj.paid)
