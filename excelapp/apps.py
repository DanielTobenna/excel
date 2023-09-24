from django.apps import AppConfig


class ExcelappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'excelapp'

    def ready(self):
    	import excelapp.signals
