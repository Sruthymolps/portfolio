from django.urls import path
from .import views

urlpatterns = [
    path("",views.Profile),
    path(" ",views.Project),
    path('home',views.home)
 ]








































#from django.urls import path
#from.import views

#urlpatterns = [
    #path('create/', views.home.html, name='home.html'),
    #path('', views.profilelist, name='profilelist'),
    #path('profile/<int:pk>/', views.profiledetail, name='profiledetail'),
#]











#from django.urls import path
#from.import views

#urlpatterns = [
    #path('create/', views.home.html, name='home.html'),
    #path('', views.profilelist, name='profilelist'),
    #path('profile/<int:pk>/', views.profiledetail, name='profiledetail'),
#]
