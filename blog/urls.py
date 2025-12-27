from django.urls import path
from .views import index,about,client,products,contact,detail


urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('client/',client,name='client'),
    path('products/',products,name='products'),
    path('contact/',contact, name='contact'),
    path('detail/<int:id>/',detail,name='detail'),
]