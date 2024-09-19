"""
O arquivo `models.py` em um projeto Django é crucial para a definição e a estruturação dos modelos de dados da
aplicação. Cada modelo representa uma tabela no banco de dados e é definido como uma classe que herda de
`django.db.models.Model`. Isso permite que você utilize a poderosa funcionalidade de ORM (Object-Relational Mapping)
do Django, que abstrai as interações com o banco de dados, permitindo que você escreva código Python em vez de
SQL diretamente.

Os atributos da classe definem os campos da tabela, e o Django converte estes atributos em colunas no banco de dados.
Você pode usar diversos tipos de campos como `CharField`, `IntegerField`, `DecimalField`, entre outros, para a
definição das propriedades de cada modelo. Além disso, o `models.py` permite implementar relacionamentos entre modelos,
como `ForeignKey`, `ManyToManyField`, e outros recursos que facilitam o gerenciamento dos dados.

Por exemplo, ao definir um modelo como este:

```python
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

A classe Cliente representa uma tabela com três colunas: nome, email e data_nascimento. O método __str__ é utilizado
para retornar uma representação legível do objeto, que é útil em interfaces administrativas ou quando você imprime
instâncias do modelo.

Em resumo, models.py é fundamental para a organização e a manipulação dos dados em um aplicativo Django, permitindo
criar, ler, atualizar e deletar registros de maneira eficiente e intuitiva em um banco de dados.
"""

import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Seviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome',  max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twiter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Recurso(Base):
    ICONE_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Notebook'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Camadas'),
    )
    recurso = models.CharField('Recurso', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.recurso


class Assinatura(Base):
    ICONE_CHOICES = (
        ('lni-package', 'Pacote'),
        ('lni-drop', 'Gota'),
        ('lni-star', 'Estrela'),
    )
    assinatura = models.CharField('Assinatura', max_length=100)
    preco = models.IntegerField('Preço', default=10)
    descricao_01 = models.CharField('Descrição', max_length=100)
    descricao_02 = models.CharField('Descrição', max_length=100)
    descricao_03 = models.CharField('Descrição', max_length=100)
    descricao_04 = models.CharField('Descrição', max_length=100)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Assinatura'
        verbose_name_plural = 'Assinaturas'

    def __str__(self):
        return self.assinatura


class Depoimento(Base):
    ICONE_CHOICES = (
        ('star-filled', 'Estrela Cheia'),
        ('star-half', 'Estrela Vazia'),
    )

    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': {'width': 200, 'height': 200, 'crop': True}},
                           null=True, blank=True)  # Permite valores nulos e que ele possa ser deixado vazio.
    nome = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=100)
    depoimento = models.TextField('Depoimento', max_length=100)

    # Campos para estrelas
    estrelas = models.IntegerField('Estrelas', choices=[(i, str(i)) for i in range(0, 6)], default=0)

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.nome
