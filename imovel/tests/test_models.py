from django.test import TestCase

from model_mommy import mommy


class TestUsuario(TestCase):
    def setUp(self):
        self.models = mommy.make("imovel.Usuario")

    def test_str(self):
        self.assertEquals(str(self.models), self.models.nome)


class TestEndereco(TestCase):
    def setUp(self):
        self.models = mommy.make("imovel.Endereco")

    def test_str(self):
        self.assertEquals(
                str(self.models),
                "{}, {} - {}, {}".format(
                    self.models.logradouro,
                    self.models.numero,
                    self.models.cidade,
                    self.models.estado
                    )
                )

class TestImovel(TestCase):
    def setUp(self):
        self.models = mommy.make("imovel.Imovel")

    def test_str(self):
        self.assertEquals(
                str(self.models),
                "[{}], {} - {}".format(
                    self.models.CATEGORIAS[self.models.tipo].nome,
                    self.models.endereco.cidade,
                    self.models.endereco.estado
                    )
                )

    def test_preco_iptu(self):
        self.assertEquals(
                str(self.models.preco_iptu),
                "R$ {}".format(self.models.iptu)
                )

    def test_preco_condominio(self):
        self.assertEquals(
                str(self.models.preco_condominio),
                "R$ {}".format(self.models.condominio)
                )

    def test_preco_total(self):
        self.assertEquals(
                str(self.models.preco_total),
                "R$ {}".format(
                    self.models.condominio + self.models.iptu + self.models.aluguel
                    )
                )
