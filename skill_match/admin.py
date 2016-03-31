from django.contrib import admin
from skill_match.models import HendersonPark, Amenity, Court


@admin.register(HendersonPark)
class HendersonParkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'url', 'img_url')


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('id', 'park', 'sport', 'other', 'img_url')