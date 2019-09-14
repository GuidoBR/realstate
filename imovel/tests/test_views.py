from django.test import TestCase, RequestFactory
from django.urls import reverse

from model_mommy import mommy

from imovel.views import index, get

class TestView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.imovel_model = mommy.make("imovel.Imovel")


    def test_index(self):
        pass

    def test_get(self):
        pass
