from django.contrib import admin
from django.urls import path, include
from list_task import views as lt

urlpatterns = [
    path('', lt.home),
    path('admin/', admin.site.urls),
    path('options/', include('list_task.urls')),
    path('account/', include('service_accounts.urls')),
]
