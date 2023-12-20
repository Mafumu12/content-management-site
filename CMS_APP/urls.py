
from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('<int:category_id>/', views.home, name='home'),
    path('post/',views.CreatePost, name='post'),
    path('update/<str:slug>/',views.updatePost, name='update'),
    path('delete/<str:slug>',views.deletePost, name='delete'),
    path('article/<str:slug>',views.detail,name='detail'),
    path('like/<uuid:pk>/',views.LikeView,name='like'),
   
]
