from django.contrib import admin
from .models import (
    StudySession,
    Tile,
    Realm,
    RealmBuilding,

)

admin.site.register(StudySession)
admin.site.register(Tile)
admin.site.register(Realm)
admin.site.register(RealmBuilding)
