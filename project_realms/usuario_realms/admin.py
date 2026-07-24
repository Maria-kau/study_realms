from django.contrib import admin
from .models import (
    Profile,
    Attributes,
    Progress,
    Avatar,
    FixaUsuario,

)

admin.site.register(Profile)
admin.site.register(Attributes)
admin.site.register(Progress)
admin.site.register(Avatar)
admin.site.register(FixaUsuario)
