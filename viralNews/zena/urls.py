from django.urls import path
from . import views

urlpatterns=[
    path("",views.news, name='news'),
    path("<str:title>", views.newDetail, name="detail"),
    # path("/contactus", views.contact, name="contact"),
    path('contact/', views.contact_us, name='contact_us'),
]