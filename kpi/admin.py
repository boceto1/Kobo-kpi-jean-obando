# coding: utf-8
from django.contrib import admin

from hub.models import ExtraUserDetail
from .models import AuthorizedApplication
from .models import Asset

# Register your models here.
admin.site.register(AuthorizedApplication)
admin.site.register(ExtraUserDetail)
admin.site.register(Asset)