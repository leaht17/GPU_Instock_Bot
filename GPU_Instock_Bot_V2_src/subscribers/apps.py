from django.apps import AppConfig

# Creates subscriber component configuration
# Args:
#   AppConfig: Authorized Gmail API service instance.
class SubscribersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscribers'
