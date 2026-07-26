import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "project_realms.settings"
)

django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "kau_admin"
password = "Kau*12345"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        password=password
    )

    print("Admin criado com sucesso!")

else:
    print("Admin já existe!")