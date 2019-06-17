from django.urls import path

from app.views import landing, stats, index, landing_alternate


urlpatterns = [
    path('', index, name='index'),
    path('landing/', landing, name='landing'),
    path('stats/', stats, name='stats'),
    path('landing_alternate/', landing_alternate, name='landing_alternate'),
]
