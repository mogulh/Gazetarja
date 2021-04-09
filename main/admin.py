from django.contrib import admin
from .models import Kategori, Lajmet, Terms, Privacy, SponsorPost

admin.site.register(Kategori)
admin.site.register(Lajmet)
admin.site.register(SponsorPost)
admin.site.register(Terms)
admin.site.register(Privacy)