from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from main.sitemaps import LajmetSitemap
from django.contrib.sitemaps.views import sitemap
from users import views as user_views
from django.views.static import serve
from django.conf.urls import handler404

handler404 = 'main.views.error_404_view'

sitemaps = {
    'lajmet': LajmetSitemap,
    }

urlpatterns = [
    path('aktivizohu-ne-gazet/', admin.site.urls),
    path('',include('main.urls')),
    path('robots.txt', include('robots.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    re_path('djga/', include('google_analytics.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('profili-juaj/', user_views.profile, name='profile'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)