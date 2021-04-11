from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Kategori, Lajmet, Terms, Privacy, SponsorPost
from users.models import Profile

from django.core.paginator import Paginator

# ---------------------------------------------------

def error_404_view(request, exception):
    query_pk_and_slug = True
    katego = Kategori.objects.all()
    shikime = Lajmet.objects.all().order_by('-shikime')
    return render(request, 'main/errorpage.html', {
        'katego': katego,
        'shikime': shikime
    })

# ----------------------------------------------------

def category(request,slug,pk):
    query_pk_and_slug = True
    katego=Kategori.objects.all()
    kategorit=Kategori.objects.get(title=slug)
    lajmet=Lajmet.objects.filter(kategorit=kategorit, verified=True).order_by('-data_e_postimit')
    lajms=Lajmet.objects.filter(kategorit=kategorit, verified=True).order_by('-data_e_postimit')[3:]
    lajmets=Lajmet.objects.filter(kategorit=kategorit, verified=True).order_by('-data_e_postimit')[7:]
    sponsor=SponsorPost.objects.all().order_by('-data_e_postimit')

    paginator = Paginator(lajmets, 15)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request,'main/category-news.html',{
        'lajmet':lajmet,
        'kategorit':kategorit,
        'katego': katego,
        'lajms': lajms,
        'page_obj': page_obj,
        'sponsor':sponsor
    })


# ---------------------------------------------------


class UserLajmetListView(ListView):
    model = Lajmet
    template_name = 'main/user_posts.html'
    context_object_name = 'lajmets'
    paginate_by = 15
    query_pk_and_slug = True

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Lajmet.objects.filter(author=user, verified=True).order_by('-data_e_postimit')

    def get_context_data(self, **kwargs):
        username = get_object_or_404(User, username=self.kwargs.get('username'))
        context = super(UserLajmetListView, self).get_context_data(**kwargs)
        context['katego'] = Kategori.objects.all()
        context['profile'] = Profile.objects.filter(user=username)
        return context


# ------------------MAIN EDITED LIST----------------------------------

class LajmetListView(ListView):
    model = Kategori
    model = Lajmet
    template_name = 'main/lajme-home.html'
    context_object_name = 'lajmets'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super(LajmetListView, self).get_context_data(**kwargs)
        context['trilajmet'] = Lajmet.objects.filter(kategorit=1, verified=True).order_by('-data_e_postimit')
        context['lajmekat'] = Lajmet.objects.filter(kategorit=1, verified=True).order_by('-data_e_postimit')[3:]
        context['lajmekata'] = Lajmet.objects.filter(kategorit=1, verified=True).order_by('-data_e_postimit')[4:]
        context['sportkat'] = Lajmet.objects.filter(kategorit=2, verified=True).order_by('-data_e_postimit')[0:]
        context['sportkata'] = Lajmet.objects.filter(kategorit=2, verified=True).order_by('-data_e_postimit')[1:]
        context['showbizkat'] = Lajmet.objects.filter(kategorit=3, verified=True).order_by('-data_e_postimit')[0:]
        context['showbizikata'] = Lajmet.objects.filter(kategorit=3, verified=True).order_by('-data_e_postimit')[1:]
        context['botkat'] = Lajmet.objects.filter(kategorit=6, verified=True).order_by('-data_e_postimit')[0:]
        context['botakata'] = Lajmet.objects.filter(kategorit=6, verified=True).order_by('-data_e_postimit')[1:]
        context['tech'] = Lajmet.objects.filter(kategorit=5, verified=True).order_by('-data_e_postimit')
        context['lajmet'] = Lajmet.objects.order_by('-data_e_postimit').filter(verified=True)
        context['katego'] = Kategori.objects.all()
        context['shikime'] = Lajmet.objects.all().order_by('-shikime')
        return context


# ------------------MAIN EDITED DETAILS----------------------------------

class LajmetDetailView(DetailView):
    model = Lajmet
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super(LajmetDetailView, self).get_context_data(**kwargs)
        context['katego'] = Kategori.objects.all()
        context['shikime'] = Lajmet.objects.all().order_by('-shikime')
        context['sponsor'] = SponsorPost.objects.all().order_by('-data_e_postimit')
        return context

    def get_object(self):
        obj = super().get_object()
        obj.shikime += 1
        obj.save()
        return obj

# ----------------------------------------------------

class LajmetCreateView(LoginRequiredMixin, CreateView):
    model = Lajmet
    fields = ['titulli', 'fotografit', 'detajet', 'kategorit', 'data_e_postimit']
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super(LajmetCreateView, self).get_context_data(**kwargs)
        context['katego'] = Kategori.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# ----------------------------------------------------

class LajmetUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lajmet
    query_pk_and_slug = True
    fields = ['titulli', 'fotografit', 'detajet', 'kategorit', 'data_e_postimit']

    def get_context_data(self, **kwargs):
        context = super(LajmetUpdateView, self).get_context_data(**kwargs)
        context['katego'] = Kategori.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        lajm = self.get_object()
        if self.request.user == lajm.author:
            return True
        return False

# ----------------------------------------------------

class TermsDetailView(DetailView):
    model = Terms
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super(TermsDetailView, self).get_context_data(**kwargs)
        context['katego'] = Kategori.objects.all()
        return context

# ----------------------------------------------------

class PrivacyDetailView(DetailView):
    model = Privacy
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super(PrivacyDetailView, self).get_context_data(**kwargs)
        context['katego'] = Kategori.objects.all()
        return context

# ----------------------------------------------------

class SponsorDetailView(DetailView):
    model = SponsorPost
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super(SponsorDetailView, self).get_context_data(**kwargs)
        context['katego'] = Kategori.objects.all()
        context['shikime'] = Lajmet.objects.all().order_by('-shikime')
        context['sponsor'] = SponsorPost.objects.all().order_by('-data_e_postimit')

        return context

    def get_object(self):
        obj = super().get_object()
        obj.shikime += 1
        obj.save()
        return obj

# ----------------------------------------------------

class SponsorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SponsorPost
    query_pk_and_slug = True
    fields = ['titulli', 'fotografit', 'detajet', 'data_e_postimit']

    def get_context_data(self, **kwargs):
        context = super(SponsorUpdateView, self).get_context_data(**kwargs)
        context['katego'] = Kategori.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        lajm = self.get_object()
        if self.request.user == lajm.author:
            return True
        return False

