from django.apps import AppConfig

class RegistersConfig(AppConfig):
    name = 'registers'

from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'