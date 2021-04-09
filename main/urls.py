from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    LajmetListView,
    LajmetDetailView,
    LajmetCreateView,
    LajmetUpdateView,
    UserLajmetListView,
    TermsDetailView,
    PrivacyDetailView,
    SponsorDetailView,
    SponsorUpdateView
)
from . import views

urlpatterns = [
    path('', LajmetListView.as_view(), name='lajme-home'),
    path("lajmi/<int:pk>/<str:slug>/", LajmetDetailView.as_view(), name='lajme-detail'),
    path('shkruaj-artikullin/', LajmetCreateView.as_view(), name='lajme-create'),
    path('lajmi/<int:pk>/<str:slug>/update/', LajmetUpdateView.as_view(), name='lajme-update'),
    path('kategoria/<int:pk>/<str:slug>/',views.category,name='category'),
    path('shkyqu-nga-gazeta/', auth_views.LogoutView.as_view(template_name='other/logout.html'), name='logout'),
    path('kyqu-te-gazeta/', auth_views.LoginView.as_view(template_name='other/login.html'), name='login'),
    path('profili/<str:username>/', UserLajmetListView.as_view(), name='user-posts'),
    path("kushtet/<int:pk>/<str:slug>/", TermsDetailView.as_view(), name='terms-detail'),
    path("politika/<int:pk>/<str:slug>/", PrivacyDetailView.as_view(), name='privacy-detail'),
    path("lajmi-sponsoruar/<int:pk>/<str:slug>/", SponsorDetailView.as_view(), name='sponsor-detail'),
    path('lajmi-sponsoruar/<int:pk>/<str:slug>/update/', SponsorUpdateView.as_view(), name='sponsor-update'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)