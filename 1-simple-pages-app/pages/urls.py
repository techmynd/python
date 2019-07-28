from django.urls import path
# from all import views
from . import views

# url for homepage

urlpatterns = [
    # three parameters > path, method, name of page
    path('', views.index, name='index'),
    # after this path
    # pages.views needs index member
    # add index method inside views file
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
