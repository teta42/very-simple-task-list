from django.contrib import admin
from django.urls import path
from list_task import views as lt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lt.home, name='home'),
    path('options/new_task', lt.new_task),
    path('options/list_task', lt.list_task),
    path('options/change_task', lt.change_task),
    path('options/delete_task', lt.delete_task),
]
