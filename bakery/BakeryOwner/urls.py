"""bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import RegisterAPI , LoginAPI , apiOverview
from knox import views as knox_views
from django.urls import path
from . import views


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    #path('', apiOverview.as_view(), name='apiOverview'),
    path('api/product-list/', views.showall, name='product-list'),
    path('api/product-detail/<int:pk>', views.viewproduct, name='product_detail'),
    path('api/product-create/', views.createproduct, name='product-create'),
    path('api/product-update/<int:pk>/', views.updateproduct, name='product-update'),
    path('api/product-delete/<int:pk>/', views.deleteproduct, name='product-delete'),
    path('api/ingredient-list/', views.showingredient, name='ingredient-list'),
    path('api/ingredient-create/', views.addingredient, name='AddIngredient'),
    path('api/ingredient-delete/<int:id>/', views.deleteingredient, name='deleteIngredient'),

]