from django.apps import AppConfig


class BiographyConfig(AppConfig):
    name = 'biography'

    def ready(self):
        from biography import signals  # noqa
