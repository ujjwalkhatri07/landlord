from django.contrib import admin
from Rooms.models import room
# Register your models here.

class abcAdmin(admin.ModelAdmin):
    list_display = ('Address','NumberOfRooms','price','im2','im3','im4','lender_contact')

admin.site.register(room,abcAdmin)
