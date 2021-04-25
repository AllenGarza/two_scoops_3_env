from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "two_scoops_3_env.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import two_scoops_3_env.users.signals  # noqa F401
        except ImportError:
            pass
