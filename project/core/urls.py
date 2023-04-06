from django.urls import path
from .views import home, about, contact, sample, blog, store

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('sample/', sample, name='sample'),
    path('blog/', blog, name='blog'),
    path('store/', store, name='store')
]