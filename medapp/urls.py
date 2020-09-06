from django.urls import path
from . import views

urlpatterns=[
    
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('addmedicine',views.addmed,name='addmedicine'),
    path('medicinelist',views.medlist,name='medicinelist'),
    path('profile',views.profile,name='profile'), 
       
    ]