from django.urls import path
from . import views

urlpatterns = [
    #--------------------APPS-----------------------------
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('apps/', views.apps_index, name='index'),
    path('apps/<int:app_id>/', views.app_detail, name='detail'),
    path('apps/create/', views.AppCreate.as_view(), name='app_create'),
    path('apps/<int:pk>/update/', views.AppUpdate.as_view(), name='app_update'),
    path('apps/<int:pk>/delete/', views.AppDelete.as_view(), name='app_delete'),
    path('apps/<int:app_id>/good/', views.app_good, name='good'),
    path('apps/<int:app_id>/bad/', views.app_bad, name='bad'),

    #--------------------ACCOUNTS-----------------------------
    path('accounts/signup/', views.signup, name='signup'),

    #--------------------PHOTOS-----------------------------
    path('apps/<int:app_id>/add_photo/', views.add_photo, name='add_photo'),

]