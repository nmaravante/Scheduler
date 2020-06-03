from django.contrib import admin

# Register your models here.
from scheduler_app.models import Assets,Scheduler


admin.site.register(Assets)
admin.site.register(Scheduler)