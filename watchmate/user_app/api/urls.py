from rest_framework.authtoken import views
from user_app.api.views import registerAV,logoutAV
from django.urls import path,include
urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('register/',registerAV,name='register'),
    path('logout/',logoutAV,name='logout')

]