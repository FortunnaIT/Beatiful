from django.urls import path
from .views import index,about,client,products,contact,detail,MahsulotCreate,MahsulotUpdate,MahsulotDelete


urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('client/',client,name='client'),
    path('products/',products,name='products'),
    path('contact/',contact, name='contact'),
    path('detail/<int:id>/',detail,name='detail'),
    path('mahsulot/create/',MahsulotCreate.as_view(),name='create'),
    path('mahsulot/update/<int:pk>/', MahsulotUpdate.as_view(), name='update'),
    path('mahsulot/delete/<int:pk>/',MahsulotDelete.as_view(), name='delete')

]