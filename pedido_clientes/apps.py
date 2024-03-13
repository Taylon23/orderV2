# pedido_clientes/apps.py
from django.apps import AppConfig

class PedidoClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pedido_clientes'

    def ready(self):
        import pedido_clientes.signals  # Importa os sinais quando o aplicativo estiver pronto
