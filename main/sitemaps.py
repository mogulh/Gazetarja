from django.contrib.sitemaps import Sitemap
from main.models import Lajmet

class LajmetSitemap(Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Lajmet.objects.all()