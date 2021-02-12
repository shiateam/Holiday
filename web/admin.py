from django.contrib import admin
from .models.models import *
from .models.MobileVsTablets import *
from .models.SoundVsMedia import *

admin.site.register(Mobile)
admin.site.register(Category)
admin.site.register(Brand)


class MobileAdmin(admin.ModelAdmin):
    list_display = ('id','title','count','countsell','brand','owner')
    search_fields = ('id','title','owner','brand')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category')
    search_fields = ('id','category')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','Brand')
    search_fields = ('id','Brand')


