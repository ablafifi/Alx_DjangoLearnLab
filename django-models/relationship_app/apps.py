from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Specifies the default field type for auto-generated primary keys.
    name = 'relationship_app'  # The name of the app. This is the full Python path to the app.
