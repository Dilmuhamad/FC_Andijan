from django.contrib import admin
from .models import *


class ClubAdmin(admin.ModelAdmin):
    pass

class AcademyAdmin(admin.ModelAdmin):
    pass

class ArenaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Club, ClubAdmin)
admin.site.register(Academy, AcademyAdmin)
admin.site.register(Arena, ArenaAdmin)
admin.site.register(Header)
admin.site.register(Video)
admin.site.register(Player)
admin.site.register(Shop)
admin.site.register(ArenasInformation)
admin.site.register(Partner)
admin.site.register(New)
admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Leadership)
admin.site.register(Level)
admin.site.register(Leader)
admin.site.register(Coach)