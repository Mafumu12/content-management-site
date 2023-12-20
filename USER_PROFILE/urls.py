
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/<str:profile_id>',views.UserProfile, name='profile'),
    path('account',views.account,name='account'),
    path('create_profile',views.CreateProfile,name='create_profile'),
    path('update_profile/<str:profile_id>/',views.UpdateProfile,name='update_profile'),
    path('delete_profile/<str:profile_id>/',views.DeleteProfile,name='delete_profile'),
    
]
