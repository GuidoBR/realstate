from csv import DictReader
from datetime import datetime
from pytz import UTC
from django.core.management import BaseCommand, CommandError
from imovel.models import Usuario, Endereco, Servico, Imovel, Foto, Meta, Video, Locacao, Propriedade


ALREADY_LOADED_ERROR = """ 
If you need to reload the Imovel data from the CSV file,
first destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from legacy_database.csv into the new models"

    def handle(self, *args, **options):
        try:
            if Imovel.objects.exists():
                print("Imovel data already loaded ... exiting")
                print(ALREDY_LOADED_ERROR)
                return
            
            print("Creating Imovel data...")
            for row in DictReader(open('./legacy_database.csv')):
                imovel = Imovel()
                imovel.descricao = row['descricao']
                imovel.breve_descricao = row['breve_descricao']
                imovel.quantidade_quartos = row['quantidade_quartos']
                imovel.area = row['area']
                imovel.garagem = row['garagem']
                imovel.tipo = row['tipo']
                imovel.iptu = row['iptu']
                imovel.aluguel = row['aluguel']
                imovel.condominio = row['condominio']
                imovel.destaque = row['destaque']

                imovel.save()
        except:
            raise CommandError("Something went wrong here")
