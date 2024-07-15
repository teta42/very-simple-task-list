from django.urls import path
from list_task import views as lt

urlpatterns = [
    path('new_task', lt.new_task),
    path('list_task', lt.list_task),
    path('change_task', lt.change_task),
    path('delete_task', lt.delete_task),
]
