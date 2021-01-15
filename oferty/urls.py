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
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('kontakt/', views.ContactView.as_view(), name='crispy-contact'),
    path('dziekujemy/', views.ThankYou.as_view(), name='thankyou'),
    path('polityka-prywatnosci/', views.PrivacyPolicy.as_view(),
         name='policy'),
    path('pdf/', views.DetailPdf.as_view(), name='detail-pdf'),
    path('add/', views.ClipboardAdd.as_view(), name='add'),
    path('delete/', views.ClipboardDelete.as_view(), name='delete'),
    path('delete_all/', views.ClipboardDeleteAll.as_view(), name='delete_all'),
    path('schowek/', views.clipboard, name='clipboard'),
    path('link/<str:token>/', views.link, name='link'),
    path('get_link/', views.GetLink.as_view(), name='get_link'),
]
