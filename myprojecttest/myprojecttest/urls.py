from django.urls import path
from testapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('reg/', views.reg, name='reg')
]
