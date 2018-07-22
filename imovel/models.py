from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    ADMIN = 1
    OPERADOR = 2
    LOCATARIO = 3
    PROPRIETARIO = 4
    OUTROS = 5

    USERS_ROLES = (
            (ADMIN, 'Administrador'),
            (OPERADOR, 'Operador'),
            (LOCATARIO, 'Locatario'),
            (PROPRIETARIO, 'Proprietario'),
            (OUTROS, 'Outros')
            )

    nome = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=2, choices=USERS_ROLES, default=OUTROS)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Usuarios'
        get_latest_by = "created_at"


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {} - {}, {}".format(
                self.logradouro,
                self.numero,
                self.cidade,
                self.estado
                )

    class Meta:
        db_table = 'Enderecos'
        get_latest_by = "created_at"


class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="servicos/")
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Servicos'
        get_latest_by = "created_at"

class Imovel(models.Model):
    APARTAMENTO = 1
    CASA = 2
    SALA = 3
    LOJA = 4

    TIPO_IMOVEL = (
            (0, ''),
            (APARTAMENTO, 'APARTAMENTO'),
            (CASA, 'CASA'),
            (SALA, 'SALA'),
            (LOJA, 'LOJA')
            )
    descricao = models.TextField()
    breve_descricao = models.CharField(max_length=255)
    quantidade_quartos = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    garagem = models.IntegerField(default=0)
    tipo = models.IntegerField(choices=TIPO_IMOVEL, default=CASA)
    iptu = models.DecimalField(max_digits=8, decimal_places=2)
    condominio = models.DecimalField(max_digits=8, decimal_places=2)
    destaque = models.BooleanField(default=False)

    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    locatario = models.ManyToManyField(Usuario, through='Locacao')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "[{}] - ".format(self.TIPO_IMOVEL[self.tipo][1], self.endereco)

    @property
    def iptu(self):
        return "R$ {}".format(self.iptu)

    @property
    def condominio(self):
        return "R$ {}".format(self.condominio)

    class Meta:
        db_table = 'Imoveis'
        get_latest_by = "created_at"


class Foto(models.Model):
    def get_upload_path(self, filename):
        return os.path.join('imoveis',
                self.imovel,
                now().date().strftime("%Y_%m_%d_%H_%M_%s"),
                filename
                )

    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to=get_upload_path)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Fotos'
        get_latest_by = "created_at"


class Video(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Videos'
        get_latest_by = "created_at"

class Locacao(models.Model):
    TEMPORADA = 1
    COMERCIAL = 2
    RESIDENCIAL = 3

    TIPO_LOCACAO = (
            (TEMPORADA, 'ALUGUEL-POR-TEMPORADA'),
            (COMERCIAL, 'ALUGUEL-COMERCIAL'),
            (RESIDENCIAL, 'ALUGUEL-RESIDENCIAL')
            )
    tipo_locacao = models.IntegerField(choices=TIPO_LOCACAO, default=RESIDENCIAL)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    locador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def preco(self):
        return "R$ {}".format(self.preco)

    def __str__(self):
        return 'Imóvel em {} alugado para {}'.format(self.imovel, self.locatario)

    class Meta:
        db_table = 'Locacoes'
        get_latest_by = "created_at"


class Propriedade(models.Model):
    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Propriedade'
        get_latest_by = "created_at"
