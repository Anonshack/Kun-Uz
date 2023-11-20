from django.contrib import admin
from .models import (HeadKunUz,
                     InternalMenus,
                     TodayNews,
                     UnderKunUz,
                     ThreeInfoUnder
                     )
# Register your models here.
models = [HeadKunUz, InternalMenus, TodayNews, UnderKunUz, ThreeInfoUnder]
for i in models:
    admin.site.register(i)