from django.contrib import admin
from first_app.models import AccessRecord, Topic, WebPage, UserInfo

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
