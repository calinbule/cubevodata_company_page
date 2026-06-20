from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'

    def ready(self):
        # Full pages are cached by the cache middleware, so clear the cache
        # whenever editable content changes to make admin edits show up at once.
        from django.core.cache import cache
        from django.db.models.signals import post_delete, post_save

        from .models import AIService, Project, Service

        def clear_cache(**kwargs):
            cache.clear()

        for model in (Service, AIService, Project):
            for signal in (post_save, post_delete):
                signal.connect(
                    clear_cache,
                    sender=model,
                    dispatch_uid=f'clear_cache_{signal}_{model.__name__}',
                    weak=False,
                )
