from django.contrib import admin

# Register your models here.
from .models import user_field ,task ,relation

admin.site.register(user_field)
admin.site.register(task)
admin.site.register(relation)