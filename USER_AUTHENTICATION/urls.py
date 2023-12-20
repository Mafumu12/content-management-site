
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.UserLogin,name='login'),
    path('logout/',views.UserLogout,name='logout'),
    path('signup/',views.UserSignUp,name='signup'),
     

]
