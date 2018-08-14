from django.conf.urls import url, include
from django.urls import re_path, path
from envelope.views import ContactView
from . import views
from .forms import CategorizedContactForm, DetailContactForm

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'post_data/', views.post_data, name='post_data'),
    path(r'get_est_id/', views.get_est_id, name='get_est_id'),
    re_path(r'(?P<rodzaj>[\w-]+)/(?P<typ>[\w-]+)/(?P<miasto>[\w-]+)/$',
            views.result,
            name='result'),
    path(r'sprzedane/', views.sprzedane, name='sprzedane'),
    path(r'najnowsze/oferty/', views.najnowsze, name='najnowsze'),
    re_path(r'(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    path(r'kontakt/', ContactView.as_view(
        form_class = CategorizedContactForm,
        template_name = 'envelope/crispy_contact.html',
        success_url = "/dziekujemy"),
        name='crispy-contact'),
    path(r'dziekujemy/', views.thankyou, name='thankyou'),
    path(r'cristal/', views.cristal, name="cristal"),
]

