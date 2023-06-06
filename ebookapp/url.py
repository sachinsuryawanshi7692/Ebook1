
from django.urls import path,include
from ebookapp import views

urlpatterns = [
    
    path('',views.home),
    path('base1',views.reuse),
    path('sort/<sv>',views.sort),
    path('catfilter/<catv>',views.catfilter),
    path('pricerange',views.pricerange),
    path('pdetails/<pid>',views.product_details),
    path('addbook',views.addbook),
    path('delbook/<rid>',views.delbook),
    path('editbook/<rid>',views.editbook),
    #path('register',views.register),
    #path('login',views.login),
    #path('logout',views.logout),
    path('djangoform',views.djangoform),
    path('modelform',views.modelform),
    path('register',views.user_register),
    path('login',views.user_login),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('cart',views.addtocart),
    path('logout',views.user_logout),
    
   
]