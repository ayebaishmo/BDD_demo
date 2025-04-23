from django.contrib import admin
from django.urls import path
from login_test.views import login_view
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]