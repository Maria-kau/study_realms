from django.contrib import admin
from .models import (
    Subject,
    LibraryContent,
    UserLibrary,
    Module,
)

admin.site.register(Subject)
admin.site.register(Module)
admin.site.register(LibraryContent)
admin.site.register(UserLibrary)
