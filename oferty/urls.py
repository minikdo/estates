from django.urls import re_path, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post_data/', views.post_data, name='post_data'),
    path('get_est_id/', views.get_est_id, name='get_est_id'),
    re_path('(?P<rodzaj>[\w-]+)/(?P<typ>[\w-]+)/(?P<miasto>[\w-]+)/$',
            views.result,
            name='result'),
    path('sprzedane/', views.sprzedane, name='sprzedane'),
    path('najnowsze/oferty/', views.najnowsze, name='najnowsze'),
    re_path('(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    path('kontakt/', views.ContactView.as_view(), name='crispy-contact'),
    path('dziekujemy/', views.ThankYou.as_view(), name='thankyou'),
    path('polityka-prywatnosci/', views.PrivacyPolicy.as_view(),
         name='policy'),
    path('crystal/', views.CrystalResort.as_view(), name="crystal"),
    path('<int:pk>/pdf/', views.detail_pdf, name='detail-pdf'),
]
